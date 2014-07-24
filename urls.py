from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import databrowse
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.views.generic.simple import direct_to_template

from satchmo_store.urls import urlpatterns as satchmo_urls
from satchmo_store.contact.views import ajax_get_state
from satchmo_store.shop.satchmo_settings import get_satchmo_setting
from payment.views.checkout import success

from localsite.views import sfst_success, confirm_info


ssl = get_satchmo_setting('SSL', default_value=True)
handler404 = 'sfst.localsite.views.view_404'
handler500 = 'sfst.localsite.views.view_500'

# Public URLS
urlpatterns = patterns('localsite.views',
    url(r'^$', 'home', {'SSL': ssl}, name='home'),
    # url(r'^cart/$', 'cart', name='cart'),
    url(r'^affiliate-checkout/$', 'affiliate_checkout', {'SSL': ssl}, name='affiliate_checkout'),
    url(r'^product/(?P<tour_type_slug>[\w\-]+)/$', 'product', {'SSL': ssl}, name='product'),
    url(r'^ajax-get-schedule/(?P<tour_type_id>\d+)/$', 'ajax_get_schedule', {'SSL': ssl}, name='ajax_get_schedule'),
    url(r'^ajax-get-schedule-adjust/(?P<tour_type_id>\d+)/$', 'ajax_get_schedule', {'SSL': ssl}, name='ajax_get_schedule_adjust'),
    url(r'^accounts/dispatcher/', 'login_dispatcher', {'SSL': ssl}, name='login_dispatcher'),
    url(r'^clear-affiliate', 'clear_affiliate', {'SSL': ssl}, name='clear_affiliate'),
    url(r'^get-city-country-details/$', 'zip_to_city_country', {'SSL': ssl}, name='zip_to_city_country'),
    url(r'^customer-adjust/(?P<order_hash>\w+)/$', 'customer_order_detail',
        {'SSL': ssl}, name='customer_order_detail'),
    url(r'^customer-adjust/(?P<order_item>\d+)/(?P<action_type>\w+)/$', 'customer_adjust_item',
        {'SSL': ssl}, name='customer_adjust_item'),
    url(r'^customer-adjust/check/(?P<order_item>\d+)/$', 'check_move_availability',
        {'SSL': ssl}, name='check_move_availability'),
    url(r'^customer-adjust/void/(?P<order_id>\d+)/$', 'void_order',
        {'SSL': ssl}, name='void_order'),
    url(r'^customer-adjust-not-allowed-reason/$', 'customer_adjust_not_allowed_reason',
        {'SSL': ssl}, name='customer_adjust_not_allowed_reason'),
    url(r'^sentry/', include('sentry.web.urls')),

    url(r'^0I3S1SYhWxhEZyXzhHKe2w--.html$', direct_to_template, {'template': 'blank.html'}),
    url(r'^booking-error-form/$', 'booking_error_form', {'SSL': ssl}, name="booking_error_form")

)


urlpatterns += patterns('',
    (r'^administration/', include('administration.urls')),
    (r'^concierges/', include('concierges.urls')),
    (r'^reseller/', include('resellers.urls')),
    (r'^databrowse/(.*)', login_required(databrowse.site.root)),
    url(r'^creg/$', 'concierges.views.registration', name='creg'),
    url(r'^public-inventory/$', 'administration.views.public_inventory', name='public_inventory'),
)

# Redirects
urlpatterns += patterns('django.views.generic.simple',
    (r'^cadm/$', 'redirect_to', {'url': '/administration/concierges/', 'permanent': True})
)

# override some satchmo views, replace_urlpattern wasn't working!
urlpatterns += patterns('',
    url(r'^accounts/ajax_state/$', ajax_get_state, {'SSL': ssl}, 'satchmo_contact_ajax_state'),
    url(r'^checkout/credit/success/$', sfst_success, {'SSL' : ssl}, 'satchmo_checkout-success'),
    (r'^checkout/credit/confirm/$', confirm_info, {'SSL':ssl}, 'AUTHORIZENET_satchmo_checkout-step3'),
)

urlpatterns += satchmo_urls

if settings.IS_DEV:
    urlpatterns += patterns('',
        url(r'^static/(.*)$', 'django.views.static.serve',\
            kwargs={'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^404/$', handler404),
        (r'^500/$', handler500)
    )
