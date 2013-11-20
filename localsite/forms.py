from datetime import date, datetime
import logging
import urllib2
import calendar
from urllib import urlencode
from livesettings import config_get
from livesettings import config_value
from decimal import Decimal, ROUND_HALF_UP
from l10n.utils import moneyfmt


from django import forms
from django.utils.safestring import mark_safe
from django.core.mail import send_mail
from django.conf import settings as django_settings
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _, ugettext
from django.utils.encoding import smart_str
from apps.l10n.models import Country

from common.helper import start_thread, send_mail as helper_send_mail
from satchmo_store.shop.models import OrderItem, Config
from satchmo_store.shop.utils import clean_field
from satchmo_utils.views import CreditCard


from product.models import Option
from localsite.models import TourSchedule, TourProduct, OverbookingAttempt, TourType
from localsite.session import SessionManager
from localsite.exceptions import ComboScheduleNotBookable
from adjustments.models import Adjustment, AdjustmentHistory


NUMBER_OF_TICKETS_CHOICES = []
for x in xrange(0, 21):
    NUMBER_OF_TICKETS_CHOICES.append((x, x))

DAY_OF_MONTH_CHOICES = []
for x in xrange(1, 32):
    DAY_OF_MONTH_CHOICES.append((x, x))

class BookItForm(forms.Form):

    MONTH_CHOICES = [(1,'January'),
            (2,'February'),
            (3,'March'),
            (4,'April'),
            (5,'May'),
            (6,'June'),
            (7,'July'),
            (8,'August'),
            (9,'September'),
            (10,'October'),
            (11,'November'),
            (12,'December')
        ]

    def __init__(self, tour_type=None, from_admin=False, request=None, *args, **kwargs):
        super(BookItForm, self).__init__(*args, **kwargs)
        self.from_admin = from_admin
        self.tour_type = tour_type
        self.options = tour_type.get_options()
        self.request = request  # for session access

        # Set the options dynamically for this tour typ
        for option in self.options:
            option.field_name = 'option_%d' % option.id
            if tour_type.seats_available < len(NUMBER_OF_TICKETS_CHOICES):
                num_ticket_choices = []
                for x in xrange(0, tour_type.seats_available + 1):
                    num_ticket_choices.append((x, x))
            else:
                num_ticket_choices = NUMBER_OF_TICKETS_CHOICES
            if tour_type.sell_in_even_quantities_only:
                num_ticket_choices = [num for num in num_ticket_choices if num[0] % 2 == 0]
            self.fields[option.field_name] = forms.ChoiceField(required=False, initial=0, choices=num_ticket_choices,
                                                               widget=forms.Select(attrs={'rel': option.name}))

        # for mobile only, hence not required. Auto-fills to current day/month/year
        if self.__kick_in_mobile_logic():
            current_time = datetime.now()
            year_choices = [
                (current_time.year, '%s' % current_time.year),
                (current_time.year + 1, '%s' % (current_time.year+1))
            ]

            self.fields['day_of_month'] = forms.ChoiceField(required=False, choices=DAY_OF_MONTH_CHOICES, initial=current_time.day)
            self.fields['month'] = forms.ChoiceField(required=False, choices=self.MONTH_CHOICES, initial=current_time.month)
            self.fields['year'] = forms.ChoiceField(required=False, choices=year_choices)

        # get valid schedules for given date or default to today
        SCHEDULE_CHOICES = []
        schedule_date = date.today()

        try:    # putting a try catch block since tour_date is coming in as junk sometimes. See exceptions Feb. 21, 2011
            if 'tour_date' in self.data and self.data['tour_date']:
                month, day, year = map(int, self.data['tour_date'].split('/'))
            elif 'day_of_month' in self.data and self.data['day_of_month']: # mobile request
                month, day, year = map(int, [self.data['month'], self.data['day_of_month'], self.data['year']])
            schedule_date = date(year, month, day)
        except:
            logging.error('Invalid tour_date: %s' % self.data.get('tour_date'))    # schedule_date will get set to today

        for schedule in tour_type.get_schedule_for_day(schedule_date):
            SCHEDULE_CHOICES.append([schedule.id, schedule.pretty_time])
        self.fields['schedule'].choices = SCHEDULE_CHOICES
        # If only one choice, it should be selected by default
        if len(SCHEDULE_CHOICES) == 1:
            self.fields['schedule'].initial = SCHEDULE_CHOICES[0][0]

    tour_date = forms.DateField(widget=forms.HiddenInput, required=False)
    schedule = forms.ChoiceField(required=True, choices=[], widget=forms.RadioSelect, error_messages={
        'required': 'Please select a time.',
        'invalid_choice': 'That is not a valid time. Please select another time.'
    })
    ticket_types_specified = forms.BooleanField(required=False, error_messages={
        'required': 'Please specify the number of tickets you want to purchase.',
    })

    def __kick_in_mobile_logic(self):
        return self.request and self.request.mobile and not self.from_admin

    def clean_tour_date(self):
        """Only kicks in for non-mobile. For mobile see def clean()"""
        if not self.__kick_in_mobile_logic():
            if not self.cleaned_data.get('tour_date'):
                raise forms.ValidationError('Please select a date from the calendar.')

            tour_date = self.cleaned_data['tour_date']
            if tour_date < date.today():
                raise forms.ValidationError('Please select a date that is later than today.')
            return tour_date

    def clean_ticket_types_specified(self):
        specified = False
        for o in self.options:
            if o.field_name in self.data and int(self.data[o.field_name]) > 0:
                specified = True
        if not specified:
            raise forms.ValidationError(self.fields['ticket_types_specified'].error_messages['required'])
        return True

    def clean(self):
        cd = self.cleaned_data

        # update cd with tour_date if mobile logic is to kick in
        if self.__kick_in_mobile_logic():
            # print self.cleaned_data
            if not self.cleaned_data.get('day_of_month') or not self.cleaned_data.get('month') or not self.cleaned_data.get('year'):
                raise forms.ValidationError('Please select a tour date.')

            try:
                tour_date = datetime.strptime('%s %s %s' % (self.cleaned_data['month'], self.cleaned_data['day_of_month'], self.cleaned_data['year']), '%m %d %Y').date()
            except:
                raise forms.ValidationError('Please select a valid tour date.')
            if tour_date < date.today():
                raise forms.ValidationError('Please select a date that is later than today.')
            cd['tour_date'] = tour_date

        total_tickets = 0
        for o in self.options:
            try:
                total_tickets += int(cd[o.field_name])
            except ValueError:
                # Might not be a int value in cd for this field_name
                pass

        # no need to enforce name rule when doing moves etc. in admin.
        if not self.from_admin and self.tour_type.requires_names:
            names = []
            for option in self.options:
                names += self.request.POST.getlist(option.name + '-names')
            names = filter(lambda x: x.strip() != '', names)
            if len(names) != total_tickets:
                raise forms.ValidationError('You must enter names for each ticket you purchase.')

        if cd.get('schedule'):
            schedule = TourSchedule.objects.get(active=True, id=int(cd['schedule']))

            if 'tour_date' in cd and schedule:
                # Inventory check
                if self.tour_type.is_combo:
                    try:
                        tour_products = self.tour_type.get_combo_products(cd['tour_date'])
                    except ComboScheduleNotBookable:
                        raise forms.ValidationError('We are unable to book this Combo given the tour day/time constraints. Please select another date.')
                else:
                    tour_products = [self.tour_type.get_product(cd['tour_date'], schedule=schedule),]

                for tour_product in tour_products:
                    if not tour_product.seats_left(total_tickets):
                        if not self.from_admin:
                            # if overbook attempt already recorded
                            if self.request and not SessionManager(self.request).do_record_overbook_attempt(tour_product):
                                pass
                            else:
                                overbook = OverbookingAttempt.objects.create(tour=tour_product, num_overbooked=total_tickets - tour_product.seats_available())
                                overbook.save()
                                tour_product.overbooking_attempts += total_tickets - tour_product.seats_available()
                                tour_product.save()

                        raise forms.ValidationError('The tour date/time you selected is SOLD OUT, however, \
                            there are seats available on other days/times. Please try another selection.')

        return cd

    def option_fields(self):
        fields = []
        for o in self.options:
            bf = self.__getitem__(o.field_name)
            fields.append({
                'id': o.id,
                'label': o.name,
                'price': o.price,
                'html': bf.as_widget(),
                })
        return fields

    def get_products(self):
        cd = self.cleaned_data
        schedule = TourSchedule.objects.get(active=True, id=int(cd['schedule']))
        product = self.tour_type.get_product(cd['tour_date'], schedule=schedule)
        cp = product.product.configurableproduct
        products = []
        for o in self.options:
            try:
                quantity = int(cd[o.field_name])
            except ValueError:
                # Might not be a int value in cd for this field_name
                quantity = 0
            if quantity > 0:
                product = cp.get_product_from_options([o,])
                products.append({
                    'quantity': quantity,
                    'product': product
                })
        return products


