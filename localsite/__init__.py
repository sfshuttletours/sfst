import logging

from django.db.models import signals as django_signals
from django.contrib.auth.models import User
from django.conf import settings as django_settings

from apps.payment.forms import SimplePayShipForm
from satchmo_store.shop import signals as satchmo_signals
from satchmo_store.mail import send_html_email
from south.modelsinspector import add_introspection_rules
from payment.listeners import form_terms_listener
from satchmo_store.shop.models import CartItem, Order, OrderItem
from satchmo_store.contact.forms import ContactInfoForm
from satchmo_store.shop.notification import order_success_listener as nt_order_success_listener
from signals_ahoy.signals import form_init
from satchmo_store.contact.models import Contact
from payment import signals as payment_signals
from satchmo_store.shop.signals import satchmo_context, rendering_store_mail
from satchmo_ext.satchmo_toolbar.listeners import add_toolbar_context
from product.models import OptionGroup

from resellers.models import Reseller
from concierges.models import Concierge
from localsite.models import TourType, OrderConfirmationSection, OrderConfirmationBannerText, OrderConfirmationCoupon,\
    OrderCompletedSiteSkin, SiteSkin
from localsite.listeners import (
    tour_type_default_seats_available_updated,
    tour_type_base_price_changed,
    modify_order_confirmation_email_subject,  # check_product_inventory
    satchmo_cart_changed_listener,
    satchmo_post_copy_item_to_order,
    order_success_listener,
    immediate_fire_email_order_success_listener,
    contact_role_permission_sync,
    sfst_object_link,
    form_terms_listener,
    orderitem_status_listener,
    sanity_check,
    tour_type_default_seats_available_updated,
    order_init,
    add_to_email_context,
    option_group_changed,
    order_orderhash_listener
)

# satchmo_signals.satchmo_cart_add_verify.connect(check_product_inventory)

# modify the email confirmation subject ... had to disconnect and connect the send_html_email listner to get this to work
satchmo_signals.sending_store_mail.disconnect(send_html_email)
satchmo_signals.sending_store_mail.connect(modify_order_confirmation_email_subject)
satchmo_signals.sending_store_mail.connect(send_html_email)
satchmo_signals.satchmo_post_copy_item_to_order.connect(satchmo_post_copy_item_to_order)
satchmo_signals.satchmo_cart_changed.connect(satchmo_cart_changed_listener)
satchmo_signals.order_success.disconnect(nt_order_success_listener)
satchmo_signals.order_success.connect(order_success_listener)
satchmo_signals.order_success.connect(nt_order_success_listener)
satchmo_signals.order_success.connect(immediate_fire_email_order_success_listener)
form_init.connect(form_terms_listener, sender=SimplePayShipForm)
payment_signals.confirm_sanity_check.connect(sanity_check)

django_signals.pre_save.connect(tour_type_default_seats_available_updated, sender=TourType)  # fired on tour_type seats update
django_signals.pre_save.connect(tour_type_base_price_changed, sender=TourType)  # if base price changes then update all product prices too
django_signals.post_save.connect(contact_role_permission_sync, sender=Contact)
django_signals.post_save.connect(sfst_object_link, sender=Contact)
django_signals.post_init.connect(sfst_object_link, sender=Contact)
django_signals.post_init.connect(orderitem_status_listener, sender=OrderItem)
django_signals.post_init.connect(order_init, sender=Order)
django_signals.post_save.connect(option_group_changed, sender=OptionGroup)
django_signals.post_save.connect(order_orderhash_listener, sender=Order)

rendering_store_mail.connect(add_to_email_context)

# disconnect context add signal for toolbar
satchmo_context.disconnect(add_toolbar_context)

add_introspection_rules([], ["^shipping\.fields\.ShippingChoiceCharField"])   # to get south working with localsite app


# Adds an add_note method to Order
def add_note(self, note):
    current_notes = ''
    if self.notes is not None:
        current_notes = self.notes
    notes = map(lambda x: x.strip(), filter(lambda x: x, current_notes.split('::')))
    if note not in notes:
        notes.append(note)
    self.notes = ' :: '.join(notes)


def is_affiliate_order(self):
    if Reseller.objects.filter(orders__in=[self]) or Concierge.objects.filter(orders__in=[self]):
        return True

    return False


def is_concierge_order(self):
    if Concierge.objects.filter(orders__in=[self]):
        return True

    return False


def get_concierge_if_any(self):
    if self.concierge_set.all():
        return self.concierge_set.all()[0]
    return None

Order.add_note = add_note
Order.is_affiliate_order = is_affiliate_order
Order.is_concierge_order = is_concierge_order
Order.get_concierge_if_any = get_concierge_if_any


