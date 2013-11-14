from decimal import Decimal
from datetime import date, datetime
import json
from StringIO import StringIO

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, Http404
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.views.decorators.cache import never_cache

from satchmo_store.shop.exceptions import OutOfStockError
from satchmo_store.contact.models import Contact, PhoneNumber, AddressBook
from satchmo_store.shop.models import Cart, Order, OrderItem, OrderPayment
from satchmo_store.shop import signals
from satchmo_utils.views import bad_or_missing
from l10n.models import Country

from localsite.session import SessionManager
from localsite import update_context_order_conf_extra
from common.http import JsonResponse
from common.yahoo_placefinder import get_location_details
from localsite.models import TourCategory, TourType, TourGuest, OrderCompletedSiteSkin, CartGuest, OrderHash, TourProduct, TourSchedule
from localsite.forms import BookItForm, PassengerInformationForm, UserAdjustmentRefundForm, UserAdjustmentMoveForm, AuthorizeNetError, PaymentAndCardholderInfoForm, PaymentAndMoveForm, ContactForm
from concierges.models import Concierge
from resellers.models import Reseller
from adjustments.models import Adjustment


def __clear_affiliate(request):
    """
    Clears the affiliate session and also logs user back in to old user if one is there.
    """
    request.session['affiliate'] = None
    if 'old_user_id' in request.session:
        old_user = User.objects.get(id=request.session['old_user_id'])
        old_user.backend = 'django.contrib.auth.backends.ModelBackend'
        logout(request)
        login(request, old_user)


def home(request, template="localsite/home_categories.html"):
    cat_to_tour_map = {}
    d = {}
    tour_categories = TourCategory.objects.filter(active=True, site_skins=request.site_skin)

    aff = None
    if 'affiliate' in request.session:
        affiliate = request.session['affiliate']
        if type(affiliate) is Reseller:
            aff = 'reseller'
        else:
            aff = 'affiliate'

    for cat in tour_categories:
        cat_to_tour_map[cat] = []
        for tour in cat.tours.filter(active=True, featured=True):
            avail_affiliate = aff != 'affiliate' or tour.is_tour_available_to_concierges
            avail_reseller = aff != 'reseller' or tour.is_tour_available_to_resellers
            if avail_affiliate and avail_reseller:
                cat_to_tour_map[cat].append(tour)

    d['tour_categories'] = [cat for cat in tour_categories if cat_to_tour_map[cat]]
    d['cat_to_tour_map'] = cat_to_tour_map
    ctx = RequestContext(request, d)

    return render_to_response(template, context_instance=ctx)

# def home(request, template="localsite/home.html"):
#     d = {}
#     tour_types = TourType.objects.filter(active=True, featured=True)
#
#     d['tour_types'] = tour_types
#     ctx = RequestContext(request, d)
#
#     return render_to_response(template, context_instance=ctx)

def product(request, tour_type_slug, template="localsite/product.html"):
    tour_type = get_object_or_404(TourType, slug=tour_type_slug, active=True)
    d = {}

    if 'affiliate' in request.session:
        affiliate = request.session['affiliate']
        if type(affiliate) is Reseller:
            if not tour_type.is_tour_available_to_resellers:
                return redirect('home')
        elif not tour_type.is_tour_available_to_concierges:
            return redirect('home')

    if request.method == 'POST':
        form = BookItForm(data=request.POST, tour_type=tour_type, request=request)
        if form.is_valid():
            products_to_add = form.get_products()

            for add_info in products_to_add:
                quantity = add_info['quantity']
                product = add_info['product']

                names = []
                for option in form.options:
                    if product.productvariation.optionkey == option.value:
                        names = request.POST.getlist(option.name + '-names')

                # code borrowed from satchmo_store.shop.views.cart.add()
                cart = Cart.objects.from_request(request, create=True)
                # send a signal so that listeners can update product details before we add it to the cart.
                signals.satchmo_cart_details_query.send(
                        cart,
                        product=product,
                        quantity=quantity,
                        request=request,
                        )
                try:
                    added_item = cart.add_item(product, number_added=quantity)
                    # # got to here with no error, now send a signal so that listeners can also operate on this form.
                    signals.satchmo_cart_add_complete.send(cart, cart=cart, cartitem=added_item, product=product, request=request)
                    signals.satchmo_cart_changed.send(cart, cart=cart, request=request)

                    if tour_type.requires_names and names:
                        for name in names:
                            CartGuest.objects.create(cart_item=added_item, name=name)
                except OutOfStockError, cap:
                    d['out_of_stock'] = True

            if not d.get('out_of_stock'):
                return HttpResponseRedirect(reverse('satchmo_cart'))
    else:
        form = BookItForm(tour_type=tour_type, request=request)
        if tour_type.min_calendar_start_date and date.today() < tour_type.min_calendar_start_date:  # min date is ahead of today!
            d['calendar_min_date'] = (tour_type.min_calendar_start_date - date.today()).days
        if tour_type.max_calendar_end_date:
            d['calendar_max_date'] = 0 if date.today() > tour_type.max_calendar_end_date else (tour_type.max_calendar_end_date - date.today()).days

    d.update({'tour_type': tour_type, 'form': form})
    ctx = RequestContext(request, d)

    return render_to_response(template, context_instance=ctx)


