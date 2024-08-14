from django.conf.urls import url, include

from game.views.level import play_default_level
from game.views.level_selection import python_levels

urlpatterns = [
    url(r"^$", python_levels, name="python_levels"),
    url(r"^(?P<levelName>[A-Z0-9]+)/$", play_default_level, name="play_python_default_level"),
]