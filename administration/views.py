from datetime import date, datetime, timedelta
from decimal import Decimal
from random import random
import logging

import django
from django.utils.encoding import force_unicode
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login, logout
from django.contrib.auth.models import User, Group
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.db import IntegrityError
from django.db.models import Q, Count
from django.conf import settings as django_settings
from django.core.mail import send_mass_mail, send_mail
from django.contrib.localflavor.us.us_states import STATE_CHOICES

from product.models import Product
from satchmo_store.contact.models import ContactRole, Contact, AddressBook, PhoneNumber
from satchmo_store.shop.models import Cart, OrderItem
from l10n.models import Country
from satchmo_store.shop.models import Order
from pygooglechart import Axis, StackedVerticalBarChart, StackedHorizontalBarChart, PieChart3D
from django_common.helper import form_errors_serialize
from common.helper import send_mail_in_thread

from common.http import JsonResponse
from common.helper import start_thread, send_mail_using_template

from localsite import update_context_order_conf_extra
from localsite.models import TourType, TourGuest, TourProduct, DayOfWeek, TourSchedule, SiteSkin
from concierges.models import Concierge
from resellers.models import Reseller, ResellerRequest, ResellerCategory
from common.utils import first_and_last_date_in_month, parse_date
from administration.forms import ResellerApprovalForm, BulkInventoryUpdator, AdvancedAnalyticsForm, OrderCheckinForm,\
    EmailCustomerForm, LastNDaysStatsForm
from administration.models import ConciergeMessage, InventoryDayNote, OrderCheckin, OrderItemCheckin,\
    TourProductCheckinFinalization
from administration.forms import GlobalMessageForm, GlobalEmailForm
from product.modules.configurable.models import ConfigurableProduct
from adjustments.models import Adjustment
from adjustments.forms import AdjustmentCreditVoucherForm, AdjustmentDeleteForm


class AdvancedAnalytics(object):
    def __init__(self, orders, exclude_usa=True):
        self.__US_COUNTRY_OBJECT = Country.objects.get(iso2_code='US')
        self.__exclude_usa = exclude_usa

        self.__orders = orders
        self.__order_items = OrderItem.objects.filter(order__in=orders).select_related('product')

        self.total_orders = len(orders)
        self.total_tours_sold = len(self.__order_items)
        self.tour_type_pie_chart_url = self.__tour_type_pie_chart().get_url()
        # self.state_order_graph_url = self.__state_order_graph().get_url()
        self.country_order_graph_url = self.__country_order_graph().get_url()

    def __tour_type_pie_chart(self):
        """
        pie chart showing division of tour types across orders
        """
        # calculate a map of tour_type to #num of them
        tour_type_to_num = {}
        main_products = []
        for item in self.__order_items:
            try:
                main_products.append(item.product.productvariation.parent.product)
            except:
                pass    # old alcatraz tours ?

        # get a list of 2 entry dictionaries.
        for main_product in main_products:
            if tour_type_to_num.get(main_product.tourproduct.tour_type):
                tour_type_to_num[main_product.tourproduct.tour_type] += 1
            else:
                tour_type_to_num[main_product.tourproduct.tour_type] = 1

        # tour_types_sold = TourProduct.objects.filter(product__in=main_products)\
        #     .values('tour_type')\
        #     .annotate(num_sold=Count('tour_type'))

        # Create a chart object of certain size
        pie_chart = PieChart3D(950, 220)

        # Add some data
        tour_types_list = tour_type_to_num.keys()
        data = []
        for tt in tour_types_list:
            data.append(tour_type_to_num.get(tt))
        pie_chart.add_data(data)

        # Assign the labels / colors to the pie data
        pie_chart.set_pie_labels(map(lambda x: '%s (%s)' % (x.name[:35], tour_type_to_num.get(x)), tour_types_list))
        pie_chart.set_colours([self.__random_hex_color() for i in range(0, len(tour_types_list))])
        return pie_chart

    def __country_order_graph(self):
        """
        Shows a vertical bar graph of # orders coming from each US state
        """
        addresses_qset = map(lambda x: x.contact.addressbook_set.all(), self.__orders)
        country_num_map = {}
        for qset in addresses_qset:
            if qset:
                country = qset[0].country
                if not country:
                    continue

                if country_num_map.get(country.name):
                    country_num_map[country.name] += 1
                else:
                    country_num_map[country.name] = 1

        if self.__exclude_usa and country_num_map.get(self.__US_COUNTRY_OBJECT.name):
            del country_num_map[self.__US_COUNTRY_OBJECT.name]
        country_list = country_num_map.keys()

        data = []
        for country_name in country_list:
            data.append(country_num_map.get(country_name))
        data.reverse()
        max_x = max(country_num_map.values()) if len(country_num_map.values()) > 0 else 1
        x_axis = range(0, max_x + 1, max_x/5 if max_x >= 5 else 1)
        x_axis[0] = ''

        chart = StackedHorizontalBarChart(450, len(country_list) * 12, x_range=[0, max_x])
        chart.set_bar_width(7)
        chart.add_data(data)
        chart.set_axis_labels(Axis.LEFT, country_list)
        chart.set_axis_labels(Axis.BOTTOM, x_axis)
        return chart

    def __state_order_graph(self):
        """
        Shows a vertical bar graph of # orders coming from each US state
        """
        addresses_qset = map(lambda x: x.contact.addressbook_set.filter(\
            country=self.__US_COUNTRY_OBJECT), self.__orders)
        states_num_map = {}
        for qset in addresses_qset:
            if qset:
                state = qset[0].state
                if len(state.strip()) == 0:
                    continue

                if states_num_map.get(state):
                    states_num_map[state] += 1
                else:
                    states_num_map[state] = 1

        states_list = map(lambda x: x[0], STATE_CHOICES)
        data = []
        for state in states_list:
            data.append(states_num_map.get(state) if states_num_map.get(state) else 0)

        max_y = max(states_num_map.values()) if len(states_num_map.values()) > 0 else 1
        left_axis = range(0, max_y + 1, max_y/5 if max_y >= 5 else 1)
        left_axis[0] = ''

        state_chart = StackedVerticalBarChart(1000, 220, y_range=[0, max_y])
        state_chart.set_bar_width(13)
        state_chart.add_data(data)
        state_chart.set_axis_labels(Axis.BOTTOM, states_list)
        state_chart.set_axis_labels(Axis.LEFT, left_axis)
        return state_chart

    def __random_hex_color(self):
        color = ''
        for i in range(5):
          color += '%X' % round(random() * 255)
        return color[0:6]

