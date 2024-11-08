from django.contrib import admin
from django.urls import include, path, re_path
from portal import urls as portal_urls

from game import urls as game_urls
from game import python_den_urls

admin.autodiscover()

urlpatterns = [
    re_path(r"^", include(portal_urls)),
    path("administration/", admin.site.urls),
    re_path(r"^rapidrouter/", include(game_urls)),
    re_path(r"^pythonden/", include(python_den_urls)),
]
