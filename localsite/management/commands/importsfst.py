
# encoding: utf-8
"""
import.py

Created by Peter Sheats on 2010-05-14.
Copyright (c) 2010 Peter Sheats. All rights reserved.
"""
import os
import re
import sys
import getopt
import urllib
import subprocess
from decimal import Decimal
from datetime import date, time, timedelta
from time import sleep

from django.contrib.auth.models import User, Permission, Group
from django.contrib.sites.models import Site
from django.core.validators import ValidationError
from django.core.files.base import File
from django.core.management.base import BaseCommand
from django.conf import settings
from django.db.models import Sum

from product.models import Product
from legacy.shelf import Shelf
from legacy.models import *
from legacy.models import ContactOrganization as LegacyOrg
from localsite.models import TourType, TeamMember, TourSchedule, DayOfWeek
from concierges.models import Concierge, ConciergeCommission
from resellers.models import Reseller, ResellerRequest, ResellerCategory
from adjustments.models import Adjustment, AdjustmentHistory
from product.modules.configurable.models import ProductVariation

from satchmo_store.contact.models import Contact, ContactRole, Organization, ContactOrganization, ContactOrganizationRole, PhoneNumber, AddressBook
from satchmo_store.shop.models import Order, OrderItem, OrderPayment
from payment.models import CreditCardDetail
from l10n.models import Country


help_message = '''
The help message goes here.
'''

# PROJECT_ROOT_DIR = '/Users/sheats/www/sfst/'
PROJECT_ROOT_DIR = '/home/sfst/work/sfst/src/sfst/'

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def convert(old_object, new_object, exclude=[]):
    fields = [f.name for f in old_object._meta.fields]
    for field in fields:
        if field not in exclude and hasattr(new_object, field):
            setattr(new_object, field, getattr(old_object, field))

def get_object(klass, old_object):
    try:
        obj = klass.objects.get(id=old_object.id)
    except klass.DoesNotExist:
        obj = klass(id=old_object.id)
    return obj

def get_tour_type(old_product_id):
    """
    Old products and IDs
    1 5 Hour City Tour
    2 Wine Country Napa Tour
    3 Muir Woods (only) Tour
    4 Muir Woods/City Tour Package
    5 Alcatraz Tour
    6 Alcatraz/City Tour Package
    7 Monterey Cruiser Tour -- 7 was deleted on production, still referenced by some old data
    8 Gift Certificate
    9 Monterey Cruiser Tour
    10 Alcatraz/Monterey Combo


    """
    TOUR_TYPE_MAPPING = {
        1: 1,
        2: 2,
        3: 5,
        4: 4,
        5: 6, # No Varients
        6: 7, # No Varients
        7: 3,
        8: 8, # No Varients
        9: 3, # No Varients
        10: 9, # No Varients
    }
    tt = TourType.objects.get(id=TOUR_TYPE_MAPPING[int(old_product_id)])
    tt.old_product_id = int(old_product_id) # don't ask :)
    return tt

def is_multiproduct(product_id):
    """
        4|9
        6|0
        10|0    
    """
    return int(product_id) in (4, 6, 10)

def get_tour_types_for_old_id(product_id):
    """
        1|4|1
        2|4|3
        3|6|1
        4|6|5
        5|10|9
        6|10|5        
    """
    pid = int(product_id)
    if pid == 4:
        return (get_tour_type(1), get_tour_type(3))
    elif pid == 6:
        return (get_tour_type(1), get_tour_type(5))
    elif pid == 10:
        return (get_tour_type(5), get_tour_type(9))
    # to make code below easier:
    else:
        return (get_tour_type(pid), )

def import_users():
    """
    Found two problems:
        1. Some usernames were greater than 30 characters
        2. Duplicate usernames which violates unique key constraint
    """
    # Change the length of the username field so we don't lose data on usernames
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute('ALTER TABLE auth_user MODIFY COLUMN username varchar(40)')

    old_users = AuthUser.objects.all().iterator()
    for old_user in old_users:
        new_user = get_object(User, old_user)
        convert(old_user, new_user)

        # prevent duplicate and too long username errors
        # if len(old_user.username) > 30:
        #     print 'DESTROYING DATA, username too long: ', old_user.username
        #     # print old_user.username, len(old_user.username)
        #     new_username = old_user.username[:30]
        # 

        new_username = old_user.username.strip()
        # PREVENT DUPLICATES
        for x in xrange(1, 9):
            try:
                User.objects.filter(username__iexact=new_username).exclude(id=new_user.id)[0]
                new_username = '%s%d' % (old_user.username[:29], x)
                print 'DUPLICATE USERNAME, changing "%s" to "%s"' % (old_user.username, new_username)
            except IndexError:
                break
        new_user.username = new_username
        new_user.save();

