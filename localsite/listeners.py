from decimal import Decimal
from datetime import datetime
import logging

import django
from django.conf import settings as django_settings
from django.contrib.auth.models import Group
from django import forms
from django.core.mail import send_mass_mail
from django.core.urlresolvers import reverse

from common.helper import start_thread

from satchmo_store.shop.exceptions import OutOfStockError
from satchmo_store.shop.models import OrderItem

from common.helper import send_mail_html
from concierges.models import Concierge
from localsite.models import SiteSkin, TourGuest, OrderHash
from resellers.models import Reseller
from adjustments.models import Adjustment


MIN_LEFT_TO_SEND_EMAIL = 5  # If number of seats of tours left less than this number then send an email alert

def satchmo_post_copy_item_to_order(sender, cartitem=None, order=None, orderitem=None, **kwargs):
    """
    Adds guest names to order items if appropriate
    """
    if orderitem:
        for guest in cartitem.guests.all():
            TourGuest.objects.create(order_item=orderitem, name=guest.name)

def satchmo_cart_changed_listener(sender, cart=None, request=None, **kwargs):
    """
    Applies logic to give customer a discount when they book multiple tours
    """
    # First find out how many unique tours there are
    tour_product_ids = []
    for item in cart.cartitem_set.all():
        # remove all old details
        item.details.all().delete()
        tp_id = item.product.productvariation.parent.product.id
        if tp_id not in tour_product_ids:
            tour_product_ids.append(tp_id)

    unique_tour_count = len(tour_product_ids)
    # TODO I think we are only supposed to give it on multiple tour_type_ids, not product ids
    # see: https://tivix.basecamphq.com/W2553551
    if unique_tour_count > 1:
        # If we have more than 1 unique tour, everything gets a discount
        detail_data = {
            'name': 'Multiple Tour Discount',
            'value': 'multiple_tour_discount',
            'sort_order': 0,
            'price_change': Decimal(-2)
        }
        for item in cart.cartitem_set.all():
            item.add_detail(detail_data)

    #  Add discount for resellers of type Mark-up Reseller
    affiliate = request.session.get('affiliate', None)
    if affiliate:
        if hasattr(affiliate, 'reseller_type') and affiliate.reseller_type == Reseller.TYPE_MARKUP:
            detail_data = {
                'name': 'Markup Reseller Discount',
                'value': 'markup_reseller_discount',
                'sort_order': 1,
                'price_change': Decimal('-%s' % str(affiliate.discount))
            }
            for item in cart.cartitem_set.all():
                # safe to add to all since all details are removed above
                item.add_detail(detail_data)

def order_success_listener(sender, order=None, **kwargs):
    """
    Keeps the total_sold number up-to-date on the main product when any combos are sold.

    Also sends out "low inventory" emails if number of tours left is less than a certain number
    """
    def __update_inventory_dict(d, product):
        d[product] = int(product.items_in_stock - product.total_sold)

    #  Create hash for an Order when the success signal is sent
    orderhash, created = OrderHash.objects.get_or_create(order=order)
    orderhash.save()
    num_left_map = {}

    order_items = order.orderitem_set.all()
    for item in order_items:
        product = item.product.productvariation.parent.product
        tour_product = product.tourproduct
        tour_type = tour_product.tour_type
        if tour_type.is_combo:
            # If it's a combo, the user actually bought a seat on each of these tours
            tour_products = tour_type.get_combo_products(tour_product.day)
            for tour_product in tour_products:
                # from IPython.Shell import IPShellEmbed; IPShellEmbed()()
                product_variation = tour_product.get_variation(item.product.productvariation.optionkey)

                new_item = OrderItem()
                new_item.order = item.order
                new_item.product = product_variation
                new_item.quantity = item.quantity
                new_item.unit_price = Decimal('0.00')
                new_item.line_item_price = Decimal('0.00')
                new_item.save()

                # The root product
                real_product = product_variation.productvariation.parent.product
                real_product.total_sold += item.quantity
                real_product.save()

                __update_inventory_dict(num_left_map, real_product)

            # create a note to add to this order since its a combo
            combo_note = 'Combo-'
            combo_note += '/'.join(map(lambda x: x.tour_type.name, tour_products))
            order.add_note(combo_note)
            order.save()
        else:
            product.total_sold += item.quantity
            product.save()

            __update_inventory_dict(num_left_map, product)

        # create an email message and send!
        message_list = []
        for p, num_left in num_left_map.items():
            if num_left < MIN_LEFT_TO_SEND_EMAIL:
                message_list += [('Almost sold out: %s' % p.name,
                    'Low inventory (only %s seats left!) for %s. Check it here: http://%s%s?product=%s' %\
                        (num_left, p.name, django_settings.SITE_DOMAIN, reverse('inventory_detail'), p.id),
                    django_settings.DEFAULT_FROM_EMAIL, (django_settings.DEFAULT_TO_EMAIL,))]

        if len(message_list) > 0:
            start_thread(send_mass_mail, tuple(message_list))


