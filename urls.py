from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'aprspasscode.passcode.views.passcode_request'),
    (r'^complete', 'django.views.generic.simple.direct_to_template', { 'template': 'complete.html'}),

    (r'^admin/passcode/passcoderequest/(?P<passcode_request_id>\d+)/approve$', 'aprspasscode.passcode.admin_views.approve'),
    (r'^admin/passcode/passcoderequest/(?P<passcode_request_id>\d+)/deny$', 'aprspasscode.passcode.admin_views.deny'),
    (r'^admin/', include(admin.site.urls)),
)
