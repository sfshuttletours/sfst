from datetime import date, timedelta
from decimal import Decimal

from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import reverse
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.contrib import messages

from satchmo_store.contact.models import Contact

from localsite.models import TourType, TourCategory, DayOfWeek, TeamMember, SiteSkin
from common.utils import parse_date, first_and_last_date_in_month
from common.http import JsonResponse
from concierges.forms import ConciergeInformationForm, ConciergeRegistrationForm, MessageForm
from concierges.models import Concierge
from concierges.decorators import only_concierges
from administration.models import ConciergeMessage



MAX_CONCIERGE_MESSAGES = 3

def registration(request, template="concierges/registration.html"):
    d = {}
    if request.method == 'POST':
        form = ConciergeRegistrationForm(request.POST)
        if form.is_valid():
            site_skin = request.site_skin
            try:
                contact = Contact.objects.from_request(request)
                site_skin = contact.concierge.site_skin
            except: pass
            form.save(site_skin=site_skin)
            d['success'] = True
    else:
        form = ConciergeRegistrationForm()
    d['form'] = form
    ctx = RequestContext(request, d)

    return render_to_response(template, context_instance=ctx)

@login_required
@only_concierges
def home(request, concierge, template="concierges/home.html"):
    global_message = ''
    qset = ConciergeMessage.objects.filter(is_global=True)
    if qset:
        global_message = qset.get().message

    cat_to_tour_map = {}
    tour_categories = list(TourCategory.objects.filter(active=True, site_skins=concierge.site_skin))
    for cat in tour_categories:
        cat_to_tour_map[cat] = []
        for tour in cat.tours.filter(active=True, featured=True, default_site_skin__is_concierge_cta=True,
                                     is_tour_available_to_concierges=True):
            cat_to_tour_map[cat].append(tour)

    for cat in tour_categories:
        if not cat_to_tour_map[cat]:
            tour_categories.remove(cat)

    ctx = RequestContext(request, {
        'concierge': concierge,
        'tour_categories': tour_categories,
        'cat_to_tour_map': cat_to_tour_map,
        'global_message': global_message,
        'other_messages': ConciergeMessage.objects.filter(is_global=False, concierge=concierge).order_by('id')
    })

    return render_to_response(template, context_instance=ctx)

@login_required
@only_concierges
def commissions(request, concierge, template="concierges/commission.html"):
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

    total_commission, orders = concierge.order_report(start_date, end_date)

    recent_periods = []

    for x in xrange(0, 6):
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

    ctx = RequestContext(request, {
        'recent_periods': recent_periods,
        'label': label,
        'start_date': start_date,
        'end_date': end_date,
        'concierge': concierge,
        'total_commission': total_commission,
        'orders': orders,
        'tour_types': TourType.objects.filter(active=True, featured=True, default_site_skin__is_concierge_cta=True),
    })

    return render_to_response(template, context_instance=ctx)

@login_required
@only_concierges
def inventory(request, concierge, template="concierges/inventory_check.html"):
    """
    Quick 2 day inventory check for concierges
    """
    inventory = []
    for x in xrange(0, 2):
        day = date.today() + timedelta(days=x)
        dow = DayOfWeek.objects.get(isoweekday=day.isoweekday())
        day_info = {'day': day, 'times': []}
        schedules = dow.tourschedule_set.filter(active=True, tour_type__active=True,
            tour_type__default_site_skin__is_concierge_cta=True).order_by('tour_type__order')
        for sched in schedules:
            product = sched.tour_type.get_product(day, schedule=sched).product
            tour_info = {
                'day': day,
                'time': sched.pretty_time,
                'tour_type': sched.tour_type,
                'seats_available': Decimal(product.items_in_stock) - Decimal(product.total_sold)
            }
            day_info['times'].append(tour_info)

        inventory.append(day_info)

    ctx = RequestContext(request, {
        'concierge': concierge,
        'inventory': inventory
    })

    return render_to_response(template, context_instance=ctx)

