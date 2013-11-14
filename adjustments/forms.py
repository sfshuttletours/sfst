from datetime import date
import urllib2
from urllib import urlencode
from decimal import Decimal, ROUND_HALF_UP

from django.contrib.auth.models import User
from django import forms
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.conf import settings as django_settings

from common.helper import start_thread, send_mail as helper_send_mail
from satchmo_store.shop.models import OrderItem
from livesettings import config_get

from adjustments.models import Adjustment, AdjustmentHistory
from localsite.models import TourType, TourSchedule
from localsite.forms import BookItForm

class AuthorizeNetError(Exception):
    """Raised if Authorize.net transaction was not successful"""
    pass


class BaseAdjustmentForm(forms.Form):

    def __init__(self, request, order, *args, **kwargs):
        self.request = request
        self.order = order
        super(BaseAdjustmentForm, self).__init__(*args, **kwargs)
        # Setup valid item choices
        item_choices = []
        for item in order.orderitem_set.all():
            tour_type = item.product.productvariation.parent.product.tourproduct.tour_type
            if not tour_type.is_combo:
                item_choices.append((item.id, item.id))
        self.fields['item'].choices = item_choices
        self.fields['user'].initial = request.user.id

    user = forms.ModelChoiceField(queryset=User.objects.filter(is_staff=True), widget=forms.HiddenInput, label='User')
    item = forms.MultipleChoiceField(widget=forms.MultipleHiddenInput, required=False)

    def clean_item(self):
        val = self.cleaned_data['item']
        if not len(val):
            raise forms.ValidationError("You must select at least one item to adjust from above.")
        return val

    def get_items(self):
        cd = self.cleaned_data
        items = []
        for item_id in cd['item']:
            items.append(OrderItem.objects.get(id=int(item_id)))
        return items

    def send_message(self, message, prefix='Reservation'):
        subject = "%s #%d changed by %s" % (prefix, self.order.id, self.request.user.username)
        pre_msg = "%s #%d from customer %s was changed\n\n" % (prefix, self.order.id, self.order.contact.full_name)
        mail_message = '%s %s' % (pre_msg, message)
        mail_message += '\n\nhttp://%s%s' % (Site.objects.get_current().domain, reverse('order_detail', args=[self.order.id,]))
        start_thread(send_mail, subject, mail_message, django_settings.DEFAULT_FROM_EMAIL, [django_settings.DEFAULT_TO_EMAIL,])

    def add_history(self, item, new_status, notes=''):
        old_status = None
        old_status_display = ''
        try:
            adjustment = Adjustment.objects.get(item=item)
            old_status = adjustment.status
            old_status_display = adjustment.get_status_display()
        except Adjustment.DoesNotExist:
            adjustment = Adjustment(item=item)

        adjustment.status = new_status
        adjustment.save()

        history = AdjustmentHistory(adjustment=adjustment)
        history.user = self.request.user
        history.from_status = old_status
        history.to_status = adjustment.status
        history.notes = notes
        history.save()
        return history

    def release_seats(self, item):
        """Subtract quantity of item from total seats sold"""
        p = item.product.productvariation.parent.product
        p.total_sold -= item.quantity
        p.save()
        return '%d seats added back to %s\n' % (int(item.quantity), p)

    def reserve_seats(self, item):
        """Add quantity of item to total seats sold"""
        p = item.product.productvariation.parent.product
        p.total_sold += item.quantity
        p.save()
        return '%d seats subtracted from %s\n' % (int(item.quantity), p)

