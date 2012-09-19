from django.conf.urls import patterns, include, url
import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
# All Posts,Categories, and Tags have a space in the root domain. Check for those last.
urlpatterns += patterns('website.views',
    url(r'^{0}/$'.format(settings.default_blogs_page), 'blogs'),
    url(r'^{0}/(?P<page>\d+)/$'.format(settings.default_blogs_page), 'blogs'),
    url(r'^$', 'posts'),
    url(r'^(?P<link>\w+)/$', 'posts'),
    url(r'^(?P<link>\w+)/(?P<page>\d+)$', 'posts'),
)