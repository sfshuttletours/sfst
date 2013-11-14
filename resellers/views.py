from datetime import date

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.conf import settings as django_settings

from resellers.forms import ResellerRequestForm
from resellers.models import Reseller
from localsite.models import TourType
from common.utils import parse_date
from common.helper import start_thread


def main(request, template="resellers/main.html"):
    """
    Static info for resellers and a signup form
    """
    d = {}
    
    if request.method == 'POST':
        form = ResellerRequestForm(request.POST)
        if form.is_valid():
            reseller_request = form.save()
            
            # shoot an email saying a new reseller request has arrived
            mail_subject = 'New reseller request: %s' % form.cleaned_data['company_name']
            mail_body = 'Name: %s %s\n\n' % (form.cleaned_data['first_name'], form.cleaned_data['last_name'])
            mail_body += 'Description: %s\n\n' % form.cleaned_data['description']
            mail_body += 'Approve by clicking here: http://%s%s' % (django_settings.SITE_DOMAIN, reverse('pending_reseller_request', args=[reseller_request.id]))
            start_thread(send_mail, mail_subject, mail_body, django_settings.DEFAULT_FROM_EMAIL, [django_settings.DEFAULT_TO_EMAIL,])
            
            d['success'] = True
            d['reseller_request'] = reseller_request
            form = ResellerRequestForm()
    else:
        form = ResellerRequestForm()
        
    d['form'] = form
    
    ctx = RequestContext(request, d)
    
    return render_to_response(template, context_instance=ctx)

@login_required
@permission_required('resellers.is_reseller')
def home(request, template="resellers/home.html"):
    reseller = get_object_or_404(Reseller, contact__user=request.user)

    tour_types = TourType.objects.filter(active=True, is_tour_available_to_resellers=True)
    
    ctx = RequestContext(request, {
        'reseller': reseller,
        'site': Site.objects.get_current(),
        'tour_types': tour_types,
    })
    
    return render_to_response(template, context_instance=ctx)


@login_required
@permission_required('resellers.is_reseller')
def change_password(request, template="resellers/change_password.html"):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your password has been change')
            return HttpResponseRedirect(reverse('resellers_home'))
    else:
        form = PasswordChangeForm(request.user,)
    ctx = RequestContext(request, {
        'form': form,
    })

    return render_to_response(template, context_instance=ctx)