@login_required
@staff_member_required
def home(request, template="administration/home.html"):
    if request.user.has_perm('resellers.is_reseller') and not request.user.is_staff:
        return HttpResponseRedirect(reverse('resellers_home'))

    d = {}
    if request.user.is_superuser:
        if request.GET.get('last_n_days_stats'):
            last_n_days_stats_form = LastNDaysStatsForm(request.GET)

            if last_n_days_stats_form.is_valid():
                last_n_days_stats = last_n_days_stats_form.cleaned_data['last_n_days_stats']
            else:
                last_n_days_stats = 7
        else:
            last_n_days_stats_form = LastNDaysStatsForm()
            last_n_days_stats = 7

        d['last_n_days_stats_form'] = last_n_days_stats_form

        # show basic stats ?
        select_data = {"date": """date_format(time_stamp, '%%m/%%d/%%Y')"""}
        d['num_orders_7_days'] = num_orders_list_7_days = Order.objects.filter(
            time_stamp__gt=(datetime.today().date() - timedelta(days=last_n_days_stats))).\
            order_by('-time_stamp').\
            extra(select=select_data).\
            values('date').annotate(num_orders=Count('id'))

        # one year ago
        today_minus_one_year = datetime.today().date() - timedelta(days=364)
        today_minus_one_year_minus_one_week = today_minus_one_year - timedelta(days=2*last_n_days_stats)    # 2*n to make sure we have enough buffer going back.
        d['num_orders_7_days_one_year_ago'] = num_orders_list_7_days_one_year_ago = Order.objects.filter(
            time_stamp__gt=today_minus_one_year_minus_one_week).\
            filter(time_stamp__lt=today_minus_one_year).\
            order_by('-time_stamp').\
            extra(select=select_data).\
            values('date').annotate(num_orders=Count('id'))[:num_orders_list_7_days.count()]

        # calculate % change
        d['percent_change_from_year_ago'] = []
        day_num = 0
        totals = [0,0,float(0)]

        for num_orders in num_orders_list_7_days:
            totals[0] += num_orders_list_7_days[day_num]['num_orders']
            if num_orders_list_7_days_one_year_ago and num_orders_list_7_days_one_year_ago[day_num] > 0:
                # print num_orders_list_7_days[day_num]['num_orders']
                totals[1] += num_orders_list_7_days_one_year_ago[day_num]['num_orders']
                percent_change = int(round((float(num_orders_list_7_days[day_num]['num_orders'] - num_orders_list_7_days_one_year_ago[day_num]['num_orders'])\
                    /num_orders_list_7_days_one_year_ago[day_num]['num_orders'])*100))
            else:
                percent_change = 'N/A'
            d['percent_change_from_year_ago'].append(percent_change)
            day_num += 1

        # total %
        try:
            totals[2] = int(round((float(totals[0] - totals[1])/totals[1]) * 100))
        except:
            pass

        d['totals_7_days_ago'] = totals[0]
        d['totals_year_go'] = totals[1]
        d['totals_percent_change'] = totals[2]

        if request.method == 'POST':
            form = AdvancedAnalyticsForm(request.POST)
            if form.is_valid():
                # stats based on passed in dates + order_date_type
                if form.cleaned_data['order_date_type'] == str(AdvancedAnalyticsForm.TYPE_ORDER_DATE):
                    d['analytics_total'] = AdvancedAnalytics(Order.objects.filter(\
                        time_stamp__range=(form.cleaned_data['from_date'], form.cleaned_data['to_date'] + timedelta(days=1))),
                        exclude_usa=form.cleaned_data['exclude_usa'])
                else:
                    d['analytics_total'] = AdvancedAnalytics(Order.objects.filter(\
                        id__in=TourProduct.objects.get_order_ids_for_tours_between(\
                            form.cleaned_data['from_date'], form.cleaned_data['to_date'])
                        ), exclude_usa=form.cleaned_data['exclude_usa'])
        else:
            form = AdvancedAnalyticsForm(initial={'exclude_usa': True})

        d['form'] = form

    return render_to_response(template, d, RequestContext(request))

@login_required
@staff_member_required
def inventory(request, template='localsite/inventory.html'):
    d = __calculate_inventory_and_return_context_map(request)
    return render_to_response(template, d, context_instance=RequestContext(request))

@login_required
@staff_member_required
def tour_guests(request, template='administration/tour_guests.html'):
    start_date = datetime.today()
    if 'start_date' in request.GET:
        start_date = datetime.strptime(request.GET['start_date'], '%m/%d/%Y')
    end_date = start_date + timedelta(days=1)

    tour_products = TourProduct.objects.filter(day__gte=start_date,
        day__lte=end_date,
        tour_type__requires_names=True)\
        .order_by('tour_type__name')

    d = {'tour_products': tour_products, 'start_date': start_date}
    return render_to_response(template, d, context_instance=RequestContext(request))

@login_required
@staff_member_required
def tour_guests_update(request):
    tour_guest = TourGuest.objects.get(id=request.POST['id'])
    tour_guest.name = request.POST['name']
    tour_guest.save()
    return JsonResponse()

def public_inventory(request, template='localsite/public_inventory.html'):
    """Page that renders the inventory view (minus links/overbooks/checkins etc.) and makes it accessible to anyone.
    Only TourType's that are is_inventory_public=True are visible on this page."""
    start_date = parse_date(request.GET.get('start_date', ''))
    if not start_date:
        start_date = date.today()
    if start_date < datetime.today().date():
        return HttpResponseRedirect(reverse('public_inventory'))

    d = __calculate_inventory_and_return_context_map(request, only_consider_public_inventory_tours=True)
    return render_to_response(template, d, context_instance=RequestContext(request))

def __calculate_inventory_and_return_context_map(request, only_consider_public_inventory_tours=False):
    """Helper function that takes in a request and responds back with a dictionary with keys: start_date, tour_dates
    and today. tour_dates captures all the data necessary to display the number of seats booked, available, total etc.
    for each tour schedule.

    Optional param is when we only want to consider tour_type's that have is_inventory_public=True"""
    tour_dates = []
    full_inventory = request.GET.get('full', False)
    if full_inventory:
        perfect_inventory = False
    else:
        perfect_inventory = True

    start_date = parse_date(request.GET.get('start_date', ''))
    if not start_date:
        start_date = date.today()
    end_date = start_date + timedelta(days=30)

    inventory_notes = InventoryDayNote.objects.filter(for_date__gte=start_date, for_date__lte=end_date,
        type=InventoryDayNote.TYPE_INVENTORY)
    inventory_notes_map = {}    # date to note instance
    for note in inventory_notes:
        inventory_notes_map[note.for_date] = note

    for x in xrange(0, 30):
        day = start_date + timedelta(days=x)
        dow = DayOfWeek.objects.get(isoweekday=day.isoweekday())
        day_info = {'day': day, 'times': []}

        # If day is greater than today then we loop through schedules so that we don't have to spend the time
        # to create all missing products
        if day >= date.today():
            schedules = dow.tourschedule_set.filter(tour_type__is_combo=False)
            if only_consider_public_inventory_tours:
                schedules = schedules.filter(tour_type__is_inventory_public=True)
            schedules = schedules.select_related('tour_type').order_by('-tour_type__featured', 'tour_time')    # were sorted by tour_type order in the past

            for sched in schedules:
                # active schedule or if not, then at least a tour product exists for it
                if sched.active or sched.tour_type.get_product(day, schedule=sched, create=False):
                    tour_info = {
                        'day': day,
                        'time': sched.pretty_time,
                        'schedule': sched,
                        'tour_type': sched.tour_type,
                        'tour_product': sched.tour_type.get_product(day, schedule=sched, create=False),
                    }
                    if not tour_info['tour_type'].featured and not tour_info['tour_product']:
                        pass
                    elif not tour_info['tour_type'].featured and tour_info['tour_product'] and \
                        tour_info['tour_product'].product.total_sold <= 0:
                        pass
                    elif not tour_info['tour_type'].in_perfect_inventory and not full_inventory:
                        pass
                    else:
                        day_info['times'].append(tour_info)
        # If not, we loop through actual products that have been created since it is possible that the current
        # schedules don't match previous tour schedules
        else:
            tour_products = TourProduct.objects.filter(day=day)
            if not full_inventory:
                tour_products = tour_products.filter(tour_type__in_perfect_inventory=True)
            if only_consider_public_inventory_tours:
                tour_products = tour_products.filter(tour_type__is_inventory_public=True)
            tour_products = tour_products.order_by('-tour_type__featured', 'tour_time')   # were sorted by tour_type order in the past

            for tp in tour_products:
                tour_info = {
                    'day': day,
                    'time': tp.pretty_time,
                    'schedule': tp.schedule,
                    'tour_type': tp.tour_type,
                    'tour_product': tp
                }
                day_info['times'].append(tour_info)

        if day_info['times']:
            day_info['note'] = inventory_notes_map.get(day)
            tour_dates.append(day_info)

    return {
        'start_date': start_date,
        'tour_dates': tour_dates,
        'today': date.today(),
        'is_perfect_inventory': perfect_inventory
    }

