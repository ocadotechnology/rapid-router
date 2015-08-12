# -*- coding: utf-8 -*-
# Code for Life
#
# Copyright (C) 2015, Ocado Limited
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
from game.models import Block, Decor, Theme


def setup_themes():
    Theme.objects.create(name='grass', background='a0c53a', border='#70961f', selected='#bce369')
    Theme.objects.create(name='snow', background='#eef7ff', border='#83c9fe', selected='#b3deff')
    Theme.objects.create(name='farm', background='#a0c53a', border='#70961f', selected='#bce369')
    Theme.objects.create(name='city', background='#969696', border='#686868', selected='#C1C1C1')


def setup_blocks():
    Block.objects.create(type='move_forwards')
    Block.objects.create(type='turn_left')
    Block.objects.create(type='turn_right')
    Block.objects.create(type='turn_around')
    Block.objects.create(type='wait')
    Block.objects.create(type='deliver')
    Block.objects.create(type='controls_repeat')
    Block.objects.create(type='controls_repeat_while')
    Block.objects.create(type='controls_repeat_until')
    Block.objects.create(type='controls_if')
    Block.objects.create(type='logic_negate')
    Block.objects.create(type='at_destination')
    Block.objects.create(type='road_exists')
    Block.objects.create(type='dead_end')
    Block.objects.create(type='traffic_light')
    Block.objects.create(type='call_proc')
    Block.objects.create(type='declare_proc')


def setup_decor():
    grass = Theme.objects.get(name='grass')
    snow = Theme.objects.get(name='snow')
    farm = Theme.objects.get(name='farm')
    city = Theme.objects.get(name='city')

    Decor.objects.create(name='tree1', theme=grass, url='decor/grass/tree1.svg', height=100,
                         width=100)
    Decor.objects.create(name='tree2', theme=grass, url='decor/grass/tree2.svg', height=100,
                         width=100)
    Decor.objects.create(name='bush', theme=grass, url='decor/grass/bush.svg', height=50,
                         width=50)
    Decor.objects.create(name='house', theme=grass, url='decor/grass/house.svg', height=50,
                         width=50)
    Decor.objects.create(name='cfc', theme=grass, url='decor/grass/cfc.svg', height=107,
                         width=100)
    Decor.objects.create(name='pond', theme=grass, url='decor/grass/pond.svg', height=100,
                         width=150)
    Decor.objects.create(name='tree1', theme=snow, url='decor/snow/tree1.svg', height=100,
                         width=100)
    Decor.objects.create(name='tree2', theme=snow, url='decor/snow/tree2.svg', height=100,
                         width=100)
    Decor.objects.create(name='bush', theme=snow, url='decor/snow/bush.svg', height=50,
                         width=50)
    Decor.objects.create(name='house', theme=snow, url='decor/snow/house.svg', height=50,
                         width=50)
    Decor.objects.create(name='cfc', theme=snow, url='decor/snow/cfc.svg', height=107,
                         width=100)
    Decor.objects.create(name='pond', theme=snow, url='decor/snow/pond.svg', height=100,
                         width=150)
    Decor.objects.create(name='tile1', theme=grass, url='decor/grass/tile1.svg', height=100,
                         width=100)
    Decor.objects.create(name='tile1', theme=snow, url='decor/snow/tile1.svg', height=100,
                         width=100)
    Decor.objects.create(name='tile2', theme=snow, url='decor/snow/tile2.svg', height=100,
                         width=100)
    Decor.objects.create(name='house', theme=farm, url='decor/farm/house1.svg', height=224,
                         width=184)
    Decor.objects.create(name='cfc', theme=farm, url='decor/farm/cfc.svg', height=301,
                         width=332)
    Decor.objects.create(name='bush', theme=farm, url='decor/farm/bush.svg', height=30,
                         width=50)
    Decor.objects.create(name='tree1', theme=farm, url='decor/farm/tree1.svg', height=100,
                         width=100)
    Decor.objects.create(name='tree2', theme=farm, url='decor/farm/house2.svg', height=88,
                         width=65)
    Decor.objects.create(name='pond', theme=farm, url='decor/farm/crops.svg', height=100,
                         width=150)
    Decor.objects.create(name='tile1', theme=farm, url='decor/farm/tile1.svg', height=337,
                         width=194)
    Decor.objects.create(name='tile1', theme=city, url='decor/city/pavementTile.png', height=100,
                         width=100)
    Decor.objects.create(name='house', theme=city, url='decor/city/house.svg', height=50,
                         width=50)
    Decor.objects.create(name='bush', theme=city, url='decor/city/bush.svg', height=50,
                         width=50)
    Decor.objects.create(name='tree1', theme=city, url='decor/city/shop.svg', height=70,
                         width=70)
    Decor.objects.create(name='tree2', theme=city, url='decor/city/school.svg', height=100,
                         width=100)
    Decor.objects.create(name='pond', theme=city, url='decor/city/hospital.svg', height=157,
                         width=140)
    