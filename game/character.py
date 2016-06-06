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
    Character data
'''

from rest_framework.reverse import reverse


class Character(object):
    def __init__(self, pk, name, en_face, top_down, width, height):
        self.id = self.pk = pk
        self.name = name
        self.en_face = en_face
        self.top_down = top_down
        self.width = width
        self.height = height


CHARACTER_DATA = {
    'Van': Character(pk=1, name=u'Van', en_face=u'characters/front_view/Van.svg', top_down=u'characters/top_view/Van.svg', height='20', width='40'),
    'Dee': Character(pk=2, name=u'Dee', en_face=u'characters/front_view/Dee.svg', top_down=u'characters/top_view/Dee.svg', height='28', width='52'),
    'Nigel': Character(pk=3, name=u'Nigel', en_face=u'characters/front_view/Nigel.svg', top_down=u'characters/top_view/Nigel.svg', height='32', width='56'),
    'Kirsty': Character(pk=4, name=u'Kirsty', en_face=u'characters/front_view/Kirsty.svg', top_down=u'characters/top_view/Kirsty.svg', height='32', width='60'),
    'Wes': Character(pk=5, name=u'Wes', en_face=u'characters/front_view/Wes.svg', top_down=u'characters/top_view/Wes.svg', height='20', width='40'),
    'Phil': Character(pk=6, name=u'Phil', en_face=u'characters/front_view/Phil.svg', top_down=u'characters/top_view/Phil.svg', height='40', width='40'),
}


def get_character(name):
    """ Helper method to get a character."""
    return CHARACTER_DATA[name]


def get_all_character():
    return CHARACTER_DATA.values()


def get_character_by_pk(pk):
    for character in CHARACTER_DATA.values():
        if character.pk == int(pk):
            return character
    raise KeyError


def get_characters_url(pk, request):
    return reverse('character-detail', args={pk}, request=request)
