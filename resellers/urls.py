from django.conf.urls.defaults import *

urlpatterns = patterns('sfst.resellers.views',
    url(r'^$', 'main', name='resellers_main'),
    url(r'^home/$', 'home', name='resellers_home'),
    url(r'^change_password/$', 'change_password', name='resellers_change_password'),
)

urlpatterns += patterns('',
    url(r'^reports/$', 'administration.views.reseller_report', name='resellers_reports'),
)
