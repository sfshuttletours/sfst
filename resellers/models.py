from datetime import date, timedelta

from django.db import models

from satchmo_store.contact.models import Contact
from satchmo_store.shop.models import Order
from common.utils import first_and_last_date_in_month

class ResellerCategory(models.Model):
    
    name = models.CharField(max_length=64)
    color = models.CharField(max_length=7)
    
    def __unicode__(self):
        return self.name

class Reseller(models.Model):
    TYPE_COMMISSION_CHECK = 1
    TYPE_MARKUP = 2
    TYPE_CREDIT_CARD_PROCESSOR = 3
    RESELLER_TYPE_CHOICES = (
        (TYPE_COMMISSION_CHECK, 'Commission Check Reseller'),
        (TYPE_MARKUP, 'Mark-up Reseller'),
        (TYPE_CREDIT_CARD_PROCESSOR, 'Credit Card Processing Reseller'),
    )
    
    reseller_type = models.IntegerField(choices=RESELLER_TYPE_CHOICES, default=TYPE_COMMISSION_CHECK, db_index=True)
    company_name = models.CharField(max_length=128)
    contact = models.ForeignKey(Contact, related_name='resellers', null=True, unique=True)
    commission = models.DecimalField(max_digits=5, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    special = models.BooleanField(default=False)
    website = models.CharField(max_length=256, blank=True)
    category = models.ForeignKey(ResellerCategory, null=True, blank=True)
    code = models.CharField(max_length=64, unique=True, blank=True, db_index=True)
    orders = models.ManyToManyField(Order)
    voucher = models.BooleanField(default=False, help_text="Gives customers a voucher to be shown to tour guide before boarding.")
    
    class Meta:
        permissions = (
            ("is_reseller", "Is Reseller"),
        )
        ordering = ('company_name', )
        
    def __unicode__(self):
        return 'Reseller: %s' % self.company_name
    
    def name(self):
        return self.company_name
    
    def handle(self):
        return self.name()
    
    def total_orders_this_month(self):
        start, end = first_and_last_date_in_month(date.today()) 
        return self.orders.filter(time_stamp__range=(start, end)).count()
        
    def total_orders_last_month(self):
        day_in_last_month = date.today() - timedelta(days=(date.today().day + 1))
        start, end = first_and_last_date_in_month(day_in_last_month)
        return self.orders.filter(time_stamp__range=(start, end)).count()
    
    def add_note_to_order(self, order):
        """
        Adds relevant note(s) to orders to keep things DRY
        """
        if self.voucher:
            order.add_note('MUST COLLECT VOUCHER - %s' % self.company_name)
        else:
            order.add_note('Paid in full - %s' % self.company_name)
        
        order.save()

class ResellerRequest(models.Model):
    first_name = models.CharField('Last Name', max_length=30)
    last_name = models.CharField('First Name', max_length=30)
    company_name = models.CharField('Company Name', max_length=128)
    street = models.CharField(max_length=80, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    zip_code = models.CharField('Zip', max_length=30, blank=True)
    phone = models.CharField('Direct Phone', max_length=30)
    email = models.EmailField('Email Address', max_length=75)
    website = models.CharField('Website (URL) you will be using to sell tours', max_length=256)
    description = models.TextField('Description of what you do to sell tours (tell us about your company)')
    estimate = models.IntegerField('How many tours do you think you will sell per month')
    reseller_type = models.IntegerField(choices=Reseller.RESELLER_TYPE_CHOICES, default=Reseller.TYPE_COMMISSION_CHECK)
    
    def __unicode__(self):
        return 'Reseller Request: %s %s from %s' % (self.first_name, self.last_name, self.company_name)
