from aimmo import urls as aimmo_urls
from django.conf.urls import include, url
from django.contrib import admin
from portal import urls as portal_urls

from game import urls as game_urls

admin.autodiscover()

urlpatterns = [
    url(r"^", include(portal_urls)),
    url(r"^administration/", include((admin.site.urls[0], "admin"), namespace="admin")),
    url(r"^rapidrouter/", include(game_urls)),
    url(r"^aimmo/", include(aimmo_urls)),
]
