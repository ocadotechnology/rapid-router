# -*- coding: utf-8 -*-
# Code for Life
#
# Copyright (C) 2015, Ocado Innovation Limited
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
    Decor data
'''

from rest_framework.reverse import reverse
from game.theme import get_theme, get_all_themes


class Decor(object):
    def __init__(self, pk, name, url, width, height, theme, z_index):
        self.id = self.pk = pk
        self.name = name
        self.url = url
        self.width = width
        self.height = height
        self.theme = theme
        self.z_index = z_index


DECOR_DATA = {
    (u'tree1', u'grass'): Decor(z_index=4, name=u'tree1', url=u'decor/grass/tree1.svg', height=100, width=100, theme=get_theme('grass'), pk=1),
    (u'tree2', u'grass'): Decor(z_index=4, name=u'tree2', url=u'decor/grass/tree2.svg', height=100, width=100, theme=get_theme('grass'), pk=2),
    (u'bush', u'grass'): Decor(z_index=3, name=u'bush', url=u'decor/grass/bush.svg', height=50, width=50, theme=get_theme('grass'), pk=3),
    (u'house', u'grass'): Decor(z_index=1, name=u'house', url=u'decor/grass/house.svg', height=50, width=50, theme=get_theme('grass'), pk=4),
    (u'cfc', u'grass'): Decor(z_index=1, name=u'cfc', url=u'decor/grass/cfc.svg', height=107, width=100, theme=get_theme('grass'), pk=5),
    (u'pond', u'grass'): Decor(z_index=2, name=u'pond', url=u'decor/grass/pond.svg', height=100, width=150, theme=get_theme('grass'), pk=6),
    (u'tree1', u'snow'): Decor(z_index=4, name=u'tree1', url=u'decor/snow/tree1.svg', height=100, width=100, theme=get_theme('snow'), pk=7),
    (u'tree2', u'snow'): Decor(z_index=4, name=u'tree2', url=u'decor/snow/tree2.svg', height=100, width=100, theme=get_theme('snow'), pk=8),
    (u'bush', u'snow'): Decor(z_index=3, name=u'bush', url=u'decor/snow/bush.svg', height=50, width=50, theme=get_theme('snow'), pk=9),
    (u'house', u'snow'): Decor(z_index=1, name=u'house', url=u'decor/snow/house.svg', height=50, width=50, theme=get_theme('snow'), pk=10),
    (u'cfc', u'snow'): Decor(z_index=1, name=u'cfc', url=u'decor/snow/cfc.svg', height=107, width=100, theme=get_theme('snow'), pk=11),
    (u'pond', u'snow'): Decor(z_index=2, name=u'pond', url=u'decor/snow/pond.svg', height=100, width=150, theme=get_theme('snow'), pk=12),
    (u'tile1', u'grass'): Decor(z_index=0, name=u'tile1', url=u'decor/grass/tile1.svg', height=100, width=100, theme=get_theme('grass'), pk=13),
    (u'tile1', u'snow'): Decor(z_index=0, name=u'tile1', url=u'decor/snow/tile1.svg', height=100, width=100, theme=get_theme('snow'), pk=14),
    (u'tile2', u'snow'): Decor(z_index=0, name=u'tile2', url=u'decor/snow/tile2.svg', height=100, width=100, theme=get_theme('snow'), pk=15),
    (u'house', u'farm'): Decor(z_index=1, name=u'house', url=u'decor/farm/house1.svg', height=224, width=184, theme=get_theme('farm'), pk=16),
    (u'cfc', u'farm'): Decor(z_index=1, name=u'cfc', url=u'decor/farm/cfc.svg', height=301, width=332, theme=get_theme('farm'), pk=17),
    (u'bush', u'farm'): Decor(z_index=3, name=u'bush', url=u'decor/farm/bush.svg', height=30, width=50, theme=get_theme('farm'), pk=18),
    (u'tree1', u'farm'): Decor(z_index=4, name=u'tree1', url=u'decor/farm/tree1.svg', height=100, width=100, theme=get_theme('farm'), pk=19),
    (u'tree2', u'farm'): Decor(z_index=4, name=u'tree2', url=u'decor/farm/house2.svg', height=88, width=65, theme=get_theme('farm'), pk=20),
    (u'pond', u'farm'): Decor(z_index=2, name=u'pond', url=u'decor/farm/crops.svg', height=100, width=150, theme=get_theme('farm'), pk=21),
    (u'tile1', u'farm'): Decor(z_index=0, name=u'tile1', url=u'decor/farm/tile1.svg', height=337, width=194, theme=get_theme('farm'), pk=22),
    (u'tile1', u'city'): Decor(z_index=0, name=u'tile1', url=u'decor/city/pavementTile.png', height=100, width=100, theme=get_theme('city'), pk=23),
    (u'house', u'city'): Decor(z_index=1, name=u'house', url=u'decor/city/house.svg', height=50, width=50, theme=get_theme('city'), pk=24),
    (u'bush', u'city'): Decor(z_index=3, name=u'bush', url=u'decor/city/bush.svg', height=50, width=50, theme=get_theme('city'), pk=25),
    (u'tree1', u'city'): Decor(z_index=4, name=u'tree1', url=u'decor/city/shop.svg', height=70, width=70, theme=get_theme('city'), pk=26),
    (u'tree2', u'city'): Decor(z_index=4, name=u'tree2', url=u'decor/city/school.svg', height=100, width=100, theme=get_theme('city'), pk=27),
    (u'pond', u'city'): Decor(z_index=2, name=u'pond', url=u'decor/city/hospital.svg', height=157, width=140, theme=get_theme('city'), pk=28),
    (u'cfc', u'city'): Decor(z_index=1, name=u'cfc', url=u'decor/grass/cfc.svg', height=107, width=100, theme=get_theme('city'), pk=29),
    (u'tile2', u'grass'): Decor(z_index=0, name=u'tile2', url=u'decor/snow/tile2.svg', height=100, width=100, theme=get_theme('grass'), pk=30),
    (u'tile2', u'farm'): Decor(z_index=0, name=u'tile2', url=u'decor/snow/tile2.svg', height=100, width=100, theme=get_theme('farm'), pk=31),
    (u'tile2', u'city'): Decor(z_index=0, name=u'tile2', url=u'decor/snow/tile2.svg', height=100, width=100, theme=get_theme('city'), pk=32),
}


def get_decor_element(name, theme):
    """ Helper method to get a decor element corresponding to the theme or a default one."""
    try:
        return DECOR_DATA[(name, theme.name)]
    except KeyError:
        for theme_object in get_all_themes():
            try:
                return DECOR_DATA[(name, theme_object.name)]
            except KeyError:
                pass
    raise KeyError


def get_all_decor():
    return DECOR_DATA.values()


def get_decor_element_by_pk(pk):
    for decor in DECOR_DATA.values():
        if decor.pk == int(pk):
            return decor
    raise KeyError


def get_decors_url(pk, request):
    return reverse('decor-detail', args={pk}, request=request)
