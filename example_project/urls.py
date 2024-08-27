from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from portal import urls as portal_urls

from game import urls as game_urls
from game import python_den_urls

admin.autodiscover()

urlpatterns = [
    url(r"^", include(portal_urls)),
    path("administration/", admin.site.urls),
    url(r"^rapidrouter/", include(game_urls)),
    url(r"^pythonden/", include(python_den_urls)),
]