def __num_customers_checked_in(tour_product):
    total = 0
    item_checkins = OrderItemCheckin.objects.filter(order_item__in=tour_product.items)
    for checkin in item_checkins:
        total += checkin.num_checkedin
    return int(total)

def __num_customers_expected(tour_product):
    """
    Returns number of customers not checked in yet + ones checked in (may be less than what were expected (order_item quantity))
    """
    item_checkins = OrderItemCheckin.objects.filter(order_item__in=tour_product.items)

    checked_in_items = map(lambda x: x.order_item, item_checkins)
    not_checked_in_items = filter(lambda x: x not in checked_in_items, tour_product.items)

    total = 0
    for checkin in item_checkins:
        total += checkin.num_checkedin
    for item in not_checked_in_items:
        total += item.quantity

    return int(total)

def __total_cash_owed(tour_product):
    """
    Returns all the $'s owed by concierge orders minus the orders that have already checked in (partially or fully)
    """
    total_cash_owed = 0
    order_items = tour_product.items
    orders = set(map(lambda x: x.order, order_items))
    for order in orders:
        if order.is_concierge_order() and not OrderCheckin.objects.filter(order=order): # if concierge and not checkedin already
            total_cash_owed += order.balance
    return total_cash_owed

def __num_seats_available_for_walkins(tour_product):
    """
    Returns the availability of the tour + no-shows (since now they are available)
    """
    walkin_seats_availble = tour_product.seats_available()
    item_checkins = OrderItemCheckin.objects.filter(order_item__in=tour_product.items)
    for item_checkin in item_checkins:
        if item_checkin.num_checkedin != item_checkin.order_item.quantity:
            walkin_seats_availble += (item_checkin.order_item.quantity - item_checkin.num_checkedin)
    return int(walkin_seats_availble)

@login_required
@staff_member_required
def inventory_detail(request, template="localsite/inventory-detail.html"):
    d = {}

    day = parse_date(request.GET.get('date', ''))
    product_id = request.GET.get('product', None)
    schedule_id = request.GET.get('schedule', None)

    if product_id:
        tour_products = TourProduct.objects.filter(product__id=int(product_id)).order_by('tour_time')
        tour_product = tour_products.get()

        day = tour_products[0].day
        if request.GET.get('checkin'):  # checkin page being requested
            note_qset = InventoryDayNote.objects.filter(for_date=day, type=InventoryDayNote.TYPE_CHECKIN)
            d['checkin_note'] = note_qset.get() if note_qset else ''
            if TourProductCheckinFinalization.objects.is_finalized(tour_product):
                d['tour_product_finalization'] = TourProductCheckinFinalization.objects.get(tour_product=tour_product)
            else:
                d['tour_product_finalization'] = None
            d['num_customers_checked_in'] = __num_customers_checked_in(tour_product)
            d['num_customers_expected'] = __num_customers_expected(tour_product)
            d['num_seats_available_for_walkins'] = __num_seats_available_for_walkins(tour_product)
            d['total_cash_owed'] = __total_cash_owed(tour_product)
            template='localsite/inventory_checkin.html'
    elif schedule_id:
        # let inactive ones come through too, since some tour products might exist for them
        schedule = get_object_or_404(TourSchedule, id=int(schedule_id))
        tour_products = [schedule.tour_type.get_product(day, schedule=schedule, create=False), ]
    else:
        tour_products = TourProduct.objects.filter(day=day).order_by('tour_time')

    form = GlobalEmailForm()
    if request.method == 'POST':   # a form was posted
        if request.POST.get('is_global_email'):   # global email. Send a mass mail.
            form = GlobalEmailForm(request.POST)
            if form.is_valid():
                message_list = []
                for product in tour_products:
                    for c in product.passengers():
                        if c.email:
                            message_list += [(form.cleaned_data['subject'], form.cleaned_data['message'],
                                django_settings.DEFAULT_FROM_EMAIL, (c.email,))]
                start_thread(send_mass_mail, tuple(message_list))
                messages.success(request, '%s Emails successfully sent' % len(message_list))

    d['global_email_form'] = form

    d.update({
        'tour_products': tour_products,
        'day': day,
        'tomorrow': day + timedelta(days=1),
        'yesterday': day - timedelta(days=1),
    })

    return render_to_response(template, d, context_instance=RequestContext(request))

@login_required
@staff_member_required
def checkin_customer(request):
    """
    Expects request POST params 'order_id' and 'product_id'. Also 'is_cash', relevant if its a concierge order.
    """
    if not request.method == 'POST' or not request.POST.get('order_id') or not request.POST.get('product_id'):
        raise Http404

    d = {}

    if not request.POST.get('is_cash'):
        is_cash = True
    else:
        is_cash = request.POST.get('is_cash') == 'true'

    product = get_object_or_404(Product, id=request.POST.get('product_id'))
    tour_product = product.tourproduct
    order = get_object_or_404(Order, id=request.POST.get('order_id'))
    order_items = OrderItem.objects.filter(order=order, product__in=product.configurableproduct.productvariation_set.all())

    order_checkin, created = OrderCheckin.objects.get_or_create(order=order)
    if created and order.is_concierge_order():  # $'s are owed etc.
        d['total_cash_owed'] = str(__total_cash_owed(tour_product)) # optimization to not call unless $ owed
        order_checkin.amount_taken_sales = order.balance
        order_checkin.amount_type = OrderCheckin.TYPE_CASH if is_cash else OrderCheckin.TYPE_CREDIT
        order_checkin.save()

    for item in order_items:
        OrderItemCheckin.objects.get_or_create(order_checkin=order_checkin, order_item=item, num_checkedin=item.quantity)

    d.update({
        'num_customers_checkedin': __num_customers_checked_in(tour_product),
        'num_customers_expected': __num_customers_expected(tour_product),
    })
    return JsonResponse(data=d)