def immediate_fire_email_order_success_listener(sender, order=None, **kwargs):
    order_items = order.orderitem_set.all()
    for item in order_items:
        product = item.product.productvariation.parent.product
        tour_product = product.tourproduct
        tour_type = tour_product.tour_type

        # If we need to fire an email immediately
        if tour_type.immediate_followup_email_required and order.contact.email:
            send_mail_html(
                tour_type.immediate_followup_email_subject,
                tour_type.immediate_followup_email_body,
                tour_type.followup_email_from,
                [order.contact.email],
                connection=django.core.mail.get_connection(backend='django.core.mail.backends.smtp.EmailBackend'))  # don't CC SFST email


def contact_role_permission_sync(sender, instance, created, **kwargs):
    """
    This is called when a Contact instance is saved.  It makes sure that the Contact's User
    object is part of the correct auth Group.
    """
    contact = instance
    if contact.role and contact.user:
        group, created = Group.objects.get_or_create(name=contact.role.name)
        try:
            in_group = contact.user.groups.get(id=group.id)
        except Group.DoesNotExist:
            contact.user.groups.add(group)
            contact.user.save()


def sfst_object_link(sender, instance, **kwargs):
    """
    This is called whenever init() or save() are called on a Contact object.  It makes sure
    that there is a Concierge or Reseller object for any Contact object that has that role.  It also
    adds a link to that object at contact.concierge or contact.reseller.
    """
    contact = instance
    if contact.role:
        if contact.role.name.lower() == 'concierge':
            try:
                c = Concierge.objects.get(contact=contact)
            except Concierge.DoesNotExist:
                c = Concierge(contact=contact, site_skin=SiteSkin.objects.get(is_default=True))
                c.save()
            contact.concierge = c
        elif contact.role.name.lower() == 'reseller':
            try:
                r = Reseller.objects.get(contact=contact)
            except Reseller.DoesNotExist:
                r = Reseller(contact=contact)
                r.save()
            contact.reseller = r


def form_terms_listener(sender, form=None, **kwargs):
    """Adds a 'do you accept the terms and conditions' checkbox to the form"""
    url = u'http://sanfranshuttletours.com/terms_privacy.htm'
    link = u'<a target="_blank" href="%s">terms and conditions</a>' % url
    form.fields['terms'] = forms.BooleanField(
        label='I accept the %s' % link,
        widget=forms.CheckboxInput(),
        required=True)


def orderitem_status_listener(sender, instance, **kwargs):
    """Adds a status attribute to the order item"""
    try:
        adjustment = Adjustment.objects.get(item=instance)
        instance.STATUS = adjustment.get_status_display()
        instance.status_id = adjustment.status
    except Adjustment.DoesNotExist:
        instance.STATUS = None
        instance.status_id = None


def order_init(sender, instance, **kwargs):
    """Add the affiliate object to order.AFFILIATE.

    Also, if order.notes is None, set it to ''
    """
    affiliate = None
    if instance.id:
        try:
            affiliate = instance.concierge_set.all()[0]
        except IndexError:
            pass

        try:
            affiliate = instance.reseller_set.all()[0]
        except IndexError:
            pass

    instance.AFFILIATE = affiliate

    if instance.notes is None:
        instance.notes = ''
