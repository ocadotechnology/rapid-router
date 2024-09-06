from django.conf.urls import url

from game.views.level import play_default_python_level, start_python_episode
from game.views.level_selection import python_levels
from game.views.scoreboard import python_scoreboard

urlpatterns = [
    url(r"^$", python_levels, name="python_levels"),
    url(
        r"^(?P<level_name>[A-Z0-9]+)/$",
        play_default_python_level,
        name="play_python_default_level",
    ),
    url(
        r"^episode/(?P<episodeId>[0-9]+)/$",
        start_python_episode,
        name="start_python_episode",
    ),
    url(r"^scoreboard/$", python_scoreboard, name="python_scoreboard"),
]