def import_contacts():
    Contact.objects.filter(user__id=1).delete()
    old_contacts = ContactContact.objects.all().iterator()
    for old_contact in old_contacts:
        new_contact = get_object(Contact, old_contact)
        convert(old_contact, new_contact, exclude=['role', 'user'])
        # print old_contact.first_name
        if len(old_contact.first_name) > 30:
            # TODO What to do with these?
            print 'DESTROYING DATA, first_name too long: ', old_contact.first_name
            new_contact.first_name = old_contact.first_name[:30]
        if len(old_contact.last_name) > 30:
            # TODO What to do with these?
            print 'DESTROYING DATA, last_name too long: ', old_contact.last_name
            new_contact.last_name = old_contact.last_name[:30]
        if old_contact.role:
            role, created = ContactRole.objects.get_or_create(key=old_contact.role, name=old_contact.role.title())
            new_contact.role = role                

        if old_contact.user:
            new_contact.user = User.objects.get(id=old_contact.user.id)

        new_contact.save()
        
        # Concierge Specific Stuff
        if hasattr(new_contact, 'concierge') and new_contact.concierge:
            d = {}
            c = new_contact.concierge
            key_values = old_contact.notes.split(' ')
            for kv in key_values:
                if '=' in kv:
                    key, val = kv.split('=')
                    d[key] = val
                else:
                    print kv
                
            
            if 'addrPref' in d:
                if d['addrPref'] == 'False':
                    c.send_checks_to = Concierge.SEND_CHECKS_TO_HOME
                elif d['addrPref'] == 'True':
                    c.send_checks_to = Concierge.SEND_CHECKS_TO_HOTEL
                else:
                    assert False, 'addrPref: %s' % d['addrPref']
            
            if 'notification' in d:
                if d['notification'] == 'True':
                    c.email_notifications = True
                else:
                    c.email_notifications = False
            
            if 'type' in d:
                if d['type'] == 'A':
                    c.booking_type = Concierge.BOOKING_TYPE_COMMISSION_CHECK
                else:
                    c.booking_type = Concierge.BOOKING_TYPE_DEPOSIT
            
            if 'frequency' in d and d['frequency'] not in ('not_found', ):
                c.frequency = d['frequency'].replace('_', ' ')
            
            if 'perweek' in d and d['perweek'] not in ('not_found', ):
                c.per_week = d['perweek'].replace('_', ' ')

            c.save()



def import_orders():
    old_orders = ContactOrder.objects.all().iterator()
    # old_orders = ContactOrder.objects.filter(contact__first_name='Manual').iterator()
    for old_order in old_orders:
        new_order = get_object(Order, old_order)
        convert(old_order, new_order, exclude=('contact', ))
        new_order.site = Site.objects.get_current()
        new_order.time_stamp = old_order.timestamp
        contact = Contact.objects.get(id=old_order.contact_id)
        if old_order.notes and old_order.contact.first_name == 'Manual' and old_order.contact.last_name == 'Confirmation' and 'NS' not in old_order.notes:
            contact.first_name = ''
            contact.last_name = ''
            
            parts = old_order.notes.split(' ')
            if len(parts) > 2:
                contact.first_name = parts[0]
                try:
                    contact.last_name = parts[1]
                except IndexError:
                    print '***********************************', old_order.notes
                contact.save()
                # print 'Found Manual:', contact.first_name, contact.last_name
        new_order.contact = contact
        if old_order.contact.notes:
            new_order.add_note(old_order.contact.notes)
            print new_order.id, old_order.contact.notes
        try:
            new_order.save()
        except Exception:
            from IPython.Shell import IPShellEmbed; IPShellEmbed()()
        