class PassengerInformationForm(forms.Form):
    first_name = forms.CharField(label='(Optional) Passenger First Name', max_length=30, required=False)
    last_name = forms.CharField(label='Passenger Last Name', max_length=30)
    email = forms.EmailField(label='(Optional) Email address', required=False)
    cell_phone = forms.CharField(label='(Optional) Cell Phone', required=False, help_text='(Needed to possibly contact you)', max_length=30)


class AuthorizeNetError(Exception):
    """Raised if Authorize.net transaction was not successful"""
    pass


class BaseUserAdjustmentForm(forms.Form):

    def __init__(self, request, order_item, action, *args, **kwargs):
        self.request = request
        self.order = order_item.order
        self.order.contact = order_item.order.contact
        self.order_item = order_item
        self.action = action
        super(BaseUserAdjustmentForm, self).__init__(*args, **kwargs)
        # Setup valid item choices

        self.fields['item'].initial = self.order_item.id
        self.fields['action_type'].initial = self.action

    item = forms.CharField(widget=forms.HiddenInput, required=False)
    action_type = forms.CharField(widget=forms.HiddenInput)
    amount = forms.CharField(widget=forms.HiddenInput, required=False)

    def get_items(self):
        cd = self.cleaned_data
        items = []
        items.append(OrderItem.objects.get(id=int(cd['item'])))
        optionkey = items[0].product.productvariation.optionkey
        tp = items[0].product.productvariation.parent.product.tourproduct
        if tp.tour_type.is_combo:
            # get all combo products
            combo_products = map(lambda x: x.product, tp.tour_type.get_combo_products(day=tp.day))

            # filter all items containing combo_products
            combo_items = items[0].order.orderitem_set.filter(product__productvariation__parent__product__in=combo_products)

            # filter items only with the same option group
            combo_items = filter(lambda x: x.product.productvariation.optionkey == optionkey, combo_items)
            items += list(combo_items)
        return items

    def send_message(self, message, prefix='Reservation'):
        subject = "%s #%d changed by customer: %s" % (prefix, self.order.id, self.order.contact.full_name)
        pre_msg = "%s #%d from customer %s was changed by them\n\n" % (prefix, self.order.id, self.order.contact.full_name)
        mail_message = '%s %s' % (pre_msg, message)
        mail_message += '\n\nhttp://%s%s' % (Site.objects.get_current().domain,
            reverse('order_detail', args=[self.order.id, ]))
        start_thread(send_mail, subject, mail_message, django_settings.DEFAULT_FROM_EMAIL,
            [django_settings.DEFAULT_TO_EMAIL, ] if django_settings.IS_PROD else ['sfst@tivix.com'])

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
        history.from_status = old_status
        history.to_status = adjustment.status
        history.notes = notes
        history.save()
        return history

    def release_seats(self, item):
        """Subtract quantity of item from total seats sold"""
        p = item.product.productvariation.parent.product
        p.total_sold -= item.quantity
        if p.total_sold < 0:
            p.total_sold = 0
        p.save()
        return '%d seats added back to %s\n' % (int(item.quantity), p)

    def reserve_seats(self, item):
        """Add quantity of item to total seats sold"""
        p = item.product.productvariation.parent.product
        p.total_sold += item.quantity
        p.save()
        return '%d seats subtracted from %s\n' % (int(item.quantity), p)

