import os.path
from django.conf.urls.defaults import *
from timetracking.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

site_media = os.path.join( 
  os.path.dirname(__file__), 'site_media' 
) 

urlpatterns = patterns('',
    # Example:
    # (r'^experior/', include('experior.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
    
    # TimeTracking app
    (r'^$', main_page),
    (r'^activities/$', activities_page),
    (r'^about/$', about_page),
    (r'^help/$', help_page),
    (r'^reports/$', reports_page),
    (r'^misc/$', misc_page),
    (r'^account/$', account_page),
   
   # Account admin
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),     

    # Media files
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', 
        { 'document_root': site_media }),
)
