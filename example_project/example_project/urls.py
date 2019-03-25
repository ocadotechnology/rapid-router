from django.conf.urls import include, patterns, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^', include('portal.urls')),
    url(r'^administration/', include(admin.site.urls)),
    url(r'^rapidrouter/', include('game.urls')),
    url(r'^aimmo/', include('aimmo.urls')),
)
