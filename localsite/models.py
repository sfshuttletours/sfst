from datetime import timedelta, date, datetime, time
from decimal import Decimal
import math
import logging

from django.conf import settings
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Q, F
from django.template.defaultfilters import slugify

from adjustments.models import Adjustment
from common.db_fields import RandomHashField
from localsite.exceptions import ComboScheduleNotBookable
from product.models import Product, OptionGroup, Price
from product.modules.configurable.models import ConfigurableProduct
from satchmo_store.shop.models import Order, OrderItem, CartItem
from satchmo_utils.thumbnail.field import ImageWithThumbnailField


SATCHMO_PRODUCT = True


def get_product_types():
    return ('TourProduct',)


class DayOfWeek(models.Model):
    isoweekday = models.IntegerField(unique=True, db_index=True)
    name = models.CharField(max_length=16, unique=True)

    def __unicode__(self):
        return self.name


class SiteSkin(models.Model):
    """
    Captures all the information needed to skin the entire checkout process including top banner, link, order confirmation
    content (and email) etc.
    """
    name = models.CharField(max_length=128, unique=True)
    code = models.CharField(max_length=16, unique=True, db_index=True)
    hash = RandomHashField(update_on_save=True)

    header_banner_link = models.URLField(verify_exists=False)
    header_banner_image = models.ImageField('Header banner image (1024px X 88px)',
        upload_to='images/siteskinheader', max_length=128)
    concierge_reg_ui_banner = models.ImageField('Concierge banner image',
        upload_to='images/siteskinbanner', max_length=128, blank=True, null=True)

    is_default = models.BooleanField(default=False, db_index=True, verbose_name='Is this the default skin?')
    custom_css = models.TextField(blank=True)

    order_confirmation_logo = models.ImageField('Order confirmation logo (350px X 59px)',
        upload_to='images/orderconfirmationlogos', max_length=128)
    order_confirmation_contact_info = models.TextField(blank=True)

    toc_text = models.CharField(max_length=512, verbose_name='Terms & Conditions link text')
    toc_link = models.URLField(verify_exists=False, verbose_name='Link to the Terms & Conditions')

    is_concierge_cta = models.BooleanField(default=True, verbose_name='Does this skin support Concierges?')
    reseller_lp_content = models.TextField(blank=True, verbose_name='Reseller landing page content')
    concierge_lp_content = models.TextField(blank=True, verbose_name='Concierge landing page content')
    tour_page_step1_text = models.CharField(max_length=512, null=True, blank=True)

    conversion_code = models.TextField(blank=True, null=True,
        help_text='Google Adwords or similar. Include "script" tag etc.')

    favicon = models.FileField('Favicon', blank=True, null=True,
        upload_to='images/favicons', max_length=128)

    def __unicode__(self):
        return '%s (%s)' % (self.name, self.code)


class OrderCompletedSiteSkinManager(models.Manager):
    def link(self, order, site_skin):
        qset = self.filter(order=order)
        if qset:
            order_skin = qset.get()
            order_skin.site_skin = site_skin
            order_skin.save()
        else:
            self.create(order=order, site_skin=site_skin)


class OrderCompletedSiteSkin(models.Model):
    """
    Used to store the SiteSkin instance used when this order was made. Useful since the order email generation etc.
    doesn't have access to the request object, just the context.
    """
    order = models.OneToOneField(Order)
    site_skin = models.ForeignKey(SiteSkin)

    objects = OrderCompletedSiteSkinManager()

    def __unicode__(self):
        return '#%s -- (%s)' % (self.order.id, self.site_skin.name)


class TourCategory(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=True, db_index=True)
    order = models.IntegerField(db_index=True, default=0)
    site_skins = models.ManyToManyField(SiteSkin, blank=True, null=True)

    class Meta:
        ordering = ('order', )

    def __unicode__(self):
        return '%s --- %s' % (self.name, ', '.join(map(lambda x: x.__unicode__(), self.site_skins.all())))