def import_order_items():
    idx = 0
    chunk = 2000
    total = ContactOrderitem.objects.all().count()
    # old_items = ContactOrderitem.objects.filter(order__id__gte=15014).iterator()
    # old_items = ContactOrderitem.objects.filter(contactorderitemdetail__name='date', contactorderitemdetail__value='01-06-2010')
    # old_items = ContactOrderitem.objects.filter(contactorderitemdetail__name__in=('REFUND', 'VOID', 'transmutation'))
    while idx < total:
        print '*'*75, idx
        old_items = ContactOrderitem.objects.all().order_by('id')[idx:idx+chunk]
        idx += chunk
        for old_item in old_items:
            # TODO old_items have a boolean called insurance?  is this satchmo or custom and is it necessary?
                
            details_dict = {}
            details = old_item.contactorderitemdetail_set.all().iterator()
            for d in details:
                details_dict[d.name] = d.value
        
        
            if 'date' not in details_dict or details_dict['date'] == '77-77-7777':
                day = date(2009, 1, 1)
            else:
                d, month, year = map(int, details_dict['date'].split('-'))
                if year < 15:
                    year = year + 2000
                try:
                    day = date(year, month, d)
                except Exception, e:
                    print details_dict
                    from IPython.Shell import IPShellEmbed; IPShellEmbed()()
                        
            # Quantity, sample: 'quantity_Children (12 and under)::0__quantity_Senior (65+)::3__quantity_Adults::2'
            # Quantity, sample: 'quantity_default::2'
            # quantity_Senior (65+)::0__quantity_Children (12 and under) (with Aquarium)::0__quantity_Adults::4__quantity_Children (12 and under)::2__quantity_Senior (65+) (with aquarium)::0__quantity_Adults (with Aquarium)::0
            # print old_item.quantity
            children = seniors = adults = default = 0
            raw_quantities = old_item.quantity.split('__')
        
            for raw_q in raw_quantities:
                quan = Decimal(raw_q.split('::')[-1])
                if 'Children' in raw_q:
                    children += quan
                if 'Senior' in raw_q:
                    seniors += quan
                if 'Adults' in raw_q:
                    adults += quan
                if 'default' in raw_q:
                    default += quan
        
            options = {
                'Adult': adults + default,
                'Senior': seniors,
                'Child': children
            }
            # print 'Adults: %(Adult)d Senior: %(Senior)d Child: %(Child)d' % options
            # sleep(1)
            # continue
        
            order = Order.objects.get(id=old_item.order.id)
            for key, quantity in options.items():
                if quantity == 0:
                    continue
                # so if this product is actually a multiproduct, we need to create items for both products
                tour_types = get_tour_types_for_old_id(int(old_item.product_id))            
                for tour_type in tour_types:
                    tour_time = None
                    if 'time' not in details_dict or details_dict['time'] == '-1':
                        # Probably a multiproduct:
                        if is_multiproduct(int(old_item.product_id)):
                            old_product = ProductProduct.objects.get(id=int(old_item.product_id))
                            dts2s = ProductDatetimeschema2.objects.filter(product=old_product)
                            for dts2 in dts2s:
                                if dts2.dts.product.id == tour_type.old_product_id:
                                    tour_time = dts2.dts.get_nice_data()[0]
                    else:
                        tour_time, days = ProductDatetimeschema.objects.get(id=details_dict['time']).get_nice_data()
                    if tour_time is None:
                        if int(old_item.product_id) == 8:
                            # move on, this is a gift certificate
                            continue
                        else:
                            if int(old_item.product_id) == 4:
                                print 'Houston, we have a problem'
                                from IPython.Shell import IPShellEmbed; IPShellEmbed()()
                            continue
                    tour_product = tour_type.get_product(day, tour_time=tour_time)
                    new_item = OrderItem(order=order)
                    new_item.quantity = quantity
                    # These don't have product variations
                    if tour_type.id in (6, 7, 8):
                        new_item.product = tour_product.product
                    else:
                        try:
                            new_item.product = tour_product.product.configurableproduct.productvariation_set.get(options__value=key).product
                        except:
                            print 'uhh'
                            from IPython.Shell import IPShellEmbed; IPShellEmbed()()
        
                    new_item.tax = 0
                    new_item.unit_tax = 0
        
                    new_item.line_item_price = old_item.unit_price * int(quantity)
                    new_item.unit_price = old_item.unit_price
        
                    try:
                        new_item.full_clean()
                    except ValidationError, e:
                        print 'full_clean'
                        from IPython.Shell import IPShellEmbed; IPShellEmbed()()
                        assert False
                    new_item.save()
                
                    # Handle VOID, REFUND, and transmutation
                
                    if 'VOID' in details_dict:
                        adjustment = Adjustment(item=new_item)
                        adjustment.status = Adjustment.VOIDED
                        adjustment.save()
                        print details_dict
                
                    elif 'REFUND' in details_dict:
                        adjustment = Adjustment(item=new_item)
                        adjustment.status = Adjustment.VOIDED
                        adjustment.save()
                        print details_dict
                    
                    elif 'transmutation' in details_dict:
                        # Don't think there were any of these
                        from IPython.Shell import IPShellEmbed; IPShellEmbed()()

                    else:
                        # update inventory
                        product = tour_product.product
                        product.total_sold = Decimal(product.total_sold) + Decimal(quantity)
                        product.save()
        
                    print 'Saved OrderItem: ', new_item.id, ' Order #', order.id

            if 'CODE' in details_dict and details_dict['CODE']:
                try:
                    reseller = Reseller.objects.get(code=details_dict['CODE'])
                    reseller.orders.add(order)
                    reseller.save()
                    # print 'Matched order ', order.id, ' and reseller ', reseller.company_name
                except Reseller.DoesNotExist:
                    try:
                        concierge = Concierge.objects.get(code=details_dict['CODE'])
                        concierge.orders.add(order)
                        concierge.save()
                        print 'Matched order ', order.id, ' and reseller ', concierge.name
                    except Concierge.DoesNotExist:
                        print 'No reseller/concierge for code: ', details_dict['CODE']
            
def import_order_payments():
    old_payments = ContactOrderpayment.objects.all().iterator()
    for old_payment in old_payments:
        new_payment = get_object(OrderPayment, old_payment)
        convert(old_payment, new_payment, exclude=('order', ))
        new_payment.time_stamp = old_payment.timestamp
        new_payment.order = Order.objects.get(id=old_payment.order.id)
        new_payment.save()
        order = new_payment.order
        order.force_recalculate_total()
        order.save()
        # print old_payment.payment, old_payment.amount

