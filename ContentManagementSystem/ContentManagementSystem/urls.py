from django.conf.urls import patterns, include, url
from ContentManagementSystem import settings
from database.views import writeup
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', writeup, {}),
    
    # Examples:
    # url(r'^$', 'ContentManagementSystem.views.home', name='home'),
    # url(r'^ContentManagementSystem/', include('ContentManagementSystem.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',  
     {'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<name>[-\w]+)/$', writeup, {}),
)