class TourType(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    slug = models.CharField(unique=True, max_length=128, blank=True, db_index=True)
    categories = models.ManyToManyField(TourCategory, blank=True, null=True, related_name='tours')

    default_site_skin = models.ForeignKey(SiteSkin,
        help_text='Default Site Skin for this tour type. The only thing this affects is the default skin to use in Reseller links and whether or not show this tour for concierges to book (depends on whether the SiteSkin supports concierge concept or not)')

    image = models.ImageField('Main Image ( max 250x130px )', upload_to='images/tours', max_length=128, blank=True)
    rollover_off = models.ImageField('Roll Over Off Image ( not more than 360x80px )', upload_to='images', max_length=128, blank=True)
    rollover_on = models.ImageField('Roll Over On Image ( not more than 360x80px )', upload_to='images', max_length=128, blank=True)
    seats_available = models.IntegerField('Default Seats (or buses!) Available')
    base_price = models.DecimalField(max_digits=6, decimal_places=2)
    price_raise_num_days = models.IntegerField(null=True, blank=True)
    price_raise_rate = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2)
    option_group = models.ForeignKey(OptionGroup, blank=True, null=True, related_name='tour_types')  # TODO: should blank/null be allowed?
    active = models.BooleanField(default=False, db_index=True,
        help_text='Check this if the tour is currently active. Inactive tours cannot be booked and do not appear on the site or to concierges.')
    has_brochures = models.BooleanField('Has Brochures?', default=False, db_index=True)
    order = models.IntegerField(db_index=True)
    featured = models.BooleanField(default=True, db_index=True,
        help_text='Check this if you want this tour type featured on the home page(s) of the site skins they belong to.')
    is_inventory_public = models.BooleanField(default=False, db_index=True,
        help_text='Check this if you would like tour inventory to be available publicly (to vineyards etc. for example)')

    min_calendar_start_date = models.DateField(null=True, blank=True,
        verbose_name='Minimum date to start the calendar on (optional)')
    max_calendar_end_date = models.DateField(null=True, blank=True,
        verbose_name='Max date to end the calendar on (optional)')

    default_commission = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))

    is_combo = models.BooleanField(default=False, db_index=True)

    requires_names = models.BooleanField(default=False,
        help_text='Require that names be entered for all the quantity of tickets being bought for this tour')

    is_tour_available_to_concierges = models.BooleanField(default=True)
    is_tour_available_to_resellers = models.BooleanField('Is available to resllers and/or different skins?', default=True)

    sell_in_even_quantities_only = models.BooleanField(default=False)

    customer_names_page_headline = models.CharField(max_length=64, null=True, blank=True,
        verbose_name='Customer Names Page Headline')
    customer_names_page_explanation = models.TextField(blank=True,
        verbose_name='Customer Names Page Explanation')

    # TODO: somehow we need to make sure that we don't have multiple times in the same day for the same tour type
    # on other words, we need one time for each tour_type referenced.
    combo_schedules = models.ManyToManyField('TourSchedule', blank=True, null=True, through='ComboSchedule',
                help_text="""Select only if this is a combo""")

    allow_refunds = models.BooleanField(default=True)
    in_perfect_inventory = models.BooleanField(default=True)

    immediate_followup_email_required = models.BooleanField(default=False,
        help_text='Whether you want an email to fire to the customer immediately after their order is complete')
    immediate_followup_email_subject = models.TextField(blank=True)
    immediate_followup_email_body = models.TextField(blank=True)

    followup_email_from = models.CharField(max_length=254, default=settings.DEFAULT_FROM_EMAIL)

    prior_to_tour_email_required = models.BooleanField(default=False,
        help_text='Whether you want an email to fire to the customer sometime prior to their tour')
    prior_to_tour_email_hours = models.IntegerField(blank=True, null=True)
    prior_to_tour_email_subject = models.TextField(blank=True)
    prior_to_tour_email_body = models.TextField(blank=True)

    class Meta:
        ordering = ('-active', 'order', 'name')

    def __unicode__(self):
        return u'Tour Type: %s -- %s %s' % (self.name, self.default_site_skin, '' if self.active else '(NOT ACTIVE)')

    def get_absolute_url(self):
        return reverse('product', args=[self.slug])

    def generate_future_tour_products(self, days=1, start_date=date.today()):
        """
        Create Products for all future days for this tour type if they don't
        already exist.
        """
        for idx in xrange(0, days):
            day = start_date + timedelta(days=idx)
            schedules = self.schedules.filter(day_of_week__isoweekday=day.isoweekday())
            for schedule in schedules:
                self.get_product(day, schedule)

    def get_combo_products(self, day, create=True):
        products = []
        combo_schedules = []

        for cs in self.comboschedule_set.all():
            # if day.isoweekday() + cs.days_after == 7 (Sunday!!!) then we don't have to do modulo
            calculated_isoweekday = 7 if day.isoweekday() + cs.days_after == 7 else\
                (day.isoweekday() + cs.days_after) % 7

            if cs.tourschedule.day_of_week.filter(isoweekday=calculated_isoweekday).exists():
                combo_schedules.append(cs)

        # TODO: maybe we should throw error all the way back to user ??
        if len(self.combo_schedules.all()) != len(combo_schedules):
            logging.info('This tour combo: %s is not configured correctly properly.' % self.name)
            raise ComboScheduleNotBookable()

        for cs in combo_schedules:
            cs_day = day + timedelta(days=cs.days_after)
            schedule = cs.tourschedule
            products.append(schedule.tour_type.get_product(cs_day, schedule=schedule, create=create))
        return products

    def get_product(self, day, schedule=None, tour_time=None, create=True):
        """
        Get the TourProduct for the given day and time.  If create is false and product does
        not exist, return None.
        """

        if schedule and tour_time:
            assert False, 'Make up your mind, use a schedule or a tour_time, not both'
        if not schedule and not tour_time:
            assert False, 'Need a time buddy'

        try:
            if schedule:
                tour_product = TourProduct.objects.filter(tour_type=self, day=day).filter(
                    Q(schedule=schedule) | Q(tour_time=schedule.tour_time))[0]
            else:
                tour_product = TourProduct.objects.get(tour_type=self, day=day, tour_time=tour_time)

            if tour_product.tour_type.has_price_raise():
                p = tour_product.product.price_set.all()[0]
                p.price = self.get_raised_base_price(tour_product.day)
                p.save()

            return tour_product
        except (TourProduct.DoesNotExist, IndexError):
            if create:
                # print 'creating product... ', day
                product = Product()
                product.site = Site.objects.get_current()
                product.name = '%s on %s at ' % (self.name, day.strftime('%B %d, %Y'))
                if schedule:
                    product.name += schedule.tour_time.strftime('%I:%M %p')
                else:
                    product.name += tour_time.strftime('%I:%M %p')
                product.items_in_stock = self.get_capacity_for_day(day)
                product.shipclass = 'NO'  # see product.models.SHIP_CLASS_CHOICES
                product.save()

                tour_product = TourProduct()
                tour_product.product = product
                tour_product.tour_type = self
                tour_product.day = day
                if schedule:
                    tour_product.schedule = schedule
                    tour_product.tour_time = schedule.tour_time
                else:
                    tour_product.schedule = None
                    tour_product.tour_time = tour_time
                tour_product.save()

                p = Price()
                p.product = product
                if tour_product.tour_type.has_price_raise():
                    p.price = self.get_raised_base_price(tour_product.day)
                else:
                    p.price = self.base_price
                p.save()

                # Create Variations
                if self.option_group_id:
                    configurable_product = ConfigurableProduct(product=product)
                    configurable_product.save()
                    configurable_product.option_group.add(self.option_group)
                    configurable_product.create_subs = True
                    configurable_product.save()
                return tour_product
            else:
                return None

    def create_all_variations(self):
        """Helper function to call if you want to re-generate variations for all (future) products of this tour type. This is
        necessary for example if you change options in a certain option group (thats linked to this tour type)."""
        today = datetime.today().date()
        for tp in TourProduct.objects.filter(tour_type=self, day__gte=today).select_related('product'):
            for cp in ConfigurableProduct.objects.filter(product=tp.product):
                cp.create_all_variations()

    def get_schedule_for_day(self, day):
        return self.schedules.filter(active=True, day_of_week=day.isoweekday()).order_by('tour_time')

    def get_capacity_for_day(self, day):
        try:
            capacity_rule = self.capacities.filter(from_date__lte=day, to_date__gte=day, day_of_week=day.isoweekday()).order_by('-updated_on')[0]
            return capacity_rule.seats_available
        except IndexError:
            return self.seats_available

    def get_options(self, day=None):
        """
        Returns options with price attribute added
        """
        options = self.option_group.option_set.all()
        for o in options:
            if day and self.has_price_raise():
                base_price = self.get_raised_base_price(day)
            else:
                base_price = self.base_price
            o.price = '%.2f' % (base_price + o.price_change)
        return options

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        if not self.followup_email_from:
            self.followup_email_from = settings.DEFAULT_FROM_EMAIL
        super(TourType, self).save(*args, **kwargs)

    def has_price_raise(self):
        if self.price_raise_num_days and self.price_raise_rate:
            return True
        return False

    def get_raised_base_price(self, day):
        if not self.has_price_raise():
            return 0

        if (day - timedelta(days=self.price_raise_num_days)) <= date.today():
            return self.base_price + self.price_raise_rate
        else:
            return self.base_price