class AdjustmentDeleteForm(BaseAdjustmentForm):
    TYPE_CONCIERGE = 'Concierge'
    TYPE_RESELLER = 'Reseller'
    TYPE_MANUAL_ADD_ON = 'Manual Add-On'

    FREE_ORDER_CHOICES = (
        (TYPE_CONCIERGE, 'Concierge'),
        (TYPE_RESELLER, 'Reseller'),
        (TYPE_MANUAL_ADD_ON, 'Manual Add-On'),
    )

    free_order_type = forms.ChoiceField(choices=FREE_ORDER_CHOICES, label='What kind of tour was this (concierge or reseller or manual add-on)?')
    concierge_account = forms.CharField(required=False, label='If it was a concierge order, which concierge account did it come from?')
    concierge_trend = forms.BooleanField(required=False, initial=False, label='Does this concierge have a trend (3 or more recent) no-show customers?')
    double_booking = forms.BooleanField(required=False, initial=False, label='Is this a double booking?')
    additional_notes = forms.CharField(required=False, label='Additional Comments to Management:', widget=forms.Textarea)

    def do_it(self):
        cd = self.cleaned_data

        pre_msg = ''
        for field in self.fields:
            if field not in ('item', 'user'):
                pre_msg += '%s %s\n' % (self.fields[field].label, cd[field])
        pre_msg += '\n'

        msg = pre_msg
        items = self.get_items()
        for item in items:
            product = item.product.productvariation.parent.product
            tour_product = product.tourproduct

            history = self.add_history(item, Adjustment.DELETED, pre_msg)

            msg += '%d of %s' % (item.quantity, unicode(item.product))
            if history.from_status:
                msg += ' change from %s to %s' % (history.get_from_status_display(), history.get_to_status_display())
            else:
                msg += ' status set to %s' % history.get_to_status_display()
            msg += '\n'

            product.total_sold -= item.quantity
            product.save()
            msg += 'Added %d seats back to inventory for %s\n\n' % (item.quantity, unicode(product))

            # TODO update inventory

        self.send_message(msg)
        return 'Items were successfully deleted'

class AdjustmentMoveForm(BaseAdjustmentForm):

    def __init__(self, *args, **kwargs):
        super(AdjustmentMoveForm, self).__init__(*args, **kwargs)
        self.fields['tour_schedule'].choices = TourSchedule.objects.filter(active=True).values_list('id', 'tour_time')
    tour_type = forms.ModelChoiceField(queryset=TourType.objects.filter(is_combo=False, active=True), empty_label=None)
    day = forms.DateField()
    tour_schedule = forms.ModelChoiceField(queryset=TourSchedule.objects.filter(active=True))

    def clean_item(self):
        val = self.cleaned_data['item']
        if not len(val):
            raise forms.ValidationError("You most select at least one item to adjust from above.")
        if len(val) > 1:
            raise forms.ValidationError("You can only move one item at a time.")
        return val

    def clean(self):
        cd = self.cleaned_data

        if 'day' in cd and 'tour_schedule' in cd and 'item' in cd:
            item = self.get_items()[0]

            # Now collect data for BookItForm
            data = {'tour_date': cd['day'].strftime('%m/%d/%Y'), 'schedule': cd['tour_schedule'].id}

            # Convert old optionkey into new option key
            new_tour_product = cd['tour_type'].get_product(cd['day'], schedule=cd['tour_schedule'])
            new_product = new_tour_product.product
            options = new_product.configurableproduct.get_all_options()

            variation = item.product.productvariation
            new_option = None
            for option_list in options:
                option = option_list[0]
                if new_option is None:
                    # If we don't have one yet we want to take the first
                    new_option = option
                if option.value == variation.optionkey:
                    new_option = option
            data['option_%d' % new_option.id] = int(item.quantity)

            self.book_it = BookItForm(tour_type=cd['tour_type'], from_admin=True, data=data)
            if self.book_it.is_valid():
                pass
            else:
                raise forms.ValidationError(self.book_it.errors)

        return cd

    def do_it(self):
        msg = ''
        cd = self.cleaned_data
        new_product = self.book_it.get_products()[0]['product']

        item = self.get_items()[0]
        release_msg = ''
        try:
            # don't release seats if item was in a standby status since seats were already released
            if item.adjustment and item.adjustment.status not in AdjustmentCreditVoucherForm.STANDBY_IDS:
                release_msg = self.release_seats(item)
        except Adjustment.DoesNotExist:
            # This get's raised if there is no previous adjustment on this item
            release_msg = self.release_seats(item)

        old_product = item.product
        item.product = new_product
        item.save()
        reserve_msg = self.reserve_seats(item)

        msg += 'Moved %s to %s\n' % (old_product, new_product)
        msg += release_msg + reserve_msg

        self.add_history(item, Adjustment.MOVED, msg)

        self.send_message(msg)
        return 'Order item %s was successfully moved to %s.' % (old_product, new_product)

