from django.conf.urls import patterns, include, url
from joshgachnang.settings import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'joshgachnang.views.home', name='home'),
    # url(r'^joshgachnang/', include('joshgachnang.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += patterns('website.views',
    url(r'^{}/$'.format(settings.default_blogs_page), 'blogs'),
    url(r'^{}(?P<page>\d+)/$'.format(settings.default_blogs_page), 'blogs'),
    url(r'^$', 'posts'),
    url(r'^(?P<link>\w+)/$', 'posts'),
    url(r'^(?P<link>\w+)/(?P<page>\d+)$', 'posts'),
    #url(r'^posts/$', 'posts'),
    #url(r'^p/(?P<url>\w+)/$', 'individual_post'),
    #url(r'^category/(?P<category>\w+)', 'posts'),
)