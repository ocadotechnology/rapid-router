from django.conf.urls import url, include

from game.views.level_selection import python_levels

urlpatterns = [
    url(r"^$", python_levels, name="python_levels"),
]