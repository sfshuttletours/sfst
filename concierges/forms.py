from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import HiddenInput
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.conf import settings as django_settings

from satchmo_store.contact.models import Contact, ContactRole

from common.helper import start_thread

from localsite.models import TourType
from concierges.models import Concierge, ConciergeCommission


class ConciergeInformationForm(forms.Form):
    
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    phone = forms.CharField(max_length=30)
    
    street = forms.CharField(max_length=80, required=False)
    city = forms.CharField(max_length=50, required=False)
    state = forms.CharField(max_length=50, required=False)
    postal_code = forms.CharField(max_length=30, label='Zip', required=False)
    
    hotel_name = forms.CharField(max_length=80)
    hotel_phone = forms.CharField(max_length=30)
    hotel_street = forms.CharField(max_length=80)
    hotel_city = forms.CharField(max_length=50)
    hotel_state = forms.CharField(max_length=50)
    hotel_postal_code = forms.CharField(max_length=30, label='Hotel Zip')
    
    email_notifications = forms.BooleanField(label='Would you like to be notified via email of all global and individual notices on your account?', required=False)
    send_checks_to = forms.ChoiceField(label='Where would you like your checks to be sent?', choices=Concierge.SEND_CHECKS_TO_CHOICES)
    
    frequency = forms.CharField(max_length=64, label='How often do you book our tours?', required=False)
    per_week = forms.CharField(max_length=32, label='What is the average number of tours you book per week?', required=False)
    
    image = forms.ImageField(required=False)
    
    def save(self, concierge):
        cd = self.cleaned_data
        
        if 'image' in cd and cd['image']:
            concierge.image = cd['image']
        concierge.email_notifications = cd['email_notifications']
        if 'send_checks_to' in cd:
            concierge.send_checks_to = cd['send_checks_to']
        concierge.frequency = cd['frequency']
        concierge.per_week = cd['per_week']
        concierge.hotel_name = cd['hotel_name']        
        concierge.save()
        
        contact = concierge.contact
        
        contact.first_name = cd['first_name']
        contact.last_name = cd['last_name']
        contact.save()
        
        home_phone = concierge.home_phone(create=True)
        home_phone.phone = cd['phone']
        home_phone.save()
        
        home_address = concierge.home_address(create=True)
        home_address.street1 = cd['street']
        home_address.city = cd['city']
        home_address.state = cd['state']
        home_address.postal_code = cd['postal_code']
        home_address.save()
        
        hotel_phone = concierge.hotel_phone(create=True)
        hotel_phone.phone = cd['hotel_phone']
        hotel_phone.save()
        
        hotel_address = concierge.hotel_address(create=True)
        hotel_address.street1 = cd['hotel_street']
        hotel_address.city = cd['hotel_city']
        hotel_address.state = cd['hotel_state']
        hotel_address.postal_code = cd['hotel_postal_code']
        hotel_address.save()
    
class ConciergeRegistrationForm(ConciergeInformationForm):
    def __init__(self, *args, **kwargs):
        super(ConciergeInformationForm, self).__init__(*args, **kwargs)
        self.fields['hotel_street'].label = 'Street'
        self.fields['hotel_city'].label = 'City'
        self.fields['hotel_state'].label = 'State'
        self.fields['hotel_postal_code'].label = 'Zip'
        self.fields['email_notifications'].label = 'I would like to be notified of all global and individual notices on my account.'
    
    email = forms.EmailField()
    username = forms.CharField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    send_checks_to_bool = forms.BooleanField(label='I would like checks to be sent to my address (not the hotel).', required=False)
    send_checks_to = forms.BooleanField(required=False) # to override
    booking_type = forms.ChoiceField(label='', choices=(
        (Concierge.BOOKING_TYPE_COMMISSION_CHECK, 'I want a commission check / I do not take deposits'),
        (Concierge.BOOKING_TYPE_DEPOSIT, 'I take deposits'),))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        existing_count = User.objects.filter(username=username).count()
        if existing_count > 0:
            raise forms.ValidationError('That username is already taken.')
        return username
            
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError("The two password fields didn't match.")
        return password2

    def save(self, site_skin):
        cd = self.cleaned_data

        user = User()
        user.username=cd['username']
        user.email = cd['email']
        user.first_name = cd['first_name']
        user.last_name = cd['last_name']
        user.is_active = True
        user.save()
        user.set_password(cd['password1'])
        
        contact = Contact()
        contact.user = user
        contact.role = ContactRole.objects.get(key='Concierge')
        contact.email = cd['email']
        contact.save()
        
        # the listeners.sfst_object_link creates the concierge and adds it to contact.concierge.
        concierge = contact.concierge
        concierge.site_skin = site_skin
        concierge.contact = contact
        concierge.booking_type = cd['booking_type']
        if 'send_checks_to_bool' in cd and cd['send_checks_to_bool']:
            concierge.send_checks_to = Concierge.SEND_CHECKS_TO_HOME
        concierge.save()

        super(ConciergeRegistrationForm, self).save(concierge)
        
        # create default commissions for this new concierge
        for tour_type in TourType.objects.filter(active=True):
            ConciergeCommission.objects.create(concierge=concierge, tour_type=tour_type, amount=tour_type.default_commission)
        
        # shoot emails to concierge about this
        c_subject = 'Your Concierge Account with SF Shuttle Tours / NY Sprinter Tours has been setup!'
        c_message = 'Thank you for creating your Concierge Account with us! You will now be able to easily book tours online, track your sales commission, request brochures, and send us messages through your own account.\n\n'
        c_message += 'PLEASE BOOKMARK THIS LINK: http://%s%s\n\n' % (django_settings.SITE_DOMAIN, reverse('concierges_home'))
        c_message += 'This is the link you will use on a daily basis. If you are having any trouble with your account, please call us at 415-513-5400 (for NY concierges call 1-888-996-9286) and we will be happy to help you!\n\n'
        c_message += 'Regards,\nSF Shuttle Tours / NY Sprinter Tours Team!\n\n'
        start_thread(send_mail, c_subject, c_message, django_settings.DEFAULT_FROM_EMAIL, [django_settings.DEFAULT_TO_EMAIL, contact.email])
        
        # shoot an email to admins about this
        a_subject = '"%s %s" has just created a Concierge Account' % (user.first_name, user.last_name)
        a_message = 'Concierge Name: %s %s\n' % (user.first_name, user.last_name)
        a_message += 'Hotel name: %s\n' % concierge.hotel_name
        a_message += 'Phone number: %s  %s\n' % (concierge.hotel_phone(), concierge.home_phone())
        a_message += 'How often they book our tours: %s\n' % concierge.frequency
        a_message += 'Average number of tours they book per week: %s\n' % concierge.per_week
        start_thread(send_mail, a_subject, a_message, django_settings.DEFAULT_FROM_EMAIL, [django_settings.DEFAULT_TO_EMAIL,])


class MessageForm(forms.Form):
    message_id = forms.CharField(widget=HiddenInput, initial='')
    message = forms.CharField(widget=forms.Textarea, required=False)