def ajax_get_schedule(request, tour_type_id):
    tour_type = get_object_or_404(TourType, id=int(tour_type_id))
    selected_date = request.GET.get('selected_date', None)
    schedules = None
    day = None
    if selected_date:
        try:
            month, day, year = map(int, selected_date.split('/'))
            day = date(year, month, day)
            schedules = tour_type.get_schedule_for_day(day)
        except:
            pass
    else:
        schedules = tour_type.schedules.filter(active=True)
    if schedules:
        return JsonResponse({
            'schedules': [{'id': s.id, 'time': s.pretty_time} for s in schedules],
            'prices': [{'id': o.id, 'label': o.name, 'price': o.price} for o in tour_type.get_options(day=day)]
        })
    else:
        return JsonResponse(data={}, errors=['Invalid date'])

# def ajax_schedules_with_seats(request, tour_type_id, order_item):
#     tour_type = get_object_or_404(TourType, id=int(tour_type_id))
#     selected_date = request.GET.get('selected_date', None)
#     schedules = None
#     order_item = OrderItem.objects.get(id=order_item)
#     available_schedules = []
#     if selected_date:
#         try:
#             month, day, year = map(int, selected_date.split('/'))
#             day = date(year, month, day)
#             schedules = tour_type.get_schedule_for_day(day)
#             for schedule in schedules:
#                 tour = TourProduct.objects.filter(tour_type=tour_type, day=day, tour_time=schedule.tour_time)
#                 if tour.seats_left(order_item.quantity):
#                     available_schedules.append(schedule)
#                 else:
#                     continue
#         except:
#             pass
#     else:
#         available_schedules = tour_type.schedules.filter(active=True)
#     if available_schedules:
#         return JsonResponse({
#             'schedules': [{'id': s.id, 'time': s.pretty_time} for s in available_schedules],
#         })
#     else:
#         return JsonResponse(data={}, errors=['Invalid date'])