@login_required
@staff_member_required
def edit_customer_checkin(request, template_name='administration/fragments/edit_customer_checkin.html'):
    """
    Edit more data (like $'s given through cash/credit card), # of customers checked in etc.
    Expects GET params 'order_id' and 'product_id'.
    """
    if request.method == 'GET':
        if not request.GET.get('order_id') or not request.GET.get('product_id'):
            raise Http404

        product = get_object_or_404(Product, id=request.GET.get('product_id'))
        order = get_object_or_404(Order, id=request.GET.get('order_id'))

        order_checkin = get_object_or_404(OrderCheckin, order=order)

        order_items = OrderItem.objects.filter(order=order, product__in=product.configurableproduct.productvariation_set.all())
        order_item_checkins = OrderItemCheckin.objects.filter(order_checkin=order_checkin, order_item__in=order_items)
        for item_checkin in order_item_checkins:
            item_checkin.quantity_range_list = range(0, item_checkin.order_item.quantity + 1)

        d = {}
        d['product'] = product
        d['order_checkin'] = order_checkin
        d['order_checkin_form'] = OrderCheckinForm(instance=order_checkin)
        d['order_item_checkins'] = order_item_checkins
        d['is_concierge_order'] = order.is_concierge_order()
        return render_to_response(template_name, d, RequestContext(request))
    else:
        order_checkin = get_object_or_404(OrderCheckin, id=request.POST.get('order_checkin_id'))
        product = get_object_or_404(Product, id=request.POST.get('product_id'))

        order_checkin_form = OrderCheckinForm(request.POST, instance=order_checkin)
        if order_checkin_form.is_valid():
            order_checkin_form.save()

            order_items = OrderItem.objects.filter(order=order_checkin.order, \
                product__in=product.configurableproduct.productvariation_set.all())
            order_item_checkins = OrderItemCheckin.objects.filter(order_checkin=order_checkin, order_item__in=order_items)

            for item_checkin in order_item_checkins:
                if request.POST.get('order_item_checkin_%s' % item_checkin.id):
                    item_checkin.num_checkedin = int(request.POST.get('order_item_checkin_%s' % item_checkin.id))
                    item_checkin.save()

            tour_product = product.tourproduct
            return JsonResponse(data={
                        'num_customers_checkedin': __num_customers_checked_in(tour_product),
                        'num_customers_expected': __num_customers_expected(tour_product),
                        'num_seats_available_for_walkins': __num_seats_available_for_walkins(tour_product),
                        # 'total_cash_owed': str(__total_cash_owed(tour_product))
                    })
        else:
            return JsonResponse(success=False, errors=[force_unicode(order_checkin_form.non_field_errors())])

@login_required
@staff_member_required
def finalize_checkin(request):
    """
    Expects a POST param 'tour_product_id'
    """
    if request.method != 'POST':
        raise Http404

    tour_product_id = request.POST.get('tour_product_id')
    if not tour_product_id:
        raise Http404

    tour_product = get_object_or_404(TourProduct, pk=tour_product_id)
    if not TourProductCheckinFinalization.objects.filter(tour_product=tour_product):
        TourProductCheckinFinalization.objects.create(tour_product=tour_product, done_by=request.user)

    # create vouchers for all that didn't show for this tour
    checked_in_items = map(lambda x: x.order_item, OrderItemCheckin.objects.filter(order_item__in=tour_product.items))
    not_checked_in_items = filter(lambda x: x not in checked_in_items, tour_product.items)
    orders_with_other_items_to_voucher = []  # for combo vouchering warning message
    for item in not_checked_in_items:
        if item.order.is_concierge_order():
            concierge = item.order.get_concierge_if_any()
            form = AdjustmentDeleteForm(request, item.order, {
                'user': request.user.id,
                'item': [item.id],
                'free_order_type': AdjustmentDeleteForm.TYPE_CONCIERGE,
                'additional_notes': 'NO SHOW!! (Concierge Order) ',
                'concierge_account': str(concierge)
            })
            if form.is_valid():
                form.do_it()

                # send an email to concierge
                concierge_email = concierge.contact.email
                if concierge_email:
                    send_mail("order #%s: Customer did not show up for tour" % item.order.id,
                        "Please be advised that your customer (%s) did not show up for their tour today.  We wanted to make sure you were informed of this.  --- Customer Service" % item.order.contact.full_name,
                        django_settings.DEFAULT_FROM_EMAIL,
                        [django_settings.DEFAULT_TO_EMAIL, concierge.contact.email])
        else:
            form = AdjustmentCreditVoucherForm(request, item.order, initial={
                'user': request.user.id,
                'item': [item.id],
                'voucher_type': Adjustment.VOUCHER_STANDBY_CREATED,
                'notes': 'NO SHOW!! '
            })

            form.do_it_noshow(item.id, 'NO SHOW! - Checkin finalized by: %s' % request.user)

            # warning message to voucher order items part of a combo
            if 'combo' in item.order.notes.lower() and item.order not in orders_with_other_items_to_voucher:
                orders_with_other_items_to_voucher.append(item.order)

    if len(not_checked_in_items) > 0 and len(orders_with_other_items_to_voucher) > 0:
        order_error_string = ''
        for order in orders_with_other_items_to_voucher:
            order_error_string += '<a href="%s">%s</a>, ' % (reverse('order_detail', args=[order.id]), order.id)
        messages.error(request, "ALERT: Following orders may require vouchering for the combo part of this tour: %s" % order_error_string)

    # generate a security email
    suspicious_items = []   # list of items that need to be reported to superuser (John hardcoded here)
    for item in checked_in_items:
        if item.order.is_concierge_order() and\
            OrderItemCheckin.objects.get(order_item=item).order_checkin.amount_taken_sales != item.order.balance:
            item.is_checked_in = True
            item.concierge = Concierge.objects.get(orders=item.order)
            # if checked in and balance not maching up
            suspicious_items.append(item)

    for item in not_checked_in_items:
        if item.order.is_concierge_order():
            item.is_checked_in = False
            item.concierge = Concierge.objects.get(orders=item.order)
            suspicious_items.append(item)

    if len(suspicious_items) > 0:
        logging.debug('Sending suspicious order emails about: %s' % suspicious_items)
        send_mail_using_template('Security Email - based on Finalization of %s' % tour_product,
            'administration/emails/finalization_security_email.html', django_settings.DEFAULT_FROM_EMAIL,
            ['john@sanfranshuttletours.com'], {'user': request.user, 'tour_product': tour_product,
                'suspicious_items': suspicious_items},
                connection=django.core.mail.get_connection(backend='django.core.mail.backends.smtp.EmailBackend'))

    return JsonResponse()

