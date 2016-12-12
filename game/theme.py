# -*- coding: utf-8 -*-
# Code for Life
#
# Copyright (C) 2016, Ocado Innovation Limited
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ADDITIONAL TERMS – Section 7 GNU General Public Licence
#
# This licence does not grant any right, title or interest in any “Ocado” logos,
# trade names or the trademark “Ocado” or any other trademarks or domain names
# owned by Ocado Innovation Limited or the Ocado group of companies or any other
# distinctive brand features of “Ocado” as may be secured from time to time. You
# must not distribute any modification of this program using the trademark
# “Ocado” or claim any affiliation or association with Ocado or its employees.
#
# You are not authorised to use the name Ocado (or any of its trade names) or
# the names of any author or contributor in advertising or for publicity purposes
# pertaining to the distribution of this program, without the prior written
# authorisation of Ocado.
#
# Any propagation, distribution or conveyance of this program must include this
# copyright notice and these terms. You must not misrepresent the origins of this
# program; modified versions of the program must be marked as such and not
# identified as the original program.

'''
    Theme data
'''

from rest_framework.reverse import reverse


class Theme(object):
    def __init__(self, pk, name, background, border, selected):
        self.id = self.pk = pk
        self.name = name
        self.background = background
        self.border = border
        self.selected = selected


THEME_DATA = {
    'grass': Theme(name=u'grass', selected=u'#bce369', background=u'#eef7ff', border=u'#70961f', pk=1),
    'snow': Theme(name=u'snow', selected=u'#b3deff', background=u'#eef7ff', border=u'#83c9fe', pk=2),
    'farm': Theme(name=u'farm', selected=u'#bce369', background=u'#eef7ff', border=u'#70961f', pk=3),
    'city': Theme(name=u'city', selected=u'#C1C1C1', background=u'#eef7ff', border=u'#686868', pk=4),
}


def get_theme(name):
    """ Helper method to get a theme."""
    return THEME_DATA[name]


def get_all_themes():
    return THEME_DATA.values()


def get_theme_by_pk(pk):
    for theme in THEME_DATA.values():
        if theme.pk == int(pk):
            return theme
    raise KeyError


def get_themes_url(pk, request):
    return reverse('theme-detail', args={pk}, request=request)
