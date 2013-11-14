from django.conf.urls.defaults import *


urlpatterns = patterns('concierges.views',
    url(r'^$', 'home', name='concierges_home'),
    url(r'^commissions/$', 'commissions', name='concierges_commissions'),
    url(r'^inventory/$', 'inventory', name='concierges_inventory'),
    url(r'^brochures/$', 'brochures', name='concierges_brochures'),
    url(r'^information/$', 'information', name='concierges_information'),
    url(r'^meet-the-team/$', 'meet_the_team', name='concierges_meet_the_team'),
    url(r'^update-message/$', 'update_message', name='concierges_update_message'),
    url(r'^clear-message/$', 'clear_message', name='concierges_clear_message'),
)