def filter_duplicate_orders():
    orders = Order.objects.all().iterator()
    dupes = []
    print 'Collecting dupes...'
    for order in orders:
        contact = order.contact
        if contact.order_set.all().count() > 1 and not contact.user:
            dupes.append(contact)

    print len(dupes), 'Dupes'
    
    def delete_order(o):
        for i in o.orderitem_set.all():
            try:
                product = i.product.productvariation.parent.product
            except ProductVariation.DoesNotExist:
                product = i.product
            product.total_sold -= i.quantity
            product.save()
        o.delete()
    for contact in dupes:
        orders = contact.order_set.all()
        # print orders.count()
        timestamps = {}
        for order in orders:
            count = order.orderitem_set.all().count()
            # item_ids = order.orderitem_set.all().values_list('id', flat=True)
            details_count = ContactOrderitemdetail.objects.filter(item__order__id=order.id).count()
            if not details_count:
                print 'Deleting because no details', order
                delete_order(order)
                continue
            try:
                payment = order.payments.get()
                if payment.transaction_id == 'PENDING':
                    print 'Deleting because of PENDING', order
                    delete_order(order)
                    continue
            except:
                pass
            ts = order.time_stamp
            if ts in timestamps and timestamps[ts] == count:
                print 'Deleting because of exact timestamp and count', order
                delete_order(order)
            else:
                if len(timestamps.keys()) > 0:
                    for t, c in timestamps.items():
                        if count != c:
                            continue
                        if ts > t:
                            if (ts - t) < timedelta(minutes=1):
                                print 'Deleting cuz of close time: ', order
                                delete_order(order)
                                continue
                        else:
                            if (t-ts) < timedelta(minutes=1):
                                print 'Deleting cuz of close time: ', order
                                delete_order(order)
                                continue
                else:
                    timestamps[ts] = count
    
    
def import_cc_details():
    old_ccs = PaymentCreditcarddetail.objects.all().iterator()
    for old_cc in old_ccs:
        new_cc = get_object(CreditCardDetail, old_cc)
        convert(old_cc, new_cc, exclude=['orderpayment', ])
        new_cc.orderpayment = OrderPayment.objects.get(id=old_cc.orderpayment.id)
        new_cc.expire_month = old_cc.expiremonth
        new_cc.expire_year = old_cc.expireyear
        new_cc.display_cc = old_cc.displaycc
        new_cc.encrypted_cc = old_cc.encryptedcc
        new_cc.credit_type = old_cc.credittype
        new_cc.save()
        print 'saved cc_info: ', new_cc.id, ' order_payment: ', new_cc.orderpayment.id

def import_contact_phone_numbers():
    old_phones = ContactPhonenumber.objects.all().iterator()
    for old_phone in old_phones:
        if not old_phone.phone:
            continue
        new_phone = get_object(PhoneNumber, old_phone)
        convert(old_phone, new_phone, exclude=('contact', ))
        new_phone.contact = Contact.objects.get(id=old_phone.contact.id)
        if len(old_phone.phone) > 30:
            print 'DESTROYING DATA, PHONE TOO LONG: ', old_phone.phone
            new_phone.phone = old_phone.phone[:30]
        if old_phone.primary:
            new_phone.type = 'Home'
        else:
            new_phone.type = 'Work'
        new_phone.save()


def import_address_books():
    USA = Country.objects.get(iso2_code='US')
    old_addresses = ContactAddressbook.objects.all().iterator()
    for old_address in old_addresses:
        new_address = get_object(AddressBook, old_address)
        convert(old_address, new_address, exclude=('contact', 'country'))
        new_address.contact = Contact.objects.get(id=old_address.contact.id)
        new_address.addressee = '%s %s' % (new_address.contact.first_name, new_address.contact.last_name)
        if old_address.country == 'US' or old_address.country.strip() == '' or old_address.country.strip() == 'United States':
            new_address.country = USA
        elif old_address.country == 'Canada':
            new_address.country, created = Country.objects.get_or_create(
                iso2_code='CA',
                name='Canada',
                printable_name='Canada',
                iso3_code='CAN',
                numcode=124,
                continent='NA', # see l10n.models.CONTINENTS
                )
        elif old_address.country == 'Switzerland':
            new_address.country, created = Country.objects.get_or_create(
                iso2_code='CH',
                name='Switzerland',
                printable_name='Switzerland',
                iso3_code='CHE',
                numcode=756,
                continent='EU', # see l10n.models.CONTINENTS
                )        
        else:
            assert False, 'No country named %s' % old_address.country
        try:
            new_address.save()
        except Exception, e:
            # Unicode error on one address so we're skipping
            print e

def import_concierge_images():
    concierge_image_url = 'http://securebookingshuttletours.com/static/con_images/concierge_image_%d.png'
    concierges = Concierge.objects.all().iterator()
    for concierge in concierges:
        image_url = concierge_image_url % concierge.contact.id
        file_name = image_url.split('/')[-1]
        local_path = os.path.join('/tmp', file_name)
        try:
            print 'Downloading %s...' % image_url
            urllib.urlretrieve(image_url, local_path)
            if os.access(local_path, os.R_OK) and os.path.getsize(local_path) > 1000:
                f = File(open(local_path))
                concierge.image = f
        except IOError:
            pass
        concierge.save()     
    