@login_required
@staff_member_required
def checkin_reports(request, template_name='administration/checkin_reports.html'):
    tour_date = parse_date(request.GET.get('tour_date', ''))
    if not tour_date:
        tour_date = date.today()

    class ProductData(object):
        def __init__(self):
            self.num_checkedin = 0
            self.amount_taken_sales = 0
            self.amount_taken_change_order_fees = 0

            self.total_amount_collected = 0
            self.cash_received = 0
            self.cc_batch = 0
            self.grand_total = 0

            self.finalization = None

        def __iadd__(self, other):
            self.num_checkedin += other.num_checkedin
            self.amount_taken_sales += other.amount_taken_sales
            self.amount_taken_change_order_fees += other.amount_taken_change_order_fees

            self.total_amount_collected += other.total_amount_collected
            self.cash_received += other.cash_received
            self.cc_batch += other.cc_batch
            self.grand_total += other.grand_total

            return self

    d = {}
    product_ids = []

    for tour_product in TourProduct.objects.filter(day=tour_date):
        try:
            product_ids += tour_product.product.configurableproduct.productvariation_set.all().values_list(\
                'product__id', flat=True)
        except ConfigurableProduct.DoesNotExist:
            product_ids += [tour_product.product.id]

    order_item_checkins = OrderItemCheckin.objects.filter(order_item__product__id__in=product_ids)
    # product_set = set(map(lambda x: x.order_item.product.productvariation.parent.product, order_item_checkins))

    product_to_data_map = {}
    order_checkin_processed = []    # so as to count $'s only once per order
    for item_checkin in order_item_checkins:
        product = item_checkin.order_item.product.productvariation.parent.product
        if not product_to_data_map.get(product):
            product_to_data_map[product] = ProductData()
            if TourProductCheckinFinalization.objects.is_finalized(product):
                product_to_data_map[product].finalization = TourProductCheckinFinalization.objects.get(tour_product=product)

        if item_checkin.order_checkin not in order_checkin_processed:
            data = product_to_data_map[product]
            order_checkin = item_checkin.order_checkin

            # incoming $'s
            if order_checkin.amount_taken_sales:
                data.amount_taken_sales += order_checkin.amount_taken_sales
            if order_checkin.amount_taken_change_order_fees:
                data.amount_taken_change_order_fees += order_checkin.amount_taken_change_order_fees

            # totals
            if order_checkin.amount_type == OrderCheckin.TYPE_CASH:
                data.cash_received += order_checkin.total_amount_in()
            else:
                data.cc_batch += order_checkin.total_amount_in()
            data.total_amount_collected = order_checkin.total_amount_in()
            data.grand_total += order_checkin.gross_amount()

            # append to list so as not to re-process
            order_checkin_processed.append(item_checkin.order_checkin)

        product_to_data_map[product].num_checkedin += item_checkin.num_checkedin

    cross_tour_totals = ProductData()
    for k, v in product_to_data_map.items():
        cross_tour_totals += v

    # print product_to_data_map
    d['product_to_data_map'] = product_to_data_map
    d['cross_tour_totals'] = cross_tour_totals
    d['tour_date'] = tour_date

    note_qset = InventoryDayNote.objects.filter(for_date=tour_date, type=InventoryDayNote.TYPE_CHECKIN)
    d['checkin_note'] = note_qset.get() if note_qset else ''

    return render_to_response(template_name, d, RequestContext(request))

@login_required
@staff_member_required
def inventory_update(request):
    product_id = request.POST.get('product_id')

    if not product_id:  # when no product exists for that tour type / schedule yet
        date = parse_date(request.POST.get('date', ''))
        schedule_id = request.POST.get('schedule_id')
        if date and schedule_id:
            schedule = get_object_or_404(TourSchedule, id=schedule_id)
            product_id = schedule.tour_type.get_product(date, schedule, create=True).product.id

    new_inventory = request.POST.get('new_inventory')
    if not product_id or not new_inventory or int(new_inventory) < 0:
        return JsonResponse(success=False)

    product = get_object_or_404(Product, id=product_id)
    product.items_in_stock = new_inventory
    product.save()
    return JsonResponse()

@login_required
@staff_member_required
def bulk_inventory_updator(request, template='administration/bulk_inventory_updator.html'):
    if not request.user.is_superuser:
        raise Http404

    d = {}

    if request.method == 'GET':
        d['form'] = BulkInventoryUpdator()
    else:
        form = d['form'] = BulkInventoryUpdator(request.POST)
        if form.is_valid():
            tour_schedule = form.cleaned_data['tour_schedule']
            tour_type = tour_schedule.tour_type
            day = form.cleaned_data['start_date']
            while day <= form.cleaned_data['end_date']:
                if day.isoweekday() in map(lambda x: x.isoweekday, form.cleaned_data['days_of_week']):
                    product = tour_type.get_product(day, tour_schedule).product
                    product.items_in_stock = form.cleaned_data['inventory']
                    product.save()
                day = day + timedelta(days=1)
            d['success'] = True

    return render_to_response(template, d, RequestContext(request))

@login_required
@staff_member_required
def concierge_admin(request, template="administration/concierge_admin.html"):
    """
    Renders the home screen of the concierge admin with links etc. and 2 forms:
    + To post a global message on the concierge homepages
    + To send a global email to all concierges
    """
    d = {}

    d['global_email_form'] = GlobalEmailForm()
    qset = ConciergeMessage.objects.filter(is_global=True)

    if qset:
        global_concierge_message = qset.get()
        d['global_message_form'] = GlobalMessageForm(instance=global_concierge_message)
    else:
        d['global_message_form'] = GlobalMessageForm()

    if request.method == 'POST':   # a form was posted
        if request.POST.get('is_global_note'): # global note
            form = GlobalMessageForm(request.POST)
            if form.is_valid():
                if qset:
                    global_concierge_message.message = form.cleaned_data['message']
                    global_concierge_message.save()

                    if not form.cleaned_data['not_notify_email']:   # user did not check the checkbox
                        message_list = []

                        message_subject = 'There is a global note from SF Shuttle Tours'
                        message_body = 'SF Shuttle Tours has updated the Global Note in the Concierge Admin.\n\n'
                        message_body += 'You can see the note here: http://%s%s' % (django_settings.SITE_DOMAIN, reverse('concierges_home'))

                        for c in Concierge.objects.select_related('contact').all():
                            message_list += [(message_subject, message_body,
                                django_settings.DEFAULT_FROM_EMAIL, (c.contact.email,))]

                        start_thread(send_mass_mail, tuple(message_list))
                else:
                    ConciergeMessage.objects.create(is_global=True, message=form.cleaned_data['message'])
                return HttpResponseRedirect(reverse('concierge_admin'))
            else:
                d['global_message_form'] = form
        elif request.POST.get('is_global_email'):   # global email. Send a mass mail.
            form = GlobalEmailForm(request.POST)
            if form.is_valid():
                message_list = []
                for c in Concierge.objects.select_related('contact').all():
                    message_list += [(form.cleaned_data['subject'], form.cleaned_data['message'],
                        django_settings.DEFAULT_FROM_EMAIL, (c.contact.email,))]

                start_thread(send_mass_mail, tuple(message_list))
                return HttpResponseRedirect(reverse('concierge_admin'))
            else:
                 d['global_email_form'] = form

    ctx = RequestContext(request, d)
    return render_to_response(template, context_instance=ctx)