# def check_product_inventory(sender, cart=None, cartitem=None, added_quantity=None, details=None, **kwargs):
#     num_left = cartitem.product.productvariation.parent.product.items_in_stock - \
#         cartitem.product.productvariation.parent.product.total_sold
#     if added_quantity > num_left:
#         raise OutOfStockError(cartitem.product, num_left, added_quantity)



def sanity_check(sender, controller=None, **kwargs):
    """Using this signal to connect reseller orders to the reseller since we have
    access to the request and the order through the controller
    """
    request = controller.request
    order = controller.order
    affiliate = request.session.get('affiliate', None)
    if affiliate:
        affiliate.orders.add(order)
        affiliate.save()

        # if a reseller order then add a note
        if hasattr(affiliate, 'voucher'):
            affiliate.add_note_to_order(order)


def tour_type_default_seats_available_updated(sender, instance, **kwargs):
    """
    If the seats_available on a TourType is changed, then change the items_in_stock for the the satchmo product
    associated with all future TourProduct's to that number (even though admin may have changed them in the past
    through the inventory screen)
    """
    from localsite.models import TourType, TourProduct
    try:
        current_tour_type = TourType.objects.get(id=instance.id)
        if current_tour_type.seats_available != instance.seats_available:   # seats_available is changing
            today = datetime.today().date()
            for tour_product in TourProduct.objects.filter(tour_type=instance, day__gte=today):
                tour_product.product.items_in_stock = instance.seats_available
                tour_product.product.save()

        # update variations just in case needed
        instance.create_all_variations()
    except TourType.DoesNotExist:
        # Throws this error if the tourtype is being created the first time so there is
        # no need to adjust TourProducts because none could be FKed to this
        pass


def modify_order_confirmation_email_subject(sender, send_mail_args={}, context={}, **kwargs):
    """
    Insert the order# and tour details (1 or more) into the email subject of the confirmation that goes out to customers
    """
    if not 'order' in context:
        return

    subject = ''
    order = context['order']
    if context.get('affiliate'):
        subject += '%s - ' % context.get('affiliate').handle()

    subject += 'Order: %d' % order.id
    for item in order.orderitem_set.all():
        if item.line_item_price == 0:
            continue
        tour_product = item.product.productvariation.parent.product.tourproduct
        subject += ', '
        subject += tour_product.tour_type.name
        subject += ' on %s' % tour_product.day.strftime('%B %d, %Y')

    send_mail_args['subject'] = subject


def tour_type_base_price_changed(sender, instance, **kwargs):
    """
    Updates the price of the Satchmo product whenever the price of a TourType instance is updated. This is necessary
    to make sure the cart accurately shows the price, since Satchmo logic really depends on this pricing etc.
    """
    from localsite.models import TourType, TourProduct
    from product.models import Price
    try:
        current_tour_type = TourType.objects.get(id=instance.id)
        if current_tour_type.base_price != instance.base_price:   # base price is changing
            today = datetime.today().date()
            products_to_update_price_for = map(lambda x: x.product, TourProduct.objects.filter(tour_type=instance, day__gte=today))
            for price in Price.objects.filter(product__in=products_to_update_price_for):
                price.price = instance.base_price
                price.save()
    except TourType.DoesNotExist:
        # Throws this error if the tourtype is being created the first time so there is
        # no need to adjust TourProducts because none could be FKed to this
        pass

def add_to_email_context(sender, send_mail_args={}, context={}, **kwargs):
    """
    Adds coupon / banner and other static info to the email context.
    """
    from localsite import update_context_order_conf_extra
    update_context_order_conf_extra(context)

def option_group_changed(sender, instance, **kwargs):
    """(re) creates all product variations when an option_group linked to a tour type is changed"""
    from localsite.models import TourType

    for tour_type in TourType.objects.filter(option_group=instance):
        tour_type.create_all_variations()

def order_orderhash_listener(sender, instance, **kwargs):
    from satchmo_store.shop.models import Order
    from localsite.models import OrderHash

    order = Order.objects.get(id=instance.id)
    orderhash, created = OrderHash.objects.get_or_create(order=order)