def import_tour_days():
    tour_days = ProductTourday.objects.all().iterator()
    days = []
    diff_count = 0
    diffs = {}
    for tour_day in tour_days:
        try:
            d, m, y = map(int, tour_day.date.split('-'))
        except ValueError:
            print 'BAD DATE: ', tour_day.date

        if y < 100:
            y = y + 2000
        try:
            day = date(y, m, d)
        except ValueError, e:
            if 'month must be in' in e:
                try:
                    day = date(y, d, m)
                except ValueError, e:
                    print e
                    continue
        
        # Orders were deleted pre 2009-10-1
        if day < date.today():#date(2010, 1, 1):
            continue
        print tour_day.id
        try:
            dts = ProductDatetimeschema.objects.get(id=int(tour_day.time))
        except ProductDatetimeschema.DoesNotExist:
            # print 'PDTS not found: %s -- What are these?' % tour_day.time, tour_day.date
            continue
        tyme, weekdays = dts.get_nice_data()
        tour_type = get_tour_type(tour_day.product_id)
        tour_product = tour_type.get_product(day, tour_time=tyme, create=False)
        if tour_product:
            product = tour_product.product
            total_sold = int(product.total_sold)
            seats_filled = int(tour_day.seatsfilled)
            diff = seats_filled - total_sold
            if diff != 0:
                print tour_type.name, tour_product.day, tour_product.pretty_time, 'New: ', total_sold, ' Old: ', seats_filled
                
                old_items = ContactOrderitem.objects.filter(
                            contactorderitemdetail__name='date', 
                            contactorderitemdetail__value=tour_day.date).filter(
                            contactorderitemdetail__name='time',
                            contactorderitemdetail__value=tour_day.time,)
                new_items = tour_product.items
                new_items_ids = list(new_items.values_list('id', flat=True))
                sold = seats = 0
                for old_item in old_items:
                    sub_sold = sub_seats = 0
                    raw_quantities = old_item.quantity.split('__')
                    for raw_q in raw_quantities:
                        quan = Decimal(raw_q.split('::')[-1])
                        sub_seats += quan                    
                    
                    fname = old_item.order.contact.first_name
                    lname = old_item.order.contact.last_name
                    if lname == 'Confirmation':
                        fname, lname = old_item.order.notes.split(' ')[:2]
                    new = new_items.filter(order__contact__first_name=fname, order__contact__last_name=lname)
                    if new.count() == 0:
                        pass
                    #     print 'new_count = 0'
                    #     from IPython.Shell import IPShellEmbed; IPShellEmbed()()
                    elif new.count == 1:
                        new_items_ids.pop(new_items_ids.index(new.id))
                        sub_sold += new[0].quantity
                        # print int(new[0].quantity), old_item.quantity
                    else:
                        q = 0
                        for n in new:
                            try:
                                new_items_ids.pop(new_items_ids.index(n.id))
                            except ValueError:
                                if fname != 'Manual' and lname != 'Confirmation':
                                    pass
                                    # print 'id not in list', n.id, new_items_ids
                                    # from IPython.Shell import IPShellEmbed; IPShellEmbed()()
                                
                            q += n.quantity
                        sub_sold += q
                        if int(sub_seats) != int(sub_sold):
                            print int(q), old_item.quantity
                            # print 'subs not equal', sub_sold, sub_seats
                            # from IPython.Shell import IPShellEmbed; IPShellEmbed()()
                        sold += sub_sold
                        seats += sub_seats
                # if len(new_items_ids):
                #     print 'items left', new_items_ids
                #     from IPython.Shell import IPShellEmbed; IPShellEmbed()()
                    # new_item = new_items.get(id=old_item.id)
                    # from IPython.Shell import IPShellEmbed; IPShellEmbed()()
                if int(sold) != int(seats):
                    diff_count += 1
                print 'Accurate:', sold, seats
                    # from IPython.Shell import IPShellEmbed; IPShellEmbed()()
    print diff_count
                # diffs.setdefault(diff, [])
                # diffs[diff].append(tour_product)
            # print seats_filled, total_sold
            # if int(product.total_sold) != int(tour_day.seatsfilled):
            #     from IPython.Shell import IPShellEmbed; IPShellEmbed()()
            #     assert False
    
    from IPython.Shell import IPShellEmbed; IPShellEmbed()()
    assert False
    print days

def import_resellers():  
    reseller_requests = ContactResellerrequest.objects.all().iterator()
    for rr in reseller_requests:
        new_rr = ResellerRequest()
        new_rr.first_name = rr.fname
        new_rr.last_name = rr.lname
        new_rr.company_name = rr.cname
        new_rr.phone = rr.phone
        new_rr.email = rr.email
        new_rr.website = rr.web
        new_rr.description = rr.desc
        try:
            new_rr.estimate = int(rr.tourmonths)
        except ValueError:
            new_rr.estimate = 0
        new_rr.save()
    
    resellers = ContactReseller.objects.all().order_by('coname').iterator()
    for r in resellers:
        if not r.cid or not r.coname:
            continue
        # print 'Importing ', r.coname
        code = hash(r.coname.strip())
        try:
            new_r = Reseller.objects.get(code=code)
        except Reseller.DoesNotExist:
            new_r = Reseller()
        new_r.company_name = r.coname
        try:
            new_r.contact = Contact.objects.get(id=int(r.cid))
        except Contact.DoesNotExist:
            continue
            print 'No contact: ', r.coname
        new_r.commission = r.commission
        new_r.discount = r.discount
        new_r.special = r.special
        new_r.reseller_type = Reseller.TYPE_COMMISSION_CHECK
        if new_r.special:
            new_r.reseller_type = Reseller.TYPE_CREDIT_CARD_PROCESSOR
        elif new_r.discount != '0':
            new_r.reseller_type = Reseller.TYPE_MARKUP
            
        # try:
        #     dupe = Reseller.objects.get(code=code)
        #     from IPython.Shell import IPShellEmbed; IPShellEmbed()()
        # except Reseller.DoesNotExist:
        #     pass        
        new_r.code = code
        new_r.save()
        
        user = new_r.contact.user
        user.groups.add(Group.objects.get(name='Reseller'))
        user.save()
        
    from legacy.html import RESELLER_HTML
    COLORS = {
        '#78E89A': 'Reg Reseller',
        '#ABB3FB': 'CC Reseller',
        '#F4B3C5': 'Pow Wow',
        '#E7F981': 'Travel Agent',
        '#D7D1D1': 'Admin',
        '#F6B490': 'Couponing',
        '#C1EAE8': 'Unknown',
    }
    
    snippets = re.findall('<div style="width:100%;background-color:#.*\n.*\n.*\n', RESELLER_HTML)
    
    for s in snippets:
        match = re.search(r'/contact/contact/(\d+)', s)
        contact_id = int(match.groups()[0])
        match = re.search(r'background-color:(.+);', s)
        color = match.groups()[0]
        
        reseller_category, created = ResellerCategory.objects.get_or_create(name=COLORS[color.upper()], color=color)
        try:
            reseller = Reseller.objects.get(contact__id=contact_id)
            reseller.category = reseller_category
            reseller.save()
            # print contact_id, color, reseller.company_name
        except Reseller.DoesNotExist:
            print '****************', 'no reseller'
        except Reseller.MultipleObjectsReturned:
            print '****************', 'multiple resellers'
            pass
        
