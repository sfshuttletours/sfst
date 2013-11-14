from django.conf.urls.defaults import *


urlpatterns = patterns('adjustments.views',

    url(r'^main/(?P<order_id>\d+)/(?P<action_type>\w+)/$', 'main', name='adjustment_main'),
)
