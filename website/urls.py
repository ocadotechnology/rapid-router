from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.contrib.auth.views import login, logout
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'website.views.home', name='home'),
    url(r'^home/', 'website.views.home'),
    url(r'^game/', include('game.urls')),
    url(r'^reports/', include('reports.urls')),
    url(r'^feedback/', 'website.views.feedback'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout, {'next_page': '/'}),
)
