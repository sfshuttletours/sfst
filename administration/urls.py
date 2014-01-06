from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required

from concierges.models import Concierge


urlpatterns = patterns('administration.views',

    url(r'^debug/$', 'debug', name='debug'),
    url(r'^$', 'home', name='administration_home'),

    url(r'^tour-guests/$', 'tour_guests', name='tour_guests'),
    url(r'^tour-guests/update/$', 'tour_guests_update', name='tour_guests_update'),

    url(r'^inventory/$', 'inventory', name='inventory'),
    url(r'^inventory/detail/$', 'inventory_detail', name='inventory_detail'),
    url(r'^inventory/(?P<tour_id>\d+)/overbookings/$', 'overbookings_detail', name='overbookings_detail'),
    url(r'^inventory-update/$', 'inventory_update', name='inventory_update'),
    url(r'^bulk-inventory-updator/$', 'bulk_inventory_updator', name='bulk_inventory_updator'),

    # checkin related views
    url(r'^checkin-customer/$', 'checkin_customer', name='checkin_customer'),
    url(r'^edit-customer-checkin/$', 'edit_customer_checkin', name='edit_customer_checkin'),
    url(r'^finalize-checkin/$', 'finalize_checkin', name='finalize_checkin'),
    url(r'^checkin-reports/$', 'checkin_reports', name='checkin_reports'),

    url(r'^concierges/$', 'concierge_admin', name='concierge_admin'),

    url(r'^concierges/list/$', login_required(direct_to_template), {'template': 'administration/concierge_list.html',\
        'extra_context': {'concierges': Concierge.objects.select_related('contact').order_by('contact__first_name').all }},
        name='concierge_list'),

    url(r'^concierges/contact-sheet/$', 'concierge_contact_sheet', name='concierge_contact_sheet'),
    url(r'^concierges/adjust-commissions/$',     login_required(direct_to_template), {'template': 'administration/adjust_concierge_commissions.html',\
        'extra_context': {'concierges': Concierge.objects.select_related('contact').order_by('contact__first_name').all }},
        name='adjust_concierge_commissions'),

    url(r'^concierges/pay-commission/$', 'concierge_pay_commission', name='concierge_pay_commission'),
    url(r'^concierges/concierge-commission-print/(\d+)/', 'concierge_commission_print', name='concierge_commission_print'),

    url(r'^become/(\d+)/$', 'become_user', name='become_user'),

    url(r'^back-to-old-user/$', 'back_to_old_user', name='back_to_old_user'),
    url(r'^resellers/manage/$', 'manage_resellers', name='manage_resellers'),
    url(r'^resellers/report/(?P<reseller_id>\d+)/$', 'reseller_report', name='reseller_report'),
    url(r'^resellers/pending/(\d+)/$', 'pending_reseller_request', name='pending_reseller_request'),

    url(r'^sample-order-confirmation/$', 'sample_order_confirmation', name='sample_order_confirmation'),

    url(r'^orders/search/$', 'search_orders', name='search_orders'),
    url(r'^orders/detail/(\d+)/$', 'order_detail', name='order_detail'),
    url(r'^orders/email-customer/(\d+)/$', 'order_email_customer', name='order_email_customer'),

    url(r'^logout/$', 'logout_from_administration', name='logout_from_administration'),

    url(r'^day-note-update/$', 'day_note_update', name='day_note_update')
)

urlpatterns += patterns('',
    (r'adjust/', include('adjustments.urls')),
)