def import_commissions():
    shelf = Shelf('%smsgshelf.db' % PROJECT_ROOT_DIR)
    items = shelf.items()
    shelf.close()
    for key, val in items:
        try:
            commission = float(val)
        except (TypeError, ValueError):
            continue
        user_id, old_product_id = map(int, key.split('_'))
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            # print '*********************************************No User: ', user_id
            continue
        
        
        # from IPython.Shell import IPShellEmbed; IPShellEmbed()()
        # assert False
        try:
            contact = user.contact_set.all()[0]
        except IndexError:
            print 'Deleting: %s %s' % (user.username, user.email)
            user.delete()
            continue
        
        try:
            concierge = contact.concierge
        except AttributeError:
            # print '*********************************************not a concierge'
            continue
        
        
        if not concierge.hotel_name:
            concierge.hotel_name = concierge.get_hotel_name()
            concierge.save()
        tour_type = get_tour_type(old_product_id)
        cc, created = ConciergeCommission.objects.get_or_create(concierge=concierge, tour_type=tour_type)
        cc.amount = str(commission)
        cc.save()
        print 'Saved: ', cc.concierge, cc.tour_type.name
        
def import_team():
    TeamMember.objects.all().delete()
    data = urllib.urlopen('http://securebookingshuttletours.com/static/team_images/')
    images = re.findall('>([A-Z].*\.png)<', data.read())
    for i in images:
        image_path = 'http://securebookingshuttletours.com/static/team_images/%s' % i
        no_extension = i.replace('.png', '')
        first, last, title = no_extension.split('___')
        t = TeamMember(first_name=first, last_name=last, job_title=title)
        
        local_path = '/tmp/tmp_image'
        urllib.urlretrieve(image_path, local_path)
        t.image = File(open(local_path))
        t.save()
        print first, last, title

def create_concierges():
    concierge_role = ContactRole.objects.get(key='Concierge')
    concierges = concierge_role.contact_set.all().iterator()
    for contact in concierges:
        con = Concierge(contact=contact)
        con.save()    

def import_inventory():
    """Update Items in Stock"""
    tour_days = ProductTourday.objects.all().iterator()
    days = []
    diff_count = 0
    diffs = {}
    for tour_day in tour_days:
        try:
            d, m, y = map(int, tour_day.date.split('-'))
        except ValueError:
            print 'BAD DATE: ', tour_day.date

        if y < 100:
            y = y + 2000
        try:
            day = date(y, m, d)
        except ValueError, e:
            if 'month must be in' in e:
                try:
                    day = date(y, d, m)
                except ValueError, e:
                    print e
                    continue
        
        try:
            dts = ProductDatetimeschema.objects.get(id=int(tour_day.time))
        except ProductDatetimeschema.DoesNotExist:
            # print 'PDTS not found: %s -- What are these?' % tour_day.time, tour_day.date
            continue
        tyme, weekdays = dts.get_nice_data()
        tour_type = get_tour_type(tour_day.product_id)
        # print tour_type
        tour_product = tour_type.get_product(day, tour_time=tyme, create=False)
        if tour_product:
            product = tour_product.product
            if tour_day.numberofseats == -999:
                seats = tour_day.product.numseats
            else:
                seats = tour_day.numberofseats
            print int(product.items_in_stock), seats
            product.items_in_stock = int(seats)
            product.save()
    
    

def troubleshoot():
    products = Product.objects.active(variations=False).filter(orderitem__isnull=False)
    for p in products:
        quan = p.orderitem_set.all().aggregate(Sum('quantity'))['quantity__sum']
        sold, quan =  int(p.total_sold), int(quan)
        if sold != quan:
            from IPython.Shell import IPShellEmbed; IPShellEmbed()()
            assert False
        tp = p.tourproduct
        try:
            tour_day = ProductTourday.objects.get(date=tp.day.strftime('%d-%m-%Y'), hour=tp.tour_time.hour, minute=tp.tour_time.minute)
        except ProductTourday.DoesNotExist:
            from IPython.Shell import IPShellEmbed; IPShellEmbed()()
            assert False
        