@login_required
def affiliate_checkout(request, template='localsite/affiliate_checkout.html'):
    """Allows priviledged users to book "free" tickets.
    """
    if not request.user.can_book_free_tours():
        return HttpResponseRedirect(reverse('satchmo_checkout-step1'))

    d = {}
    cart = Cart.objects.from_request(request, create=False)
    if not cart.numItems:
        return HttpResponseRedirect(reverse('satchmo_cart'))

    if request.method == 'POST':
        form = PassengerInformationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            contact = Contact(first_name=data['first_name'], last_name=data['last_name'])
            if data['email']:
                contact.email = data['email']
            contact.save()

            # Create dummy addresses -- Order.save needs them
            USA = Country.objects.get(iso2_code='US')
            AddressBook(contact=contact, is_default_shipping=True, country=USA).save()
            AddressBook(contact=contact, is_default_billing=True, country=USA).save()

            if data['cell_phone']:
                phone = PhoneNumber(primary=True, type='Mobile', contact=contact)
                phone.phone = data['cell_phone']
                phone.save()

            # Logic taken from Satchmo's update_orderitems
            try:
                order = Order.objects.from_request(request)
                if order.status != '':
                    # This order is being processed. We should not touch it!
                    order = None
            except Order.DoesNotExist:
                order = None

            if not order:
                order = Order(site=cart.site)

            order.contact = contact
            order.total = Decimal('0.00')
            order.tax = Decimal('0.00')
            order.sub_total = cart.total
            order.method = 'Online'
            order.save()

            # Connect to affiliate account, before we ave order status as 'New' (since that fires the email listners
            # and we want the affiliate linked to order because email subject is prepended with their handle)
            affiliate = request.session.get('affiliate', None)
            if affiliate:
                affiliate.orders.add(order)
                affiliate.save()


            order.status = 'New'
            order.save()

            # store what skin was used in the ordering
            OrderCompletedSiteSkin.objects.link(order, request.site_skin)

            for item in cart.cartitem_set.all():
                new_order_item = OrderItem(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    unit_price=item.unit_price,
                    line_item_price=item.line_total)
                new_order_item.save()

                for guest in item.guests.all():
                    TourGuest.objects.create(order_item=new_order_item, name=guest.name)

            # request.session['orderID'] = order.id
            cart.empty()
            order.order_success() # sends signals
            order.recalculate_total()
            order.save()

            # concierge
            if hasattr(affiliate, 'booking_type'):
                # Put amount owed in order.notes and record deposits for concierges that take deposits
                if affiliate.booking_type == Concierge.BOOKING_TYPE_DEPOSIT:
                    deposit_total = 0
                    for item in order.orderitem_set.all():
                        # Check price > 0. Combo product items get priced as 0.
                        # This way combo products won't get charged combo comission + its contents!
                        if item.unit_price > 0:
                            tour_product = item.product.productvariation.parent.product.tourproduct
                            commission = affiliate.commission_for_tour_type(tour_product.tour_type)
                            deposit_total += commission * item.quantity
                    d['deposit_total'] = deposit_total

                    payment = OrderPayment(order=order)
                    payment.payment = 'Concierge Deposit'
                    payment.amount = deposit_total
                    payment.time_stamp = datetime.now()
                    payment.save()
                    order.recalculate_total()

                note = 'Owes $%s by %s' % (str(order.balance), affiliate.handle())
                order.add_note(note)
                order.save()
            # reseller
            elif affiliate:
                affiliate.add_note_to_order(order)
            else:
                order.add_note('Free seat booked by %s' % request.user.username)
                order.save()

            d['order'] = order
            update_context_order_conf_extra(d)
            # __clear_affiliate(request)
    else:
        # default email address in the affiliate checkout form for Concierges
        affiliate = request.session.get('affiliate', None)
        if affiliate and hasattr(affiliate, 'booking_type'):
            form = PassengerInformationForm(initial={'email': affiliate.contact.email})
        else:
            form = PassengerInformationForm()

    d['form'] = form
    ctx = RequestContext(request, d)

    return render_to_response(template, context_instance=ctx)

def login_dispatcher(request):
    user = request.user
    if user.is_staff:
        return HttpResponseRedirect(reverse('administration_home'))
    if user.has_perm('concierges.is_concierge'):
        return HttpResponseRedirect(reverse('concierges_home'))
    if user.has_perm('resellers.is_reseller'):
        return HttpResponseRedirect(reverse('resellers_home'))
    return HttpResponseRedirect(reverse('administration_home'))

def clear_affiliate(request):
    __clear_affiliate(request)
    return JsonResponse()

#
# SATCHMO overrides
#

def sfst_success(request, template_name='shop/checkout/success.html'):
    """
    Overriding the success page satchmo view
    """
    try:
        order = Order.objects.from_request(request)
        # Creates a hash for an Order when the success page is hit by an anonymous user.
    except Order.DoesNotExist:
        return bad_or_missing(request, _('Your order has already been processed.'))

    logout(request) # force logout the user

    SessionManager(request).site_skin(request.site_skin.id)

    # del request.session['orderID']
    d = {}
    d['order'] = order
    update_context_order_conf_extra(d)

    return render_to_response(template_name, d, context_instance=RequestContext(request))
