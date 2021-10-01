"""
    Theme data
"""

from builtins import object
from rest_framework.reverse import reverse
from django.utils.translation import ugettext


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
        name=u"grass",
        text=ugettext(u"Grass"),
        selected=u"#bce369",
        background=u"#a0c53a",
        border=u"#70961f",
        pk=1,
    ),
    "snow": Theme(
        name=u"snow",
        text=ugettext(u"Snow"),
        selected=u"#b3deff",
        background=u"#eef7ff",
        border=u"#83c9fe",
        pk=2,
    ),
    "farm": Theme(
        name=u"farm",
        text=ugettext(u"Farm"),
        selected=u"#bce369",
        background=u"#a0c53a",
        border=u"#70961f",
        pk=3,
    ),
    "city": Theme(
        name=u"city",
        text=ugettext(u"City"),
        selected=u"#C1C1C1",
        background=u"#969696",
        border=u"#686868",
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
