from django.conf.urls import patterns, include, url
import settings
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/images/favicon.ico'}),
    url(r'^robots\.txt$', direct_to_template,
     {'template': 'robots.txt', 'mimetype': 'text/plain'}),
)
# All Posts,Categories, and Tags have a space in the root domain. Check for those last.
urlpatterns += patterns('website.views',
    url(r'^contact_send', 'contact_send'),
    url(r'^contact_thanks', 'contact_thanks'),
    url(r'^{0}/$'.format(settings.default_blogs_page), 'blogs'),
    url(r'^{0}/(?P<page>\d+)/$'.format(settings.default_blogs_page), 'blogs'),
    url(r'^$', 'posts'),
    url(r'^(?P<link>\w+)/$', 'posts'),
    url(r'^(?P<link>\w+)/(?P<page>\d+)$', 'posts'),
)