def import_combo_items():
    idx = 0
    chunk = 2000
    total = ContactOrderitem.objects.all().count()
    # old_items = ContactOrderitem.objects.filter(order__id__gte=15014).iterator()
    # old_items = ContactOrderitem.objects.filter(contactorderitemdetail__name='date', contactorderitemdetail__value='01-06-2010')
    # old_items = ContactOrderitem.objects.filter(contactorderitemdetail__name__in=('REFUND', 'VOID', 'transmutation'))
    while idx < total:
        print '*'*75, idx
        old_items = ContactOrderitem.objects.all().order_by('id')[idx:idx+chunk]
        idx += chunk
        for old_item in old_items:
            if not is_multiproduct(int(old_item.product_id)):
                continue
            

            details_dict = {}
            details = old_item.contactorderitemdetail_set.all().iterator()
            for d in details:
                details_dict[d.name] = d.value


            if 'date' not in details_dict or details_dict['date'] == '77-77-7777':
                day = date(2009, 1, 1)
            else:
                d, month, year = map(int, details_dict['date'].split('-'))
                if year < 15:
                    year = year + 2000
                try:
                    day = date(year, month, d)
                except Exception, e:
                    print details_dict
                    from IPython.Shell import IPShellEmbed; IPShellEmbed()()

            # Quantity, sample: 'quantity_Children (12 and under)::0__quantity_Senior (65+)::3__quantity_Adults::2'
            # Quantity, sample: 'quantity_default::2'
            # quantity_Senior (65+)::0__quantity_Children (12 and under) (with Aquarium)::0__quantity_Adults::4__quantity_Children (12 and under)::2__quantity_Senior (65+) (with aquarium)::0__quantity_Adults (with Aquarium)::0
            # print old_item.quantity
            children = seniors = adults = default = 0
            raw_quantities = old_item.quantity.split('__')

            for raw_q in raw_quantities:
                quan = Decimal(raw_q.split('::')[-1])
                if 'Children' in raw_q:
                    children += quan
                if 'Senior' in raw_q:
                    seniors += quan
                if 'Adults' in raw_q:
                    adults += quan
                if 'default' in raw_q:
                    default += quan

            options = {
                'Adult': adults + default,
                'Senior': seniors,
                'Child': children
            }
            # print 'Adults: %(Adult)d Senior: %(Senior)d Child: %(Child)d' % options
            # sleep(1)
            # continue

            order = Order.objects.get(id=old_item.order.id)
            for key, quantity in options.items():
                if quantity == 0:
                    continue

                tour_type = get_tour_type(int(old_item.product_id))            
                old_product = ProductProduct.objects.get(id=int(old_item.product_id))
                dts2s = ProductDatetimeschema2.objects.filter(product=old_product)
                times = []
                for dts2 in dts2s:
                    times.append(dts2.dts.get_nice_data()[0])
                mp_start_time = min(times)
                # This all just makes sure a schedule exists for the right times.
                try:
                    schedule = tour_type.get_schedule_for_day(day)[0]
                except IndexError:
                    # get schedule at this time and add this isoweekday to it, or create a new one
                    try:
                        schedule = tour_type.schedules.filter(tour_time=mp_start_time)[0]
                    except IndexError:
                        schedule = TourSchedule(tour_time=mp_start_time, tour_type=tour_type)
                        schedule.save()
                    
                    
                    dow = DayOfWeek.objects.get(isoweekday=day.isoweekday())
                    schedule.day_of_week.add(dow)
                    schedule.save()
                # print tour_type, min(times), schedule
                tour_product = tour_type.get_product(day, tour_time=mp_start_time)
                new_item = OrderItem(order=order)
                new_item.quantity = quantity
                new_item.product = tour_product.product            
                new_item.tax = 0
                new_item.unit_tax = 0
                # i = old_item
                # print i.unit_price, i.unit_tax, i.line_item_price, i.tax, i.discount
                new_item.line_item_price = old_item.line_item_price
                new_item.unit_price = old_item.unit_price
                # print old_item.line_item_price, order.id
                if new_item.line_item_price == 0:
                    # SUMIT:  Put code in here to figure out what these combos should be priced at for reports
                    
                    # print tour_product.product.price
                    # if tour_type.id == 7: # City / Alcatraz
                        # new_item.line_item_price = Decimal('109.99') * new_item.quantity
                    # else:
                        # print tour_type
                        # from IPython.Shell import IPShellEmbed; IPShellEmbed()()
                        # assert False
                    # if tour_type == 
                    #     new_item.line_item_price = Decimal('153.99')
                    # from IPython.Shell import IPShellEmbed; IPShellEmbed()()
                    # assert False
                    print new_item.line_item_price, order.total, tour_type.base_price
            
                # new_item.save()
                # Handle VOID, REFUND, and transmutation
            
                if 'VOID' in details_dict:
                    adjustment = Adjustment(item=new_item)
                    adjustment.status = Adjustment.VOIDED
                    adjustment.save()
                    print details_dict
                            
                elif 'REFUND' in details_dict:
                    adjustment = Adjustment(item=new_item)
                    adjustment.status = Adjustment.VOIDED
                    adjustment.save()
                    print details_dict
                            
                elif 'transmutation' in details_dict:
                    # Don't think there were any of these
                    from IPython.Shell import IPShellEmbed; IPShellEmbed()()
            
                    # update inventory
                    # product = tour_product.product
                    # product.total_sold = Decimal(product.total_sold) + Decimal(quantity)
                    # product.save()
                print 'Saved OrderItem: ', new_item.id, ' Order #', order.id
        