@login_required
@staff_member_required
def concierge_contact_sheet(request, template='administration/concierge_contact_sheet.html'):
    """
    Expects an optional "sort_by" parameter. It should be of value 'name' or 'rev'
    """
    sort_by = request.GET.get('sort_by')
    concierges = Concierge.objects.select_related('contact', 'orders').all()

    for c in concierges:
        if len(c.orders.all()) > 0:
            all_orders = c.orders.all()
            # for o in all_orders:
            #     o.force_recalculate_total()
            #     o.save()
            #
            c.total_revenue = reduce(lambda x, y: x + y, map(lambda x: x.total, all_orders)).quantize(Decimal('0'))
            c.months_12_revenue = reduce(lambda x, y: x + y,\
                map(lambda x: x.total if (x.time_stamp >= datetime.today() - timedelta(days=365)) else Decimal('0'), all_orders))\
                .quantize(Decimal('0'))
        else:
            c.total_revenue = 0
            c.months_12_revenue = 0

    if sort_by == 'name':
        concierges = sorted(concierges, key=lambda x:x.contact.first_name)
    else:
        concierges = sorted(concierges, lambda x, y: int(y.months_12_revenue - x.months_12_revenue))

    d = {'concierges': concierges}
    return render_to_response(template, d, RequestContext(request))

@login_required
@staff_member_required
def concierge_pay_commission(request, template="administration/concierge_pay_commission.html"):
    """
    Gives date options and lists all the concierges due for commission in that pay period
    """
    d = {}

    label = ''
    date_format = '%B %d, %Y'
    today = date.today()
    start_date = parse_date(request.GET.get('start_date', ''))
    end_date = parse_date(request.GET.get('end_date', ''))
    day = parse_date(request.GET.get('day'))

    # Default range is previous half of whatever is today. So if 16th, then 1-15th of current month. If 14th, then 1-15th
    # of previous month.
    if not start_date and not end_date and not day:
        if today.day > 15:
            start_date = date(today.year, today.month, 1)
            end_date = date(today.year, today.month, 15)
        else:
            today_minus_15 = today - timedelta(days=15)
            first_day, last_day = first_and_last_date_in_month(today_minus_15)  # of previous month
            start_date = date(today_minus_15.year, today_minus_15.month, 16)
            end_date = last_day
    # If we have a day, find the half of month the day is in
    elif day:
        first_day, last_day = first_and_last_date_in_month(day)
        if day.day <= 15:
            start_date = first_day
            end_date = date(day.year, day.month, 15)
        else:
            start_date = date(day.year, day.month, 16)
            end_date = last_day
    elif start_date and end_date:
        label = '%s to %s' % (start_date.strftime(date_format), end_date.strftime(date_format))

    recent_periods = []

    for x in xrange(0, 4):
        new_month = today.month - x
        new_year = today.year
        if new_month < 1:
            new_month = 12 - abs(new_month)
            new_year = new_year - 1
        beg_date = date(new_year, new_month, 1)
        mid_date = date(new_year, new_month, 16)
        if mid_date < today:
            recent_periods.insert(0, [mid_date, mid_date.strftime('%B'), '2nd Half'])
        if beg_date < today:
            recent_periods.insert(0, [beg_date, beg_date.strftime('%B'), '1st Half'])

    if not label:
        half = 'First Half' if start_date.day <= 15 else 'Second Half'
        label = '%s of %s' % (half, start_date.strftime('%B'))

    # now figure out which concierges to show
    order_ids = TourProduct.objects.get_order_ids_for_tours_between(start_date, end_date)
    concierges = set(Concierge.objects.filter(orders__in=order_ids))

    d.update({
        'recent_periods': recent_periods,
        'label': label,
        'start_date': start_date,
        'end_date': end_date,
        'concierges': concierges
    })

    return render_to_response(template, d, RequestContext(request))

@login_required
@staff_member_required
def concierge_commission_print(request, cid, template="administration/concierge_commission_print.html"):
    d = {}
    start_date = parse_date(request.GET.get('start_date', ''))
    end_date = parse_date(request.GET.get('end_date', ''))

    if not start_date or not end_date:
        raise Http404

    concierge = get_object_or_404(Concierge, id=cid)
    total_commission, orders = concierge.order_report(start_date, end_date)

    d.update({
        'total_commission': total_commission,
        'orders': orders,
        'concierge': concierge,
        'start_date': start_date,
        'end_date': end_date,
        'tour_types': TourType.objects.filter(active=True, featured=True, default_site_skin__is_concierge_cta=True),
    })
    return render_to_response(template, d, RequestContext(request))

@login_required
@staff_member_required
def become_user(request, user_id):
    old_user_id = request.user.id
    new_user = get_object_or_404(User, id=int(user_id))
    new_user.backend = 'django.contrib.auth.backends.ModelBackend'
    logout(request)
    login(request, new_user)
    request.session['old_user_id'] = old_user_id
    if new_user.has_perm('concierges.is_concierge'):
        return HttpResponseRedirect(reverse('concierges_home'))
    else:
        return HttpResponseRedirect(reverse('resellers_home'))

@login_required
def back_to_old_user(request):
    if 'old_user_id' not in request.session:
        raise Http404
    old_user = User.objects.get(id=request.session['old_user_id'])
    old_user.backend = 'django.contrib.auth.backends.ModelBackend'
    logout(request)
    login(request, old_user)
    return HttpResponseRedirect(reverse('administration_home'))

@login_required
@staff_member_required
def manage_resellers(request, template="administration/manage_resellers.html"):
    reseller_categories = ResellerCategory.objects.all()
    resellers = Reseller.objects.all()
    pending = ResellerRequest.objects.all()
    ctx = RequestContext(request, {
        'reseller_categories': reseller_categories,
        'resellers': resellers,
        'pending': pending,
    })

    return render_to_response(template, context_instance=ctx)