class AdjustmentRefundRequestForm(BaseAdjustmentForm):
    notes = forms.CharField(widget=forms.Textarea)

    def do_it(self):
        cd = self.cleaned_data
        items = self.get_items()

        for item in items:
            adjust_total_sold = True
            if Adjustment.objects.filter(item=item) and item.adjustment.status == Adjustment.REFUND_REQUESTED:   # already requested
                adjust_total_sold = False

            self.add_history(item, Adjustment.REFUND_REQUESTED, cd['notes'])

            if adjust_total_sold:
                # Update Inventory
                p = item.product.productvariation.parent.product
                p.total_sold -= item.quantity
                p.save()

        self.send_message('Items requested to be refunded/voided for the following reason:\n\n%s' % cd['notes'],
            prefix='Refund Request for Order')
        return 'Your refund request has been sent'

class AdjustmentRefundForm(BaseAdjustmentForm):

    def __init__(self, request, order, *args, **kwargs):
        super(AdjustmentRefundForm, self).__init__(request, order, *args, **kwargs)
        biggest_payment = self.biggest_payment()
        if biggest_payment:
            self.fields['amount'].initial = biggest_payment.amount.quantize(Decimal('.01'), ROUND_HALF_UP)

    CHOICES = (
        ('refund', 'Refund'),
        ('reject', 'Reject'),
        ('void', 'Void'),
    )
    action = forms.ChoiceField(choices=CHOICES)
    amount = forms.DecimalField(decimal_places=2, help_text="Amount ignored if Rejecting or Voiding")
    notes = forms.CharField(label="Additional notes for future reference", widget=forms.Textarea, required=False)

    def extra_row(self):
        s = """<tr><th>Order Timestamp</th><td>%s</td></tr>""" % self.order.time_stamp
        return s

    def biggest_payment(self):
        """Return the largest payment made since there can be 0.00 payments on an order."""
        max_paid = max([p.amount for p in self.order.payments_completed()])
        for p in self.order.payments.all():
            if p.amount == max_paid:
                return p
        return None

    def clean(self):
        cd = self.cleaned_data

        cd['payment'] = self.biggest_payment()
        if cd['payment'] is None:
            raise forms.ValidationError('No valid payment on account for this order.')

        return cd

    def do_it(self):
        cd = self.cleaned_data

        def make_call(x_type, amount=None):
            GROUP = 'PAYMENT_AUTHORIZENET'
            TRANKEY = config_get(GROUP, 'TRANKEY').value
            LOGIN = config_get(GROUP, 'LOGIN').value
            WE_ARE_LIVE = config_get(GROUP, 'LIVE').value
            TEST_URL = config_get(GROUP, 'CONNECTION_TEST').value
            LIVE_URL = config_get(GROUP, 'CONNECTION').value

            THE_URL = LIVE_URL if WE_ARE_LIVE else TEST_URL

            payment = cd['payment']
            cc = payment.credit_card

            data = {
                'x_card_num': cc.display_cc,
                'x_trans_id': payment.transaction_id,
                'x_login': LOGIN,
                'x_tran_key': TRANKEY,
                'x_delim_data': 'TRUE',
                'x_delim_char': '|',
                'x_type': x_type
            }

            if amount:
                data['x_amount'] = amount
            req = urllib2.Request(url=THE_URL, data=urlencode(data))
            f = urllib2.urlopen(req)
            response = f.read()
            response_code = int(response.split('|')[0])
            success = response_code == 1
            return (success, response)

        successful = True
        notes = cd['notes']
        response = ''
        if cd['action'] == 'refund':
            new_status = Adjustment.REFUNDED
            successful, response = make_call('CREDIT', amount=str(cd['amount']))

            # shoot an email to the customer if successful
            if successful:
                order = self.get_items()[0].order
                if order.contact.email:
                    success_message = 'Dear Customer,\n\nRefund of $%s towards Order #%s has been successfully processed.\n\n%s\n\nPlease wait for 5 business days, for the refund to appear on your account.\n\n' %\
                        (str(cd['amount']), order.id, notes)
                    success_message += response
                    success_message += '\n\nBest,\nSan Francisco Shuttle Tours\n\n'
                    helper_send_mail("San Francisco Shuttle Tours - Refund processed",
                        success_message, django_settings.DEFAULT_FROM_EMAIL, [order.contact.email])
        elif cd['action'] == 'void':
            new_status = Adjustment.VOIDED
            successful, response = make_call('VOID')

            # shoot an email to the customer if successful
            if successful:
                order = self.get_items()[0].order
                if order.contact.email:
                    success_message = 'Dear Customer,\n\nThe credit card charge of $%s towards Order #%s has been successfully voided.\n\n%s\n\n' %\
                        (str(cd['amount']), order.id, notes)
                    success_message += response
                    success_message += '\n\nBest,\nSan Francisco Shuttle Tours\n\n'
                    helper_send_mail("San Francisco Shuttle Tours - Charge voided",
                        success_message, django_settings.DEFAULT_FROM_EMAIL, [order.contact.email])
        elif cd['action'] == 'reject':
            new_status = Adjustment.REFUND_REQUEST_REJECTED

        if not successful:
            raise AuthorizeNetError(response)

        if response:
            notes += ' -- ' + response
        msg = 'The following items were %sed\n' % cd['action'].title()
        items = self.get_items()
        for item in items:
            msg += '%s\n' % unicode(item)
            self.add_history(item, new_status, notes)

        msg += 'Additional Information:\n%s' % notes
        self.send_message(msg)

        return 'Item %sed. Extra Info: %s' % (cd['action'].title(), notes)