sfst_success = never_cache(sfst_success)

from payment.modules.authorizenet.views import confirm_info as satchmo_confirm_info

def confirm_info(request):
    """
    Overriden just so as to create OrderCompletedSiteSkin instances in the db before order actually completes.
    """
    try:
        order = Order.objects.from_request(request)
    except: # if no order found then redirect to the homepage
        return redirect('home')

    if order:
        OrderCompletedSiteSkin.objects.link(order, request.site_skin)

    return satchmo_confirm_info(request)
confirm_info = never_cache(confirm_info)


def zip_to_city_country(request):
    """Expects a GET parameter 'zip_code' and returns json for city/country etc. mapping to it"""
    zip_code = request.GET.get('zip_code')
    if not zip_code:
        return JsonResponse(success=False)

    try:    # in case there are any Y! side errors or bad json being passed back etc.
        location_details_json = get_location_details(zip_code)
        locations = json.load(StringIO(location_details_json))['places']
    except:
        return JsonResponse(success=False)

    if not locations.get('place'):
        return JsonResponse(success=False)

    location = locations['place'][0]

    data = dict(country=location['country'],
                state=location['admin1'],
                city=location['locality1'] or location['admin2'])
    state_code = location['admin1 attrs'].get('code', '')
    # state code is always with country prefix, f.e. US-CA, US-DC, PL-WA
    if '-' in state_code:
        state_code = state_code.split('-')[1]
    data['state_code'] = state_code
    return JsonResponse(data={'location': data})


def customer_order_detail(request, order_hash, template="localsite/customer_order_detail.html"):
    '''
    View for user to attempt a refund, reschedule, or void of a tour order
    '''
    order_hash = get_object_or_404(OrderHash, hash=order_hash)
    order = order_hash.order
    order.force_recalculate_total()
    order.save()
    contact = order.contact
    changeable_order_items = []
    order_items = []
    already_voided = []
    already_refunded = []
    settled = order.orderhash.is_settled
    void_form = None

    for item in order.orderitem_set.all():
        tour_product = item.product.productvariation.parent.product.tourproduct
        # if to exclude subproducts
        if item.line_item_price == 0:
            continue
        else:
            order_items.append(item)

        # adds items that were already refunded or voided into lists of said items and doesn't add them to changeable list
        try:
            if item.adjustment.status == 2:
                already_refunded.append(item)
                continue
            if item.adjustment.status == 3:
                already_voided.append(item)
                continue
        except Adjustment.DoesNotExist:
            pass

        # if to check whether an item is refundable/rescheduleable
        if tour_product.status != 'NOT_CHANGEABLE':
            changeable_order_items.append(item)

    # if there hasn't been any payments, none of the objects are changeable and the page shows an error message
    if not order.payments.all():
        changeable_order_items = []
        order_items = []
        messages.error(request, 'This order has no recorded payments and so is not changeable.')

    # sets a void form if the order hasn't settled in the system and there aren't any unchangeable items
    if not settled:
        if order_items:
            void_form = UserAdjustmentRefundForm(request, order_items[0], 'void')

    ctx = RequestContext(request, {
        'order': order,
        'contact': contact,
        'changeable_order_items': changeable_order_items,
        'order_items': order_items,
        'void_form': void_form,
        'already_voided': already_voided,
        'already_refunded': already_refunded,
    })

    return render_to_response(template, context_instance=ctx)


def void_order(request, order_id):
    order = get_object_or_404(Order, id=int(order_id))
    # redirect if already voided
    if order.orderhash.already_voided:
        redirect('customer_order_detail', order.orderhash.hash)
    order_item = order.orderitem_set.all()[:1][0]
    action_type = 'void'
    if request.method == 'POST':
        form = UserAdjustmentRefundForm(request, order_item, action_type, request.POST)
        if form.is_valid():
            try:
                msg = form.do_it()
                messages.success(request, msg)
                return redirect('customer_order_detail', order.orderhash.hash)
            except AuthorizeNetError, e:
                messages.error(request, 'There was an error with calling Authorize.NET: %s' % e)
    else:
        raise Http404