@login_required
def reseller_report(request, reseller_id=None, template="administration/reseller_report.html"):
    """This view is used by admin and resellers"""

    try:
        reseller = Reseller.objects.get(contact__user=request.user)
    except Reseller.DoesNotExist:
        # This isn't a reseller viewing the page, safe to get by id
        # after we check for proper permissions TODO: check for proper perms
        reseller = get_object_or_404(Reseller, id=int(reseller_id))

    try:
        reseller_address = reseller.contact.addressbook_set.all()[0]
    except IndexError:
        reseller_address = None

    today = date.today()
    day_in_month = parse_date(request.GET.get('day_in_month', ''))
    start_date = parse_date(request.GET.get('start_date', ''))
    end_date = parse_date(request.GET.get('end_date', ''))

    if day_in_month:
        start_date, end_date = first_and_last_date_in_month(day_in_month)
    elif not start_date:
        # before the 15th of the month we default to last month
        if today.day <= 15:
            day_in_last_month = today - timedelta(days=16)
            start_date, end_date = first_and_last_date_in_month(day_in_last_month)
        # after the 15th of the month we default to this month
        else:
            start_date, end_date = first_and_last_date_in_month(today)

    # figure out all the products and their id's within the date range
    order_ids = TourProduct.objects.get_order_ids_for_tours_between(start_date, end_date, orders_in=reseller.orders.all())

    orders = reseller.orders.filter(id__in=order_ids).order_by('id')

    total_tickets = 0
    total_cost = 0
    for order in orders:
        # total_cost += order.total
        for item in order.orderitem_set.all():
            total_tickets += item.quantity
            total_cost += item.line_total

    total_reseller_pays = total_reseller_commission = 0
    if reseller.discount:
        total_reseller_pays = round(total_cost * ((100 - reseller.discount) / 100), 2)
        invoice_amount = float(total_cost) - total_reseller_pays
    if reseller.commission:
        total_reseller_commission = round(total_cost * (reseller.commission / 100), 2)
        invoice_amount = float(total_cost) - total_reseller_commission

    recent_months = []
    for x in xrange(0, 6):
        new_month = today.month - x
        new_year = today.year
        # account for rolling over new years
        if new_month < 1:
            new_month = 12 - abs(new_month)
            new_year = today.year - 1
        recent_months.insert(0, date(new_year, new_month, 1))

    ctx = RequestContext(request, {
        'start_date': start_date,
        'end_date': end_date,
        'reseller': reseller,
        'reseller_address': reseller_address,
        'orders': orders,
        'total_tickets': total_tickets,
        'total_cost': total_cost,
        'total_reseller_pays': total_reseller_pays,
        'total_reseller_commission': total_reseller_commission,
        'recent_months': recent_months,
        'invoice_amount': invoice_amount
    })

    return render_to_response(template, context_instance=ctx)

@login_required
@staff_member_required
def pending_reseller_request(request, request_id, template="administration/pending_reseller_request.html"):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('manage_resellers'))

    d = {}
    rr = get_object_or_404(ResellerRequest, id=int(request_id))

    initial = {
        'username': rr.email,
        'password': User.objects.make_random_password(length=6),
        'reseller_type': rr.reseller_type,
    }

    if request.method == 'POST':
        approve = request.POST.get('approve', False)
        delete = request.POST.get('delete', False)

        if approve:
            form = ResellerApprovalForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                group, created = Group.objects.get_or_create(name='Reseller')
                role, created = ContactRole.objects.get_or_create(key='Reseller')

                user = User()
                user.username = cd['username']
                user.first_name = rr.first_name
                user.last_name = rr.last_name
                user.email = rr.email
                user.save()
                user.groups.add(group)
                user.save()

                user.set_password(cd['password']) # TODO What should we default to?

                contact = Contact()
                contact.first_name = rr.first_name
                contact.last_name = rr.last_name
                contact.user = user
                contact.role = role
                contact.email = rr.email
                contact.notes = rr.description
                contact.save()

                address = AddressBook()
                address.contact = contact
                address.street1 = rr.street
                address.city = rr.city
                address.state = rr.state
                address.postal_code = rr.zip_code
                address.country = Country.objects.get(iso2_code='US')
                address.save()

                phone = PhoneNumber()
                phone.contact = contact
                phone.type = 'Work'
                phone.phone = rr.phone
                phone.primary = True
                phone.save()

                reseller = Reseller()
                reseller.contact = contact
                reseller.company_name = rr.company_name
                reseller.commission = cd['commission']
                reseller.discount = cd['discount']
                reseller.website = rr.website
                reseller.reseller_type = rr.reseller_type
                reseller.code = hash(user.username + rr.company_name)
                reseller.save()

                rr.delete()
                messages.success(request, 'Reseller "%s" successfully created.' % reseller.company_name)

                # shoot a success email to the reseller
                r_subject = "You're Approved"
                r_message = "YOU'RE APPROVED!!! Thank you for being accepted to sell San Francisco Shuttle Tours and/or Tours of California to your clients and website customers.\n\n"
                r_message += 'You can login at the url below with the email address this was sent to and the temporary password "%s". Please change your password after you login.\n\n' % cd['password']
                r_message += 'http://%s%s\n\n' % (django_settings.SITE_DOMAIN, reverse('resellers_home'))
                r_message += 'After logging in, you will also be able to view your discount urls. If you have any questions about how to proceed, please contact us at 415-513-5400 and ask for a Manager.\n'

                start_thread(send_mail, r_subject, r_message, django_settings.DEFAULT_FROM_EMAIL, [django_settings.DEFAULT_TO_EMAIL, rr.email])

                return HttpResponseRedirect(reverse('manage_resellers'))
        if delete:
            messages.success(request, 'Reseller request for "%s" successfully deleted' % rr.company_name)
            rr.delete()
            return HttpResponseRedirect(reverse('manage_resellers'))
    else:
        form = ResellerApprovalForm(initial=initial)

    d['form'] = form
    d['rr'] = rr
    ctx = RequestContext(request, d)
    return render_to_response(template, context_instance=ctx)

@login_required
@staff_member_required
def search_orders(request, template="administration/search_orders.html"):
    orders = []
    if request.GET.keys():
        search_conducted = True

        order_id = request.GET.get('order_id', 0)
        fname = request.GET.get('fname', '')
        lname = request.GET.get('lname', '')
        order_date = parse_date(request.GET.get('order_date', ''))
        tour_date = parse_date(request.GET.get('tour_date', ''))
        status = int(request.GET.get('status', 0))

        orders = Order.objects.filter(status="New").order_by('-time_stamp')
        if order_id:
            try:
                orders = orders.filter(id=order_id)
            except: pass
        if fname:
            orders = orders.filter(contact__first_name__icontains=fname)
        if lname:
            orders = orders.filter(contact__last_name__icontains=lname)
        if order_date:
            orders = orders.filter(time_stamp__year=order_date.year, time_stamp__month=order_date.month, time_stamp__day=order_date.day)
        if status != 0:
            orders = orders.filter(orderitem__adjustment__status=status)
            # I hate django templates sometimes -- this is so i can compare an int with an int on the status select box
            request.status = int(status)


        if tour_date:
            # figure out all variation product_id's
            order_ids = TourProduct.objects.get_order_ids_for_tours_between(tour_date, tour_date)

            if order_ids:
                orders = orders.filter(id__in=order_ids)
        orders = orders.distinct()
    else:
        orders = []
        search_conducted = False

    ctx = RequestContext(request, {
        'orders': orders,
        'search_conducted': search_conducted
    })

    return render_to_response(template, context_instance=ctx)