class TourSchedule(models.Model):
    tour_type = models.ForeignKey(TourType, related_name='schedules')
    day_of_week = models.ManyToManyField(DayOfWeek)
    tour_time = models.TimeField()
    active = models.BooleanField(default=True, db_index=True)

    def __unicode__(self):
        days = [d.name[:3] for d in self.day_of_week.all()]
        return '%s @ %s on %s' % (self.tour_type.name, self.pretty_time, ', '.join(days))

    @property
    def pretty_time(self):
        return self.tour_time.strftime('%I:%M %p')


class ComboSchedule(models.Model):
    tourschedule = models.ForeignKey(TourSchedule)
    tourtype = models.ForeignKey(TourType)
    days_after = models.PositiveIntegerField('days after', default=0)

    class Meta(object):
        unique_together = ("tourschedule", "tourtype", "days_after")


class TourCapacity(models.Model):
    """
    TODO: remove. Old ... not used anymore.
    """
    tour_type = models.ForeignKey(TourType, related_name='capacities')
    from_date = models.DateField()
    to_date = models.DateField()
    day_of_week = models.ManyToManyField(DayOfWeek)
    seats_available = models.IntegerField()
    updated_on = models.DateField(auto_now=True)  # If there are overlapping rules we pick the one updated most recently


class TourProductManager(models.Manager):
    def get_order_ids_for_tours_between(self, start_date, end_date, exclude_adjusted_orders=True, orders_in=None):
        """
        Returns all the order_id's for tours between these dates.
        It excludes adjusted orders so we don't have to worry in reseller and concierge reporting!
        """
        # figure out all the products and their id's within the date range
        num_days = (end_date - start_date).days + 1
        tour_dates = [start_date + timedelta(days=x) for x in range(0, num_days)]
        product_ids = []
        for tour_product in self.filter(day__in=tour_dates):
            try:
                product_ids += tour_product.product.configurableproduct.productvariation_set.all().values_list(
                    'product__id', flat=True)
            except ConfigurableProduct.DoesNotExist:
                product_ids += [tour_product.product.id]

        # figure out the OrderItem instances
        order_items = OrderItem.objects.select_related('order').filter(product__id__in=product_ids)
        if orders_in is not None:
            order_items = order_items.filter(order__in=orders_in)
        order_ids = map(lambda x: x.order.id, order_items)

        if exclude_adjusted_orders:
            adjusted_order_ids = map(lambda x: x.item.order.id, Adjustment.objects.filter(
                item__order__id__in=order_ids).exclude(status__in=[Adjustment.MOVED, Adjustment.REFUND_REQUEST_REJECTED]))
            order_ids = filter(lambda x: x not in adjusted_order_ids, order_ids)
        return order_ids


