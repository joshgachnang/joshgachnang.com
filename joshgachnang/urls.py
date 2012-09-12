from django.conf.urls import patterns, include, url

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
    url(r'^$', 'homepage'),
    url(r'^posts/$', 'posts'),
    url(r'^p/(?P<url>\w+)/$', 'individual_post'),
    url(r'^category/(?P<category>\w+)', 'posts'),
)