class UserAdjustmentRefundForm(BaseUserAdjustmentForm):

    def __init__(self, request, order_item, action, *args, **kwargs):
        super(UserAdjustmentRefundForm, self).__init__(request, order_item, action, *args, **kwargs)
        self.fields['amount'].initial = self.order_item.line_total

    def clean(self):
        cd = self.cleaned_data
        cd['payment'] = self.order.payments.all()[:1][0]
        if cd['payment'] is None:
            raise forms.ValidationError('No valid payment on account for this order.')
        item = cd['item']

        if cd['action_type'] == 'refund':
            amount = 0
            amount = Decimal(amount)
            order_item = OrderItem.objects.get(id=item)
            amount += order_item.sub_total
            amount = str(amount)
            amount = Decimal(amount)
            amount = amount * Decimal('.7')
            cd['amount'] = amount.quantize(Decimal('.01'), rounding=ROUND_HALF_UP)
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

            if cd['amount'] and cd['action_type'] == 'refund':
                data['x_amount'] = cd['amount']
            req = urllib2.Request(url=THE_URL, data=urlencode(data))
            f = urllib2.urlopen(req)
            response = f.read()
            response_code = int(response.split('|')[0])
            success = response_code == 1
            return (success, response)

        successful = True
        response = ''
        items = self.get_items()

        if cd['action_type'] == 'refund':
            successful, response = make_call('CREDIT', amount=str(cd['amount']))
            # shoot an email to the customer if successful
            if successful:
                new_status = Adjustment.REFUNDED
                for item in items:
                    self.release_seats(item)
                order = self.get_items()[0].order
                if order.contact.email:
                    success_message = 'Dear Customer,\n\nRefund of $%s towards Order #%s has been successfully processed.\n\nPlease wait for 5 business days, for the refund to appear on your account.\n\n' %\
                        (str(cd['amount']), order.id)
                    success_message += response
                    success_message += '\n\nBest,\nSan Francisco Shuttle Tours\n\n'
                    helper_send_mail("San Francisco Shuttle Tours - Refund processed",
                        success_message, django_settings.DEFAULT_FROM_EMAIL, [order.contact.email])

        else:
            successful, response = make_call('VOID')
            # shoot an email to the customer if successful
            if successful:
                new_status = Adjustment.VOIDED
                # all items in order are voided so we don't need to use get_items
                for item in items[0].order.orderitem_set.all():
                    self.release_seats(item)
                order = self.get_items()[0].order
                order_payment = order.payments.all()[:1][0]
                if order.contact.email:
                    success_message = 'Dear Customer,\n\nYour order #%s has been voided and the amount of $%s has been credited to your card.' %\
                        (order.id, order_payment.amount)
                    success_message += response
                    success_message += '\n\nBest,\nSan Francisco Shuttle Tours\n\n'
                    helper_send_mail("San Francisco Shuttle Tours - Charge voided",
                        success_message, django_settings.DEFAULT_FROM_EMAIL, [order.contact.email])
            else:
                for item in items[0].order.orderitem_set.all():
                    item.order.orderhash.void_failed = True

        if not successful:
            raise AuthorizeNetError(response)

        if cd['action_type'] == 'refund':
            msg = 'The following items were %sed\n' % ('Refund')
            items = self.get_items()
            for item in items:
                msg += '%s\n' % unicode(item)
                self.add_history(item, new_status)

            self.send_message(msg)

            return 'Item %sed.' % ('Refund')
        else:
            msg = 'The following order was voided: %s' % (order.id)
            for item in order.orderitem_set.all():
                self.add_history(item, new_status)
            self.send_message(msg)

            return 'Order #%s was voided and %s was credited towards your card' % (order.id, moneyfmt(order_payment.amount))