class TourProduct(models.Model):
    """
    This is a Satchmo "custom product"

    See: http://www.satchmoproject.com/docs/dev/custom-product.html#custom-product-modules
    """
    product = models.OneToOneField(Product, verbose_name='Product', primary_key=True)
    tour_type = models.ForeignKey(TourType)
    day = models.DateField(db_index=True)
    schedule = models.ForeignKey(TourSchedule, null=True, blank=True)
    tour_time = models.TimeField()
    active = models.BooleanField(default=True, db_index=True)
    overbooking_attempts = models.IntegerField(default=0)

    objects = TourProductManager()

    class Meta:
        verbose_name = 'Tour Product'
        verbose_name_plural = 'Tour Products'
        unique_together = ('tour_type', 'day', 'tour_time')
        permissions = (
            ("can_book_free_tours", "Can Book Free Tours"),
        )

    def _get_subtype(self):
        return 'TourProduct'

    def __unicode__(self):
        return u'TourProduct: %s' % self.product.name

    @property
    def pretty_time(self):
        return self.tour_time.strftime('%I:%M %p')

    def seats_available(self):
        # TODO: Edge case, sometimes # booked is negative... need to investigate
        if int(self.product.total_sold) < 0:
            return 0

        return int(self.product.items_in_stock) - int(self.product.total_sold)

    def seats_left(self, number_needed):
        return int(number_needed) <= self.seats_available()

    def passengers(self):
        """
        Returns a list of contacts. Appends 'order' and 'items' (of type <code>OrderItem</code>) to each contact object
        to be accessed nicely in the templates.
        """
        contacts = []
        # variations = self.product.configurableproduct.productvariation_set.all()
        # for variation in variations:
        #     order_items = variation.product.orderitem_set.all()
        for item in self.items.iterator():
            if item.status_id and item.adjustment.moved:
                if item.adjustment.history.latest('timestamp').user:
                    item.order.add_note('Moved -- Collect Change Fee')
                else:
                    item.order.add_note('Moved -- Change fee paid')
            if item.status_id and item.adjustment.voucher_created:
                item.order.add_note('Voucher -- Collect Change Fee')

            c = item.order.contact

            if c not in contacts:
                # append a is_checked_in to the contact
                try:
                    assert item.order.checkin
                    assert item.checkin
                    c.is_checked_in = True
                except Exception:
                    c.is_checked_in = False

                c.order = item.order
                c.items = [item, ]
                try:
                    c.cell = c.phonenumber_set.all()[0].phone
                except:
                    pass
                contacts.append(c)
            else:
                contacts[contacts.index(c)].items.append(item)

        contacts.sort(key=lambda x: x.last_name.lower())
        # contacts.sort(key=lambda x: x.order.id)

        return contacts

    @property
    def items(self):
        """Return all order items for this tour product"""
        # These are all the variations of this main product
        try:
            product_ids = self.product.configurableproduct.productvariation_set.all().values_list('product__id', flat=True)
        except ConfigurableProduct.DoesNotExist:
            product_ids = [self.product.id, ]

        exclude_status_ids = [
            Adjustment.DELETED,
            Adjustment.REFUNDED,
            Adjustment.VOIDED,
            Adjustment.VOUCHER_STANDBY_CREATED,
            Adjustment.VOUCHER_OK_TO_BOOK,
            Adjustment.REFUND_REQUESTED,
        ]

        # MOVED = 4
        # VOUCHER_STANDBY_USED = 7
        # REFUND_REQUEST_REJECTED = 9

        return OrderItem.objects.filter(
            product__id__in=product_ids).exclude(
            adjustment__status__in=exclude_status_ids).order_by('order__contact__last_name')

    def get_variation(self, optionkey):
        try:
            variation = self.product.configurableproduct.productvariation_set.get(options__value=optionkey)
        except Exception:
            variation = self.product.configurableproduct.productvariation_set.all().order_by('optionkey')[0]  # should get Adult as default

        return variation.product

    @property
    def status(self):
        tour_datetime = datetime.combine(self.day, self.tour_time)
        time_difference = tour_datetime - datetime.now()
        if not self.tour_type.allow_refunds:
            return 'NOT_CHANGEABLE'
        else:
            if time_difference.days >= 3:
                return 'RETURN_OR_CHANGE'
            else:
                return 'NOT_CHANGEABLE'


