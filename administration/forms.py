from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import HiddenInput

from administration.models import ConciergeMessage, OrderCheckin, OrderItemCheckin
from resellers.models import Reseller, ResellerCategory
from localsite.models import TourSchedule, DayOfWeek


class ResellerApprovalForm(forms.Form):
    username = forms.CharField(max_length=254)
    password = forms.CharField(max_length=30)
    discount = forms.DecimalField(max_digits=5, decimal_places=2)
    commission = forms.DecimalField(max_digits=5, decimal_places=2)
    reseller_type = forms.ChoiceField(choices=Reseller.RESELLER_TYPE_CHOICES)
    category = forms.ModelChoiceField(queryset=ResellerCategory.objects.all())

    def clean_username(self):
        username = self.cleaned_data.get('username')
        existing_count = User.objects.filter(username=username).count()
        if existing_count > 0:
            raise forms.ValidationError('That username is already taken.')
        return username


class GlobalMessageForm(forms.ModelForm):
    not_notify_email = forms.BooleanField(required=False)
    is_global_note = forms.CharField(widget=HiddenInput, initial='1')

    class Meta:
        model = ConciergeMessage
        fields = ('message',)


class GlobalEmailForm(forms.Form):
    is_global_email = forms.CharField(widget=HiddenInput, initial='1')
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)


class BulkInventoryUpdator(forms.Form):
    tour_schedule = forms.ModelChoiceField(queryset=TourSchedule.objects.filter(active=True, tour_type__is_combo=False, tour_type__active=True))
    inventory = forms.IntegerField()
    start_date = forms.DateField()
    end_date = forms.DateField()
    days_of_week = forms.ModelMultipleChoiceField(queryset=DayOfWeek.objects.all())

    def clean_inventory(self):
        if self.cleaned_data.get('inventory') and self.cleaned_data.get('inventory') < 0:
            raise forms.ValidationError('Inventory can\'t be less than 0!')
        return self.cleaned_data['inventory']

    def clean(self):
        if self.cleaned_data.get('start_date') and self.cleaned_data.get('end_date'):
            if self.cleaned_data.get('end_date') < self.cleaned_data.get('start_date'):
                raise forms.ValidationError('Start date needs to be less than or equal to end date')

        return self.cleaned_data


class AdvancedAnalyticsForm(forms.Form):
    """
    Form on homepage of administration screen for super-users to run to get country / state level segmentation
    data.
    """
    TYPE_ORDER_DATE = 1
    TYPE_TOUR_DATE = 2

    ORDER_DATE_TYPE_CHOICES = (
        (TYPE_ORDER_DATE, 'Order Date'),
        (TYPE_TOUR_DATE, 'Tour Date'),
    )

    from_date = forms.DateField()
    to_date = forms.DateField()
    exclude_usa = forms.BooleanField(label='Exclude the US in Country Chart?', required=False)
    order_date_type = forms.ChoiceField(choices=ORDER_DATE_TYPE_CHOICES, label='Report by:')

    def clean(self):
        if self.cleaned_data.get('from_date') and self.cleaned_data.get('to_date'):
            if self.cleaned_data.get('from_date') > self.cleaned_data.get('to_date'):
                raise forms.ValidationError('From date should be less than to date')

        return self.cleaned_data


class OrderCheckinForm(forms.ModelForm):
    class Meta:
        model = OrderCheckin
        fields = ('amount_taken_sales', 'amount_taken_change_order_fees', 'amount_type')

    def clean(self):
        """
        Both amount and type need to be provided
        """
        if self.cleaned_data.get('amount_taken_sales') or self.cleaned_data.get('amount_taken_change_order_fees') or\
                self.cleaned_data.get('amount_type'):
            if not ((self.cleaned_data.get('amount_taken_sales') or self.cleaned_data.get('amount_taken_sales') or
                    self.cleaned_data.get('amount_taken_change_order_fees')) and self.cleaned_data.get('amount_type')):
                raise forms.ValidationError('Both amount and type are needed if customer paid.')

        return self.cleaned_data


class EmailCustomerForm(forms.Form):
    """Rendered in a fragment that lets admins email messages to customers"""
    email_subject = forms.CharField(widget=forms.TextInput(attrs={'size': '100'}))
    email_body = forms.CharField(widget=forms.Textarea)


class LastNDaysStatsForm(forms.Form):
    last_n_days_stats = forms.IntegerField(initial=7)