def get_initial_schedules(tour_type):
    schedules = tour_type.get_schedule_for_day(date.today())
    return [(s.id, s.pretty_time) for s in schedules]

class UserAdjustmentMoveForm(BaseUserAdjustmentForm):

    def __init__(self, request, order_item, action, *args, **kwargs):
        super(UserAdjustmentMoveForm, self).__init__(request, order_item, action, *args, **kwargs)
        self.fields['tour_schedule'].choices = get_initial_schedules(self.order_item.product.productvariation.parent.product.tourproduct.tour_type)
        self.fields['tour_type'].initial = order_item.product.productvariation.parent.product.tourproduct.tour_type
    tour_type = forms.ModelChoiceField(queryset=TourType.objects.filter(active=True), widget=forms.HiddenInput)
    day = forms.DateField(required=False)
    tour_schedule = forms.ModelChoiceField(queryset=TourSchedule.objects.filter(active=True))

    def get_new_tour_product_dict(self, new_product):
        new_tourproduct = new_product.productvariation.parent.product.tourproduct
        combo_products_dict = {new_tourproduct.tour_type: new_tourproduct}
        if new_tourproduct.tour_type.is_combo:
            combo_products = new_tourproduct.tour_type.get_combo_products(day=new_tourproduct.day, create=True)
            for cp in combo_products:
                combo_products_dict[cp.tour_type] = cp
        return combo_products_dict

    def clean(self):
        cd = self.cleaned_data
        cd['payment'] = self.order.payments.all()[:1][0]
        if cd['payment'] is None:
            raise forms.ValidationError('No valid payment on account for this order.')
        if cd['day'] is None or cd['day'] == '':
            raise forms.ValidationError('Please enter a valid day to move your tour to.')
        if 'day' in cd and 'tour_schedule' in cd and 'item' in cd:
            items = self.get_items()
            new_tour_product = cd['tour_type'].get_product(cd['day'], schedule=cd['tour_schedule'])
            new_product = new_tour_product.get_variation(items[0].product.productvariation.optionkey)
            new_tour_product_dict = self.get_new_tour_product_dict(new_product)

            for item in items:
                # Convert old optionkey into new option key
                # new_tour_product = cd['tour_type'].get_product(cd['day'], schedule=cd['tour_schedule'])

                tour_type = item.product.productvariation.parent.product.tourproduct.tour_type
                new_tour_product = new_tour_product_dict[tour_type]

                try:
                    if not new_tour_product.seats_left(item.quantity):
                        raise forms.ValidationError('The tour date/time you selected is SOLD OUT, however, \
                            there are seats available on other days/times. Please try another selection.')
                except TourProduct.DoesNotExist:
                    new_tour_product.tour_type.generate_future_tour_products(days=90)
                    if not new_tour_product.seats_left(item.quantity):
                        raise forms.ValidationError('The tour date/time you selected is SOLD OUT, however, \
                            there are seats available on other days/times. Please try another selection.')
        return cd


