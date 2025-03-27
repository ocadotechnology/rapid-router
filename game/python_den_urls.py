from django.urls import re_path
from django.views.generic.base import TemplateView

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
    re_path(
        r"^editor/$",
        TemplateView.as_view(template_name="game/python_den_worksheet.html"),
        name="editor",
    ),
    re_path(r"^scoreboard/$", python_scoreboard, name="python_scoreboard"),
]