FORMS = {
    'move': UserAdjustmentMoveForm,
    'refund': UserAdjustmentRefundForm,
}


def customer_adjust_item(request, order_item, action_type, template='localsite/customer_item_adjustments.html'):
    order_item = get_object_or_404(OrderItem, id=int(order_item))
    tour_product = order_item.product.productvariation.parent.product.tourproduct
    tour_type = tour_product.tour_type
    payment_form = None
    available = False
    if order_item.line_item_price == 0 or tour_product.status == 'NOT_CHANGEABLE' or action_type == 'void':
        raise Http404
    try:
        if order_item.adjustment.status == 2 or order_item.adjustment.status == 3:
            raise Http404
    except Adjustment.DoesNotExist:
        pass
    contact = order_item.order.contact
    FormClass = FORMS[action_type]
    if request.method == 'POST':
        if action_type == 'move':
            if 'street1' not in request.POST:
                form = UserAdjustmentMoveForm(request, order_item, action_type, request.POST)
            else:
                form = PaymentAndMoveForm(request, order_item, action_type, request.POST)
        else:
            form = FormClass(request, order_item, action_type, request.POST)
        if form.is_valid():
            if form.cleaned_data.get('day'):
                available = True
            try:
                msg = form.do_it()
                messages.success(request, msg)
                return redirect('customer_order_detail', order_item.order.orderhash.hash)
            except AuthorizeNetError, e:
                messages.error(request, 'There was an error with calling Authorize.NET: %s' % e)
        else:
            if 'SOLD OUT' in str(form.errors):
                available = False
            if 'street1' in request.POST:
                available = True
    else:
        form = FormClass(request, order_item, action_type)

    ctx = RequestContext(request, {
        'order': order_item.order,
        'order_item': order_item,
        'contact': contact,
        'action_type': action_type,
        'form': form,
        'tour_type': tour_type,
        'payment_form': payment_form,
        'available': available
    })

    return render_to_response(template, context_instance=ctx)

def check_move_availability(request, order_item, template='localsite/fragments/adjustment_form.html'):
    order_item = get_object_or_404(OrderItem, id=int(order_item))
    action_type = 'move'
    tour_type = order_item.product.productvariation.parent.product.tourproduct.tour_type
    order = order_item.order
    contact = order.contact
    credit_card = order.credit_card
    available = False
    payment_form = None
    country = Country.objects.get(iso2_code=order.bill_country)
    if request.method == 'POST':
        if 'street1' not in request.POST:
            form = UserAdjustmentMoveForm(request, order_item, action_type, request.POST)
            if form.is_valid():
                available = True
                payment_form = PaymentAndCardholderInfoForm(initial={'first_name': contact.first_name, 'last_name': contact.last_name, 'postal_code': order.bill_postal_code, 'street1': order.bill_street1, 'city': order.bill_city,
                    'country': country, 'credit_type': credit_card.credit_type, 'state': order.bill_state, 'month_expires': credit_card.expire_month, 'year_expires': credit_card.expire_year})
            else:
                if 'SOLD OUT' in str(form.errors) or 'valid day' in str(form.errors):
                    available = False
                else:
                    available = True
        else:
            form = PaymentAndMoveForm(request, order_item, action_type, request.POST)
            available = True
            if form.is_valid():
                pass

    ctx = RequestContext(request,
        {'form': form, 'payment_form': payment_form, 'action_type': action_type, 'order_item': order_item,
        'tour_type': tour_type, 'available': available}
    )

    return render_to_response(template, context_instance=ctx)

def customer_adjust_not_allowed_reason(request, template='localsite/fragments/customer_adjust_not_allowed_reason.html'):
    return render_to_response(template, context_instance={})


def view_404(request):
    ctx = RequestContext(request, dict(form=ContactForm()))
    return render_to_response('404.html', context_instance=ctx)


def view_500(request):
    ctx = RequestContext(request, dict(form=ContactForm()))
    return render_to_response('500.html', context_instance=ctx)


def booking_error_form(request):
    d = {}
    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_mails()
            d['msg'] = _('Thanks for contacting us')
    ctx = RequestContext(request, d)
    return render_to_response('booking_error_msg.html', context_instance=ctx)