MONTHS = [(month, '%02d' % month) for month in range(1, 13)]

CREDITCHOICES = (
            (('Visa', 'Visa')),
            (('Mastercard', 'Mastercard')),
            (('Discover', 'Discover'))
)
shop = Config.objects.get_current()

class PaymentAndCardholderInfoForm(forms.Form):
    first_name = forms.CharField(max_length=30, label=_('First Name'))
    last_name = forms.CharField(max_length=30, label=_('Last Name'))
    postal_code = forms.CharField(max_length=10, label=_('ZIP code/Postcode'))
    street1 = forms.CharField(max_length=30, label=_('Street'))
    city = forms.CharField(max_length=30, label=_('City'))
    state = forms.CharField(max_length=30, label=_('State'))
    country = forms.ModelChoiceField(Country.objects.all(), label=_('Country'), empty_label=None)

    credit_type = forms.ChoiceField()
    credit_number = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    month_expires = forms.ChoiceField(choices=MONTHS)
    year_expires = forms.ChoiceField()
    ccv = forms.CharField(max_length=4, label='CVV Code', widget=forms.TextInput(attrs={'autocomplete': 'off'}))


    def __init__(self, *args, **kwargs):
        super(PaymentAndCardholderInfoForm, self).__init__(*args, **kwargs)

        self.cc = None

        self.fields['credit_type'].choices = CREDITCHOICES

        num_years = config_value('PAYMENT', 'CC_NUM_YEARS')
        year_now = date.today().year
        self.fields['year_expires'].choices = [(year, year) for year in range(year_now, year_now + num_years + 1)]

    def clean_credit_number(self):
        """ Check if credit card is valid. """
        data = self.cleaned_data
        credit_number = data['credit_number']
        card = CreditCard(credit_number, data['credit_type'])
        results, msg = card.verifyCardTypeandNumber()
        if not results:
            raise forms.ValidationError(msg)

        return credit_number

    def clean_month_expires(self):
        if len(self.cleaned_data['month_expires']) == 1:
            month = str(0) + self.cleaned_data['month_expires']
        else:
            month = self.cleaned_data['month_expires']
        return month

    def clean_year_expires(self):
        """ Check if credit card has expired. """
        month = int(self.cleaned_data['month_expires'])
        year = int(self.cleaned_data['year_expires'])
        max_day = calendar.monthrange(year, month)[1]
        if date.today() > date(year=year, month=month, day=max_day):
            raise forms.ValidationError(_('Your card has expired.'))
        return self.cleaned_data['year_expires']

    def clean_ccv(self):
        """ Validate a proper CCV is entered. Remember it can have a leading 0 so don't convert to int and return it"""
        try:
            check = int(self.cleaned_data['ccv'])
            return self.cleaned_data['ccv'].strip()
        except ValueError:
            raise forms.ValidationError(_('Invalid ccv.'))