class Command(BaseCommand):
    requires_model_validation = False
    
    def handle(self, *args, **options):
        if False:
            from legacy.models import *
            for name, model in locals().items():
                # try:
                if hasattr(model, 'objects'):
                    count = None
                    count = model.objects.all().count()
                    if count > 0:
                        print count, name
                # except AttributeError:
                    # pass
            from IPython.Shell import IPShellEmbed; IPShellEmbed()()
            assert False
        else:
            
            if 'clear' in args:
                if 'south' in settings.INSTALLED_APPS:
                    sys.exit('Please comment out south from INSTALLED_APPS')
                
                DB_PASSWORD_STR = '-psfst-rules'
                subprocess.call('mysql -uroot %s -e "drop database sfst"' % DB_PASSWORD_STR if not settings.IS_DEV else '', shell=True)
                subprocess.call('mysql -uroot %s -e "create database sfst DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_unicode_ci;"'\
                    % DB_PASSWORD_STR if not settings.IS_DEV else '', shell=True)
                
                subprocess.call('rm -rf %simages/*', shell=True)
                subprocess.call('%smanage.py syncdb --noinput' % PROJECT_ROOT_DIR, shell=True)
                subprocess.call('%smanage.py loaddata site' % PROJECT_ROOT_DIR, shell=True)
                subprocess.call('%smanage.py loaddata l10n_data' % PROJECT_ROOT_DIR, shell=True)
                subprocess.call('%smanage.py loaddata shop_config' % PROJECT_ROOT_DIR, shell=True)
                subprocess.call('%smanage.py loaddata setting' % PROJECT_ROOT_DIR, shell=True)
                subprocess.call('%smanage.py loaddata dayofweek' % PROJECT_ROOT_DIR, shell=True)
                subprocess.call('%smanage.py loaddata optiongroup' % PROJECT_ROOT_DIR, shell=True)
                subprocess.call('%smanage.py loaddata option' % PROJECT_ROOT_DIR, shell=True)
                subprocess.call('%smanage.py loaddata tourtype' % PROJECT_ROOT_DIR, shell=True)
                subprocess.call('%smanage.py loaddata tourschedule' % PROJECT_ROOT_DIR, shell=True)
                
                Group.objects.create(name='Customer')
                reseller_group = Group.objects.create(name='Reseller')
                reseller_group.permissions.add(Permission.objects.get(codename='is_reseller'))
                concierge_group = Group.objects.create(name='Concierge')
                concierge_group.permissions.add(Permission.objects.get(codename='is_concierge'))
                concierge_group.save()

            
            if 'users' in args or 'all' in args:
                import_users()
            
            if 'contacts' in args or 'all' in args:
                import_contacts()
            
            
            if 'phone' in args or 'all' in args:
                PhoneNumber.objects.all().delete()
                import_contact_phone_numbers()

            if 'address' in args or 'all' in args:
                import_address_books()

            if 'resellers' in args or 'all' in args:
                import_resellers()
            
            if 'commissions' in args or 'all' in args:
                import_commissions()
                import_concierge_images()
                
            if 'team' in args or 'all' in args:
                import_team()
            
            if 'just_orders' in args:
                subprocess.call('mysql -uroot -e "drop database sfst"', shell=True)
                subprocess.call('mysql -uroot -e "create database sfst DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_unicode_ci;"', shell=True)
                subprocess.call('mysql -uroot sfst < ../db_backups/pre-orders.dump', shell=True)
                
            if 'orders' in args or 'all' in args or 'just_orders' in args:
                # Order.objects.all().delete()
                # Product.objects.all().delete()
                import_orders()

            if 'items' in args or 'all' in args or 'just_orders' in args:
                OrderItem.objects.all().delete()
                import_order_items()

            if 'payments' in args or 'all' in args or 'just_orders' in args:
                import_order_payments()

            if 'cc' in args or 'all' in args or 'just_orders' in args:
                import_cc_details()

            # if 'seats' in args or 'all' in args or 'just_orders' in args:
                # update_available_seats()
            
            # if 'inventory' in args or 'all' in args:
                # import_inventory()
            
            if 'dupes' in args:
                # subprocess.call('mysql -uroot -e "drop database sfst"', shell=True)
                # subprocess.call('mysql -uroot -e "create database sfst DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_unicode_ci;"', shell=True)
                # subprocess.call('mysql -uroot sfst < ../db_backups/pre-dupe.dump', shell=True)
                filter_duplicate_orders()
            
            if 'troubleshoot' in args:
                troubleshoot()
            
            if 'tour_days' in args:
                import_tour_days()
            
            if 'combos' in args:
                import_combo_items()