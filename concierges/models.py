from django.db import models
from django.conf import settings
from django.db.models import signals as django_signals
from django.utils.safestring import mark_safe

from satchmo_utils.thumbnail.field import ImageWithThumbnailField
from satchmo_store.contact.models import Contact, AddressBook, PhoneNumber
from satchmo_store.shop.models import Order
from l10n.models import Country

from localsite.models import TourProduct, SiteSkin


def add_concierge_methods_to_contact(sender, contact, **kwargs):
    pass
django_signals.post_init.connect(Contact, add_concierge_methods_to_contact)

HOTEL_ADDRESS = 'hotel address'
CONCIERGE_ADDRESS = 'concierge address'


class Concierge(models.Model):
    SEND_CHECKS_TO_HOME = 1
    SEND_CHECKS_TO_HOTEL = 2
    SEND_CHECKS_TO_CHOICES = (
        (SEND_CHECKS_TO_HOME, 'Home'),
        (SEND_CHECKS_TO_HOTEL, 'Hotel'),
    )

    BOOKING_TYPE_COMMISSION_CHECK = 1
    BOOKING_TYPE_DEPOSIT = 2
    BOOKING_TYPE_CHOICES = (
        (BOOKING_TYPE_COMMISSION_CHECK, 'Commission Check'),
        (BOOKING_TYPE_DEPOSIT, 'Deposit'),
    )

    contact = models.ForeignKey(Contact, related_name='concierges')
    image = ImageWithThumbnailField(
        upload_to='images/concierges',
        blank=True,
        max_length=128,
        auto_rename=True,
    )

    code = models.CharField(max_length=64, unique=True, null=True, db_index=True)
    email_notifications = models.BooleanField(default=False)
    send_checks_to = models.IntegerField(blank=True, null=True, choices=SEND_CHECKS_TO_CHOICES)
    booking_type = models.IntegerField(blank=True, null=True, choices=BOOKING_TYPE_CHOICES)
    frequency = models.CharField(max_length=64, blank=True, null=True)
    per_week = models.CharField(max_length=32, blank=True, null=True)
    orders = models.ManyToManyField(Order, null=True, blank=True)
    hotel_name = models.CharField(max_length=128)
    site_skin = models.ForeignKey(SiteSkin)

    class Meta:
        permissions = (
            ("is_concierge", "Is Concierge"),
        )

    def __unicode__(self):
        return 'Concierge: %s' % self.handle()

    def name(self):
        return '%s %s' % (self.contact.first_name, self.contact.last_name)

    def handle(self):
        return '%s @ %s' % (self.contact.first_name, self.hotel_name)

    def get_image_url(self):
        if self.image:
            return self.image.url
        return '%simg/person.jpg' % settings.MEDIA_URL

    def get_hotel_name(self):
        """Legacy location of hotel_name was as street2 in hotel address"""
        hotel_address = self.hotel_address()
        if hotel_address:
            return hotel_address.street2
        else:
            return ''

    def create_address(self, description):
        a = AddressBook(contact=self.contact, description=description)
        a.country = Country.objects.get(iso2_code='US')
        a.save()
        return a

    def hotel_address(self, create=False):
        try:
            return self.contact.addressbook_set.filter(description__istartswith=HOTEL_ADDRESS)[0]
        except IndexError:
            if create:
                return self.create_address(HOTEL_ADDRESS)
            else:
                return None

    def home_address(self, create=False):
        try:
            return self.contact.addressbook_set.filter(description__istartswith=CONCIERGE_ADDRESS)[0]
        except IndexError:
            if create:
                return self.create_address(CONCIERGE_ADDRESS)
            else:
                return None

    def home_phone(self, create=False):
        PHONE_TYPE = 'Home'
        try:
            return self.contact.phonenumber_set.filter(type=PHONE_TYPE)[0]
        except IndexError:
            if create:
                # primary=True is legacy logic but thought I'd stay consistent.  We're using PHONE_TYPE
                # now to tell the diff between home and hotel, Home and Work
                return PhoneNumber.objects.create(type=PHONE_TYPE, contact=self.contact, primary=True)
            return None

    def hotel_phone(self, create=False):
        PHONE_TYPE = 'Work'
        try:
            return self.contact.phonenumber_set.filter(type=PHONE_TYPE)[0]
        except:
            if create:
                return PhoneNumber.objects.create(type=PHONE_TYPE, contact=self.contact)
            return None

    def pretty_home_address(self):
        a = self.home_address()
        if a:
            s = ''
            if a.street1:
                s += a.street1 + '<br />'
            if a.street2:
                s += a.street2 + '<br />'
            csz = a.city
            if csz and (a.state or a.postal_code):
                csz += ', '
            if a.state:
                csz += ' ' + a.state
            if a.postal_code:
                csz += ' ' + a.postal_code
            s += csz
            return s
        return ''

    def commission_for_tour_type(self, tour_type):
        return tour_type.default_commission

        # keeping this around for no reason, but to not have to re-code a bunch of things
        # if not hasattr(self, '_rates'):
        #     self._rates = {}
        # if tour_type not in self._rates:
        #     try:
        #         rate = self.commissions.filter(tour_type=tour_type)[0].amount
        #     except IndexError:
        #         rate = 0
        #     self._rates[tour_type] = rate
        # return self._rates[tour_type]

    def order_report(self, start_date, end_date):
        """
        start / end date are used to filter based on *tour date*
        """
        total_commission = 0
        order_ids = TourProduct.objects.get_order_ids_for_tours_between(start_date, end_date, orders_in=self.orders.all() if self.orders.all() else [])
        orders = self.orders.filter(id__in=order_ids)

        # iterate over orders to get to commissions etc.
        for order in orders:
            order.tour_products = []
            order.commission = 0
            order.quantities = {}
            for item in order.orderitem_set.all():
                if item.unit_price > 0:  # to not have tours within combos show up
                    optionkey = item.product.productvariation.optionkey
                    if optionkey not in order.quantities:
                        order.quantities[optionkey] = 0
                    order.quantities[optionkey] += item.quantity

                    tour_product = item.product.productvariation.parent.product.tourproduct
                    if tour_product.day < start_date or tour_product.day > end_date:
                        continue
                    tour_type = tour_product.tour_type
                    if tour_type not in order.tour_products:
                        order.tour_products.append(tour_product)

                    commission = (self.commission_for_tour_type(tour_type) * item.quantity)
                    order.commission += commission
                    total_commission += commission
            order.tours_string = mark_safe('<br/> '.join(map(lambda x: '%s (%s at %s)' %\
                (x.tour_type.name, x.day.strftime('%B %d, %Y'), x.tour_time.strftime('%I:%M %p')), order.tour_products)))
        return (total_commission, orders)

    def save(self, *args, **kwargs):
        if not self.code and self.contact.user:
            self.code = hash(self.contact.user.username.strip())

        super(Concierge, self).save(*args, **kwargs)


class ConciergeCommission(models.Model):

    concierge = models.ForeignKey(Concierge, related_name='commissions')
    tour_type = models.ForeignKey('localsite.TourType')
    amount = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    class Meta:
        unique_together = ('concierge', 'tour_type')