class PaymentAndMoveForm(UserAdjustmentMoveForm, PaymentAndCardholderInfoForm):
    def __init__(self, request, order_item, action, *args, **kwargs):
        super(PaymentAndMoveForm, self).__init__(request, order_item, action, *args, **kwargs)

    def clean(self):
        super(PaymentAndMoveForm, self).clean()
        cd = self.cleaned_data
        cd['payment'] = self.order.payments.all()[:1][0]
        if cd['payment'] is None:
            raise forms.ValidationError('No valid payment on account for this order.')
        if 'day' in cd and 'tour_schedule' in cd and 'item' in cd:
            items = self.get_items()

            # Now collect data for BookItForm
            data = {'tour_date': cd['day'].strftime('%m/%d/%Y'), 'schedule': cd['tour_schedule'].id}

            # Convert old optionkey into new option key
            new_tour_product = cd['tour_type'].get_product(cd['day'], schedule=cd['tour_schedule'])
            new_product = new_tour_product.get_variation(items[0].product.productvariation.optionkey)
            new_tour_product_dict = self.get_new_tour_product_dict(new_product)

            for item in items:
                tour_type = item.product.productvariation.parent.product.tourproduct.tour_type
                item_new_tour_product = new_tour_product_dict[tour_type]

                try:
                    if not item_new_tour_product.seats_left(item.quantity):
                        raise forms.ValidationError('The tour date/time you selected is SOLD OUT, however, \
                            there are seats available on other days/times. Please try another selection.')
                except TourProduct.DoesNotExist:
                    item_new_tour_product.tour_type.generate_future_tour_products(days=90)
                    if not item_new_tour_product.seats_left(item.quantity):
                        raise forms.ValidationError('The tour date/time you selected is SOLD OUT, however, \
                            there are seats available on other days/times. Please try another selection.')

            item = items[0]
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
                amount = 0
                amount = Decimal(amount)
                amount += (item.quantity * 15)
                cd['amount'] = amount.quantize(Decimal('.01'), rounding=ROUND_HALF_UP)
            else:
                raise forms.ValidationError(self.book_it.errors)
        return cd

    def do_it(self):
        msg = ''
        cd = self.cleaned_data

        def make_call(x_type, amount=None):
            GROUP = 'PAYMENT_AUTHORIZENET'
            TRANKEY = config_get(GROUP, 'TRANKEY').value
            LOGIN = config_get(GROUP, 'LOGIN').value
            WE_ARE_LIVE = config_get(GROUP, 'LIVE').value
            TEST_URL = config_get(GROUP, 'CONNECTION_TEST').value
            LIVE_URL = config_get(GROUP, 'CONNECTION').value

            THE_URL = LIVE_URL if WE_ARE_LIVE else TEST_URL

            data = {
                'x_login': LOGIN,
                'x_tran_key': TRANKEY,
                'x_delim_data': 'TRUE',
                'x_delim_char': '|',
                'x_type': x_type,
                'x_method': 'CC',
                'x_card_num': cd['credit_number'],
                'x_card_code': cd['ccv'],
                'x_exp_date': cd['month_expires'] + cd['year_expires'][-2:],
                'x_first_name': cd['first_name'],
                'x_last_name': cd['last_name'],
                'x_address': cd['street1'],
                'x_city': smart_str(cd['city']),
                'x_state': cd['state'],
                'x_zip': cd['postal_code'],
                'x_country': cd['country']

            }
            if cd['amount']:
                data['x_amount'] = cd['amount']
            req = urllib2.Request(url=THE_URL, data=urlencode(data))
            f = urllib2.urlopen(req)
            response = f.read()
            response_code = int(response.split('|')[0])
            success = response_code == 1
            return (success, response)

        new_product = self.book_it.get_products()[0]['product']

        # build dict with new tour product per each tour type from combo
        new_tourproduct = new_product.productvariation.parent.product.tourproduct
        combo_products_dict = {new_tourproduct.tour_type: new_product}
        if new_tourproduct.tour_type.is_combo:
            combo_products = new_tourproduct.tour_type.get_combo_products(day=new_tourproduct.day, create=True)
            for cp in combo_products:
                combo_products_dict[cp.tour_type] = cp.get_variation(new_product.productvariation.optionkey)

        for item in self.get_items():
            release_msg = ''
            try:
                # don't release seats if item was in a standby status since seats were already released
                if item.adjustment:
                    release_msg = self.release_seats(item)
            except Adjustment.DoesNotExist:
                # This get's raised if there is no previous adjustment on this item
                release_msg = self.release_seats(item)

            tour_type = item.product.productvariation.parent.product.tourproduct.tour_type
            old_product = item.product
            new_product = combo_products_dict[tour_type]
            item.product = new_product
            item.save()

            reserve_msg = self.reserve_seats(item)
            item_msg = ''
            item_msg += 'Moved %s to %s\n' % (old_product, new_product)
            item_msg += release_msg + reserve_msg

            self.add_history(item, Adjustment.MOVED, item_msg)
            msg += item_msg

        self.send_message(msg)

        successful = True
        response = ''
        successful, response = make_call('AUTH_CAPTURE', amount=str(cd['amount']))

        # shoot an email to the customer if successful
        if successful:
            order = self.get_items()[0].order
            if order.contact.email:
                success_message = 'Dear Customer,\n\na charge of $%s towards Order #%s has been successfully processed.\n\nOrder item %s was successfully moved to %s.' % (str(cd['amount']), order.id, old_product, new_product)
                success_message += response
                success_message += '\n\nThank You,\nSF/NY Shuttle Tours and Wine Country Tour Shuttle\n\n'
                helper_send_mail("Customer Move Tour has been Processed!",
                    success_message, django_settings.DEFAULT_FROM_EMAIL, [order.contact.email])
        if not successful:
            raise AuthorizeNetError(response)
        return 'Order item %s was successfully moved to %s.  Your credit card has been charged $%s' % (old_product, new_product, cd['amount'])


class ContactForm(forms.Form):
    phone_number = forms.CharField(label=_('Phone number'), max_length=30, required=False)
    email = forms.EmailField(label=_('Email address'), max_length=30, required=False)

    def send_mails(self):
        cd = self.cleaned_data
        if not cd['phone_number'] and not cd['email']:
            return
        body = 'Here is the customers phone and email\n\n%(phone_number)s\n%(email)s' % cd
        start_thread(send_mail, _('CUSTOMER HAD ISSUE BOOKING A TOUR'), body, django_settings.DEFAULT_FROM_EMAIL,
            [django_settings.DEFAULT_TO_EMAIL, ] if django_settings.IS_PROD else ['sfst@tivix.com'])

