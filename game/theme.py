"""
    Theme data
"""

from builtins import object
from rest_framework.reverse import reverse
from django.utils.translation import gettext


class Theme(object):
    def __init__(self, pk, name, text, background, border, selected):
        self.id = self.pk = pk
        self.name = name
        self.text = text
        self.background = background
        self.border = border
        self.selected = selected


THEME_DATA = {
    "grass": Theme(
        name="grass",
        text=gettext("Grass"),
        selected="#bce369",
        background="#a0c53a",
        border="#70961f",
        pk=1,
    ),
    "snow": Theme(
        name="snow",
        text=gettext("Snow"),
        selected="#b3deff",
        background="#eef7ff",
        border="#83c9fe",
        pk=2,
    ),
    "farm": Theme(
        name="farm",
        text=gettext("Farm"),
        selected="#bce369",
        background="#a0c53a",
        border="#70961f",
        pk=3,
    ),
    "city": Theme(
        name="city",
        text=gettext("City"),
        selected="#C1C1C1",
        background="#969696",
        border="#686868",
        pk=4,
    ),
}


def get_theme(name):
    """Helper method to get a theme."""
    return THEME_DATA[name]


def get_all_themes():
    return list(THEME_DATA.values())


def get_theme_by_pk(pk):
    for theme in list(THEME_DATA.values()):
        if theme.pk == int(pk):
            return theme
    raise KeyError


def get_themes_url(pk, request):
    return reverse("theme-detail", args={pk}, request=request)