class AdjustmentCreditVoucherForm(BaseAdjustmentForm):

    CHOICES = (
        (Adjustment.VOUCHER_STANDBY_CREATED, 'Standby Basis'),
        (Adjustment.VOUCHER_OK_TO_BOOK, 'OK to Book Seat'),
        (Adjustment.VOUCHER_STANDBY_USED, 'Standby Used'),
    )
    STANDBY_IDS = [choice[0] for choice in CHOICES]
    voucher_type = forms.ChoiceField(choices=CHOICES, help_text="If you want to record the date/time this voucher was used, <br />please use the Change Date/Time button.")
    notes = forms.CharField(label="Additional notes for future reference", widget=forms.Textarea, required=False)

    def do_it(self):
        cd = self.cleaned_data
        display = ''
        for id, txt in AdjustmentCreditVoucherForm.CHOICES:
            if id == int(cd['voucher_type']):
                display = txt
        items = self.get_items()
        msg = 'The following items were assigned vouchers of "%s"\n' % display
        voucher_status_ids = [choice[0] for choice in self.CHOICES]
        for item in items:
            msg += '%s\n' % unicode(item)
            release_message = ''
            if cd['voucher_type'] != Adjustment.VOUCHER_STANDBY_USED:
                if cd['notes']:
                    release_message = ' :: '
                release_message += self.release_seats(item)
            msg += release_message
            self.add_history(item, cd['voucher_type'], cd['notes'] + release_message )

        msg += '\n\nAdditional Notes: %s' % cd['notes']
        self.send_message(msg)
        return 'Items changed to %s' % display

    def do_it_noshow(self, item_id, note):
        """
        Hack to keep code DRY. This is called from the checkin finalization screen when the user "finalizes" a
        tour_product.
        """
        display = ''
        voucher_type = Adjustment.VOUCHER_STANDBY_CREATED
        for id, txt in AdjustmentCreditVoucherForm.CHOICES:
            if id == int(voucher_type):
                display = txt
        items = [OrderItem.objects.get(id=int(item_id))]
        msg = 'The following items were assigned vouchers of "%s"\n' % display
        voucher_status_ids = [choice[0] for choice in self.CHOICES]
        for item in items:
            msg += '%s\n' % unicode(item)
            release_message = ''
            if note:
                release_message = ' :: '

            """Subtract quantity of item from total seats sold"""
            p = item.product.productvariation.parent.product
            p.total_sold -= item.quantity
            p.save()
            release_message += '%d seats added back to %s\n' % (int(item.quantity), p)

            msg += release_message
            self.add_history(item, voucher_type, note + release_message )

        msg += '\n\nAdditional Notes: %s' % note
        self.send_message(msg, prefix='Reservation')
        return 'Items changed to %s' % display