class OverbookingAttempt(models.Model):
    """
    Contains datetime information or each overbooking attempt on a tour.
    """
    tour = models.ForeignKey(TourProduct, related_name='overbookings',
        help_text='tour that experienced the overbooking attempt')
    occurred_at = models.DateTimeField(auto_now_add=True)
    num_overbooked = models.IntegerField(default=0)

    def __unicode__(self):
        return u"%s: %s" % (self.tour.product.name, self.occured_at)


class OrderHash(models.Model):
    order = models.OneToOneField(Order)
    hash = RandomHashField()
    void_failed = models.BooleanField(default=False)

    @property
    def is_settled(self):
        now = datetime.now()
        settlement_time = time(hour=15, minute=45)
        order_timestamp = self.order.time_stamp
        time_difference = now - order_timestamp
        settlement_time_on_order_day = datetime.combine(order_timestamp, settlement_time)
        next_settlement_time = settlement_time_on_order_day + timedelta(days=1)
        if time_difference.days < 1 and time_difference.seconds < 82800 and not self.void_failed and not self.already_voided:
            if order_timestamp < settlement_time_on_order_day:
                if now > settlement_time_on_order_day:
                    return True
                else:
                    return False
            else:
                if now > next_settlement_time:
                    self.void_failed = True
                    return True
                else:
                    return False
        else:
            self.void_failed = True
            return True

    @property
    def already_voided(self):
        for item in self.order.orderitem_set.all():
            try:
                if item.adjustment.status == 3:
                    return True
            except Adjustment.DoesNotExist:
                pass
        return False

    def __unicode__(self):
        return u"Order:%s, Hash:%s" % (self.order, self.hash)


