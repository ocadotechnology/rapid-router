from django.urls import re_path

from game.views.level import play_default_python_level, start_python_episode
from game.views.level_selection import python_levels
from game.views.scoreboard import python_scoreboard

urlpatterns = [
    re_path(r"^$", python_levels, name="python_levels"),
    re_path(
        r"^(?P<level_name>[A-Z0-9]+)/$",
        play_default_python_level,
        name="play_python_default_level",
    ),
    re_path(
        r"^episode/(?P<episodeId>[0-9]+)/$",
        start_python_episode,
        name="start_python_episode",
    ),
    re_path(r"^scoreboard/$", python_scoreboard, name="python_scoreboard"),
]