@login_required
@only_concierges
def brochures(request, concierge, template="concierges/brochures.html"):
    d = {}
    if request.method == 'POST':
        post = request.POST.copy()
        message = ''
        for key, value in post.items():
            if 'tt' in key and value != '0':
                tt_id = int(key.split('_')[-1])
                tour_type = TourType.objects.get(id=tt_id)
                message += '%s brochures for *%s*\n' % (value, tour_type.name)

        message += '\nSend to Address:\n\n%s' % post['address']
        message += '\n\nSent from Concierge: %s' % concierge.handle()
        subject = 'Brochure Request From %s' % concierge.handle()
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_TO_EMAIL, concierge.contact.email])
        d['sent_request'] = True

    d['concierge'] = concierge
    d['tour_types'] = TourType.objects.filter(has_brochures=True, active=True)

    ctx = RequestContext(request, d)

    return render_to_response(template, context_instance=ctx)

@login_required
@only_concierges
def information(request, concierge, template="concierges/information.html"):

    contact = concierge.contact
    home_address = concierge.home_address(create=True)
    hotel_address = concierge.hotel_address(create=True)
    home_phone = concierge.home_phone(create=True)
    hotel_phone = concierge.hotel_phone(create=True)

    initial = {
        'first_name': contact.first_name,
        'last_name': contact.last_name,
        'email_notifications': concierge.email_notifications,
        'send_checks_to_home': concierge.send_checks_to,
        'frequency': concierge.frequency,
        'per_week': concierge.per_week,
        'street': home_address.street1,
        'city': home_address.city,
        'state': home_address.state,
        'postal_code': home_address.postal_code,
        'phone': home_phone.phone,
        'hotel_phone': hotel_phone.phone,
        'hotel_name': concierge.hotel_name,
        'hotel_street': hotel_address.street1,
        'hotel_city': hotel_address.city,
        'hotel_state': hotel_address.state,
        'hotel_postal_code': hotel_address.postal_code,
    }


    if request.method == 'POST' and 'info' in request.POST:
        form = ConciergeInformationForm(request.POST, request.FILES, initial=initial)
        if form.is_valid():
            form.save(concierge)
            messages.success(request, 'Your information has been successfully updated.')
    else:
        form = ConciergeInformationForm(initial=initial)

    if request.method == 'POST' and 'change_password' in request.POST:
        password_form = PasswordChangeForm(request.user, request.POST)
        if password_form.is_valid():
            password_form.save()
            messages.success(request, 'Your password has been successfully changed.')
    else:
        password_form = PasswordChangeForm(request.user)

    ctx = RequestContext(request, {
        'concierge': concierge,
        'form': form,
        'password_form': password_form,
    })

    return render_to_response(template, context_instance=ctx)

@login_required
@only_concierges
def meet_the_team(request, concierge, template="concierges/team.html"):

    ctx = RequestContext(request, {
        'concierge': concierge,
        'team_members': TeamMember.objects.all(),
    })

    return render_to_response(template, context_instance=ctx)

@login_required
@only_concierges
def update_message(request, concierge, template="concierges/fragments/message.html"):
    """
    Called to add / update a concierge note
    """
    if request.method == 'GET':
        d={}
        message_id = request.GET.get('message_id')
        if message_id:
            concierge_message = get_object_or_404(ConciergeMessage, id=message_id, concierge=concierge)
            d['form'] = MessageForm(initial={'message_id': concierge_message.id, 'message': concierge_message.message})
        else:
            d['form'] = MessageForm()

        return render_to_response(template, d, RequestContext(request))
    else:
        message_id = request.POST.get('message_id')
        message = request.POST.get('message')
        if message_id:
            concierge_message = get_object_or_404(ConciergeMessage, id=message_id, concierge=concierge)
            concierge_message.message = message
            concierge_message.save()
        else:
            # create new message
            num_messages = ConciergeMessage.objects.filter(concierge=concierge).count()
            assert num_messages < MAX_CONCIERGE_MESSAGES    # <, cause a new one is being created
            ConciergeMessage.objects.create(message=message, concierge=concierge)

        #shoot an email out
        message = 'Conversation with %s has been updated.\n\n' % concierge.handle()
        message += 'You can view the page here: http://%s%s' % (settings.SITE_DOMAIN, reverse('concierges_home'))
        subject = '%s updated their message!' % concierge.handle()
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_TO_EMAIL, concierge.contact.email])

        return HttpResponseRedirect(reverse('concierges_home'))

@login_required
@only_concierges
def clear_message(request, concierge):
    if request.method != 'POST' or not request.POST.get('message_id'):
        raise Http404

    concierge_message = get_object_or_404(ConciergeMessage, id=request.POST.get('message_id'), concierge=concierge)
    concierge_message.message = ''
    concierge_message.save()

    return JsonResponse()
