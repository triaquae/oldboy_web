from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from app01.views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^website/', include('website.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
		(r'^$',index),	
	(r'^about/$',about),
	(r'^courses/$', courses),
	(r'^graduate/$', graduate),
	(r'^enroll/$', enroll),
	(r'^newClass/$', newClass),
	(r'^onLineCourse/$', onLineCourse),
	(r'^bbs/$', bbs),
	(r'^news/$', news),
	(r'^contact/$', contact),
	(r'^text/$', test),
#	url(r'^tinymce/', include('tinymce.urls')),   # for rich text 
)