class TeamMember(models.Model):
    """
    SFST staff details.
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    job_title = models.CharField(max_length=64)
    image = ImageWithThumbnailField(
        upload_to='images/team_members',
        max_length=128,
        auto_rename=True,
        )

    def __unicode__(self):
        return self.name()

    def name(self):
        return '%s %s' % (self.first_name, self.last_name)


class SurveyEmailSent(models.Model):
    """
    An entry in this model signifies that a survey email has been sent for this
    order already.
    """
    order = models.OneToOneField(Order)


class PriorToEmailSent(models.Model):
    """
    An entry in this model signifies that a email has been sent for this order
    Prior to tour date.
    """
    order = models.OneToOneField(Order)


class OrderConfirmationSection(models.Model):
    """
    Defines a section in the order confirmation screen / email.
    """
    title = models.CharField(max_length=255)
    order = models.IntegerField(default=0, db_index=True)
    live = models.BooleanField(default=True, db_index=True)
    site_skin = models.ForeignKey(SiteSkin)

    class Meta:
        ordering = ('order',)

    def __unicode__(self):
        return '%s -- %s' % (self.title, self.site_skin.name)


class OrderConfirmationSubSection(models.Model):
    """
    Links directly to a section, hence doesn't require a reference to SiteSkin at all.
    """
    section = models.ForeignKey(OrderConfirmationSection, related_name='sub_sections')
    title = models.CharField(max_length=255)
    content = models.TextField()
    order = models.IntegerField(default=0, db_index=True)
    live = models.BooleanField(default=True, db_index=True)

    class Meta:
        ordering = ('order',)

    def __unicode__(self):
        return '%s -- %s' % (self.title, self.section)


class OrderConfirmationBannerText(models.Model):
    banner_image = models.ImageField('Banner ( max 550x150px )', upload_to='images/orderconf', max_length=128, blank=True, null=True)
    text = models.CharField(max_length=255)
    header_top_text = models.TextField(default='25% REFUND FOR ALL MISSED TOURS')    # appears all the way at the top!
    site_skin = models.ForeignKey(SiteSkin, unique=True)

    def __unicode__(self):
        return '%s -- %s' % (self.text, self.site_skin.name)


class OrderConfirmationCoupon(models.Model):
    name = models.CharField(max_length=255)
    coupon_image = models.ImageField('Coupon ( max 160x130px )', upload_to='images/orderconf', max_length=128)
    order = models.IntegerField(default=0, db_index=True)
    live = models.BooleanField(default=True, db_index=True)
    site_skin = models.ForeignKey(SiteSkin)

    class Meta:
        ordering = ('order',)

    def __unicode__(self):
        return '%s -- %s' % (self.name, self.site_skin.name)


class CartGuest(models.Model):
    name = models.CharField(max_length=64)
    cart_item = models.ForeignKey(CartItem, related_name='guests')

    def __unicode__(self):
        return '%s -- %s' % (unicode(self.cart_item), self.name)


class TourGuest(models.Model):
    name = models.CharField(max_length=64)
    order_item = models.ForeignKey(OrderItem, related_name='guests')

    def __unicode__(self):
        return '%s -- %s' % (unicode(self.order_item), self.name)