@login_required
@staff_member_required
def order_detail(request, order_id, template="administration/order_detail.html"):
    order = get_object_or_404(Order, id=int(order_id))
    order.force_recalculate_total()
    order.save()

    if request.method == 'POST':
        order.notes = request.POST.get('notes')
        order.save()

    void_refund_request = False
    for item in order.orderitem_set.all():
        if item.STATUS and item.adjustment.status == Adjustment.REFUND_REQUESTED:
            void_refund_request = True

    # Free orders can be 'deleted', others have to be voided/refunded
    free_order = True
    for payment in order.payments.all():
        if payment.payment != 'Concierge Deposit':
            free_order = False

    contact = order.contact
    contact.other_orders = contact.order_set.exclude(id=order.id)
    ctx = RequestContext(request, {
        'order': order,
        'contact': contact,
        'free_order': free_order,
        'void_refund_request': void_refund_request,
    })

    return render_to_response(template, context_instance=ctx)

@login_required
@staff_member_required
def order_email_customer(request, order_id, template='administration/fragments/order_email_customer.html'):
    """Renders a fragment for email body and sends an email to the customer on POST"""
    d = {}
    order = d['order'] = get_object_or_404(Order, id=int(order_id))

    if request.method == 'GET':
        d['form'] = EmailCustomerForm(initial={'email_subject': 'Important Message from SF/LA Shuttle Tours / Wine Country Tour Shuttle'})
    else:
        form = EmailCustomerForm(request.POST)
        if form.is_valid():
            # send email
            customer_email_address = order.contact.email
            send_mail_in_thread(form.cleaned_data['email_subject'], form.cleaned_data['email_body'],
                django_settings.DEFAULT_FROM_EMAIL, [customer_email_address])
            return JsonResponse()
        else:
            return JsonResponse(success=False, data={'form': form_errors_serialize(form)})

    return render_to_response(template, context_instance=RequestContext(request, d))

@login_required
@staff_member_required
def overbookings_detail(request, tour_id, template='administration/fragments/overbookings_detail.html'):
    '''
    View to display the fragment overbookings_detail, which shows OverbookingAttempts
    for a specific TourProduct
    '''
    d = {}
    tour = get_object_or_404(TourProduct, product=tour_id)
    overbookings = tour.overbookings.all()
    d['tour'] = tour
    d['overbookings'] = overbookings
    return render_to_response(template, context_instance=RequestContext(request, d))

def debug(request):
    from django.db.models import Sum
    from decimal import Decimal
    from product.models import Product
    from legacy.shelf import Shelf
    from legacy.models import *
    from legacy.models import ContactOrganization as LegacyOrg
    from localsite.models import TourType, TeamMember
    from concierges.models import Concierge, ConciergeCommission
    from resellers.models import Reseller, ResellerRequest, ResellerCategory
    from adjustments.models import Adjustment, AdjustmentHistory
    from product.modules.configurable.models import ProductVariation

    from satchmo_store.contact.models import Contact, ContactRole, Organization, ContactOrganization, ContactOrganizationRole, PhoneNumber, AddressBook
    from satchmo_store.shop.models import Order, OrderItem, OrderPayment
    from payment.models import CreditCardDetail
    from l10n.models import Country
    from localsite.management.commands.importsfst import get_tour_type

    debug_info = []
    tour_days = ProductTourday.objects.filter(id__gte=3333).iterator()
    for tour_day in tour_days:
        try:
            d, m, y = map(int, tour_day.date.split('-'))
        except ValueError:
            pass

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
        if day < date(2010, 2, 1):
            continue

        try:
            dts = ProductDatetimeschema.objects.get(id=int(tour_day.time))
        except ProductDatetimeschema.DoesNotExist:
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

                old_items = ContactOrderitem.objects.filter(
                            contactorderitemdetail__name='date',
                            contactorderitemdetail__value=tour_day.date)

                p_id = int(tour_day.product.id)
                """
                1|4|1
                2|4|3
                3|6|1
                4|6|5
                5|10|9
                6|10|5
                """
                if p_id == 4:
                    old_items = old_items.filter(Q(product_id=str(1)) | Q(product_id=str(3)))
                elif p_id == 6:
                    old_items = old_items.filter(Q(product_id=str(1)) | Q(product_id=str(5)))
                elif p_id == 10:
                    old_items = old_items.filter(Q(product_id=str(9)) | Q(product_id=str(5)))
                else:
                    old_items = old_items.filter(product_id=str(p_id))

                old_items = old_items.order_by('order__contact__last_name')

                sold = tour_product.items.aggregate(Sum('quantity'))['quantity__sum']
                seats = 0
                for old_item in old_items:
                    print old_item.quantity
                    raw_quantities = old_item.quantity.split('__')
                    for raw_q in raw_quantities:
                        quan = Decimal(raw_q.split('::')[-1])
                        seats += int(quan)

                if int(sold) == int(seats):
                    p = tour_product.product
                    if int(p.total_sold) != int(sold):
                        p.total_sold = int(sold)
                        p.save()
                if int(sold) != int(seats):
                    info = {
                        'tour_product': tour_product,
                        'total_sold' : total_sold,
                        'sold': sold,
                        'tour_day': tour_day,
                        'seats_filled': seats_filled,
                        'seats': seats,
                        'old_items': old_items,

                    }
                    debug_info.append(info)
                    ctx = RequestContext(request, {
                        'debug_info': debug_info,
                    })

                    return render_to_response('administration/debug.html', context_instance=ctx)

def logout_from_administration(request):
    """
    Logs our user and takes them to the list of tours / homepage
    """
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
@staff_member_required
def sample_order_confirmation(request, template_name="administration/sample_order_confirmation.html"):
    """
    Takes latest order and renders order confirmation / success page to give an idea of whats going on.
    """
    d = {}

    site_skin = None
    # skin forced?
    if request.GET.get('force'):
        qset = SiteSkin.objects.filter(code=request.GET.get('force'))
        if qset:
            site_skin = qset.get()

    d['all_skins'] = SiteSkin.objects.all()
    d['order'] = Order.objects.filter(status="New").order_by('-time_stamp')[0]
    update_context_order_conf_extra(d, site_skin=site_skin)

    return render_to_response(template_name, d, RequestContext(request))

@login_required
@staff_member_required
def day_note_update(request):
    """
    Update the day note from the inventory overview page. Expects a 'day' and 'note_text' POST parameters.
    """
    if not request.method == 'POST':
        raise Http404

    if not request.POST.get('day') or not request.POST.get('note_text'):
        return JsonResponse(success=False)

    day = parse_date(request.POST.get('day', ''))
    if not day:
        return JsonResponse(success=False)
    note_text = request.POST.get('note_text')
    type = request.POST.get('type', InventoryDayNote.TYPE_INVENTORY)

    qset = InventoryDayNote.objects.filter(for_date=day, type=type)
    if qset:
        note = qset.get()
        note.note = note_text
        note.user = request.user
        note.type = type
        note.save()
    else:
        InventoryDayNote.objects.create(note=note_text, user=request.user, for_date=day, type=type)

    return JsonResponse()