# override the clean_email function (sfst-old did it too!) to stop complaining about unique emails in checkout
def new_clean_email(self):
    """Prevent account hijacking by disallowing duplicate emails."""
    email = self.cleaned_data.get('email', None)
    if self._contact:
        if self._contact.email and self._contact.email == email:
            return email
        users_with_email = Contact.objects.filter(email=email)
        if len(users_with_email) == 0:
            return email
    return email

ContactInfoForm.clean_email = new_clean_email


def can_book_free_tours(self):
    """Check if the user can book "free" tours and add an attribute to the instance.

    This is used in several places so this just keeps it DRY.  A user can book "free" tours
    if one of the following are true:
        * They are a concierge
        * The are a reseller with type "Credit Card Processing Reseller"
        * They are staff (or just staff is enough too) with the "TourProduct.can_book_free_tours" permission
        * They are a superuser
    """
    if self.is_staff:
        return True

    valid_permissions = ('concierges.is_concierge', 'localsite.can_book_free_tours')
    for perm in valid_permissions:
        if self.has_perm(perm):
            return True # This also covers superuser

    if self.has_perm('resellers.is_reseller'):
        try:
            reseller = Reseller.objects.get(contact__user=self)
            if reseller.reseller_type == Reseller.TYPE_CREDIT_CARD_PROCESSOR:
                return True
        except Reseller.DoesNotExist:
            pass
    return False

User.can_book_free_tours = can_book_free_tours


def update_context_order_conf_extra(d, site_skin=None):
    """
    Updates the passed context / map with coupons, banner static confirmation sections etc. from the db. Used for regular /
    affiliate checkout / all emails that go out etc.

    site_skin: optional arg. Used when we want to force a certain skin for email/conf generation.... example sample order
    confirmation page in admin.
    """

    # get the order to figure out what SiteSkin instance was used in the checkout
    order = d.get('order')
    if order and not site_skin:
        qset = OrderCompletedSiteSkin.objects.filter(order=order)
        site_skin = qset.get().site_skin if qset else SiteSkin.objects.get(is_default=True)

    d['site_skin'] = site_skin
    d['site_domain_name'] = django_settings.SITE_DOMAIN
    d['order_confirmation_sections'] = OrderConfirmationSection.objects.filter(live=True, site_skin=site_skin)

    qset = OrderConfirmationBannerText.objects.filter(site_skin=site_skin)
    d['order_confirmation_banner_text'] = qset.get() if qset else None

    d['order_confirmation_coupons'] = OrderConfirmationCoupon.objects.filter(live=True, site_skin=site_skin)

    # used for prepending email subject with affiliate handle
    d['affiliate'] = None
    try:
        if order.concierge_set.all():
            d['affiliate'] = order.concierge_set.all()[0]
        elif order.reseller_set.all():
            d['affiliate'] = order.reseller_set.all()[0]
    except Exception:
        logging.error('Unable to add affiliate to email context for order: %s' % order.id)

# MONKEY PATCH
# override the default django user length
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

NEW_USERNAME_LENGTH = 254

User._meta.get_field('username').max_length = NEW_USERNAME_LENGTH
User._meta.get_field('username').validators[0].limit_value = NEW_USERNAME_LENGTH

UserAdmin.form.base_fields['username'].max_length = NEW_USERNAME_LENGTH
UserAdmin.form.base_fields['username'].widget.attrs['maxlength'] = NEW_USERNAME_LENGTH
UserAdmin.form.base_fields['username'].validators[0].limit_value = NEW_USERNAME_LENGTH
UserAdmin.form.base_fields['username'].help_text = UserChangeForm.base_fields['username'].help_text.replace('30', str(NEW_USERNAME_LENGTH))

UserChangeForm.base_fields['username'].max_length = NEW_USERNAME_LENGTH
UserChangeForm.base_fields['username'].widget.attrs['maxlength'] = NEW_USERNAME_LENGTH
UserChangeForm.base_fields['username'].validators[0].limit_value = NEW_USERNAME_LENGTH
UserChangeForm.base_fields['username'].help_text = UserChangeForm.base_fields['username'].help_text.replace('30', str(NEW_USERNAME_LENGTH))

UserCreationForm.base_fields['username'].max_length = NEW_USERNAME_LENGTH
UserCreationForm.base_fields['username'].widget.attrs['maxlength'] = NEW_USERNAME_LENGTH
UserCreationForm.base_fields['username'].validators[0].limit_value = NEW_USERNAME_LENGTH
UserCreationForm.base_fields['username'].help_text = UserChangeForm.base_fields['username'].help_text.replace('30', str(NEW_USERNAME_LENGTH))
