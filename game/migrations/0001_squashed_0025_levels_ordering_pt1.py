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
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import json
from game.level_management import set_decor_inner, set_blocks_inner


# Functions from the following migrations need manual copying.
# Move them and any dependencies into this file, then update the
# RunPython operations to refer to the local versions:
# game.migrations.0001_squashed_0024_fix_levels_54_63
# game.migrations.0025_levels_ordering_pt1


def add_characters(apps, schema_editor):

    Character = apps.get_model('game', 'Character')

    Character.objects.all().delete()

    van = Character(pk=1, name="Van", en_face='characters/front_view/Van.svg',
                    top_down='characters/top_view/Van.svg', height='20',
                    width='40')
    van.save()

    Dee = Character(pk=2, name="Dee", en_face='characters/front_view/Dee.svg',
                    top_down='characters/top_view/Dee.svg', height='28',
                    width='52')
    Dee.save()

    Nigel = Character(pk=3, name="Nigel", width='56', height='32',
                      en_face='characters/front_view/Nigel.svg',
                      top_down='characters/top_view/Nigel.svg')
    Nigel.save()

    Kirsty = Character(pk=4, name="Kirsty", height='32', width='60',
                       en_face='characters/front_view/Kirsty.svg',
                       top_down='characters/top_view/Kirsty.svg')
    Kirsty.save()

    Wes = Character(pk=5, name="Wes", en_face='characters/front_view/Wes.svg',
                    top_down='characters/top_view/Wes.svg', height='20',
                    width='40')
    Wes.save()

    Phil = Character(pk=6, name="Phil", height='40', width='40',
                     en_face='characters/front_view/Phil.svg',
                     top_down='characters/top_view/Phil.svg')
    Phil.save()


def add_theme_and_decor(apps, schema_editor):

    Theme = apps.get_model('game', 'Theme')
    Decor = apps.get_model('game', 'Decor')

    grass = Theme(background='#a0c53a', border='#70961f', name='grass', selected='#bce369')
    snow = Theme(background='#eef7ff', border='#83c9fe', name='snow', selected='#b3deff')
    farm = Theme(background='#a0c53a', border='#70961f', name='farm', selected='#bce369')
    city = Theme(background='#969696', border='#686868', name='city', selected='#C1C1C1')

    grass.save()
    snow.save()
    farm.save()
    city.save()

    Decor = apps.get_model('game', 'Decor')

    decor1 = Decor(name='tree1', theme=grass, url='decor/grass/tree1.svg',
                   height=100, width=100)

    decor2 = Decor(name='tree2', theme=grass, url='decor/grass/tree2.svg',
                   height=100, width=100)

    decor3 = Decor(name='bush', theme=grass, url='decor/grass/bush.svg',
                   height=50, width=50)

    decor4 = Decor(name='house', theme=grass, url='decor/grass/house.svg',
                   height=50, width=50)

    decor5 = Decor(name='cfc', theme=grass, url='decor/grass/cfc.svg',
                   height=107, width=100)

    decor6 = Decor(name='pond', theme=grass, url='decor/grass/pond.svg',
                   height=100, width=150)

    decor7 = Decor(name='tree1', theme=snow, url='decor/snow/tree1.svg',
                   height=100, width=100)

    decor8 = Decor(name='tree2', theme=snow, url='decor/snow/tree2.svg',
                   height=100, width=100)

    decor9 = Decor(name='bush', theme=snow, url='decor/snow/bush.svg',
                   height=50, width=50)

    decor10 = Decor(name='house', theme=snow, url='decor/snow/house.svg',
                    height=50, width=50)
    decor11 = Decor(name='cfc', theme=snow, url='decor/snow/cfc.svg',
                    height=107, width=100)

    decor12 = Decor(name='pond', theme=snow, url='decor/snow/pond.svg',
                    height=100, width=150)

    decor13 = Decor(name='tile1', theme=grass, url='decor/grass/tile1.svg',
                    height=100, width=100)

    decor14 = Decor(name='tile1', theme=snow, url='decor/snow/tile1.svg',
                    height=100, width=100)

    decor15 = Decor(name='tile2', theme=snow, url='decor/snow/tile2.svg',
                    height=100, width=100)

    decor16 = Decor(name='house', theme=farm, url='decor/farm/house1.svg',
                    height=224, width=184)

    decor17 = Decor(name='cfc', theme=farm, url='decor/farm/cfc.svg',
                    height=301, width=332)

    decor18 = Decor(name='bush', theme=farm, url='decor/farm/bush.svg',
                    height=30, width=50)

    decor19 = Decor(name='tree1', theme=farm, url='decor/farm/tree1.svg',
                    height=100, width=100)

    decor20 = Decor(name='tree2', theme=farm, url='decor/farm/house2.svg',
                    height=88, width=65)

    decor21 = Decor(name='pond', theme=farm, url='decor/farm/crops.svg',
                    height=100, width=150)

    decor22 = Decor(name='tile1', theme=farm, url='decor/farm/tile1.svg',
                    height=337, width=194)

    decor23 = Decor(name='tile1', theme=city, url='decor/city/pavementTile.png',
                    height=100, width=100)

    decor24 = Decor(name='house', theme=city, url='decor/city/house.svg',
                    height=50, width=50)

    decor25 = Decor(name='bush', theme=city, url='decor/city/bush.svg',
                    height=50, width=50)

    decor26 = Decor(name='tree1', theme=city, url='decor/city/shop.svg',
                    height=70, width=70)

    decor27 = Decor(name='tree2', theme=city, url='decor/city/school.svg',
                    height=100, width=100)

    decor28 = Decor(name='pond', theme=city, url='decor/city/hospital.svg',
                    height=157, width=140)

    decor1.save()
    decor2.save()
    decor3.save()
    decor4.save()
    decor5.save()
    decor6.save()
    decor7.save()
    decor8.save()
    decor9.save()
    decor10.save()
    decor11.save()
    decor12.save()
    decor13.save()
    decor14.save()
    decor15.save()
    decor16.save()
    decor17.save()
    decor18.save()
    decor19.save()
    decor20.save()
    decor21.save()
    decor22.save()
    decor23.save()
    decor24.save()
    decor25.save()
    decor26.save()
    decor27.save()
    decor28.save()


def add_blocks(apps, schema_editor):

    Block = apps.get_model('game', 'Block')

    block1 = Block(type='move_forwards')
    block2 = Block(type='turn_left')
    block3 = Block(type='turn_right')
    block4 = Block(type='turn_around')
    block5 = Block(type='wait')
    block6 = Block(type='deliver')
    block7 = Block(type='controls_repeat')
    block8 = Block(type='controls_repeat_while')
    block9 = Block(type='controls_repeat_until')
    block10 = Block(type='controls_if')
    block11 = Block(type='logic_negate')
    block12 = Block(type='at_destination')
    block13 = Block(type='road_exists')
    block14 = Block(type='dead_end')
    block15 = Block(type='traffic_light')
    block16 = Block(type='call_proc')
    block17 = Block(type='declare_proc')

    block1.save()
    block2.save()
    block3.save()
    block4.save()
    block5.save()
    block6.save()
    block7.save()
    block8.save()
    block9.save()
    block10.save()
    block11.save()
    block12.save()
    block13.save()
    block14.save()
    block15.save()
    block16.save()
    block17.save()


def add_levels(apps, schema_editor):

    Level = apps.get_model('game', 'Level')
    Theme = apps.get_model('game', 'Theme')
    Character = apps.get_model('game', 'Character')

    grass = Theme.objects.get(name='grass')
    snow = Theme.objects.get(name='snow')
    farm = Theme.objects.get(name='farm')
    city = Theme.objects.get(name='city')

    van = Character.objects.get(name='Van')
    dee = Character.objects.get(name='Dee')

    level1 = Level(name='1', anonymous=False, blocklyEnabled=True, character=van, default=True,
                   destinations='[[2, 3]]', direct_drive=True, fuel_gauge=False, max_fuel=50,
                   model_solution='[1]', origin='{"coordinate":[0, 3], "direction":"E"}',
                   path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[2,3],"connectedNodes":[1]}]',
                   pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level2 = Level(name='2', anonymous=False, blocklyEnabled=True, character=van, default=True,
                   destinations='[[4, 3]]', direct_drive=True, fuel_gauge=False, max_fuel=50,
                   model_solution='[3]', origin='{"coordinate":[0, 3], "direction":"E"}',
                   path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[2,3],"connectedNodes":[1,3]},{"coordinate":[3,3],"connectedNodes":[2,4]},{"coordinate":[4,3],"connectedNodes":[3]}]',
                   pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level3 = Level(name='3', anonymous=False, blocklyEnabled=True, character=van, default=True,
                   destinations='[[2, 2]]', direct_drive=True, fuel_gauge=False, max_fuel=50,
                   model_solution='[2]', origin='{"coordinate":[0, 3], "direction":"E"}',
                   path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[2,3],"connectedNodes":[1,3]},{"coordinate":[2,2],"connectedNodes":[2]}]',
                   pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level4 = Level(name='4', anonymous=False, blocklyEnabled=True, character=van, default=True,
                   destinations='[[4, 5]]', direct_drive=True, fuel_gauge=False, max_fuel=50,
                   model_solution='[5]', origin='{"coordinate":[0, 3], "direction":"E"}',
                   path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[2,3],"connectedNodes":[1,3]},{"coordinate":[3,3],"connectedNodes":[2,4]},{"coordinate":[4,3],"connectedNodes":[3,5]},{"coordinate":[4,4],"connectedNodes":[6,4]},{"coordinate":[4,5],"connectedNodes":[5]}]',
                   pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level5 = Level(name='5', anonymous=False, blocklyEnabled=True, character=van, default=True,
                   destinations='[[4, 6]]', direct_drive=True, fuel_gauge=False, max_fuel=50,
                   model_solution='[6]', origin='{"coordinate":[0, 3], "direction":"E"}',
                   path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[1,4],"connectedNodes":[1,3]},{"coordinate":[2,4],"connectedNodes":[2,4]},{"coordinate":[2,5],"connectedNodes":[3,5]},{"coordinate":[3,5],"connectedNodes":[4,6]},{"coordinate":[3,6],"connectedNodes":[5,7]},{"coordinate":[4,6],"connectedNodes":[6]}]',
                   pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level6 = Level(name='6', anonymous=False, blocklyEnabled=True, character=van, default=True,
                   destinations='[[6, 1]]', direct_drive=True, fuel_gauge=False, max_fuel=50,
                   model_solution='[10]', origin='{"coordinate":[0, 4], "direction":"E"}',
                   path='[{"coordinate":[0,4],"connectedNodes":[1]},{"coordinate":[1,4],"connectedNodes":[0,2]},{"coordinate":[2,4],"connectedNodes":[1,3]},{"coordinate":[3,4],"connectedNodes":[2,4]},{"coordinate":[3,5],"connectedNodes":[5,3]},{"coordinate":[4,5],"connectedNodes":[4,6]},{"coordinate":[5,5],"connectedNodes":[5,7]},{"coordinate":[5,4],"connectedNodes":[6,8]},{"coordinate":[5,3],"connectedNodes":[7,9]},{"coordinate":[5,2],"connectedNodes":[8,10]},{"coordinate":[5,1],"connectedNodes":[9,11]},{"coordinate":[6,1],"connectedNodes":[10]}]',
                   pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level7 = Level(name='7', anonymous=False, blocklyEnabled=True, character=van, default=True,
                   destinations='[[5, 3]]', direct_drive=True, fuel_gauge=False, max_fuel=50,
                   model_solution='[12]', origin='{"coordinate":[0, 3], "direction":"E"}',
                   path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[1,4],"connectedNodes":[1,3]},{"coordinate":[1,5],"connectedNodes":[2,4]},{"coordinate":[1,6],"connectedNodes":[3,5]},{"coordinate":[2,6],"connectedNodes":[4,6]},{"coordinate":[2,5],"connectedNodes":[5,7]},{"coordinate":[3,5],"connectedNodes":[6,8]},{"coordinate":[3,4],"connectedNodes":[7,9]},{"coordinate":[3,3],"connectedNodes":[8,10]},{"coordinate":[3,2],"connectedNodes":[9,11]},{"coordinate":[4,2],"connectedNodes":[10,12]},{"coordinate":[4,3],"connectedNodes":[11,13]},{"coordinate":[5,3],"connectedNodes":[12]}]',
                   pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level8 = Level(name='8', anonymous=False, blocklyEnabled=True, character=van, default=True,
                   destinations='[[4, 1]]', direct_drive=True, fuel_gauge=False, max_fuel=50,
                   model_solution='[9]', origin='{"coordinate":[3, 6], "direction":"S"}',
                   path='[{"coordinate":[3,6],"connectedNodes":[1]},{"coordinate":[3,5],"connectedNodes":[0,2]},{"coordinate":[3,4],"connectedNodes":[3,1]},{"coordinate":[2,4],"connectedNodes":[4,2]},{"coordinate":[1,4],"connectedNodes":[3,5]},{"coordinate":[1,3],"connectedNodes":[4,6]},{"coordinate":[1,2],"connectedNodes":[5,7]},{"coordinate":[2,2],"connectedNodes":[6,8]},{"coordinate":[3,2],"connectedNodes":[7,9]},{"coordinate":[4,2],"connectedNodes":[8,10]},{"coordinate":[4,1],"connectedNodes":[9]}]',
                   pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level9 = Level(name='9', anonymous=False, blocklyEnabled=True, character=van, default=True,
                   destinations='[[8, 1]]', direct_drive=True, fuel_gauge=False, max_fuel=50,
                   model_solution='[13]', origin='{"coordinate":[6, 3], "direction":"W"}',
                   path='[{"coordinate":[6,3],"connectedNodes":[1]},{"coordinate":[5,3],"connectedNodes":[2,0]},{"coordinate":[4,3],"connectedNodes":[3,1]},{"coordinate":[3,3],"connectedNodes":[4,2]},{"coordinate":[2,3],"connectedNodes":[5,3]},{"coordinate":[1,3],"connectedNodes":[4,6]},{"coordinate":[1,2],"connectedNodes":[5,7]},{"coordinate":[1,1],"connectedNodes":[6,8]},{"coordinate":[2,1],"connectedNodes":[7,9]},{"coordinate":[3,1],"connectedNodes":[8,10]},{"coordinate":[4,1],"connectedNodes":[9,11]},{"coordinate":[5,1],"connectedNodes":[10,12]},{"coordinate":[6,1],"connectedNodes":[11,13]},{"coordinate":[7,1],"connectedNodes":[12,14]},{"coordinate":[8,1],"connectedNodes":[13]}]',
                   pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level10 = Level(name='10', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[3, 3]]', direct_drive=True, fuel_gauge=False, max_fuel=50,
                    model_solution='[7]', origin='{"coordinate":[5, 5], "direction":"W"}',
                    path='[{"coordinate":[5,5],"connectedNodes":[1]},{"coordinate":[4,5],"connectedNodes":[2,0]},{"coordinate":[4,6],"connectedNodes":[3,1]},{"coordinate":[3,6],"connectedNodes":[4,2]},{"coordinate":[2,6],"connectedNodes":[3,5]},{"coordinate":[2,5],"connectedNodes":[4,6]},{"coordinate":[2,4],"connectedNodes":[5,7]},{"coordinate":[2,3],"connectedNodes":[6,8]},{"coordinate":[3,3],"connectedNodes":[7]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level11 = Level(name='11', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[1, 3]]', direct_drive=True, fuel_gauge=False, max_fuel=50,
                    model_solution='[12]', origin='{"coordinate":[3, 4], "direction":"W"}',
                    path='[{"coordinate":[3,4],"connectedNodes":[1]},{"coordinate":[2,4],"connectedNodes":[2,0]},{"coordinate":[2,5],"connectedNodes":[3,1]},{"coordinate":[3,5],"connectedNodes":[2,4]},{"coordinate":[4,5],"connectedNodes":[3,5]},{"coordinate":[5,5],"connectedNodes":[4,6]},{"coordinate":[5,4],"connectedNodes":[5,7]},{"coordinate":[5,3],"connectedNodes":[6,8]},{"coordinate":[5,2],"connectedNodes":[9,7]},{"coordinate":[4,2],"connectedNodes":[10,8]},{"coordinate":[3,2],"connectedNodes":[11,9]},{"coordinate":[2,2],"connectedNodes":[12,10]},{"coordinate":[1,2],"connectedNodes":[13,11]},{"coordinate":[1,3],"connectedNodes":[12]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level12 = Level(name='12', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[1, 3]]', direct_drive=True, fuel_gauge=False, max_fuel=50,
                    model_solution='[17]', origin='{"coordinate":[5, 7], "direction":"W"}',
                    path='[{"coordinate":[5,7],"connectedNodes":[17]},{"coordinate":[2,6],"connectedNodes":[18,2]},{"coordinate":[2,5],"connectedNodes":[3,1]},{"coordinate":[1,5],"connectedNodes":[2,4]},{"coordinate":[1,4],"connectedNodes":[3,5]},{"coordinate":[2,4],"connectedNodes":[4,6]},{"coordinate":[3,4],"connectedNodes":[5,7]},{"coordinate":[4,4],"connectedNodes":[6,8]},{"coordinate":[4,3],"connectedNodes":[7,9]},{"coordinate":[4,2],"connectedNodes":[10,8]},{"coordinate":[3,2],"connectedNodes":[11,9]},{"coordinate":[2,2],"connectedNodes":[12,10]},{"coordinate":[1,2],"connectedNodes":[13,11]},{"coordinate":[1,3],"connectedNodes":[12]},{"coordinate":[1,7],"connectedNodes":[15,18]},{"coordinate":[2,7],"connectedNodes":[14,16]},{"coordinate":[3,7],"connectedNodes":[15,17]},{"coordinate":[4,7],"connectedNodes":[16,0]},{"coordinate":[1,6],"connectedNodes":[14,1]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level13 = Level(name='13', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[0, 1]]', direct_drive=True, fuel_gauge=False, max_fuel=50,
                    model_solution='[11]', origin='{"coordinate":[2, 7], "direction":"S"}',
                    path='[{"coordinate":[2,7],"connectedNodes":[1]},{"coordinate":[2,6],"connectedNodes":[0,2]},{"coordinate":[3,6],"connectedNodes":[1,3,10]},{"coordinate":[4,6],"connectedNodes":[2,4]},{"coordinate":[5,6],"connectedNodes":[3,5]},{"coordinate":[6,6],"connectedNodes":[4,6]},{"coordinate":[6,5],"connectedNodes":[5,7]},{"coordinate":[6,4],"connectedNodes":[13,6,8]},{"coordinate":[6,3],"connectedNodes":[7,9]},{"coordinate":[6,2],"connectedNodes":[8,14]},{"coordinate":[3,5],"connectedNodes":[2,11]},{"coordinate":[3,4],"connectedNodes":[10,12]},{"coordinate":[4,4],"connectedNodes":[11,13,18]},{"coordinate":[5,4],"connectedNodes":[12,7]},{"coordinate":[6,1],"connectedNodes":[15,9]},{"coordinate":[5,1],"connectedNodes":[16,14]},{"coordinate":[4,1],"connectedNodes":[19,17,15]},{"coordinate":[4,2],"connectedNodes":[18,16]},{"coordinate":[4,3],"connectedNodes":[12,17]},{"coordinate":[3,1],"connectedNodes":[20,16]},{"coordinate":[2,1],"connectedNodes":[21,19]},{"coordinate":[1,1],"connectedNodes":[22,20]},{"coordinate":[0,1],"connectedNodes":[21]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level14 = Level(name='14', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[2, 5]]', direct_drive=True, fuel_gauge=False, max_fuel=50,
                    model_solution='[7]', origin='{"coordinate":[7, 2], "direction":"W"}',
                    path='[{"coordinate":[7,2],"connectedNodes":[27]},{"coordinate":[4,2],"connectedNodes":[4,14]},{"coordinate":[3,1],"connectedNodes":[3,14]},{"coordinate":[2,1],"connectedNodes":[7,2]},{"coordinate":[4,3],"connectedNodes":[10,5,1]},{"coordinate":[5,3],"connectedNodes":[4,6]},{"coordinate":[6,3],"connectedNodes":[5,11,27]},{"coordinate":[1,1],"connectedNodes":[8,3]},{"coordinate":[1,2],"connectedNodes":[21,7]},{"coordinate":[3,4],"connectedNodes":[16,10]},{"coordinate":[4,4],"connectedNodes":[9,4]},{"coordinate":[6,4],"connectedNodes":[12,6]},{"coordinate":[6,5],"connectedNodes":[20,11]},{"coordinate":[5,1],"connectedNodes":[14,15]},{"coordinate":[4,1],"connectedNodes":[2,1,13]},{"coordinate":[6,1],"connectedNodes":[13,27]},{"coordinate":[3,5],"connectedNodes":[26,17,9]},{"coordinate":[3,6],"connectedNodes":[18,16]},{"coordinate":[4,6],"connectedNodes":[17,19]},{"coordinate":[5,6],"connectedNodes":[18,20]},{"coordinate":[6,6],"connectedNodes":[19,12]},{"coordinate":[2,2],"connectedNodes":[8,22]},{"coordinate":[2,3],"connectedNodes":[23,21]},{"coordinate":[1,3],"connectedNodes":[24,22]},{"coordinate":[1,4],"connectedNodes":[25,23]},{"coordinate":[1,5],"connectedNodes":[26,24]},{"coordinate":[2,5],"connectedNodes":[25,16]},{"coordinate":[6,2],"connectedNodes":[6,0,15]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level15 = Level(name='15', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[5, 5], [7, 2]]', direct_drive=True, fuel_gauge=False,
                    max_fuel=50, model_solution='[13]',
                    origin='{"coordinate":[2, 7], "direction":"S"}',
                    path='[{"coordinate":[2,7],"connectedNodes":[1]},{"coordinate":[2,6],"connectedNodes":[0,4,2]},{"coordinate":[2,5],"connectedNodes":[3,1]},{"coordinate":[1,5],"connectedNodes":[9,2]},{"coordinate":[3,6],"connectedNodes":[1,5]},{"coordinate":[4,6],"connectedNodes":[4,6]},{"coordinate":[4,7],"connectedNodes":[7,5]},{"coordinate":[5,7],"connectedNodes":[6,8]},{"coordinate":[5,6],"connectedNodes":[7,13]},{"coordinate":[0,5],"connectedNodes":[3,10]},{"coordinate":[0,4],"connectedNodes":[9,11]},{"coordinate":[1,4],"connectedNodes":[10,12]},{"coordinate":[2,4],"connectedNodes":[11,15]},{"coordinate":[5,5],"connectedNodes":[8,14]},{"coordinate":[5,4],"connectedNodes":[16,13,17]},{"coordinate":[3,4],"connectedNodes":[12,16]},{"coordinate":[4,4],"connectedNodes":[15,14,21]},{"coordinate":[5,3],"connectedNodes":[21,14,18]},{"coordinate":[5,2],"connectedNodes":[17,19]},{"coordinate":[6,2],"connectedNodes":[18,20]},{"coordinate":[7,2],"connectedNodes":[19]},{"coordinate":[4,3],"connectedNodes":[16,17]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level16 = Level(name='16', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[7, 0], [5, 1], [1, 4]]', direct_drive=True, fuel_gauge=False,
                    max_fuel=50, model_solution='[16]',
                    origin='{"coordinate":[2, 7], "direction":"S"}',
                    path='[{"coordinate":[2,7],"connectedNodes":[1]},{"coordinate":[2,6],"connectedNodes":[2,0,11]},{"coordinate":[1,6],"connectedNodes":[1,3]},{"coordinate":[1,5],"connectedNodes":[2,4]},{"coordinate":[1,4],"connectedNodes":[3,5]},{"coordinate":[1,3],"connectedNodes":[4,6]},{"coordinate":[1,2],"connectedNodes":[5,7]},{"coordinate":[2,2],"connectedNodes":[6,8]},{"coordinate":[3,2],"connectedNodes":[7,29,9]},{"coordinate":[4,2],"connectedNodes":[8,10]},{"coordinate":[5,2],"connectedNodes":[9,27,17]},{"coordinate":[2,5],"connectedNodes":[1,12]},{"coordinate":[3,5],"connectedNodes":[11,13]},{"coordinate":[3,6],"connectedNodes":[14,12]},{"coordinate":[4,6],"connectedNodes":[13,15]},{"coordinate":[4,5],"connectedNodes":[14,21,16]},{"coordinate":[4,4],"connectedNodes":[28,15]},{"coordinate":[5,1],"connectedNodes":[10,18]},{"coordinate":[5,0],"connectedNodes":[17,19]},{"coordinate":[6,0],"connectedNodes":[18,20]},{"coordinate":[7,0],"connectedNodes":[19]},{"coordinate":[5,5],"connectedNodes":[15,22]},{"coordinate":[6,5],"connectedNodes":[21,23]},{"coordinate":[7,5],"connectedNodes":[22,24]},{"coordinate":[7,4],"connectedNodes":[23,25]},{"coordinate":[7,3],"connectedNodes":[24,26]},{"coordinate":[7,2],"connectedNodes":[27,25]},{"coordinate":[6,2],"connectedNodes":[10,26]},{"coordinate":[3,4],"connectedNodes":[16,29]},{"coordinate":[3,3],"connectedNodes":[28,8]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level17 = Level(name='17', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[4, 1], [5, 2], [5, 5], [3, 6]]', direct_drive=True,
                    fuel_gauge=False, max_fuel=50, model_solution='[16]',
                    origin='{"coordinate":[2, 6], "direction":"S"}',
                    path='[{"coordinate":[2,6],"connectedNodes":[30]},{"coordinate":[3,6],"connectedNodes":[2,28]},{"coordinate":[4,6],"connectedNodes":[1,3]},{"coordinate":[5,6],"connectedNodes":[2,6,4]},{"coordinate":[5,5],"connectedNodes":[3,5]},{"coordinate":[5,4],"connectedNodes":[10,4]},{"coordinate":[6,6],"connectedNodes":[3,7]},{"coordinate":[7,6],"connectedNodes":[6,8]},{"coordinate":[7,5],"connectedNodes":[7,9]},{"coordinate":[7,4],"connectedNodes":[8,16]},{"coordinate":[4,4],"connectedNodes":[5,26]},{"coordinate":[1,2],"connectedNodes":[29,19]},{"coordinate":[2,3],"connectedNodes":[29,13]},{"coordinate":[3,3],"connectedNodes":[12,26]},{"coordinate":[5,3],"connectedNodes":[15,17]},{"coordinate":[6,3],"connectedNodes":[14,16]},{"coordinate":[7,3],"connectedNodes":[15,9,25]},{"coordinate":[5,2],"connectedNodes":[27,14,18]},{"coordinate":[5,1],"connectedNodes":[22,17,23]},{"coordinate":[1,1],"connectedNodes":[11,20]},{"coordinate":[2,1],"connectedNodes":[19,21]},{"coordinate":[3,1],"connectedNodes":[20,22]},{"coordinate":[4,1],"connectedNodes":[21,18]},{"coordinate":[6,1],"connectedNodes":[18,24]},{"coordinate":[7,1],"connectedNodes":[23,25]},{"coordinate":[7,2],"connectedNodes":[16,24]},{"coordinate":[4,3],"connectedNodes":[13,10,27]},{"coordinate":[4,2],"connectedNodes":[26,17]},{"coordinate":[3,5],"connectedNodes":[30,1]},{"coordinate":[1,3],"connectedNodes":[12,11]},{"coordinate":[2,5],"connectedNodes":[0,28]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level18 = Level(name='18', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[2, 7], [7, 7], [8, 5], [8, 1]]', direct_drive=True,
                    fuel_gauge=False, max_fuel=50, model_solution='[19]',
                    origin='{"coordinate":[6, 1], "direction":"S"}', pythonEnabled=False,
                    path='[{"coordinate":[6,1],"connectedNodes":[4]},{"coordinate":[3,0],"connectedNodes":[49,2]},{"coordinate":[4,0],"connectedNodes":[1,3]},{"coordinate":[5,0],"connectedNodes":[2,4]},{"coordinate":[6,0],"connectedNodes":[3,0,5]},{"coordinate":[7,0],"connectedNodes":[4,6]},{"coordinate":[8,0],"connectedNodes":[5,11]},{"coordinate":[1,0],"connectedNodes":[8,49]},{"coordinate":[1,1],"connectedNodes":[9,7]},{"coordinate":[2,1],"connectedNodes":[8,10]},{"coordinate":[3,1],"connectedNodes":[9,38]},{"coordinate":[8,1],"connectedNodes":[12,6]},{"coordinate":[8,2],"connectedNodes":[13,11]},{"coordinate":[8,3],"connectedNodes":[14,12]},{"coordinate":[8,4],"connectedNodes":[15,13]},{"coordinate":[8,5],"connectedNodes":[16,14]},{"coordinate":[8,6],"connectedNodes":[17,15]},{"coordinate":[7,6],"connectedNodes":[43,18,16,42]},{"coordinate":[7,7],"connectedNodes":[19,17]},{"coordinate":[6,7],"connectedNodes":[20,18]},{"coordinate":[5,7],"connectedNodes":[21,19]},{"coordinate":[4,7],"connectedNodes":[22,20]},{"coordinate":[3,7],"connectedNodes":[30,21]},{"coordinate":[2,6],"connectedNodes":[24,30,48,29]},{"coordinate":[1,6],"connectedNodes":[25,23]},{"coordinate":[0,6],"connectedNodes":[24,26]},{"coordinate":[0,5],"connectedNodes":[25,27]},{"coordinate":[0,4],"connectedNodes":[26,31]},{"coordinate":[2,4],"connectedNodes":[29,34,33]},{"coordinate":[2,5],"connectedNodes":[23,28]},{"coordinate":[2,7],"connectedNodes":[22,23]},{"coordinate":[0,3],"connectedNodes":[27,32]},{"coordinate":[1,3],"connectedNodes":[31,33]},{"coordinate":[2,3],"connectedNodes":[32,28]},{"coordinate":[3,4],"connectedNodes":[28,35]},{"coordinate":[4,4],"connectedNodes":[34,39,36]},{"coordinate":[4,3],"connectedNodes":[35,37]},{"coordinate":[4,2],"connectedNodes":[36,38]},{"coordinate":[4,1],"connectedNodes":[10,37]},{"coordinate":[5,4],"connectedNodes":[35,40]},{"coordinate":[6,4],"connectedNodes":[39,41]},{"coordinate":[7,4],"connectedNodes":[40,42]},{"coordinate":[7,5],"connectedNodes":[17,41]},{"coordinate":[6,6],"connectedNodes":[44,17]},{"coordinate":[5,6],"connectedNodes":[43,45]},{"coordinate":[5,5],"connectedNodes":[46,44]},{"coordinate":[4,5],"connectedNodes":[47,45]},{"coordinate":[4,6],"connectedNodes":[48,46]},{"coordinate":[3,6],"connectedNodes":[23,47]},{"coordinate":[2,0],"connectedNodes":[7,1]}]',
                    theme=grass, threads=1, traffic_lights='[]')

    level19 = Level(name='19', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[4, 3]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    model_solution='[2]', origin='{"coordinate":[0, 3], "direction":"E"}',
                    path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[2,3],"connectedNodes":[1,3]},{"coordinate":[3,3],"connectedNodes":[2,4]},{"coordinate":[4,3],"connectedNodes":[3]}] ',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level20 = Level(name='20', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[4, 6]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    model_solution='[3]', origin='{"coordinate":[0, 3], "direction":"E"}',
                    path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[1,4],"connectedNodes":[1,3]},{"coordinate":[2,4],"connectedNodes":[2,4]},{"coordinate":[2,5],"connectedNodes":[3,5]},{"coordinate":[3,5],"connectedNodes":[4,6]},{"coordinate":[3,6],"connectedNodes":[5,7]},{"coordinate":[4,6],"connectedNodes":[6]}] ',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level21 = Level(name='21', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[3, 7]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    model_solution='[5]', origin='{"coordinate":[1, 6], "direction":"S"}',
                    path='[{"coordinate":[1,6],"connectedNodes":[2]},{"coordinate":[1,4],"connectedNodes":[2,3]},{"coordinate":[1,5],"connectedNodes":[0,1]},{"coordinate":[2,4],"connectedNodes":[1,4]},{"coordinate":[2,3],"connectedNodes":[3,5]},{"coordinate":[3,3],"connectedNodes":[4,6]},{"coordinate":[4,3],"connectedNodes":[5,7]},{"coordinate":[4,4],"connectedNodes":[8,6]},{"coordinate":[5,4],"connectedNodes":[7,9]},{"coordinate":[5,5],"connectedNodes":[10,8]},{"coordinate":[5,6],"connectedNodes":[11,9]},{"coordinate":[4,6],"connectedNodes":[12,10]},{"coordinate":[4,7],"connectedNodes":[13,11]},{"coordinate":[3,7],"connectedNodes":[12]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level22 = Level(name='22', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[7, 5]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    model_solution='[19]', origin='{"coordinate":[8, 3], "direction":"W"}',
                    path='[{"coordinate":[8,3],"connectedNodes":[1]},{"coordinate":[7,3],"connectedNodes":[2,0]},{"coordinate":[6,3],"connectedNodes":[3,1]},{"coordinate":[5,3],"connectedNodes":[4,2]},{"coordinate":[5,4],"connectedNodes":[5,3]},{"coordinate":[5,5],"connectedNodes":[6,4]},{"coordinate":[5,6],"connectedNodes":[7,5]},{"coordinate":[4,6],"connectedNodes":[8,6]},{"coordinate":[3,6],"connectedNodes":[9,7]},{"coordinate":[2,6],"connectedNodes":[10,8]},{"coordinate":[1,6],"connectedNodes":[9,11]},{"coordinate":[1,5],"connectedNodes":[10,12]},{"coordinate":[1,4],"connectedNodes":[11,13]},{"coordinate":[1,3],"connectedNodes":[12,14]},{"coordinate":[1,2],"connectedNodes":[13,15]},{"coordinate":[1,1],"connectedNodes":[14,16]},{"coordinate":[2,1],"connectedNodes":[15,17]},{"coordinate":[3,1],"connectedNodes":[16,18]},{"coordinate":[4,1],"connectedNodes":[17,19]},{"coordinate":[5,1],"connectedNodes":[18,20]},{"coordinate":[6,1],"connectedNodes":[19,21]},{"coordinate":[7,1],"connectedNodes":[20,22]},{"coordinate":[8,1],"connectedNodes":[21,23]},{"coordinate":[9,1],"connectedNodes":[22,24]},{"coordinate":[9,2],"connectedNodes":[25,23]},{"coordinate":[9,3],"connectedNodes":[26,24]},{"coordinate":[9,4],"connectedNodes":[27,25]},{"coordinate":[9,5],"connectedNodes":[28,26]},{"coordinate":[8,5],"connectedNodes":[29,27]},{"coordinate":[7,5],"connectedNodes":[28]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level23 = Level(name='23', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[7, 2]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    model_solution='[9]', origin='{"coordinate":[8, 6], "direction":"W"}',
                    path='[{"coordinate":[8,6],"connectedNodes":[1]},{"coordinate":[7,6],"connectedNodes":[2,0]},{"coordinate":[6,6],"connectedNodes":[3,1]},{"coordinate":[5,6],"connectedNodes":[4,2]},{"coordinate":[4,6],"connectedNodes":[5,3]},{"coordinate":[3,6],"connectedNodes":[6,4]},{"coordinate":[2,6],"connectedNodes":[5,7]},{"coordinate":[2,5],"connectedNodes":[6,8]},{"coordinate":[3,5],"connectedNodes":[7,9]},{"coordinate":[4,5],"connectedNodes":[8,10]},{"coordinate":[5,5],"connectedNodes":[9,11]},{"coordinate":[6,5],"connectedNodes":[10,12]},{"coordinate":[7,5],"connectedNodes":[11,13]},{"coordinate":[8,5],"connectedNodes":[12,14]},{"coordinate":[8,4],"connectedNodes":[15,13]},{"coordinate":[7,4],"connectedNodes":[16,14]},{"coordinate":[6,4],"connectedNodes":[17,15]},{"coordinate":[5,4],"connectedNodes":[18,16]},{"coordinate":[4,4],"connectedNodes":[19,17]},{"coordinate":[3,4],"connectedNodes":[20,18]},{"coordinate":[2,4],"connectedNodes":[19,21]},{"coordinate":[2,3],"connectedNodes":[20,22]},{"coordinate":[3,3],"connectedNodes":[21,23]},{"coordinate":[4,3],"connectedNodes":[22,24]},{"coordinate":[5,3],"connectedNodes":[23,25]},{"coordinate":[6,3],"connectedNodes":[24,26]},{"coordinate":[7,3],"connectedNodes":[25,27]},{"coordinate":[8,3],"connectedNodes":[26,28]},{"coordinate":[8,2],"connectedNodes":[29,27]},{"coordinate":[7,2],"connectedNodes":[28]}] ',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level24 = Level(name='24', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[2, 2]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    model_solution='[12]', origin='{"coordinate":[2, 6], "direction":"S"}',
                    path='[{"coordinate":[2,6],"connectedNodes":[27]},{"coordinate":[2,3],"connectedNodes":[2,28]},{"coordinate":[3,3],"connectedNodes":[1,3]},{"coordinate":[3,2],"connectedNodes":[2,4]},{"coordinate":[4,2],"connectedNodes":[3,5]},{"coordinate":[4,3],"connectedNodes":[6,4]},{"coordinate":[5,3],"connectedNodes":[5,7]},{"coordinate":[5,2],"connectedNodes":[6,8]},{"coordinate":[6,2],"connectedNodes":[7,9]},{"coordinate":[6,3],"connectedNodes":[10,8]},{"coordinate":[7,3],"connectedNodes":[9,11]},{"coordinate":[7,2],"connectedNodes":[10,12]},{"coordinate":[8,2],"connectedNodes":[11,13]},{"coordinate":[8,3],"connectedNodes":[14,12]},{"coordinate":[8,4],"connectedNodes":[15,13]},{"coordinate":[8,5],"connectedNodes":[16,14]},{"coordinate":[8,6],"connectedNodes":[17,15]},{"coordinate":[7,6],"connectedNodes":[16,18]},{"coordinate":[7,5],"connectedNodes":[19,17]},{"coordinate":[6,5],"connectedNodes":[20,18]},{"coordinate":[6,6],"connectedNodes":[21,19]},{"coordinate":[5,6],"connectedNodes":[20,22]},{"coordinate":[5,5],"connectedNodes":[23,21]},{"coordinate":[4,5],"connectedNodes":[24,22]},{"coordinate":[4,6],"connectedNodes":[25,23]},{"coordinate":[3,6],"connectedNodes":[24,26]},{"coordinate":[3,5],"connectedNodes":[27,25]},{"coordinate":[2,5],"connectedNodes":[0,26]},{"coordinate":[2,2],"connectedNodes":[1]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level25 = Level(name='25', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[8, 2]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    model_solution='[6]', origin='{"coordinate":[0, 6], "direction":"E"}',
                    path='[{"coordinate":[0,6],"connectedNodes":[1]},{"coordinate":[1,6],"connectedNodes":[0,2]},{"coordinate":[2,6],"connectedNodes":[1,3]},{"coordinate":[2,5],"connectedNodes":[2,4]},{"coordinate":[3,5],"connectedNodes":[3,5]},{"coordinate":[3,4],"connectedNodes":[4,6]},{"coordinate":[4,4],"connectedNodes":[5,7]},{"coordinate":[5,4],"connectedNodes":[6,8]},{"coordinate":[5,3],"connectedNodes":[7,9]},{"coordinate":[6,3],"connectedNodes":[8,10]},{"coordinate":[6,2],"connectedNodes":[9,11]},{"coordinate":[7,2],"connectedNodes":[10,12]},{"coordinate":[8,2],"connectedNodes":[11]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level26 = Level(name='26', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[8, 3]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    model_solution='[5]', origin='{"coordinate":[4, 6], "direction":"S"}',
                    path='[{"coordinate":[4,6],"connectedNodes":[1]},{"coordinate":[4,5],"connectedNodes":[0,2]},{"coordinate":[4,4],"connectedNodes":[1,3]},{"coordinate":[4,3],"connectedNodes":[2,4]},{"coordinate":[5,3],"connectedNodes":[3,5]},{"coordinate":[6,3],"connectedNodes":[4,6]},{"coordinate":[7,3],"connectedNodes":[5,7]},{"coordinate":[8,3],"connectedNodes":[6]}]',
                    pythonEnabled=False, theme=snow, threads=1, traffic_lights='[]')

    level27 = Level(name='27', anonymous=False, blocklyEnabled=True, character=dee, default=True,
                    destinations='[[8, 3]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    model_solution='[16, 14]', origin='{"coordinate":[4, 5], "direction":"E"}',
                    path='[{"coordinate":[4,5],"connectedNodes":[1]},{"coordinate":[5,5],"connectedNodes":[0,2]},{"coordinate":[6,5],"connectedNodes":[1,3]},{"coordinate":[7,5],"connectedNodes":[2,4]},{"coordinate":[7,6],"connectedNodes":[5,3]},{"coordinate":[7,7],"connectedNodes":[6,4]},{"coordinate":[6,7],"connectedNodes":[7,5]},{"coordinate":[5,7],"connectedNodes":[8,6]},{"coordinate":[4,7],"connectedNodes":[9,7]},{"coordinate":[3,7],"connectedNodes":[10,8]},{"coordinate":[2,7],"connectedNodes":[11,9]},{"coordinate":[1,7],"connectedNodes":[10,12]},{"coordinate":[1,6],"connectedNodes":[11,13]},{"coordinate":[1,5],"connectedNodes":[12,14]},{"coordinate":[1,4],"connectedNodes":[13,15]},{"coordinate":[1,3],"connectedNodes":[14,16]},{"coordinate":[1,2],"connectedNodes":[15,17]},{"coordinate":[2,2],"connectedNodes":[16,18]},{"coordinate":[2,1],"connectedNodes":[17,19]},{"coordinate":[3,1],"connectedNodes":[18,20]},{"coordinate":[4,1],"connectedNodes":[19,21]},{"coordinate":[5,1],"connectedNodes":[20,22]},{"coordinate":[6,1],"connectedNodes":[21,23]},{"coordinate":[7,1],"connectedNodes":[22,24]},{"coordinate":[7,2],"connectedNodes":[25,23]},{"coordinate":[8,2],"connectedNodes":[24,26]},{"coordinate":[8,3],"connectedNodes":[25]}]',
                    pythonEnabled=False, theme=farm, threads=1, traffic_lights='[]')

    level28 = Level(name='28', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[9, 4]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    model_solution='[19]', origin='{"coordinate":[1, 3], "direction":"E"}',
                    path='[{"coordinate":[1,3],"connectedNodes":[1]},{"coordinate":[2,3],"connectedNodes":[0,2]},{"coordinate":[3,3],"connectedNodes":[1,3]},{"coordinate":[3,4],"connectedNodes":[4,2]},{"coordinate":[3,5],"connectedNodes":[5,3]},{"coordinate":[3,6],"connectedNodes":[6,4]},{"coordinate":[4,6],"connectedNodes":[5,7]},{"coordinate":[5,6],"connectedNodes":[6,8]},{"coordinate":[6,6],"connectedNodes":[7,9]},{"coordinate":[6,5],"connectedNodes":[8,10]},{"coordinate":[6,4],"connectedNodes":[9,11]},{"coordinate":[6,3],"connectedNodes":[10,12]},{"coordinate":[6,2],"connectedNodes":[13,11]},{"coordinate":[5,2],"connectedNodes":[14,12]},{"coordinate":[4,2],"connectedNodes":[15,13]},{"coordinate":[3,2],"connectedNodes":[14,16]},{"coordinate":[3,1],"connectedNodes":[15,17]},{"coordinate":[4,1],"connectedNodes":[16,18]},{"coordinate":[5,1],"connectedNodes":[17,19]},{"coordinate":[6,1],"connectedNodes":[18,20]},{"coordinate":[7,1],"connectedNodes":[19,21]},{"coordinate":[8,1],"connectedNodes":[20,22]},{"coordinate":[8,2],"connectedNodes":[23,21]},{"coordinate":[9,2],"connectedNodes":[22,24]},{"coordinate":[9,3],"connectedNodes":[25,23]},{"coordinate":[9,4],"connectedNodes":[24]}]',
                    pythonEnabled=False, theme=city, threads=1, traffic_lights='[]')

    level29 = Level(name='29', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[4, 3]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    model_solution='[3]', origin='{"coordinate":[0, 3], "direction":"E"}',
                    path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[2,3],"connectedNodes":[1,3]},{"coordinate":[3,3],"connectedNodes":[2,4]},{"coordinate":[4,3],"connectedNodes":[3]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level30 = Level(name='30', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[4, 6]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    model_solution='[4]', origin='{"coordinate":[0, 3], "direction":"E"}',
                    path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[1,4],"connectedNodes":[1,3]},{"coordinate":[2,4],"connectedNodes":[2,4]},{"coordinate":[2,5],"connectedNodes":[3,5]},{"coordinate":[3,5],"connectedNodes":[4,6]},{"coordinate":[3,6],"connectedNodes":[5,7]},{"coordinate":[4,6],"connectedNodes":[6]}] ',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level31 = Level(name='31', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[3, 7]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    model_solution='[6]', origin='{"coordinate":[5, 0], "direction":"N"}',
                    path='[{"coordinate":[5,0],"connectedNodes":[1]},{"coordinate":[5,1],"connectedNodes":[2,0]},{"coordinate":[4,1],"connectedNodes":[3,1]},{"coordinate":[4,2],"connectedNodes":[4,2]},{"coordinate":[4,3],"connectedNodes":[5,3]},{"coordinate":[4,4],"connectedNodes":[6,4]},{"coordinate":[3,4],"connectedNodes":[7,5]},{"coordinate":[3,5],"connectedNodes":[8,6]},{"coordinate":[3,6],"connectedNodes":[9,7]},{"coordinate":[3,7],"connectedNodes":[8]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level32 = Level(name='32', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[5, 0]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    model_solution='[5]', origin='{"coordinate":[2, 7], "direction":"S"}',
                    path='[{"coordinate":[2,7],"connectedNodes":[1]},{"coordinate":[2,6],"connectedNodes":[0,2]},{"coordinate":[3,6],"connectedNodes":[1,3]},{"coordinate":[3,5],"connectedNodes":[2,4]},{"coordinate":[3,4],"connectedNodes":[3,5]},{"coordinate":[4,4],"connectedNodes":[4,6]},{"coordinate":[4,3],"connectedNodes":[5,7]},{"coordinate":[4,2],"connectedNodes":[6,8]},{"coordinate":[5,2],"connectedNodes":[7,9]},{"coordinate":[5,1],"connectedNodes":[8,10]},{"coordinate":[5,0],"connectedNodes":[9]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level33 = Level(name='33', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[4, 3]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    model_solution='[5]', origin='{"coordinate":[0, 3], "direction":"E"}',
                    path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[2,3],"connectedNodes":[1,3]},{"coordinate":[3,3],"connectedNodes":[2,4]},{"coordinate":[4,3],"connectedNodes":[3]}] ',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level34 = Level(name='34', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[6, 6]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    model_solution='[8, 7]', origin='{"coordinate":[1, 2], "direction":"E"}',
                    path='[{"coordinate":[1,2],"connectedNodes":[1]},{"coordinate":[2,2],"connectedNodes":[0,2]},{"coordinate":[3,2],"connectedNodes":[1,3]},{"coordinate":[4,2],"connectedNodes":[2,4]},{"coordinate":[5,2],"connectedNodes":[3,5]},{"coordinate":[6,2],"connectedNodes":[4,6]},{"coordinate":[7,2],"connectedNodes":[5,7]},{"coordinate":[8,2],"connectedNodes":[6,8]},{"coordinate":[8,3],"connectedNodes":[9,7]},{"coordinate":[8,4],"connectedNodes":[10,8]},{"coordinate":[8,5],"connectedNodes":[11,9]},{"coordinate":[8,6],"connectedNodes":[12,10]},{"coordinate":[8,7],"connectedNodes":[13,11]},{"coordinate":[7,7],"connectedNodes":[14,12]},{"coordinate":[6,7],"connectedNodes":[15,13]},{"coordinate":[5,7],"connectedNodes":[16,14]},{"coordinate":[4,7],"connectedNodes":[17,15]},{"coordinate":[3,7],"connectedNodes":[16,18]},{"coordinate":[3,6],"connectedNodes":[17,19]},{"coordinate":[3,5],"connectedNodes":[18,20]},{"coordinate":[3,4],"connectedNodes":[19,21]},{"coordinate":[4,4],"connectedNodes":[20,22]},{"coordinate":[5,4],"connectedNodes":[21,23]},{"coordinate":[6,4],"connectedNodes":[22,24]},{"coordinate":[6,5],"connectedNodes":[25,23]},{"coordinate":[6,6],"connectedNodes":[24]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level35 = Level(name='35', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[1, 1]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    model_solution='[11, 9, 8]', origin='{"coordinate":[8, 6], "direction":"W"}',
                    path='[{"coordinate":[8,6],"connectedNodes":[1]},{"coordinate":[7,6],"connectedNodes":[2,0]},{"coordinate":[6,6],"connectedNodes":[3,1]},{"coordinate":[5,6],"connectedNodes":[4,2]},{"coordinate":[4,6],"connectedNodes":[3,5]},{"coordinate":[4,5],"connectedNodes":[4,6]},{"coordinate":[4,4],"connectedNodes":[5,7]},{"coordinate":[5,4],"connectedNodes":[6,8]},{"coordinate":[6,4],"connectedNodes":[7,9]},{"coordinate":[7,4],"connectedNodes":[8,10]},{"coordinate":[8,4],"connectedNodes":[9,11]},{"coordinate":[8,3],"connectedNodes":[10,12]},{"coordinate":[8,2],"connectedNodes":[13,11]},{"coordinate":[7,2],"connectedNodes":[14,12]},{"coordinate":[6,2],"connectedNodes":[15,13]},{"coordinate":[5,2],"connectedNodes":[16,14]},{"coordinate":[4,2],"connectedNodes":[15,17]},{"coordinate":[4,1],"connectedNodes":[18,16]},{"coordinate":[3,1],"connectedNodes":[19,17]},{"coordinate":[2,1],"connectedNodes":[20,18]},{"coordinate":[1,1],"connectedNodes":[19]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level36 = Level(name='36', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[5, 3]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    model_solution='[11, 9, 8]', origin='{"coordinate":[0, 3], "direction":"E"}',
                    path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[1,4],"connectedNodes":[1,3]},{"coordinate":[1,5],"connectedNodes":[2,4]},{"coordinate":[1,6],"connectedNodes":[3,5]},{"coordinate":[2,6],"connectedNodes":[4,6]},{"coordinate":[2,5],"connectedNodes":[5,7]},{"coordinate":[3,5],"connectedNodes":[6,8]},{"coordinate":[3,4],"connectedNodes":[7,9]},{"coordinate":[3,3],"connectedNodes":[8,10]},{"coordinate":[3,2],"connectedNodes":[9,11]},{"coordinate":[4,2],"connectedNodes":[10,12]},{"coordinate":[4,3],"connectedNodes":[11,13]},{"coordinate":[5,3],"connectedNodes":[12]}] ',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level37 = Level(name='37', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[3, 2]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    model_solution='[11, 9, 8]', origin='{"coordinate":[6, 1], "direction":"E"}',
                    path='[{"coordinate":[6,1],"connectedNodes":[19]},{"coordinate":[5,3],"connectedNodes":[2,22]},{"coordinate":[4,3],"connectedNodes":[3,1]},{"coordinate":[3,3],"connectedNodes":[4,2]},{"coordinate":[2,3],"connectedNodes":[5,3]},{"coordinate":[2,4],"connectedNodes":[6,4]},{"coordinate":[2,5],"connectedNodes":[7,5]},{"coordinate":[3,5],"connectedNodes":[6,8]},{"coordinate":[4,5],"connectedNodes":[7,9]},{"coordinate":[4,4],"connectedNodes":[8,10]},{"coordinate":[5,4],"connectedNodes":[9,11]},{"coordinate":[6,4],"connectedNodes":[10,12]},{"coordinate":[6,5],"connectedNodes":[13,11]},{"coordinate":[6,6],"connectedNodes":[14,12]},{"coordinate":[7,6],"connectedNodes":[13,15]},{"coordinate":[7,5],"connectedNodes":[14,16]},{"coordinate":[7,4],"connectedNodes":[15,17]},{"coordinate":[7,3],"connectedNodes":[16,18]},{"coordinate":[7,2],"connectedNodes":[17,19]},{"coordinate":[7,1],"connectedNodes":[0,18]},{"coordinate":[3,2],"connectedNodes":[21]},{"coordinate":[4,2],"connectedNodes":[20,22]},{"coordinate":[5,2],"connectedNodes":[21,1]}] ',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level38 = Level(name='38', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[6, 0]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    model_solution='[11, 9, 8]', origin='{"coordinate":[7, 6], "direction":"W"}',
                    path='[{"coordinate":[7,6],"connectedNodes":[1]},{"coordinate":[6,6],"connectedNodes":[2,0]},{"coordinate":[5,6],"connectedNodes":[3,1]},{"coordinate":[4,6],"connectedNodes":[4,2]},{"coordinate":[3,6],"connectedNodes":[5,3]},{"coordinate":[2,6],"connectedNodes":[4,6]},{"coordinate":[2,5],"connectedNodes":[7,5]},{"coordinate":[1,5],"connectedNodes":[8,6]},{"coordinate":[1,6],"connectedNodes":[9,7]},{"coordinate":[0,6],"connectedNodes":[8,10]},{"coordinate":[0,5],"connectedNodes":[9,11]},{"coordinate":[0,4],"connectedNodes":[10,12]},{"coordinate":[1,4],"connectedNodes":[11,13]},{"coordinate":[2,4],"connectedNodes":[12,14]},{"coordinate":[3,4],"connectedNodes":[13,15]},{"coordinate":[3,5],"connectedNodes":[16,14]},{"coordinate":[4,5],"connectedNodes":[15,17]},{"coordinate":[5,5],"connectedNodes":[16,18]},{"coordinate":[6,5],"connectedNodes":[17,19]},{"coordinate":[7,5],"connectedNodes":[18,20]},{"coordinate":[7,4],"connectedNodes":[21,19]},{"coordinate":[6,4],"connectedNodes":[22,20]},{"coordinate":[5,4],"connectedNodes":[23,21]},{"coordinate":[4,4],"connectedNodes":[22,24]},{"coordinate":[4,3],"connectedNodes":[25,23]},{"coordinate":[3,3],"connectedNodes":[26,24]},{"coordinate":[2,3],"connectedNodes":[27,25]},{"coordinate":[1,3],"connectedNodes":[26,28]},{"coordinate":[1,2],"connectedNodes":[27,29]},{"coordinate":[2,2],"connectedNodes":[28,30]},{"coordinate":[3,2],"connectedNodes":[29,31]},{"coordinate":[3,1],"connectedNodes":[30,32]},{"coordinate":[3,0],"connectedNodes":[31,33]},{"coordinate":[4,0],"connectedNodes":[32,34]},{"coordinate":[4,1],"connectedNodes":[35,33]},{"coordinate":[4,2],"connectedNodes":[36,34]},{"coordinate":[5,2],"connectedNodes":[35,37]},{"coordinate":[6,2],"connectedNodes":[36,38]},{"coordinate":[6,1],"connectedNodes":[37,39]},{"coordinate":[6,0],"connectedNodes":[38]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level39 = Level(name='39', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[8, 7]]', direct_drive=False, fuel_gauge=True, max_fuel=50,
                    model_solution='[5, 6]', origin='{"coordinate":[1, 2], "direction":"E"}',
                    path='[{"coordinate":[1,2],"connectedNodes":[1]},{"coordinate":[2,2],"connectedNodes":[0,2]},{"coordinate":[3,2],"connectedNodes":[1,3]},{"coordinate":[4,2],"connectedNodes":[2,9,4]},{"coordinate":[5,2],"connectedNodes":[3,5]},{"coordinate":[6,2],"connectedNodes":[4,6]},{"coordinate":[7,2],"connectedNodes":[5,7]},{"coordinate":[8,2],"connectedNodes":[6,11,8]},{"coordinate":[9,2],"connectedNodes":[7]},{"coordinate":[4,3],"connectedNodes":[10,3]},{"coordinate":[4,4],"connectedNodes":[9]},{"coordinate":[8,3],"connectedNodes":[12,7]},{"coordinate":[8,4],"connectedNodes":[13,11]},{"coordinate":[8,5],"connectedNodes":[14,12]},{"coordinate":[8,6],"connectedNodes":[15,13]},{"coordinate":[8,7],"connectedNodes":[14]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level40 = Level(name='40', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[3, 4]]', direct_drive=False, fuel_gauge=True, max_fuel=50,
                    model_solution='[8, 9]', origin='{"coordinate":[3, 6], "direction":"E"}',
                    path='[{"coordinate":[3,6],"connectedNodes":[1]},{"coordinate":[4,6],"connectedNodes":[0,2]},{"coordinate":[5,6],"connectedNodes":[1,3]},{"coordinate":[5,5],"connectedNodes":[2,5,4]},{"coordinate":[5,4],"connectedNodes":[3,9]},{"coordinate":[6,5],"connectedNodes":[3,6]},{"coordinate":[7,5],"connectedNodes":[5,7]},{"coordinate":[7,6],"connectedNodes":[8,6]},{"coordinate":[8,6],"connectedNodes":[7]},{"coordinate":[5,3],"connectedNodes":[10,4,13]},{"coordinate":[4,3],"connectedNodes":[11,9]},{"coordinate":[3,3],"connectedNodes":[12,10]},{"coordinate":[3,4],"connectedNodes":[11]},{"coordinate":[5,2],"connectedNodes":[9,14]},{"coordinate":[5,1],"connectedNodes":[13,15]},{"coordinate":[6,1],"connectedNodes":[14,16]},{"coordinate":[7,1],"connectedNodes":[15,17]},{"coordinate":[8,1],"connectedNodes":[16,18]},{"coordinate":[8,2],"connectedNodes":[17]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level41 = Level(name='41', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[5, 3]]', direct_drive=False, fuel_gauge=True, max_fuel=50,
                    model_solution='[8, 9]', origin='{"coordinate":[0, 3], "direction":"E"}',
                    path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[2,3],"connectedNodes":[1,3,9]},{"coordinate":[2,4],"connectedNodes":[2,4]},{"coordinate":[3,4],"connectedNodes":[3,5]},{"coordinate":[4,4],"connectedNodes":[4,6]},{"coordinate":[4,3],"connectedNodes":[5,10,7]},{"coordinate":[4,2],"connectedNodes":[6,8]},{"coordinate":[3,2],"connectedNodes":[7,9]},{"coordinate":[2,2],"connectedNodes":[2,8]},{"coordinate":[5,3],"connectedNodes":[6]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level42 = Level(name='42', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[4, 2]]', direct_drive=False, fuel_gauge=True, max_fuel=50,
                    model_solution='[4]', origin='{"coordinate":[0, 3], "direction":"E"}',
                    path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[2,27,26,0]},{"coordinate":[1,4],"connectedNodes":[1,3]},{"coordinate":[1,5],"connectedNodes":[2,4]},{"coordinate":[1,6],"connectedNodes":[3,5]},{"coordinate":[1,7],"connectedNodes":[4,6]},{"coordinate":[2,7],"connectedNodes":[5,7]},{"coordinate":[3,7],"connectedNodes":[6,8]},{"coordinate":[4,7],"connectedNodes":[7,9]},{"coordinate":[5,7],"connectedNodes":[8,10]},{"coordinate":[6,7],"connectedNodes":[9,11]},{"coordinate":[7,7],"connectedNodes":[10,12]},{"coordinate":[7,6],"connectedNodes":[11,13]},{"coordinate":[7,5],"connectedNodes":[12,14]},{"coordinate":[7,4],"connectedNodes":[13,15]},{"coordinate":[7,3],"connectedNodes":[14,16]},{"coordinate":[7,2],"connectedNodes":[15,17]},{"coordinate":[7,1],"connectedNodes":[16,18]},{"coordinate":[7,0],"connectedNodes":[17,19]},{"coordinate":[6,0],"connectedNodes":[18,20]},{"coordinate":[5,0],"connectedNodes":[19,21]},{"coordinate":[4,0],"connectedNodes":[20,22]},{"coordinate":[3,0],"connectedNodes":[21,23]},{"coordinate":[2,0],"connectedNodes":[22,24]},{"coordinate":[1,0],"connectedNodes":[23,25]},{"coordinate":[1,1],"connectedNodes":[24,26]},{"coordinate":[1,2],"connectedNodes":[25,1]},{"coordinate":[2,3],"connectedNodes":[28,45,44,1]},{"coordinate":[2,4],"connectedNodes":[27,29]},{"coordinate":[2,5],"connectedNodes":[28,30]},{"coordinate":[2,6],"connectedNodes":[29,31]},{"coordinate":[3,6],"connectedNodes":[30,32]},{"coordinate":[4,6],"connectedNodes":[31,33]},{"coordinate":[5,6],"connectedNodes":[32,34]},{"coordinate":[6,6],"connectedNodes":[33,35]},{"coordinate":[6,5],"connectedNodes":[34,36]},{"coordinate":[6,4],"connectedNodes":[35,37]},{"coordinate":[6,3],"connectedNodes":[36,38]},{"coordinate":[6,2],"connectedNodes":[37,39]},{"coordinate":[6,1],"connectedNodes":[38,40]},{"coordinate":[5,1],"connectedNodes":[39,41]},{"coordinate":[4,1],"connectedNodes":[40,42]},{"coordinate":[3,1],"connectedNodes":[41,43]},{"coordinate":[2,1],"connectedNodes":[42,44]},{"coordinate":[2,2],"connectedNodes":[43,27]},{"coordinate":[3,3],"connectedNodes":[46,54,53,27]},{"coordinate":[3,4],"connectedNodes":[45,47]},{"coordinate":[3,5],"connectedNodes":[46,48]},{"coordinate":[4,5],"connectedNodes":[47,49]},{"coordinate":[5,5],"connectedNodes":[48,50]},{"coordinate":[5,4],"connectedNodes":[49,51]},{"coordinate":[5,3],"connectedNodes":[50,52]},{"coordinate":[5,2],"connectedNodes":[51,56]},{"coordinate":[3,2],"connectedNodes":[45,56]},{"coordinate":[4,3],"connectedNodes":[45,55]},{"coordinate":[4,4],"connectedNodes":[54]},{"coordinate":[4,2],"connectedNodes":[52,53]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level43 = Level(name='43', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[5, 7]]', direct_drive=False, fuel_gauge=True, max_fuel=50,
                    model_solution='[10, 11, 21]', origin='{"coordinate":[0, 5], "direction":"E"}',
                    path='[{"coordinate":[0,5],"connectedNodes":[1]},{"coordinate":[1,5],"connectedNodes":[0,2]},{"coordinate":[1,4],"connectedNodes":[1,3]},{"coordinate":[2,4],"connectedNodes":[2,4]},{"coordinate":[2,3],"connectedNodes":[5,3]},{"coordinate":[1,3],"connectedNodes":[4,6]},{"coordinate":[1,2],"connectedNodes":[5,7,8]},{"coordinate":[2,2],"connectedNodes":[6,9]},{"coordinate":[1,1],"connectedNodes":[6,9]},{"coordinate":[2,1],"connectedNodes":[8,7,10]},{"coordinate":[2,0],"connectedNodes":[9,11]},{"coordinate":[3,0],"connectedNodes":[10,12]},{"coordinate":[4,0],"connectedNodes":[11,13]},{"coordinate":[4,1],"connectedNodes":[14,12]},{"coordinate":[3,1],"connectedNodes":[15,13]},{"coordinate":[3,2],"connectedNodes":[16,14]},{"coordinate":[3,3],"connectedNodes":[17,15]},{"coordinate":[4,3],"connectedNodes":[16,18]},{"coordinate":[5,3],"connectedNodes":[17,19,28,20]},{"coordinate":[5,4],"connectedNodes":[29,18]},{"coordinate":[5,2],"connectedNodes":[18,21]},{"coordinate":[5,1],"connectedNodes":[20,22]},{"coordinate":[5,0],"connectedNodes":[21,23]},{"coordinate":[6,0],"connectedNodes":[22,24]},{"coordinate":[7,0],"connectedNodes":[23,25]},{"coordinate":[7,1],"connectedNodes":[26,24]},{"coordinate":[7,2],"connectedNodes":[27,25]},{"coordinate":[7,3],"connectedNodes":[28,26]},{"coordinate":[6,3],"connectedNodes":[18,27]},{"coordinate":[5,5],"connectedNodes":[30,40,19]},{"coordinate":[4,5],"connectedNodes":[31,29]},{"coordinate":[3,5],"connectedNodes":[32,30]},{"coordinate":[3,6],"connectedNodes":[33,31]},{"coordinate":[3,7],"connectedNodes":[41,34,32]},{"coordinate":[4,7],"connectedNodes":[33,35]},{"coordinate":[5,7],"connectedNodes":[34,36]},{"coordinate":[6,7],"connectedNodes":[35,37]},{"coordinate":[7,7],"connectedNodes":[36,38]},{"coordinate":[7,6],"connectedNodes":[37,39]},{"coordinate":[7,5],"connectedNodes":[40,38]},{"coordinate":[6,5],"connectedNodes":[29,39]},{"coordinate":[2,7],"connectedNodes":[42,33]},{"coordinate":[1,7],"connectedNodes":[41]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level44 = Level(name='44', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[6, 3]]', direct_drive=False, fuel_gauge=True, max_fuel=50,
                    model_solution='[5, 6]', origin='{"coordinate":[0, 3], "direction":"E"}',
                    path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[2,3],"connectedNodes":[1,3]},{"coordinate":[3,3],"connectedNodes":[2,4]},{"coordinate":[4,3],"connectedNodes":[3,5]},{"coordinate":[5,3],"connectedNodes":[4,6]},{"coordinate":[6,3],"connectedNodes":[5]}]',
                    pythonEnabled=False, theme=grass, threads=1,
                    traffic_lights='[{"direction":"E", "startTime":0, "sourceCoordinate":{"y":3, "x":3}, "greenDuration":2, "startingState":"RED", "redDuration":4}]')

    level45 = Level(name='45', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[0, 3]]', direct_drive=False, fuel_gauge=True, max_fuel=50,
                    model_solution='[6, 7]', origin='{"coordinate":[7, 3], "direction":"W"}',
                    path='[{"coordinate":[7,3],"connectedNodes":[6]},{"coordinate":[1,3],"connectedNodes":[7,2]},{"coordinate":[2,3],"connectedNodes":[1,3]},{"coordinate":[3,3],"connectedNodes":[2,4]},{"coordinate":[4,3],"connectedNodes":[3,5]},{"coordinate":[5,3],"connectedNodes":[4,6]},{"coordinate":[6,3],"connectedNodes":[5,0]},{"coordinate":[0,3],"connectedNodes":[1]}] ',
                    pythonEnabled=False, theme=grass, threads=1,
                    traffic_lights='[{"direction":"W", "startTime":0, "sourceCoordinate":{"y":3, "x":4}, "greenDuration":1, "startingState":"GREEN", "redDuration":4},{"direction":"W", "startTime":0, "sourceCoordinate":{"y":3, "x":5}, "greenDuration":1, "startingState":"RED", "redDuration":3}]')

    level46 = Level(name='46', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[2, 6]]', direct_drive=False, fuel_gauge=True, max_fuel=50,
                    model_solution='[8, 9]', origin='{"coordinate":[6, 5], "direction":"S"}',
                    path='[{"coordinate":[6,5],"connectedNodes":[1]},{"coordinate":[6,4],"connectedNodes":[0,2]},{"coordinate":[6,3],"connectedNodes":[3,1]},{"coordinate":[5,3],"connectedNodes":[4,2]},{"coordinate":[4,3],"connectedNodes":[5,3]},{"coordinate":[3,3],"connectedNodes":[6,4]},{"coordinate":[2,3],"connectedNodes":[7,5]},{"coordinate":[2,4],"connectedNodes":[8,6]},{"coordinate":[2,5],"connectedNodes":[9,7]},{"coordinate":[2,6],"connectedNodes":[8]}]',
                    pythonEnabled=False, theme=grass, threads=1,
                    traffic_lights='[{"direction":"W", "startTime":0, "sourceCoordinate":{"y":3, "x":5}, "greenDuration":2, "startingState":"RED", "redDuration":4}]')

    level47 = Level(name='47', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[4, 3]]', direct_drive=False, fuel_gauge=True, max_fuel=50,
                    model_solution='[8, 9]', origin='{"coordinate":[6, 1], "direction":"N"}',
                    path='[{"coordinate":[6,1],"connectedNodes":[1]},{"coordinate":[6,2],"connectedNodes":[2,0]},{"coordinate":[6,3],"connectedNodes":[3,1]},{"coordinate":[6,4],"connectedNodes":[4,2]},{"coordinate":[6,5],"connectedNodes":[5,3]},{"coordinate":[6,6],"connectedNodes":[6,4]},{"coordinate":[5,6],"connectedNodes":[7,5]},{"coordinate":[4,6],"connectedNodes":[8,6]},{"coordinate":[3,6],"connectedNodes":[9,7]},{"coordinate":[2,6],"connectedNodes":[8,10]},{"coordinate":[2,5],"connectedNodes":[9,11]},{"coordinate":[2,4],"connectedNodes":[10,12]},{"coordinate":[2,3],"connectedNodes":[11,13]},{"coordinate":[2,2],"connectedNodes":[12,14]},{"coordinate":[3,2],"connectedNodes":[13,15]},{"coordinate":[4,2],"connectedNodes":[14,16]},{"coordinate":[4,3],"connectedNodes":[15]}]',
                    pythonEnabled=False, theme=grass, threads=1,
                    traffic_lights='[{"direction": "N", "startTime": 0, "sourceCoordinate": {"y":3, "x": 6}, "greenDuration": 3, "startingState": "RED", "redDuration": 3}, {"direction":"W", "startTime": 0, "sourceCoordinate": {"y": 6, "x": 5}, "greenDuration":3, "startingState": "RED", "redDuration": 3}, {"direction": "S", "startTime":0, "sourceCoordinate": {"y": 5, "x": 2}, "greenDuration": 3, "startingState":"RED", "redDuration": 3}, {"direction": "E", "startTime": 0, "sourceCoordinate":{"y": 2, "x": 3}, "greenDuration": 3, "startingState": "GREEN", "redDuration":3}]')

    level48 = Level(name='48', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[1, 2]]', direct_drive=False, fuel_gauge=True, max_fuel=50,
                    model_solution='[12, 13]', origin='{"coordinate":[1, 5], "direction":"E"}',
                    path='[{"coordinate":[1,5],"connectedNodes":[1]},{"coordinate":[2,5],"connectedNodes":[0,2]},{"coordinate":[3,5],"connectedNodes":[1,3]},{"coordinate":[4,5],"connectedNodes":[2,4,6,5]},{"coordinate":[4,6],"connectedNodes":[7,3]},{"coordinate":[4,4],"connectedNodes":[3,10]},{"coordinate":[5,5],"connectedNodes":[3,17]},{"coordinate":[4,7],"connectedNodes":[8,4]},{"coordinate":[5,7],"connectedNodes":[7,9]},{"coordinate":[6,7],"connectedNodes":[8]},{"coordinate":[4,3],"connectedNodes":[5,11]},{"coordinate":[4,2],"connectedNodes":[14,10,12]},{"coordinate":[5,2],"connectedNodes":[11,13]},{"coordinate":[6,2],"connectedNodes":[12]},{"coordinate":[3,2],"connectedNodes":[15,11]},{"coordinate":[2,2],"connectedNodes":[16,14]},{"coordinate":[1,2],"connectedNodes":[15]},{"coordinate":[6,5],"connectedNodes":[6,18]},{"coordinate":[7,5],"connectedNodes":[17,19]},{"coordinate":[7,4],"connectedNodes":[18]}]',
                    pythonEnabled=False, theme=grass, threads=1,
                    traffic_lights='[{"direction": "E", "startTime": 0, "sourceCoordinate": {"y":5, "x": 3}, "greenDuration": 2, "startingState": "RED", "redDuration": 4}, {"direction":"S", "startTime": 0, "sourceCoordinate": {"y": 6, "x": 4}, "greenDuration":4, "startingState": "GREEN", "redDuration": 2}, {"direction": "N", "startTime":0, "sourceCoordinate": {"y": 4, "x": 4}, "greenDuration": 4, "startingState":"GREEN", "redDuration": 2}, {"direction": "W", "startTime": 0, "sourceCoordinate":{"y": 5, "x": 5}, "greenDuration": 2, "startingState": "RED", "redDuration":4}]')

    level49 = Level(name='49', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[9, 6]]', direct_drive=False, fuel_gauge=True, max_fuel=50,
                    model_solution='[12, 13, 17]', origin='{"coordinate":[3, 6], "direction":"S"}',
                    path='[{"coordinate":[3,6],"connectedNodes":[1]},{"coordinate":[3,5],"connectedNodes":[0,2]},{"coordinate":[3,4],"connectedNodes":[3,1,4,5]},{"coordinate":[2,4],"connectedNodes":[19,2]},{"coordinate":[4,4],"connectedNodes":[2,6]},{"coordinate":[3,3],"connectedNodes":[2,16]},{"coordinate":[5,4],"connectedNodes":[4,7]},{"coordinate":[6,4],"connectedNodes":[6,8]},{"coordinate":[7,4],"connectedNodes":[7,9,13]},{"coordinate":[7,5],"connectedNodes":[10,8]},{"coordinate":[7,6],"connectedNodes":[11,9]},{"coordinate":[8,6],"connectedNodes":[10,12]},{"coordinate":[9,6],"connectedNodes":[11]},{"coordinate":[7,3],"connectedNodes":[8,14]},{"coordinate":[7,2],"connectedNodes":[13,15]},{"coordinate":[8,2],"connectedNodes":[14]},{"coordinate":[3,2],"connectedNodes":[17,5]},{"coordinate":[2,2],"connectedNodes":[18,16]},{"coordinate":[1,2],"connectedNodes":[21,20,17]},{"coordinate":[1,4],"connectedNodes":[3,20]},{"coordinate":[1,3],"connectedNodes":[19,18]},{"coordinate":[0,2],"connectedNodes":[18,22]},{"coordinate":[0,1],"connectedNodes":[21]}]',
                    pythonEnabled=False, theme=city, threads=1,
                    traffic_lights='[{"direction": "S", "startTime": 0, "sourceCoordinate": {"y":5, "x": 3}, "greenDuration": 2, "startingState": "RED", "redDuration": 4}, {"direction":"E", "startTime": 0, "sourceCoordinate": {"y": 4, "x": 2}, "greenDuration":2, "startingState": "GREEN", "redDuration": 4}, {"direction": "W", "startTime":0, "sourceCoordinate": {"y": 4, "x": 4}, "greenDuration": 2, "startingState":"GREEN", "redDuration": 4}, {"direction": "N", "startTime": 0, "sourceCoordinate":{"y": 3, "x": 3}, "greenDuration": 2, "startingState": "RED", "redDuration":4}, {"direction": "S", "startTime": 0, "sourceCoordinate": {"y": 5, "x": 7},"greenDuration": 4, "startingState": "GREEN", "redDuration": 2}, {"direction":"N", "startTime": 0, "sourceCoordinate": {"y": 3, "x": 7}, "greenDuration":4, "startingState": "GREEN", "redDuration": 2}, {"direction": "E", "startTime":0, "sourceCoordinate": {"y": 4, "x": 6}, "greenDuration": 2, "startingState":"RED", "redDuration": 4}]')

    level50 = Level(name='50', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[6, 4]]', direct_drive=False, fuel_gauge=True, max_fuel=50,
                    model_solution='[16]', origin='{"coordinate":[0, 3], "direction":"E"}',
                    path='[{"coordinate":[0,3],"connectedNodes":[1]}, {"coordinate":[1,3],"connectedNodes":[0,27,2]},{"coordinate":[1,2],"connectedNodes":[1,3]}, {"coordinate":[1,1],"connectedNodes":[2,4]},{"coordinate":[2,1],"connectedNodes":[3,6,5]}, {"coordinate":[2,0],"connectedNodes":[4]},{"coordinate":[3,1],"connectedNodes":[4,7]}, {"coordinate":[4,1],"connectedNodes":[6,8]},{"coordinate":[4,2],"connectedNodes":[9,11,7]}, {"coordinate":[4,3],"connectedNodes":[10,36,8]},{"coordinate":[3,3],"connectedNodes":[9]}, {"coordinate":[5,2],"connectedNodes":[8,12]},{"coordinate":[6,2],"connectedNodes":[11,15,13]}, {"coordinate":[6,1],"connectedNodes":[12,14]},{"coordinate":[6,0],"connectedNodes":[13]}, {"coordinate":[7,2],"connectedNodes":[12,16]},{"coordinate":[8,2],"connectedNodes":[15,25,17]}, {"coordinate":[8,1],"connectedNodes":[16,18]},{"coordinate":[8,0],"connectedNodes":[17,19]}, {"coordinate":[9,0],"connectedNodes":[18,20]},{"coordinate":[9,1],"connectedNodes":[21,19]}, {"coordinate":[9,2],"connectedNodes":[22,20]},{"coordinate":[9,3],"connectedNodes":[23,21]}, {"coordinate":[9,4],"connectedNodes":[24,22]},{"coordinate":[8,4],"connectedNodes":[26,23,25]}, {"coordinate":[8,3],"connectedNodes":[24,16]},{"coordinate":[7,4],"connectedNodes":[42,28,24]}, {"coordinate":[1,4],"connectedNodes":[41,1]},{"coordinate":[7,5],"connectedNodes":[29,26]}, {"coordinate":[7,6],"connectedNodes":[32,30,28]},{"coordinate":[8,6],"connectedNodes":[29,31]}, {"coordinate":[9,6],"connectedNodes":[30]},{"coordinate":[6,6],"connectedNodes":[33,29]}, {"coordinate":[5,6],"connectedNodes":[34,32]},{"coordinate":[4,6],"connectedNodes":[33,35]}, {"coordinate":[4,5],"connectedNodes":[37,34,36]},{"coordinate":[4,4],"connectedNodes":[35,9]}, {"coordinate":[3,5],"connectedNodes":[38,35]},{"coordinate":[2,5],"connectedNodes":[39,37]}, {"coordinate":[2,6],"connectedNodes":[40,38]},{"coordinate":[1,6],"connectedNodes":[39,41]}, {"coordinate":[1,5],"connectedNodes":[40,27]},{"coordinate":[6,4],"connectedNodes":[26]} ]',
                    pythonEnabled=False, theme=city, threads=1,
                    traffic_lights='[{"direction": "E", "startTime": 0, "sourceCoordinate": {"y":1, "x": 1}, "greenDuration": 2, "startingState": "RED", "redDuration": 4}, {"direction":"N", "startTime": 2, "sourceCoordinate": {"y": 0, "x": 2}, "greenDuration":2, "startingState": "RED", "redDuration": 4}, {"direction": "W", "startTime":0, "sourceCoordinate": {"y": 1, "x": 3}, "greenDuration": 2, "startingState":"GREEN", "redDuration": 4}, {"direction": "N", "startTime": 0, "sourceCoordinate":{"y": 1, "x": 4}, "greenDuration": 2, "startingState": "RED", "redDuration":4}, {"direction": "S", "startTime": 2, "sourceCoordinate": {"y": 3, "x": 4},"greenDuration": 2, "startingState": "RED", "redDuration": 4}, {"direction":"W", "startTime": 0, "sourceCoordinate": {"y": 2, "x": 5}, "greenDuration":2, "startingState": "GREEN", "redDuration": 4}, {"direction": "E", "startTime":0, "sourceCoordinate": {"y": 5, "x": 3}, "greenDuration": 2, "startingState":"RED", "redDuration": 4}, {"direction": "S", "startTime": 2, "sourceCoordinate":{"y": 6, "x": 4}, "greenDuration": 2, "startingState": "RED", "redDuration":4}, {"direction": "N", "startTime": 0, "sourceCoordinate": {"y": 4, "x": 4},"greenDuration": 2, "startingState": "GREEN", "redDuration": 4}, {"direction":"W", "startTime": 0, "sourceCoordinate": {"y": 6, "x": 2}, "greenDuration":4, "startingState": "RED", "redDuration": 2}, {"direction": "W", "startTime":0, "sourceCoordinate": {"y": 4, "x": 9}, "greenDuration": 2, "startingState":"RED", "redDuration": 4}, {"direction": "N", "startTime": 2, "sourceCoordinate":{"y": 3, "x": 8}, "greenDuration": 2, "startingState": "RED", "redDuration":4}, {"direction": "E", "startTime": 0, "sourceCoordinate": {"y": 4, "x": 7},"greenDuration": 2, "startingState": "GREEN", "redDuration": 4}]')

    level1.save()
    level2.save()
    level3.save()
    level4.save()
    level5.save()
    level6.save()
    level7.save()
    level8.save()
    level9.save()
    level10.save()
    level11.save()
    level12.save()
    level13.save()
    level14.save()
    level15.save()
    level16.save()
    level17.save()
    level18.save()
    level19.save()
    level20.save()
    level21.save()
    level22.save()
    level23.save()
    level24.save()
    level25.save()
    level26.save()
    level27.save()
    level28.save()
    level29.save()
    level30.save()
    level31.save()
    level32.save()
    level33.save()
    level34.save()
    level35.save()
    level36.save()
    level37.save()
    level38.save()
    level39.save()
    level40.save()
    level41.save()
    level42.save()
    level43.save()
    level44.save()
    level45.save()
    level46.save()
    level47.save()
    level48.save()
    level49.save()
    level50.save()

    level1.next_level = level2
    level2.next_level = level3
    level3.next_level = level4
    level4.next_level = level5
    level5.next_level = level6
    level6.next_level = level7
    level7.next_level = level8
    level8.next_level = level9
    level9.next_level = level10
    level10.next_level = level11
    level11.next_level = level12

    level13.next_level = level14
    level14.next_level = level15
    level15.next_level = level16
    level16.next_level = level17
    level17.next_level = level18

    level19.next_level = level20
    level20.next_level = level21
    level21.next_level = level22
    level22.next_level = level23
    level23.next_level = level24
    level24.next_level = level25
    level25.next_level = level26
    level26.next_level = level27
    level27.next_level = level28

    level29.next_level = level30
    level30.next_level = level31
    level31.next_level = level32

    level33.next_level = level34
    level34.next_level = level35
    level35.next_level = level36
    level36.next_level = level37
    level37.next_level = level38
    level38.next_level = level39
    level39.next_level = level40
    level40.next_level = level41
    level41.next_level = level42
    level42.next_level = level43

    level44.next_level = level45
    level45.next_level = level46
    level46.next_level = level47
    level47.next_level = level48
    level48.next_level = level49
    level49.next_level = level50

    level1.save()
    level2.save()
    level3.save()
    level4.save()
    level5.save()
    level6.save()
    level7.save()
    level8.save()
    level9.save()
    level10.save()
    level11.save()
    level12.save()
    level13.save()
    level14.save()
    level15.save()
    level16.save()
    level17.save()
    level18.save()
    level19.save()
    level20.save()
    level21.save()
    level22.save()
    level23.save()
    level24.save()
    level25.save()
    level26.save()
    level27.save()
    level28.save()
    level29.save()
    level30.save()
    level31.save()
    level32.save()
    level33.save()
    level34.save()
    level35.save()
    level36.save()
    level37.save()
    level38.save()
    level39.save()
    level40.save()
    level41.save()
    level42.save()
    level43.save()
    level44.save()
    level45.save()
    level46.save()
    level47.save()
    level48.save()
    level49.save()
    level50.save()


def setup_blocks(apps, schema_editor):
    def add_levelBlock(level, blocks):
        for block in blocks:
            newBlock = LevelBlock(type=block, number=None, level=level)
            newBlock.save()

    def add_levelBlocks_to_levels_in_range(start, end, block_types):
        blocks = Block.objects.filter(type__in=block_types)
        if not blocks:
            raise LookupError

        levels = Level.objects.filter(pk__in=range(start,end))
        if not levels:
            raise LookupError

        for level in levels:
            add_levelBlock(level, blocks)

    def blocks_by_type(block_types):
        return Block.objects.filter(type__in=block_types)

    Level = apps.get_model('game', 'Level')
    Block = apps.get_model('game', 'Block')
    LevelBlock = apps.get_model('game', 'LevelBlock')

    add_levelBlocks_to_levels_in_range(1, 3, ["move_forwards"])

    level3 = Level.objects.get(pk=3)
    add_levelBlock(level3, blocks_by_type(["turn_right", "move_forwards"]))

    level4 = Level.objects.get(pk=4)
    add_levelBlock(level4, blocks_by_type(["turn_left", "move_forwards"]))

    add_levelBlocks_to_levels_in_range(5, 15, ["turn_right", "turn_left", "move_forwards"])

    add_levelBlocks_to_levels_in_range(15, 19, ["turn_right", "turn_left", "move_forwards", "deliver"])

    add_levelBlocks_to_levels_in_range(19, 29, ["turn_right", "turn_left", "move_forwards",
                                                "controls_repeat"])

    add_levelBlocks_to_levels_in_range(29, 33, ["turn_right", "turn_left", "move_forwards",
                                                "controls_repeat_until", "at_destination"])

    add_levelBlocks_to_levels_in_range(33, 39, ["turn_right", "turn_left", "move_forwards",
                                                "controls_repeat_until", "at_destination",
                                                "road_exists", "controls_if"])

    add_levelBlocks_to_levels_in_range(39, 44, ["turn_left", "turn_right", "move_forwards",
                                                "turn_around", "controls_repeat_until",
                                                "at_destination", "controls_if", "road_exists",
                                                "at_destination", "controls_repeat", "dead_end"])

    add_levelBlocks_to_levels_in_range(44, 46, ["move_forwards", "controls_repeat_until",
                                                "at_destination", "controls_if", "road_exists",
                                                "controls_repeat", "controls_repeat_while",
                                                "wait", "traffic_light"])


    level46 = Level.objects.get(pk=46)
    add_levelBlock(level46, blocks_by_type(["move_forwards", "turn_right", "controls_repeat_until",
                                            "at_destination", "controls_if", "road_exists",
                                            "controls_repeat", "controls_repeat_while",
                                            "wait", "traffic_light"]))

    level47 = Level.objects.get(pk=47)
    add_levelBlock(level47, blocks_by_type(["move_forwards", "turn_right", "turn_left",
                                            "controls_repeat_until", "at_destination",
                                            "controls_if", "road_exists", "controls_repeat",
                                            "controls_repeat_while", "wait", "traffic_light"]))


    add_levelBlocks_to_levels_in_range(48, 51, ["turn_left", "turn_right", "move_forwards",
                                                "controls_repeat_until", "at_destination",
                                                "controls_if", "road_exists", "at_destination",
                                                "controls_repeat", "dead_end", "controls_repeat_while",
                                                "wait", "traffic_light", "turn_around"])


def add_episodes_1_to_6(apps, schema_editor):

    Level = apps.get_model('game', 'Level')
    Episode = apps.get_model('game', 'Episode')
    Block = apps.get_model('game', 'Block')

    level1 = Level.objects.get(pk=1)

    episode1 = Episode(pk=1, name="Getting Started", first_level=level1, r_branchiness=0,
                       r_loopiness=0, r_num_tiles=10, r_curviness=0.5, r_pythonEnabled=0,
                       r_blocklyEnabled=1, r_trafficLights=0)
    episode1.save()

    level13 = Level.objects.get(pk=13)

    episode2 = Episode(pk=2, name="Shortest Route", first_level=level13, r_branchiness=0.3,
                       r_loopiness=0.05, r_num_tiles=20, r_curviness=0.15, r_pythonEnabled=0,
                       r_blocklyEnabled=1, r_trafficLights=0)
    episode2.save()

    level19 = Level.objects.get(pk=19)

    episode3 = Episode(pk=3, name="Loops and Repetitions", first_level=level19, r_branchiness=0,
                       r_loopiness=0, r_num_tiles=15, r_curviness=0.2, r_pythonEnabled=0,
                       r_blocklyEnabled=1, r_trafficLights=0)
    episode3.save()

    level29 = Level.objects.get(pk=29)

    episode4 = Episode(pk=4, name="Loops with Conditions", first_level=level29, r_branchiness=0,
                       r_loopiness=0, r_num_tiles=15, r_curviness=0.2, r_pythonEnabled=0,
                       r_blocklyEnabled=1, r_trafficLights=0)
    episode4.save()

    level33 = Level.objects.get(pk=33)

    episode5 = Episode(pk=5, name="If... Only", first_level=level33, r_branchiness=0.4,
                       r_loopiness=0.4, r_num_tiles=13, r_curviness=0.3, r_pythonEnabled=0,
                       r_blocklyEnabled=1, r_trafficLights=0)
    episode5.save()

    level44 = Level.objects.get(pk=44)

    episode6 = Episode(pk=6, name="Traffic Lights", first_level=level44, r_branchiness=0.5,
                       r_loopiness=0.1, r_num_tiles=35, r_curviness=0.2, r_pythonEnabled=0,
                       r_blocklyEnabled=1, r_trafficLights=1)
    episode6.save()


    episode1.r_blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards"])

    episode2.r_blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards",
                                                       "deliver"])

    episode3.r_blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards",
                                                       "controls_repeat"])

    episode4.r_blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards",
                                                       "controls_repeat_until", "at_destination",
                                                       "controls_repeat"])

    episode5.r_blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards",
                                                       "controls_repeat_until", "at_destination",
                                                       "controls_if", "road_exists", "dead_end",
                                                       "controls_repeat", "turn_around"])

    episode6.r_blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards",
                                                       "controls_repeat_until", "controls_if",
                                                       "road_exists", "at_destination", "wait",
                                                       "controls_repeat", "dead_end", "turn_around",
                                                       "controls_repeat_while", "traffic_light"])

    episode1.save()
    episode2.save()
    episode3.save()
    episode4.save()
    episode5.save()
    episode6.save()


def add_leveldecor(apps, schema_editor):

    Level = apps.get_model('game', 'Level')
    LevelDecor = apps.get_model('game', 'LevelDecor')

    level1 = Level.objects.get(pk=1)
    level2 = Level.objects.get(pk=2)
    level3 = Level.objects.get(pk=3)
    level4 = Level.objects.get(pk=4)
    level5 = Level.objects.get(pk=5)
    level6 = Level.objects.get(pk=6)
    level7 = Level.objects.get(pk=7)
    level8 = Level.objects.get(pk=8)
    level9 = Level.objects.get(pk=9)

    level10 = Level.objects.get(pk=10)
    level11 = Level.objects.get(pk=11)
    level12 = Level.objects.get(pk=12)
    level13 = Level.objects.get(pk=13)
    level14 = Level.objects.get(pk=14)
    level15 = Level.objects.get(pk=15)
    level16 = Level.objects.get(pk=16)
    level17 = Level.objects.get(pk=17)
    level18 = Level.objects.get(pk=18)
    level19 = Level.objects.get(pk=19)

    level20 = Level.objects.get(pk=20)
    level21 = Level.objects.get(pk=21)
    level22 = Level.objects.get(pk=22)
    level23 = Level.objects.get(pk=23)
    level24 = Level.objects.get(pk=24)
    level25 = Level.objects.get(pk=25)
    level26 = Level.objects.get(pk=26)
    level27 = Level.objects.get(pk=27)
    level28 = Level.objects.get(pk=28)
    level29 = Level.objects.get(pk=29)

    level30 = Level.objects.get(pk=30)
    level31 = Level.objects.get(pk=31)
    level32 = Level.objects.get(pk=32)
    level33 = Level.objects.get(pk=33)
    level34 = Level.objects.get(pk=34)
    level35 = Level.objects.get(pk=35)
    level36 = Level.objects.get(pk=36)
    level37 = Level.objects.get(pk=37)
    level38 = Level.objects.get(pk=38)
    level39 = Level.objects.get(pk=39)

    level40 = Level.objects.get(pk=40)
    level41 = Level.objects.get(pk=41)
    level42 = Level.objects.get(pk=42)
    level43 = Level.objects.get(pk=43)
    level44 = Level.objects.get(pk=44)
    level45 = Level.objects.get(pk=45)
    level46 = Level.objects.get(pk=46)
    level47 = Level.objects.get(pk=47)
    level48 = Level.objects.get(pk=48)
    level49 = Level.objects.get(pk=49)

    level50 = Level.objects.get(pk=50)


    LevelDecor.objects.bulk_create([
        LevelDecor(decorName='tree1', level=level1, x=100, y=100),
        LevelDecor(decorName='tree2', level=level2, x=67, y=570),
        LevelDecor(decorName='tree1', level=level2, x=663, y=443),
        LevelDecor(decorName='bush', level=level2, x=192, y=58),
        LevelDecor(decorName='tree2', level=level3, x=0, y=398),
        LevelDecor(decorName='tree2', level=level3, x=100, y=397),
        LevelDecor(decorName='tree2', level=level3, x=201, y=397),
        LevelDecor(decorName='tree2', level=level3, x=300, y=404),
        LevelDecor(decorName='tree2', level=level3, x=401, y=409),
        LevelDecor(decorName='tree2', level=level3, x=499, y=398),
        LevelDecor(decorName='tree2', level=level3, x=601, y=403),
        LevelDecor(decorName='tree2', level=level3, x=704, y=402),
        LevelDecor(decorName='tree2', level=level3, x=804, y=398),
        LevelDecor(decorName='tree2', level=level3, x=903, y=401),
        LevelDecor(decorName='tree2', level=level4, x=531, y=624),
        LevelDecor(decorName='tree1', level=level4, x=442, y=632),
        LevelDecor(decorName='tree2', level=level4, x=531, y=498),
        LevelDecor(decorName='tree1', level=level4, x=495, y=564),
        LevelDecor(decorName='tree1', level=level4, x=584, y=565),
        LevelDecor(decorName='tree1', level=level4, x=615, y=630),
        LevelDecor(decorName='tree2', level=level4, x=669, y=565),
        LevelDecor(decorName='tree1', level=level4, x=621, y=497),
        LevelDecor(decorName='tree1', level=level4, x=500, y=694),
        LevelDecor(decorName='tree1', level=level4, x=300, y=633),
        LevelDecor(decorName='tree2', level=level4, x=380, y=704),
        LevelDecor(decorName='tree1', level=level4, x=365, y=596),
        LevelDecor(decorName='tree1', level=level4, x=287, y=713),
        LevelDecor(decorName='tree1', level=level4, x=596, y=714),
        LevelDecor(decorName='bush', level=level4, x=711, y=704),
        LevelDecor(decorName='bush', level=level4, x=813, y=702),
        LevelDecor(decorName='bush', level=level4, x=906, y=700),
        LevelDecor(decorName='bush', level=level4, x=897, y=607),
        LevelDecor(decorName='bush', level=level4, x=807, y=608),
        LevelDecor(decorName='tree2', level=level4, x=719, y=636),
        LevelDecor(decorName='tree2', level=level4, x=857, y=659),
        LevelDecor(decorName='tree1', level=level4, x=766, y=701),
        LevelDecor(decorName='tree2', level=level4, x=665, y=694),
        LevelDecor(decorName='tree1', level=level4, x=851, y=568),
        LevelDecor(decorName='tree2', level=level4, x=766, y=555),
        LevelDecor(decorName='tree1', level=level4, x=155, y=680),
        LevelDecor(decorName='tree1', level=level4, x=216, y=541),
        LevelDecor(decorName='tree1', level=level4, x=530, y=402),
        LevelDecor(decorName='tree1', level=level5, x=19, y=459),
        LevelDecor(decorName='tree1', level=level5, x=135, y=564),
        LevelDecor(decorName='tree1', level=level5, x=240, y=666),
        LevelDecor(decorName='tree1', level=level5, x=52, y=184),
        LevelDecor(decorName='tree1', level=level5, x=208, y=291),
        LevelDecor(decorName='tree1', level=level5, x=338, y=410),
        LevelDecor(decorName='tree1', level=level5, x=497, y=519),
        LevelDecor(decorName='tree1', level=level5, x=467, y=701),
        LevelDecor(decorName='bush', level=level5, x=898, y=26),
        LevelDecor(decorName='bush', level=level5, x=755, y=22),
        LevelDecor(decorName='bush', level=level5, x=901, y=168),
        LevelDecor(decorName='bush', level=level5, x=900, y=322),
        LevelDecor(decorName='bush', level=level5, x=607, y=22),
        LevelDecor(decorName='bush', level=level5, x=893, y=638),
        LevelDecor(decorName='bush', level=level5, x=899, y=479),
        LevelDecor(decorName='bush', level=level5, x=445, y=23),
        LevelDecor(decorName='bush', level=level5, x=293, y=23),
        LevelDecor(decorName='bush', level=level5, x=126, y=23),
        LevelDecor(decorName='tree2', level=level6, x=224, y=654),
        LevelDecor(decorName='tree2', level=level6, x=87, y=656),
        LevelDecor(decorName='tree1', level=level6, x=63, y=591),
        LevelDecor(decorName='tree2', level=level6, x=163, y=562),
        LevelDecor(decorName='tree2', level=level6, x=100, y=506),
        LevelDecor(decorName='tree1', level=level6, x=153, y=624),
        LevelDecor(decorName='tree2', level=level6, x=608, y=480),
        LevelDecor(decorName='tree1', level=level6, x=584, y=366),
        LevelDecor(decorName='tree2', level=level6, x=591, y=220),
        LevelDecor(decorName='tree1', level=level6, x=676, y=254),
        LevelDecor(decorName='tree1', level=level6, x=689, y=351),
        LevelDecor(decorName='tree2', level=level6, x=673, y=509),
        LevelDecor(decorName='tree1', level=level6, x=557, y=574),
        LevelDecor(decorName='bush', level=level6, x=104, y=200),
        LevelDecor(decorName='bush', level=level6, x=301, y=199),
        LevelDecor(decorName='bush', level=level6, x=201, y=201),
        LevelDecor(decorName='bush', level=level6, x=102, y=102),
        LevelDecor(decorName='bush', level=level6, x=201, y=102),
        LevelDecor(decorName='bush', level=level6, x=301, y=103),
        LevelDecor(decorName='tree1', level=level6, x=147, y=197),
        LevelDecor(decorName='tree1', level=level6, x=240, y=127),
        LevelDecor(decorName='tree2', level=level6, x=154, y=121),
        LevelDecor(decorName='tree2', level=level6, x=262, y=215),
        LevelDecor(decorName='tree1', level=level6, x=328, y=155),
        LevelDecor(decorName='tree1', level=level6, x=147, y=715),
        LevelDecor(decorName='tree1', level=level6, x=65, y=144),
        LevelDecor(decorName='tree1', level=level6, x=78, y=220),
        LevelDecor(decorName='tree2', level=level6, x=262, y=70),
        LevelDecor(decorName='tree2', level=level6, x=371, y=85),
        LevelDecor(decorName='tree2', level=level6, x=64, y=63),
        LevelDecor(decorName='tree2', level=level7, x=6, y=424),
        LevelDecor(decorName='tree2', level=level7, x=5, y=559),
        LevelDecor(decorName='tree2', level=level7, x=5, y=688),
        LevelDecor(decorName='tree1', level=level7, x=676, y=644),
        LevelDecor(decorName='tree2', level=level7, x=588, y=633),
        LevelDecor(decorName='bush', level=level7, x=686, y=578),
        LevelDecor(decorName='bush', level=level7, x=766, y=659),
        LevelDecor(decorName='bush', level=level7, x=625, y=669),
        LevelDecor(decorName='tree2', level=level7, x=801, y=696),
        LevelDecor(decorName='bush', level=level7, x=610, y=576),
        LevelDecor(decorName='tree1', level=level7, x=583, y=524),
        LevelDecor(decorName='tree1', level=level7, x=762, y=584),
        LevelDecor(decorName='tree1', level=level7, x=682, y=511),
        LevelDecor(decorName='tree2', level=level7, x=699, y=716),
        LevelDecor(decorName='tree2', level=level9, x=167, y=207),
        LevelDecor(decorName='tree2', level=level9, x=263, y=203),
        LevelDecor(decorName='tree2', level=level9, x=364, y=202),
        LevelDecor(decorName='tree2', level=level9, x=571, y=203),
        LevelDecor(decorName='tree2', level=level9, x=465, y=199),
        LevelDecor(decorName='tree1', level=level9, x=29, y=433),
        LevelDecor(decorName='bush', level=level9, x=505, y=652),
        LevelDecor(decorName='tree2', level=level10, x=99, y=699),
        LevelDecor(decorName='tree2', level=level10, x=201, y=700),
        LevelDecor(decorName='tree2', level=level10, x=54, y=634),
        LevelDecor(decorName='tree2', level=level10, x=143, y=632),
        LevelDecor(decorName='tree2', level=level10, x=298, y=697),
        LevelDecor(decorName='tree2', level=level10, x=94, y=555),
        LevelDecor(decorName='tree1', level=level10, x=504, y=389),
        LevelDecor(decorName='tree2', level=level10, x=17, y=503),
        LevelDecor(decorName='tree1', level=level10, x=484, y=604),
        LevelDecor(decorName='tree1', level=level10, x=582, y=600),
        LevelDecor(decorName='tree1', level=level10, x=599, y=413),
        LevelDecor(decorName='bush', level=level10, x=606, y=501),
        LevelDecor(decorName='tree1', level=level11, x=396, y=304),
        LevelDecor(decorName='tree1', level=level11, x=600, y=302),
        LevelDecor(decorName='tree1', level=level11, x=242, y=301),
        LevelDecor(decorName='bush', level=level11, x=601, y=434),
        LevelDecor(decorName='bush', level=level11, x=599, y=701),
        LevelDecor(decorName='bush', level=level11, x=598, y=580),
        LevelDecor(decorName='tree2', level=level11, x=0, y=700),
        LevelDecor(decorName='tree2', level=level11, x=116, y=701),
        LevelDecor(decorName='tree2', level=level11, x=236, y=698),
        LevelDecor(decorName='tree2', level=level11, x=359, y=697),
        LevelDecor(decorName='tree2', level=level11, x=480, y=698),
        LevelDecor(decorName='tree1', level=level12, x=331, y=509),
        LevelDecor(decorName='tree1', level=level12, x=267, y=489),
        LevelDecor(decorName='tree1', level=level12, x=284, y=561),
        LevelDecor(decorName='tree1', level=level12, x=402, y=479),
        LevelDecor(decorName='tree1', level=level12, x=452, y=532),
        LevelDecor(decorName='tree1', level=level12, x=418, y=583),
        LevelDecor(decorName='tree1', level=level12, x=376, y=545),
        LevelDecor(decorName='tree1', level=level12, x=356, y=606),
        LevelDecor(decorName='tree2', level=level12, x=164, y=86),
        LevelDecor(decorName='tree2', level=level12, x=202, y=4),
        LevelDecor(decorName='tree2', level=level12, x=73, y=109),
        LevelDecor(decorName='tree2', level=level12, x=63, y=18),
        LevelDecor(decorName='tree2', level=level12, x=119, y=2),
        LevelDecor(decorName='tree2', level=level12, x=323, y=40),
        LevelDecor(decorName='tree2', level=level12, x=565, y=81),
        LevelDecor(decorName='tree2', level=level12, x=493, y=148),
        LevelDecor(decorName='tree2', level=level12, x=417, y=72),
        LevelDecor(decorName='tree2', level=level12, x=549, y=7),
        LevelDecor(decorName='tree2', level=level12, x=265, y=120),
        LevelDecor(decorName='tree1', level=level13, x=48, y=658),
        LevelDecor(decorName='tree1', level=level13, x=49, y=553),
        LevelDecor(decorName='tree1', level=level13, x=48, y=446),
        LevelDecor(decorName='tree1', level=level13, x=50, y=340),
        LevelDecor(decorName='tree1', level=level13, x=52, y=235),
        LevelDecor(decorName='tree2', level=level13, x=406, y=512),
        LevelDecor(decorName='tree2', level=level13, x=496, y=492),
        LevelDecor(decorName='bush', level=level13, x=500, y=302),
        LevelDecor(decorName='bush', level=level13, x=501, y=245),
        LevelDecor(decorName='bush', level=level13, x=500, y=193),
        LevelDecor(decorName='tree2', level=level14, x=209, y=392),
        LevelDecor(decorName='tree2', level=level14, x=307, y=302),
        LevelDecor(decorName='tree2', level=level14, x=281, y=187),
        LevelDecor(decorName='bush', level=level14, x=498, y=197),
        LevelDecor(decorName='tree1', level=level14, x=771, y=662),
        LevelDecor(decorName='tree1', level=level14, x=866, y=557),
        LevelDecor(decorName='tree1', level=level14, x=754, y=491),
        LevelDecor(decorName='tree1', level=level14, x=890, y=310),
        LevelDecor(decorName='tree1', level=level14, x=725, y=353),
        LevelDecor(decorName='tree1', level=level14, x=780, y=87),
        LevelDecor(decorName='tree1', level=level14, x=862, y=177),
        LevelDecor(decorName='tree1', level=level15, x=406, y=205),
        LevelDecor(decorName='tree1', level=level15, x=296, y=296),
        LevelDecor(decorName='tree2', level=level15, x=98, y=661),
        LevelDecor(decorName='tree2', level=level15, x=93, y=592),
        LevelDecor(decorName='tree2', level=level15, x=15, y=608),
        LevelDecor(decorName='tree2', level=level15, x=46, y=697),
        LevelDecor(decorName='bush', level=level15, x=579, y=501),
        LevelDecor(decorName='bush', level=level16, x=188, y=399),
        LevelDecor(decorName='bush', level=level16, x=587, y=97),
        LevelDecor(decorName='tree2', level=level16, x=652, y=704),
        LevelDecor(decorName='tree2', level=level16, x=751, y=704),
        LevelDecor(decorName='tree2', level=level16, x=787, y=627),
        LevelDecor(decorName='tree2', level=level16, x=687, y=623),
        LevelDecor(decorName='tree2', level=level16, x=924, y=699),
        LevelDecor(decorName='tree2', level=level16, x=922, y=608),
        LevelDecor(decorName='tree2', level=level16, x=843, y=690),
        LevelDecor(decorName='tree2', level=level16, x=956, y=517),
        LevelDecor(decorName='tree2', level=level16, x=544, y=675),
        LevelDecor(decorName='tree2', level=level16, x=791, y=504),
        LevelDecor(decorName='tree2', level=level16, x=926, y=425),
        LevelDecor(decorName='tree2', level=level16, x=859, y=563),
        LevelDecor(decorName='bush', level=level17, x=380, y=523),
        LevelDecor(decorName='bush', level=level17, x=580, y=479),
        LevelDecor(decorName='tree1', level=level17, x=196, y=190),
        LevelDecor(decorName='tree1', level=level17, x=296, y=402),
        LevelDecor(decorName='tree2', level=level17, x=1, y=674),
        LevelDecor(decorName='tree1', level=level17, x=170, y=403),
        LevelDecor(decorName='tree1', level=level17, x=308, y=190),
        LevelDecor(decorName='bush', level=level18, x=875, y=86),
        LevelDecor(decorName='bush', level=level18, x=874, y=448),
        LevelDecor(decorName='bush', level=level18, x=775, y=688),
        LevelDecor(decorName='tree2', level=level18, x=119, y=512),
        LevelDecor(decorName='tree2', level=level18, x=93, y=397),
        LevelDecor(decorName='tree1', level=level18, x=296, y=289),
        LevelDecor(decorName='tree1', level=level18, x=487, y=203),
        LevelDecor(decorName='tree1', level=level18, x=231, y=189),
        LevelDecor(decorName='tree1', level=level18, x=73, y=172),
        LevelDecor(decorName='tree1', level=level18, x=604, y=300),
        LevelDecor(decorName='tree1', level=level18, x=672, y=194),
        LevelDecor(decorName='tree1', level=level18, x=516, y=286),
        LevelDecor(decorName='tree2', level=level18, x=587, y=211),
        LevelDecor(decorName='tree2', level=level18, x=700, y=283),
        LevelDecor(decorName='tree2', level=level19, x=393, y=539),
        LevelDecor(decorName='tree2', level=level19, x=271, y=613),
        LevelDecor(decorName='tree1', level=level19, x=340, y=648),
        LevelDecor(decorName='tree1', level=level19, x=77, y=639),
        LevelDecor(decorName='tree2', level=level19, x=147, y=624),
        LevelDecor(decorName='tree1', level=level19, x=227, y=682),
        LevelDecor(decorName='tree1', level=level19, x=228, y=532),
        LevelDecor(decorName='tree1', level=level19, x=80, y=518),
        LevelDecor(decorName='tree2', level=level19, x=327, y=437),
        LevelDecor(decorName='tree2', level=level19, x=622, y=187),
        LevelDecor(decorName='bush', level=level19, x=645, y=45),
        LevelDecor(decorName='tree1', level=level19, x=542, y=91),
        LevelDecor(decorName='tree2', level=level19, x=707, y=284),
        LevelDecor(decorName='tree1', level=level19, x=711, y=35),
        LevelDecor(decorName='tree1', level=level19, x=826, y=26),
        LevelDecor(decorName='bush', level=level19, x=782, y=107),
        LevelDecor(decorName='tree1', level=level19, x=748, y=135),
        LevelDecor(decorName='tree2', level=level19, x=848, y=138),
        LevelDecor(decorName='tree1', level=level19, x=334, y=94),
        LevelDecor(decorName='tree2', level=level20, x=676, y=311),
        LevelDecor(decorName='tree2', level=level20, x=700, y=145),
        LevelDecor(decorName='tree2', level=level20, x=527, y=190),
        LevelDecor(decorName='tree2', level=level20, x=829, y=471),
        LevelDecor(decorName='tree1', level=level20, x=782, y=188),
        LevelDecor(decorName='tree1', level=level20, x=650, y=466),
        LevelDecor(decorName='tree1', level=level20, x=622, y=235),
        LevelDecor(decorName='tree1', level=level20, x=758, y=318),
        LevelDecor(decorName='tree1', level=level20, x=856, y=269),
        LevelDecor(decorName='tree1', level=level20, x=831, y=386),
        LevelDecor(decorName='tree2', level=level20, x=153, y=669),
        LevelDecor(decorName='tree2', level=level20, x=4, y=548),
        LevelDecor(decorName='tree1', level=level20, x=86, y=565),
        LevelDecor(decorName='tree1', level=level20, x=64, y=665),
        LevelDecor(decorName='tree1', level=level20, x=393, y=109),
        LevelDecor(decorName='tree1', level=level20, x=424, y=352),
        LevelDecor(decorName='tree2', level=level20, x=595, y=86),
        LevelDecor(decorName='tree2', level=level20, x=755, y=407),
        LevelDecor(decorName='tree1', level=level21, x=294, y=412),
        LevelDecor(decorName='tree1', level=level21, x=200, y=525),
        LevelDecor(decorName='tree1', level=level21, x=389, y=515),
        LevelDecor(decorName='tree1', level=level21, x=162, y=688),
        LevelDecor(decorName='tree2', level=level21, x=209, y=610),
        LevelDecor(decorName='tree2', level=level21, x=296, y=513),
        LevelDecor(decorName='tree2', level=level21, x=26, y=19),
        LevelDecor(decorName='tree1', level=level21, x=148, y=5),
        LevelDecor(decorName='tree1', level=level21, x=216, y=80),
        LevelDecor(decorName='tree2', level=level21, x=707, y=2),
        LevelDecor(decorName='tree2', level=level21, x=638, y=91),
        LevelDecor(decorName='tree1', level=level21, x=697, y=186),
        LevelDecor(decorName='tree1', level=level21, x=439, y=113),
        LevelDecor(decorName='tree2', level=level21, x=302, y=18),
        LevelDecor(decorName='tree2', level=level21, x=89, y=113),
        LevelDecor(decorName='tree2', level=level21, x=516, y=47),
        LevelDecor(decorName='tree2', level=level22, x=859, y=698),
        LevelDecor(decorName='tree2', level=level22, x=727, y=698),
        LevelDecor(decorName='tree2', level=level22, x=574, y=696),
        LevelDecor(decorName='tree2', level=level22, x=414, y=694),
        LevelDecor(decorName='tree2', level=level22, x=256, y=695),
        LevelDecor(decorName='tree2', level=level22, x=83, y=693),
        LevelDecor(decorName='bush', level=level22, x=840, y=1),
        LevelDecor(decorName='bush', level=level22, x=651, y=0),
        LevelDecor(decorName='tree1', level=level22, x=378, y=478),
        LevelDecor(decorName='tree1', level=level22, x=209, y=426),
        LevelDecor(decorName='tree1', level=level22, x=409, y=292),
        LevelDecor(decorName='tree1', level=level22, x=233, y=226),
        LevelDecor(decorName='tree1', level=level22, x=629, y=201),
        LevelDecor(decorName='bush', level=level23, x=1, y=4),
        LevelDecor(decorName='bush', level=level23, x=3, y=400),
        LevelDecor(decorName='bush', level=level23, x=101, y=697),
        LevelDecor(decorName='bush', level=level23, x=2, y=600),
        LevelDecor(decorName='bush', level=level23, x=200, y=2),
        LevelDecor(decorName='bush', level=level23, x=399, y=3),
        LevelDecor(decorName='bush', level=level23, x=603, y=2),
        LevelDecor(decorName='bush', level=level23, x=299, y=697),
        LevelDecor(decorName='bush', level=level23, x=501, y=699),
        LevelDecor(decorName='bush', level=level23, x=702, y=699),
        LevelDecor(decorName='bush', level=level23, x=895, y=698),
        LevelDecor(decorName='tree2', level=level24, x=476, y=109),
        LevelDecor(decorName='tree2', level=level24, x=699, y=64),
        LevelDecor(decorName='tree2', level=level24, x=572, y=20),
        LevelDecor(decorName='tree2', level=level24, x=633, y=95),
        LevelDecor(decorName='tree1', level=level24, x=75, y=560),
        LevelDecor(decorName='tree1', level=level24, x=217, y=704),
        LevelDecor(decorName='tree1', level=level24, x=101, y=696),
        LevelDecor(decorName='tree1', level=level24, x=48, y=624),
        LevelDecor(decorName='bush', level=level24, x=700, y=400),
        LevelDecor(decorName='bush', level=level24, x=552, y=402),
        LevelDecor(decorName='bush', level=level24, x=401, y=400),
        LevelDecor(decorName='bush', level=level24, x=246, y=401),
        LevelDecor(decorName='tree2', level=level25, x=295, y=589),
        LevelDecor(decorName='tree2', level=level25, x=403, y=489),
        LevelDecor(decorName='tree2', level=level25, x=207, y=399),
        LevelDecor(decorName='tree2', level=level25, x=108, y=506),
        LevelDecor(decorName='tree2', level=level25, x=596, y=391),
        LevelDecor(decorName='tree2', level=level25, x=401, y=301),
        LevelDecor(decorName='tree2', level=level25, x=497, y=205),
        LevelDecor(decorName='tree2', level=level25, x=700, y=294),
        LevelDecor(decorName='tree1', level=level25, x=6, y=110),
        LevelDecor(decorName='tree1', level=level25, x=4, y=6),
        LevelDecor(decorName='tree1', level=level25, x=0, y=230),
        LevelDecor(decorName='tree1', level=level25, x=885, y=687),
        LevelDecor(decorName='tree1', level=level25, x=651, y=689),
        LevelDecor(decorName='tree1', level=level25, x=767, y=693),
        LevelDecor(decorName='tree1', level=level25, x=885, y=575),
        LevelDecor(decorName='tree1', level=level25, x=887, y=463),
        LevelDecor(decorName='tree1', level=level29, x=96, y=599),
        LevelDecor(decorName='tree1', level=level29, x=200, y=599),
        LevelDecor(decorName='tree1', level=level29, x=300, y=600),
        LevelDecor(decorName='tree1', level=level29, x=257, y=514),
        LevelDecor(decorName='tree1', level=level29, x=149, y=512),
        LevelDecor(decorName='tree1', level=level29, x=209, y=431),
        LevelDecor(decorName='tree1', level=level30, x=117, y=700),
        LevelDecor(decorName='tree1', level=level30, x=244, y=697),
        LevelDecor(decorName='tree1', level=level30, x=55, y=594),
        LevelDecor(decorName='tree1', level=level30, x=184, y=599),
        LevelDecor(decorName='tree1', level=level30, x=117, y=490),
        LevelDecor(decorName='tree1', level=level30, x=480, y=500),
        LevelDecor(decorName='tree2', level=level30, x=412, y=397),
        LevelDecor(decorName='tree2', level=level30, x=544, y=399),
        LevelDecor(decorName='tree2', level=level30, x=487, y=295),
        LevelDecor(decorName='tree2', level=level30, x=618, y=298),
        LevelDecor(decorName='tree2', level=level30, x=414, y=188),
        LevelDecor(decorName='tree2', level=level30, x=564, y=189),
        LevelDecor(decorName='tree2', level=level30, x=704, y=189),
        LevelDecor(decorName='tree2', level=level30, x=265, y=192),
        LevelDecor(decorName='tree2', level=level30, x=342, y=295),
        LevelDecor(decorName='tree1', level=level31, x=476, y=585),
        LevelDecor(decorName='tree1', level=level31, x=424, y=476),
        LevelDecor(decorName='tree2', level=level31, x=260, y=272),
        LevelDecor(decorName='tree2', level=level31, x=197, y=388),
        LevelDecor(decorName='tree1', level=level31, x=264, y=347),
        LevelDecor(decorName='tree2', level=level31, x=313, y=94),
        LevelDecor(decorName='tree2', level=level31, x=389, y=21),
        LevelDecor(decorName='tree1', level=level31, x=547, y=233),
        LevelDecor(decorName='tree2', level=level31, x=600, y=93),
        LevelDecor(decorName='tree2', level=level31, x=537, y=163),
        LevelDecor(decorName='tree2', level=level31, x=639, y=183),
        LevelDecor(decorName='tree1', level=level31, x=311, y=13),
        LevelDecor(decorName='tree1', level=level31, x=400, y=558),
        LevelDecor(decorName='tree2', level=level31, x=494, y=512),
        LevelDecor(decorName='bush', level=level31, x=196, y=701),
        LevelDecor(decorName='bush', level=level31, x=404, y=698),
        LevelDecor(decorName='tree1', level=level32, x=153, y=476),
        LevelDecor(decorName='tree1', level=level32, x=33, y=363),
        LevelDecor(decorName='tree1', level=level32, x=189, y=297),
        LevelDecor(decorName='tree2', level=level32, x=808, y=660),
        LevelDecor(decorName='tree2', level=level32, x=888, y=593),
        LevelDecor(decorName='tree2', level=level32, x=719, y=705),
        LevelDecor(decorName='tree2', level=level32, x=694, y=570),
        LevelDecor(decorName='tree2', level=level32, x=589, y=694),
        LevelDecor(decorName='tree2', level=level32, x=919, y=490),
        LevelDecor(decorName='tree2', level=level32, x=903, y=685),
        LevelDecor(decorName='tree2', level=level32, x=817, y=748),
        LevelDecor(decorName='tree2', level=level32, x=809, y=506),
        LevelDecor(decorName='tree2', level=level32, x=886, y=360),
        LevelDecor(decorName='tree1', level=level32, x=136, y=365),
        LevelDecor(decorName='tree1', level=level32, x=82, y=427),
        LevelDecor(decorName='tree1', level=level33, x=2, y=101),
        LevelDecor(decorName='tree1', level=level33, x=101, y=100),
        LevelDecor(decorName='tree1', level=level33, x=203, y=98),
        LevelDecor(decorName='tree1', level=level33, x=306, y=101),
        LevelDecor(decorName='tree1', level=level33, x=403, y=97),
        LevelDecor(decorName='bush', level=level34, x=700, y=303),
        LevelDecor(decorName='bush', level=level34, x=397, y=298),
        LevelDecor(decorName='bush', level=level34, x=244, y=296),
        LevelDecor(decorName='bush', level=level34, x=702, y=459),
        LevelDecor(decorName='bush', level=level34, x=698, y=602),
        LevelDecor(decorName='bush', level=level34, x=246, y=97),
        LevelDecor(decorName='bush', level=level34, x=404, y=101),
        LevelDecor(decorName='bush', level=level34, x=560, y=99),
        LevelDecor(decorName='bush', level=level34, x=707, y=100),
        LevelDecor(decorName='bush', level=level34, x=894, y=102),
        LevelDecor(decorName='bush', level=level34, x=898, y=299),
        LevelDecor(decorName='bush', level=level34, x=901, y=461),
        LevelDecor(decorName='bush', level=level34, x=896, y=603),
        LevelDecor(decorName='tree1', level=level34, x=7, y=692),
        LevelDecor(decorName='tree1', level=level34, x=16, y=596),
        LevelDecor(decorName='tree2', level=level34, x=0, y=512),
        LevelDecor(decorName='tree2', level=level34, x=88, y=657),
        LevelDecor(decorName='tree2', level=level35, x=684, y=299),
        LevelDecor(decorName='tree2', level=level35, x=484, y=297),
        LevelDecor(decorName='tree1', level=level35, x=617, y=288),
        LevelDecor(decorName='tree1', level=level35, x=540, y=309),
        LevelDecor(decorName='bush', level=level35, x=577, y=501),
        LevelDecor(decorName='bush', level=level35, x=665, y=501),
        LevelDecor(decorName='tree1', level=level35, x=508, y=517),
        LevelDecor(decorName='tree2', level=level35, x=620, y=507),
        LevelDecor(decorName='tree2', level=level35, x=742, y=512),
        LevelDecor(decorName='tree1', level=level35, x=368, y=342),
        LevelDecor(decorName='tree1', level=level35, x=306, y=241),
        LevelDecor(decorName='tree2', level=level35, x=420, y=711),
        LevelDecor(decorName='tree2', level=level35, x=548, y=687),
        LevelDecor(decorName='tree2', level=level35, x=698, y=713),
        LevelDecor(decorName='tree1', level=level35, x=479, y=681),
        LevelDecor(decorName='tree1', level=level35, x=632, y=688),
        LevelDecor(decorName='tree2', level=level35, x=760, y=697),
        LevelDecor(decorName='tree1', level=level35, x=820, y=732),
        LevelDecor(decorName='tree2', level=level35, x=899, y=692),
        LevelDecor(decorName='tree1', level=level35, x=892, y=304),
        LevelDecor(decorName='bush', level=level35, x=898, y=580),
        LevelDecor(decorName='tree1', level=level35, x=899, y=521),
        LevelDecor(decorName='tree1', level=level35, x=881, y=444),
        LevelDecor(decorName='tree2', level=level35, x=888, y=371),
        LevelDecor(decorName='tree2', level=level35, x=829, y=483),
        LevelDecor(decorName='tree2', level=level36, x=350, y=337),
        LevelDecor(decorName='tree2', level=level36, x=348, y=439),
        LevelDecor(decorName='tree2', level=level36, x=344, y=540),
        LevelDecor(decorName='tree2', level=level36, x=342, y=645),
        LevelDecor(decorName='tree2', level=level37, x=424, y=640),
        LevelDecor(decorName='tree1', level=level37, x=441, y=561),
        LevelDecor(decorName='tree2', level=level37, x=503, y=545),
        LevelDecor(decorName='tree1', level=level37, x=503, y=639),
        LevelDecor(decorName='bush', level=level37, x=298, y=401),
        LevelDecor(decorName='tree1', level=level37, x=19, y=594),
        LevelDecor(decorName='tree2', level=level37, x=85, y=551),
        LevelDecor(decorName='tree2', level=level37, x=7, y=507),
        LevelDecor(decorName='bush', level=level37, x=38, y=58),
        LevelDecor(decorName='tree1', level=level37, x=6, y=89),
        LevelDecor(decorName='tree1', level=level37, x=101, y=16),
        LevelDecor(decorName='tree2', level=level37, x=177, y=6),
        LevelDecor(decorName='bush', level=level38, x=865, y=655),
        LevelDecor(decorName='bush', level=level38, x=867, y=457),
        LevelDecor(decorName='bush', level=level38, x=867, y=275),
        LevelDecor(decorName='bush', level=level38, x=864, y=91),
        LevelDecor(decorName='tree1', level=level38, x=668, y=307),
        LevelDecor(decorName='tree1', level=level38, x=542, y=301),
        LevelDecor(decorName='tree1', level=level38, x=194, y=695),
        LevelDecor(decorName='tree2', level=level38, x=340, y=704),
        LevelDecor(decorName='tree2', level=level38, x=87, y=671),
        LevelDecor(decorName='tree2', level=level38, x=187, y=50),
        LevelDecor(decorName='tree2', level=level38, x=62, y=86),
        LevelDecor(decorName='tree1', level=level40, x=377, y=509),
        LevelDecor(decorName='tree1', level=level40, x=787, y=424),
        LevelDecor(decorName='tree1', level=level40, x=609, y=364),
        LevelDecor(decorName='tree1', level=level40, x=686, y=210),
        LevelDecor(decorName='tree2', level=level40, x=752, y=307),
        LevelDecor(decorName='tree2', level=level40, x=709, y=380),
        LevelDecor(decorName='tree2', level=level40, x=389, y=420),
        LevelDecor(decorName='bush', level=level40, x=95, y=578),
        LevelDecor(decorName='tree2', level=level40, x=11, y=558),
        LevelDecor(decorName='tree1', level=level40, x=117, y=513),
        LevelDecor(decorName='tree1', level=level40, x=76, y=626),
        LevelDecor(decorName='bush', level=level40, x=48, y=481),
        LevelDecor(decorName='tree1', level=level40, x=6, y=405),
        LevelDecor(decorName='tree1', level=level40, x=191, y=435),
        LevelDecor(decorName='tree2', level=level40, x=254, y=488),
        LevelDecor(decorName='tree1', level=level41, x=99, y=597),
        LevelDecor(decorName='tree1', level=level41, x=100, y=495),
        LevelDecor(decorName='tree1', level=level41, x=117, y=408),
        LevelDecor(decorName='tree1', level=level41, x=101, y=197),
        LevelDecor(decorName='tree1', level=level41, x=92, y=107),
        LevelDecor(decorName='tree1', level=level41, x=106, y=1),
        LevelDecor(decorName='bush', level=level41, x=607, y=593),
        LevelDecor(decorName='bush', level=level41, x=590, y=493),
        LevelDecor(decorName='bush', level=level41, x=513, y=412),
        LevelDecor(decorName='tree2', level=level41, x=597, y=3),
        LevelDecor(decorName='tree2', level=level41, x=697, y=1),
        LevelDecor(decorName='tree2', level=level41, x=799, y=0),
        LevelDecor(decorName='tree1', level=level42, x=0, y=595),
        LevelDecor(decorName='tree1', level=level42, x=2, y=502),
        LevelDecor(decorName='tree1', level=level42, x=6, y=398),
        LevelDecor(decorName='tree1', level=level42, x=0, y=700),
        LevelDecor(decorName='tree1', level=level42, x=5, y=201),
        LevelDecor(decorName='tree1', level=level42, x=8, y=104),
        LevelDecor(decorName='tree1', level=level42, x=0, y=5),
        LevelDecor(decorName='bush', level=level43, x=399, y=398),
        LevelDecor(decorName='bush', level=level43, x=605, y=397),
        LevelDecor(decorName='tree1', level=level43, x=576, y=604),
        LevelDecor(decorName='tree1', level=level43, x=434, y=601),
        LevelDecor(decorName='bush', level=level43, x=600, y=199),
        LevelDecor(decorName='tree2', level=level43, x=852, y=649),
        LevelDecor(decorName='tree2', level=level43, x=853, y=499),
        LevelDecor(decorName='tree2', level=level43, x=854, y=348),
        LevelDecor(decorName='tree2', level=level43, x=855, y=198),
        LevelDecor(decorName='tree2', level=level43, x=854, y=42),
        LevelDecor(decorName='tree2', level=level43, x=176, y=598),
        LevelDecor(decorName='bush', level=level43, x=404, y=199),
        LevelDecor(decorName='tree2', level=level44, x=472, y=686),
        LevelDecor(decorName='tree2', level=level44, x=532, y=623),
        LevelDecor(decorName='tree2', level=level44, x=459, y=606),
        LevelDecor(decorName='tree2', level=level44, x=612, y=693),
        LevelDecor(decorName='tree1', level=level44, x=139, y=697),
        LevelDecor(decorName='tree1', level=level44, x=209, y=612),
        LevelDecor(decorName='tree1', level=level44, x=45, y=608),
        LevelDecor(decorName='tree1', level=level44, x=67, y=504),
        LevelDecor(decorName='tree1', level=level44, x=154, y=529),
        LevelDecor(decorName='bush', level=level44, x=265, y=20),
        LevelDecor(decorName='bush', level=level44, x=173, y=16),
        LevelDecor(decorName='bush', level=level44, x=64, y=54),
        LevelDecor(decorName='tree1', level=level45, x=198, y=702),
        LevelDecor(decorName='tree1', level=level45, x=400, y=702),
        LevelDecor(decorName='tree1', level=level45, x=600, y=700),
        LevelDecor(decorName='tree1', level=level45, x=802, y=699),
        LevelDecor(decorName='tree1', level=level45, x=100, y=601),
        LevelDecor(decorName='bush', level=level45, x=299, y=601),
        LevelDecor(decorName='bush', level=level45, x=503, y=600),
        LevelDecor(decorName='bush', level=level45, x=701, y=600),
        LevelDecor(decorName='bush', level=level45, x=899, y=601),
        LevelDecor(decorName='bush', level=level45, x=4, y=1),
        LevelDecor(decorName='bush', level=level45, x=401, y=0),
        LevelDecor(decorName='bush', level=level45, x=600, y=0),
        LevelDecor(decorName='bush', level=level45, x=801, y=0),
        LevelDecor(decorName='tree2', level=level45, x=101, y=99),
        LevelDecor(decorName='tree2', level=level45, x=299, y=97),
        LevelDecor(decorName='tree2', level=level45, x=502, y=97),
        LevelDecor(decorName='tree2', level=level45, x=700, y=106),
        LevelDecor(decorName='tree2', level=level45, x=899, y=100),
        LevelDecor(decorName='bush', level=level45, x=0, y=699),
        LevelDecor(decorName='tree2', level=level45, x=4, y=493),
        LevelDecor(decorName='tree2', level=level45, x=200, y=495),
        LevelDecor(decorName='tree2', level=level45, x=398, y=500),
        LevelDecor(decorName='tree2', level=level45, x=604, y=498),
        LevelDecor(decorName='tree2', level=level45, x=804, y=503),
        LevelDecor(decorName='tree2', level=level46, x=772, y=670),
        LevelDecor(decorName='tree2', level=level46, x=900, y=569),
        LevelDecor(decorName='tree2', level=level46, x=772, y=501),
        LevelDecor(decorName='tree1', level=level46, x=654, y=632),
        LevelDecor(decorName='tree1', level=level46, x=811, y=576),
        LevelDecor(decorName='tree1', level=level46, x=861, y=694),
        LevelDecor(decorName='tree1', level=level46, x=707, y=741),
        LevelDecor(decorName='tree2', level=level46, x=22, y=70),
        LevelDecor(decorName='tree1', level=level46, x=100, y=150),
        LevelDecor(decorName='tree2', level=level46, x=151, y=45),
        LevelDecor(decorName='tree2', level=level46, x=719, y=223),
        LevelDecor(decorName='bush', level=level46, x=654, y=103),
        LevelDecor(decorName='tree1', level=level46, x=755, y=128),
        LevelDecor(decorName='bush', level=level46, x=3, y=623),
        LevelDecor(decorName='bush', level=level46, x=59, y=697),
        LevelDecor(decorName='tree2', level=level46, x=27, y=563),
        LevelDecor(decorName='tree1', level=level46, x=111, y=680),
        LevelDecor(decorName='tree2', level=level47, x=46, y=683),
        LevelDecor(decorName='tree1', level=level47, x=8, y=589),
        LevelDecor(decorName='tree1', level=level47, x=149, y=716),
        LevelDecor(decorName='tree2', level=level47, x=106, y=568),
        LevelDecor(decorName='tree2', level=level47, x=806, y=262),
        LevelDecor(decorName='tree1', level=level47, x=760, y=165),
        LevelDecor(decorName='tree1', level=level47, x=852, y=86),
        LevelDecor(decorName='tree2', level=level47, x=761, y=51),
        LevelDecor(decorName='tree2', level=level47, x=865, y=175),
        LevelDecor(decorName='tree2', level=level48, x=144, y=399),
        LevelDecor(decorName='tree1', level=level48, x=240, y=372),
        LevelDecor(decorName='tree2', level=level48, x=169, y=294),
        LevelDecor(decorName='tree1', level=level48, x=81, y=333),
        LevelDecor(decorName='tree1', level=level48, x=520, y=605),
        LevelDecor(decorName='tree2', level=level48, x=639, y=598),
        LevelDecor(decorName='tree1', level=level48, x=740, y=560),
        LevelDecor(decorName='tree2', level=level48, x=731, y=695),
        LevelDecor(decorName='bush', level=level48, x=12, y=6),
        LevelDecor(decorName='bush', level=level48, x=203, y=6),
        LevelDecor(decorName='bush', level=level48, x=403, y=9),
        LevelDecor(decorName='bush', level=level48, x=603, y=11),
        LevelDecor(decorName='bush', level=level48, x=804, y=10),
        LevelDecor(decorName='tree1', level=level26, x=176, y=520),
        LevelDecor(decorName='tree1', level=level26, x=176, y=400),
        LevelDecor(decorName='tree1', level=level26, x=179, y=286),
        LevelDecor(decorName='bush', level=level26, x=500, y=627),
        LevelDecor(decorName='bush', level=level26, x=499, y=508),
        LevelDecor(decorName='bush', level=level26, x=500, y=388),
        LevelDecor(decorName='tree2', level=level26, x=690, y=203),
        LevelDecor(decorName='tree2', level=level26, x=780, y=81),
        LevelDecor(decorName='tree2', level=level26, x=865, y=419),
        LevelDecor(decorName='tree2', level=level26, x=875, y=180),
        LevelDecor(decorName='tree1', level=level8, x=484, y=438),
        LevelDecor(decorName='tree1', level=level8, x=660, y=410),
        LevelDecor(decorName='tree2', level=level8, x=111, y=589),
        LevelDecor(decorName='tree2', level=level8, x=39, y=491),
        LevelDecor(decorName='pond', level=level8, x=569, y=267),
        LevelDecor(decorName='tree1', level=level8, x=385, y=307),
        LevelDecor(decorName='tree1', level=level8, x=484, y=438),
        LevelDecor(decorName='tree1', level=level8, x=660, y=410),
        LevelDecor(decorName='tree2', level=level8, x=111, y=589),
        LevelDecor(decorName='tree2', level=level8, x=39, y=491),
        LevelDecor(decorName='pond', level=level8, x=569, y=267),
        LevelDecor(decorName='tree1', level=level8, x=385, y=307),
        LevelDecor(decorName='tree1', level=level27, x=647, y=351),
        LevelDecor(decorName='tree1', level=level27, x=220, y=353),
        LevelDecor(decorName='pond', level=level27, x=346, y=316),
        LevelDecor(decorName='tree1', level=level27, x=574, y=183),
        LevelDecor(decorName='bush', level=level27, x=610, y=609),
        LevelDecor(decorName='bush', level=level27, x=478, y=608),
        LevelDecor(decorName='bush', level=level27, x=354, y=608),
        LevelDecor(decorName='bush', level=level27, x=214, y=606),
        LevelDecor(decorName='tree1', level=level27, x=510, y=396),
        LevelDecor(decorName='tree1', level=level28, x=678, y=495),
        LevelDecor(decorName='bush', level=level28, x=356, y=685),
        LevelDecor(decorName='pond', level=level28, x=437, y=478),
        LevelDecor(decorName='bush', level=level28, x=429, y=684),
        LevelDecor(decorName='bush', level=level28, x=509, y=685),
        LevelDecor(decorName='bush', level=level28, x=587, y=684),
        LevelDecor(decorName='bush', level=level28, x=565, y=559),
        LevelDecor(decorName='bush', level=level28, x=385, y=490),
        LevelDecor(decorName='bush', level=level28, x=385, y=559),
        LevelDecor(decorName='bush', level=level28, x=567, y=489),
        LevelDecor(decorName='bush', level=level28, x=516, y=431),
        LevelDecor(decorName='bush', level=level28, x=436, y=431),
        LevelDecor(decorName='tree2', level=level28, x=700, y=199),
        LevelDecor(decorName='bush', level=level28, x=809, y=307),
        LevelDecor(decorName='bush', level=level28, x=752, y=307),
        LevelDecor(decorName='bush', level=level28, x=690, y=306),
        LevelDecor(decorName='bush', level=level28, x=869, y=308),
        LevelDecor(decorName='tree2', level=level49, x=501, y=487),
        LevelDecor(decorName='pond', level=level49, x=475, y=262),
        LevelDecor(decorName='tree1', level=level49, x=181, y=323),
        LevelDecor(decorName='bush', level=level49, x=65, y=489),
        LevelDecor(decorName='bush', level=level49, x=63, y=426),
        LevelDecor(decorName='bush', level=level49, x=60, y=356),
        LevelDecor(decorName='bush', level=level49, x=57, y=291),
        LevelDecor(decorName='bush', level=level49, x=130, y=489),
        LevelDecor(decorName='bush', level=level49, x=194, y=491),
        LevelDecor(decorName='bush', level=level49, x=262, y=492),
        LevelDecor(decorName='bush', level=level49, x=479, y=196),
        LevelDecor(decorName='bush', level=level49, x=400, y=290),
        LevelDecor(decorName='bush', level=level49, x=637, y=287),
        LevelDecor(decorName='bush', level=level49, x=639, y=350),
        LevelDecor(decorName='bush', level=level49, x=404, y=353),
        LevelDecor(decorName='bush', level=level49, x=556, y=196),
        LevelDecor(decorName='tree1', level=level49, x=777, y=530),
        LevelDecor(decorName='bush', level=level49, x=787, y=453),
        LevelDecor(decorName='bush', level=level49, x=789, y=380),
        LevelDecor(decorName='bush', level=level49, x=787, y=308),
        LevelDecor(decorName='pond', level=level50, x=482, y=75),
        LevelDecor(decorName='tree2', level=level50, x=797, y=491),
        LevelDecor(decorName='bush', level=level50, x=494, y=492),
        LevelDecor(decorName='bush', level=level50, x=494, y=558),
        LevelDecor(decorName='bush', level=level50, x=494, y=426),
        LevelDecor(decorName='bush', level=level50, x=495, y=356),
        LevelDecor(decorName='bush', level=level50, x=495, y=291),
        LevelDecor(decorName='tree1', level=level50, x=284, y=584),
        LevelDecor(decorName='bush', level=level50, x=686, y=39),
        LevelDecor(decorName='bush', level=level50, x=686, y=98),
        LevelDecor(decorName='bush', level=level50, x=684, y=160)])


# The addition of TestLevel is kept to keep the id of levels and decor the same
def addTestLevel(apps, schema_editor):
    Level = apps.get_model('game', 'Level')
    Block = apps.get_model('game', 'Block')
    LevelBlock = apps.get_model('game', 'LevelBlock')
    Character = apps.get_model('game', 'Character')
    Theme = apps.get_model('game', 'Theme')

    van = Character.objects.get(name="Van")
    grass = Theme.objects.get(name="grass")

    testLevel = Level(name='Limited blocks test', anonymous=False, blocklyEnabled=True, character=van, default=True,
                      destinations='[[0, 1]]', direct_drive=True, fuel_gauge=False, max_fuel=50,
                      model_solution='[11]', origin='{"coordinate":[2, 7], "direction":"S"}',
                      path='[{"coordinate":[2,7],"connectedNodes":[1]},{"coordinate":[2,6],"connectedNodes":[0,2]},{"coordinate":[3,6],"connectedNodes":[1,3,10]},{"coordinate":[4,6],"connectedNodes":[2,4]},{"coordinate":[5,6],"connectedNodes":[3,5]},{"coordinate":[6,6],"connectedNodes":[4,6]},{"coordinate":[6,5],"connectedNodes":[5,7]},{"coordinate":[6,4],"connectedNodes":[13,6,8]},{"coordinate":[6,3],"connectedNodes":[7,9]},{"coordinate":[6,2],"connectedNodes":[8,14]},{"coordinate":[3,5],"connectedNodes":[2,11]},{"coordinate":[3,4],"connectedNodes":[10,12]},{"coordinate":[4,4],"connectedNodes":[11,13,18]},{"coordinate":[5,4],"connectedNodes":[12,7]},{"coordinate":[6,1],"connectedNodes":[15,9]},{"coordinate":[5,1],"connectedNodes":[16,14]},{"coordinate":[4,1],"connectedNodes":[19,17,15]},{"coordinate":[4,2],"connectedNodes":[18,16]},{"coordinate":[4,3],"connectedNodes":[12,17]},{"coordinate":[3,1],"connectedNodes":[20,16]},{"coordinate":[2,1],"connectedNodes":[21,19]},{"coordinate":[1,1],"connectedNodes":[22,20]},{"coordinate":[0,1],"connectedNodes":[21]}]',
                      pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    testLevel.save();

    block1 = LevelBlock(type=Block.objects.get(type="move_forwards"), number=1, level=testLevel)
    block2 = LevelBlock(type=Block.objects.get(type="turn_right"), number=2, level=testLevel)
    block3 = LevelBlock(type=Block.objects.get(type="turn_left"),  number=10, level=testLevel)
    block4 = LevelBlock(type=Block.objects.get(type="controls_repeat"), number=1, level=testLevel)
    block5 = LevelBlock(type=Block.objects.get(type="wait"), number=1, level=testLevel)

    block1.save()
    block2.save()
    block3.save()
    block4.save()
    block5.save()

# Delete TestLevel
def delete_old_limit_level(apps, schema_editor):
    Level = apps.get_model('game', 'Level')

    if Level.objects.filter(name="Limited blocks test", default=True).exists():
        old_limit_level = Level.objects.get(name="Limited blocks test", default=True)
        old_limit_level.delete()


# Add episode 7 to 9
# Add levels 62, 51, 59, 57, 60, 61, 70
def add_episode_7_to_9(apps, schema_editor):

    def set_decor(level, decor):
        set_decor_inner(level, decor, LevelDecor)

    def set_blocks(level, blocks):
        set_blocks_inner(level, blocks, LevelBlock, Block)

    LevelDecor = apps.get_model('game', 'LevelDecor')
    Level = apps.get_model('game', 'Level')
    Episode = apps.get_model('game', 'Episode')
    Block = apps.get_model('game', 'Block')
    LevelBlock = apps.get_model('game', 'LevelBlock')
    Theme = apps.get_model('game', 'Theme')
    Character = apps.get_model('game', 'Character')

    def create_level62():

        level62 = Level(blocklyEnabled=True,
                        character=Character.objects.get(name="Van"),
                        destinations="[[6,2]]",
                        max_fuel="50",
                        model_solution='[15]',
                        name="62",
                        origin='{"coordinate":[1,5],"direction":"E"}',
                        path='[{"coordinate":[1,5],"connectedNodes":[1]},{"coordinate":[2,5],"connectedNodes":[0,2]},{"coordinate":[3,5],"connectedNodes":[1,3]},{"coordinate":[4,5],"connectedNodes":[2,4]},{"coordinate":[5,5],"connectedNodes":[3,5]},{"coordinate":[6,5],"connectedNodes":[4,6]},{"coordinate":[6,4],"connectedNodes":[5,7]},{"coordinate":[6,3],"connectedNodes":[6,8]},{"coordinate":[6,2],"connectedNodes":[7]}]',
                        pythonEnabled=False,
                        theme=Theme.objects.get(id=2),
                        default=True,
                        traffic_lights='[{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":4,"y":5},"direction":"E","startTime":0,"startingState":"GREEN"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":5,"y":5},"direction":"E","startTime":0,"startingState":"GREEN"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":6,"y":5},"direction":"S","startTime":0,"startingState":"GREEN"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":2,"y":5},"direction":"E","startTime":0,"startingState":"RED"}]')
        level62.save()

        move_forwards = LevelBlock(level=level62, type=Block.objects.get(type="move_forwards"))
        turn_left = LevelBlock(level=level62, type=Block.objects.get(type="turn_left"))
        turn_right = LevelBlock(level=level62, type=Block.objects.get(type="turn_right"))
        wait = LevelBlock(level=level62, type=Block.objects.get(type="wait"))
        controls_repeat_until = LevelBlock(level=level62, type=Block.objects.get(type="controls_repeat_until"))
        at_destination = LevelBlock(level=level62, type=Block.objects.get(type="at_destination"))
        traffic_light = LevelBlock(level=level62, type=Block.objects.get(type="traffic_light"))
        call_proc = LevelBlock(level=level62, type=Block.objects.get(type="call_proc"))
        declare_proc = LevelBlock(level=level62, type=Block.objects.get(type="declare_proc"))
        move_forwards.save()
        turn_left.save()
        turn_right.save()
        wait.save()
        controls_repeat_until.save()
        at_destination.save()
        traffic_light.save()
        call_proc.save()
        declare_proc.save()
        return level62

    def create_level51():

        level51 = Level(blocklyEnabled=True,
                        character=Character.objects.get(name="Van"),

                        destinations="[[8,6]]",
                        max_fuel="50",
                        name="51",
                        origin='{"coordinate":[0,4],"direction":"E"}',
                        path='[{"coordinate":[0,4],"connectedNodes":[1]},{"coordinate":[1,4],"connectedNodes":[0,2]},{"coordinate":[2,4],"connectedNodes":[1,3,11]},{"coordinate":[2,5],"connectedNodes":[5,2]},{"coordinate":[4,5],"connectedNodes":[10,7]},{"coordinate":[2,6],"connectedNodes":[6,3]},{"coordinate":[3,6],"connectedNodes":[5,10]},{"coordinate":[5,5],"connectedNodes":[4,8]},{"coordinate":[6,5],"connectedNodes":[7,20,16,9]},{"coordinate":[6,4],"connectedNodes":[8,15]},{"coordinate":[3,5],"connectedNodes":[6,4]},{"coordinate":[3,4],"connectedNodes":[2,12]},{"coordinate":[4,4],"connectedNodes":[11,13]},{"coordinate":[5,4],"connectedNodes":[12,14]},{"coordinate":[5,3],"connectedNodes":[13,15]},{"coordinate":[6,3],"connectedNodes":[14,9]},{"coordinate":[7,5],"connectedNodes":[8,17]},{"coordinate":[7,4],"connectedNodes":[16,18]},{"coordinate":[8,4],"connectedNodes":[17,19]},{"coordinate":[8,5],"connectedNodes":[24,18]},{"coordinate":[6,6],"connectedNodes":[21,8]},{"coordinate":[6,7],"connectedNodes":[22,20]},{"coordinate":[7,7],"connectedNodes":[21,23]},{"coordinate":[8,7],"connectedNodes":[22,24]},{"coordinate":[8,6],"connectedNodes":[23,19]}]',
                        pythonEnabled=False,
                        theme=Theme.objects.get(id=1),
                        default=True,
                        traffic_lights= "[]")
        level51.save()

        forwards = LevelBlock(level=level51, type=Block.objects.get(type="move_forwards"))
        left = LevelBlock(level=level51, type=Block.objects.get(type="turn_left"), number=2)
        right = LevelBlock(level=level51, type=Block.objects.get(type="turn_right"), number=3)
        forwards.save()
        left.save()
        right.save()
        return level51

    level62 = create_level62()
    level51 = create_level51()

    episode7 = Episode(pk=7, name="Procedures", first_level=level62, r_branchiness=0.5,
                       r_loopiness=0.1, r_num_tiles=35, r_curviness=0.2, r_pythonEnabled=0,
                       r_blocklyEnabled=1, r_trafficLights=1, in_development=True)
    episode7.save()

    episode8 = Episode(pk=8, name="Limited Blocks", first_level=level51, r_branchiness=0.5,
                       r_loopiness=0.1, r_num_tiles=35, r_curviness=0.2, r_pythonEnabled=0,
                       r_blocklyEnabled=1, r_trafficLights=1, in_development=True)
    episode8.save()

    grass = Theme.objects.get(name='grass')
    snow = Theme.objects.get(name='snow')
    farm = Theme.objects.get(name='farm')
    city = Theme.objects.get(name='city')

    van = Character.objects.get(name='Van')

    def create_level59():
        level59 = Level(
            name="59", blocklyEnabled=True, character=van, default=True,
            destinations="[[7,4]]", direct_drive=False, fuel_gauge=True,
            max_fuel=50, origin='{"coordinate":[0,4],"direction":"E"}',
            path='[{"coordinate":[0,4],"connectedNodes":[1]},{"coordinate":[1,4],"connectedNodes":[0,3,2,14]},{"coordinate":[2,4],"connectedNodes":[1,9,4]},{"coordinate":[1,5],"connectedNodes":[17,1]},{"coordinate":[3,4],"connectedNodes":[2,10,5,15]},{"coordinate":[4,4],"connectedNodes":[4,11,6]},{"coordinate":[5,4],"connectedNodes":[5,12,7,16]},{"coordinate":[6,4],"connectedNodes":[6,13,8,29]},{"coordinate":[7,4],"connectedNodes":[7]},{"coordinate":[2,5],"connectedNodes":[2]},{"coordinate":[3,5],"connectedNodes":[19,4]},{"coordinate":[4,5],"connectedNodes":[5]},{"coordinate":[5,5],"connectedNodes":[21,6]},{"coordinate":[6,5],"connectedNodes":[7]},{"coordinate":[1,3],"connectedNodes":[1,22]},{"coordinate":[3,3],"connectedNodes":[4]},{"coordinate":[5,3],"connectedNodes":[6]},{"coordinate":[1,6],"connectedNodes":[18,3]},{"coordinate":[2,6],"connectedNodes":[17,19]},{"coordinate":[3,6],"connectedNodes":[18,20,10]},{"coordinate":[4,6],"connectedNodes":[19,21]},{"coordinate":[5,6],"connectedNodes":[20,12]},{"coordinate":[1,2],"connectedNodes":[14,23]},{"coordinate":[2,2],"connectedNodes":[22,24]},{"coordinate":[3,2],"connectedNodes":[23,25]},{"coordinate":[4,2],"connectedNodes":[24,26]},{"coordinate":[5,2],"connectedNodes":[25,27]},{"coordinate":[6,2],"connectedNodes":[26,29,28]},{"coordinate":[7,2],"connectedNodes":[27]},{"coordinate":[6,3],"connectedNodes":[7,27]}]',
            pythonEnabled=False, theme=farm, model_solution='[5]',
            traffic_lights='[]',
        )
        level59.save()
        set_decor(level59, json.loads('[{"url":"decor/farm/tree1.svg","height":100,"width":100,"y":511,"x":9,"decorName":"tree1"},{"url":"decor/farm/tree1.svg","height":100,"width":100,"y":400,"x":813,"decorName":"tree1"},{"url":"decor/farm/crops.svg","height":100,"width":150,"y":507,"x":712,"decorName":"pond"},{"url":"decor/farm/crops.svg","height":100,"width":150,"y":290,"x":701,"decorName":"pond"},{"url":"decor/farm/bush.svg","height":30,"width":50,"y":373,"x":191,"decorName":"bush"},{"url":"decor/farm/bush.svg","height":30,"width":50,"y":373,"x":257,"decorName":"bush"}]'))
        set_blocks(level59, json.loads('[{"type":"turn_left","number":2},{"type":"turn_around","number":1},{"type":"controls_repeat_until","number":1},{"type":"at_destination","number":1},{"type":"dead_end","number":1}]'))
        return level59

    def create_level60():
        level60 = Level(
            name='60',
            default=True,
            path='[{"coordinate":[0,2],"connectedNodes":[18]},{"coordinate":[5,3],"connectedNodes":[16,2]},{"coordinate":[5,2],"connectedNodes":[5,1,12]},{"coordinate":[2,2],"connectedNodes":[18,4]},{"coordinate":[3,2],"connectedNodes":[3,5]},{"coordinate":[4,2],"connectedNodes":[4,2]},{"coordinate":[5,5],"connectedNodes":[7,16]},{"coordinate":[5,6],"connectedNodes":[9,8,6]},{"coordinate":[6,6],"connectedNodes":[7]},{"coordinate":[4,6],"connectedNodes":[10,7]},{"coordinate":[3,6],"connectedNodes":[11,9]},{"coordinate":[2,6],"connectedNodes":[14,10]},{"coordinate":[5,1],"connectedNodes":[2]},{"coordinate":[1,7],"connectedNodes":[14]},{"coordinate":[1,6],"connectedNodes":[13,11,15]},{"coordinate":[1,5],"connectedNodes":[14,17]},{"coordinate":[5,4],"connectedNodes":[6,1]},{"coordinate":[1,4],"connectedNodes":[15]},{"coordinate":[1,2],"connectedNodes":[0,3]}]',
            traffic_lights='[]',
            destinations='[[1,6]]',
            origin='{"coordinate":[0,2],"direction":"E"}',
            max_fuel=50,
            theme=Theme.objects.get(id=1),
            character=Character.objects.get(name='Van'),
            blocklyEnabled=True,
            pythonEnabled=False,
            model_solution='[5]',
        )
        level60.save()
        set_decor(level60, json.loads('[{"x":400,"y":408,"decorName":"tree2"},{"x":99,"y":482,"decorName":"bush"},{"x":190,"y":437,"decorName":"tree2"},{"x":151,"y":496,"decorName":"tree2"},{"x":116,"y":430,"decorName":"tree2"},{"x":357,"y":185,"decorName":"tree2"},{"x":283,"y":153,"decorName":"tree2"},{"x":602,"y":367,"decorName":"tree2"},{"x":683,"y":394,"decorName":"tree2"},{"x":455,"y":633,"decorName":"tree2"},{"x":528,"y":625,"decorName":"tree2"},{"x":495,"y":691,"decorName":"tree2"},{"x":610,"y":599,"decorName":"tree2"},{"x":45,"y":210,"decorName":"bush"},{"x":377,"y":747,"decorName":"bush"},{"x":673,"y":224,"decorName":"bush"},{"x":576,"y":92,"decorName":"bush"},{"x":111,"y":102,"decorName":"bush"},{"x":116,"y":284,"decorName":"bush"},{"x":157,"y":701,"decorName":"bush"}]'))
        set_blocks(level60, json.loads('[{"type":"move_forwards","number":2},{"type":"turn_right","number":1},{"type":"turn_around","number":1},{"type":"controls_repeat","number":1}]'))
        return level60

    def create_level68():
        level68 = Level(
            name="68", blocklyEnabled=True, character=van, default=True,
            destinations="[[3,3]]", direct_drive=False, fuel_gauge=True,
            max_fuel=9, origin='{"coordinate":[8,3],"direction":"W"}',
            path='[{"coordinate":[8,3],"connectedNodes":[1]},{"coordinate":[7,3],"connectedNodes":[2,0]},{"coordinate":[6,3],"connectedNodes":[3,1]},{"coordinate":[5,3],"connectedNodes":[4,2]},{"coordinate":[4,3],"connectedNodes":[5,3]},{"coordinate":[3,3],"connectedNodes":[6,4]},{"coordinate":[2,3],"connectedNodes":[7,5]},{"coordinate":[1,3],"connectedNodes":[9,6,10]},{"coordinate":[1,5],"connectedNodes":[9]},{"coordinate":[1,4],"connectedNodes":[8,7]},{"coordinate":[1,2],"connectedNodes":[7,11]},{"coordinate":[1,1],"connectedNodes":[10]}]',
            pythonEnabled=False, theme=city, model_solution='[5]',
            traffic_lights='[{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":1,"y":4},"direction":"N","startTime":0,"startingState":"RED"}]',
        )
        level68.save()
        set_decor(level68, json.loads('[{"url":"decor/city/hospital.svg","height":157,"width":140,"y":173,"x":426,"decorName":"pond"},{"url":"decor/city/shop.svg","height":70,"width":70,"y":408,"x":218,"decorName":"tree1"},{"url":"decor/city/shop.svg","height":70,"width":70,"y":206,"x":209,"decorName":"tree1"},{"url":"decor/city/school.svg","height":100,"width":100,"y":563,"x":87,"decorName":"tree2"},{"url":"decor/city/bush.svg","height":50,"width":50,"y":504,"x":190,"decorName":"bush"},{"url":"decor/city/bush.svg","height":50,"width":50,"y":560,"x":188,"decorName":"bush"},{"url":"decor/city/bush.svg","height":50,"width":50,"y":532,"x":243,"decorName":"bush"}]'))
        set_blocks(level68, json.loads('[{"type":"move_forwards","number":2},{"type":"turn_left","number":1},{"type":"turn_around","number":1},{"type":"controls_repeat_while","number":null},{"type":"road_exists","number":null},{"type":"dead_end","number":1}]'))
        return level68

    def create_level61():
        level61 = Level(
            name="61", blocklyEnabled=True, character=van, default=True,
            destinations='[[7,6]]', direct_drive=False, fuel_gauge=True,
            max_fuel=16, origin='{"coordinate":[1,6],"direction":"S"}',
            path='[{"coordinate":[1,6],"connectedNodes":[1]},{"coordinate":[1,5],"connectedNodes":[0,2]},{"coordinate":[1,4],"connectedNodes":[1,22,3]},{"coordinate":[1,3],"connectedNodes":[2,4]},{"coordinate":[1,2],"connectedNodes":[3,5]},{"coordinate":[1,1],"connectedNodes":[4,6]},{"coordinate":[2,1],"connectedNodes":[5,7]},{"coordinate":[3,1],"connectedNodes":[6,25,8]},{"coordinate":[4,1],"connectedNodes":[7,9]},{"coordinate":[5,1],"connectedNodes":[8,10]},{"coordinate":[6,1],"connectedNodes":[9,21,11]},{"coordinate":[7,1],"connectedNodes":[10,12]},{"coordinate":[8,1],"connectedNodes":[11,13]},{"coordinate":[8,2],"connectedNodes":[14,12]},{"coordinate":[8,3],"connectedNodes":[15,13]},{"coordinate":[8,4],"connectedNodes":[18,16,14]},{"coordinate":[8,5],"connectedNodes":[17,15]},{"coordinate":[8,6],"connectedNodes":[28,16]},{"coordinate":[7,4],"connectedNodes":[19,15]},{"coordinate":[6,4],"connectedNodes":[27,18,20]},{"coordinate":[6,3],"connectedNodes":[19,21]},{"coordinate":[6,2],"connectedNodes":[20,10]},{"coordinate":[2,4],"connectedNodes":[2,23]},{"coordinate":[3,4],"connectedNodes":[22,26,24]},{"coordinate":[3,3],"connectedNodes":[23,25]},{"coordinate":[3,2],"connectedNodes":[24,7]},{"coordinate":[4,4],"connectedNodes":[23,27]},{"coordinate":[5,4],"connectedNodes":[26,19]},{"coordinate":[7,6],"connectedNodes":[17]}]',
            pythonEnabled=False, theme=grass, model_solution='[6]',
            traffic_lights='[{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":1,"y":5},"direction":"S","startTime":0,"startingState":"GREEN"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":3,"y":2},"direction":"S","startTime":0,"startingState":"RED"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":6,"y":3},"direction":"N","startTime":0,"startingState":"RED"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":6,"y":2},"direction":"S","startTime":0,"startingState":"GREEN"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":3,"y":3},"direction":"N","startTime":0,"startingState":"RED"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":4,"y":4},"direction":"W","startTime":0,"startingState":"GREEN"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":2,"y":4},"direction":"E","startTime":0,"startingState":"RED"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":8,"y":4},"direction":"N","startTime":0,"startingState":"RED"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":7,"y":4},"direction":"E","startTime":0,"startingState":"RED"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":4,"y":4},"direction":"E","startTime":0,"startingState":"RED"}]'
        )
        level61.save()
        set_decor(level61, json.loads('[{"url":"decor/grass/tree1.svg","height":100,"width":100,"y":497,"x":198,"decorName":"tree1"},{"url":"decor/grass/tree1.svg","height":100,"width":100,"y":499,"x":320,"decorName":"tree1"},{"url":"decor/grass/tree1.svg","height":100,"width":100,"y":505,"x":447,"decorName":"tree1"},{"url":"decor/grass/tree1.svg","height":100,"width":100,"y":494,"x":570,"decorName":"tree1"},{"url":"decor/grass/tree1.svg","height":100,"width":100,"y":495,"x":697,"decorName":"tree1"},{"url":"decor/grass/pond.svg","height":100,"width":150,"y":254,"x":430,"decorName":"pond"}]'))
        set_blocks(level61, json.loads('[{"type":"move_forwards","number":2},{"type":"turn_left","number":1},{"type":"turn_right","number":null},{"type":"turn_around","number":2},{"type":"wait","number":1},{"type":"controls_repeat_while","number":null},{"type":"road_exists","number":null},{"type":"dead_end","number":1}]'))
        return level61

    def create_level70():
        level70 = Level(
            name="70", blocklyEnabled=True, character=van, default=True,
            destinations="[[7,3]]", direct_drive=False, fuel_gauge=True,
            max_fuel=14, origin='{"coordinate":[1,3],"direction":"E"}',
            path='[{"coordinate":[1,3],"connectedNodes":[22]},{"coordinate":[3,3],"connectedNodes":[22,23,2,24]},{"coordinate":[4,3],"connectedNodes":[1,8,3,9]},{"coordinate":[5,3],"connectedNodes":[2,25,4,26]},{"coordinate":[6,3],"connectedNodes":[3,10,5,11]},{"coordinate":[7,3],"connectedNodes":[4]},{"coordinate":[2,4],"connectedNodes":[18,23,22]},{"coordinate":[2,2],"connectedNodes":[22,24,20]},{"coordinate":[4,4],"connectedNodes":[14,2]},{"coordinate":[4,2],"connectedNodes":[2,17]},{"coordinate":[6,4],"connectedNodes":[25,12,4]},{"coordinate":[6,2],"connectedNodes":[26,4,15]},{"coordinate":[6,5],"connectedNodes":[13,28,10]},{"coordinate":[5,5],"connectedNodes":[14,12]},{"coordinate":[4,5],"connectedNodes":[19,13,8]},{"coordinate":[6,1],"connectedNodes":[16,11,29]},{"coordinate":[5,1],"connectedNodes":[17,15]},{"coordinate":[4,1],"connectedNodes":[21,9,16]},{"coordinate":[2,5],"connectedNodes":[27,19,6]},{"coordinate":[3,5],"connectedNodes":[18,14]},{"coordinate":[2,1],"connectedNodes":[30,7,21]},{"coordinate":[3,1],"connectedNodes":[20,17]},{"coordinate":[2,3],"connectedNodes":[0,6,1,7]},{"coordinate":[3,4],"connectedNodes":[6,1]},{"coordinate":[3,2],"connectedNodes":[7,1]},{"coordinate":[5,4],"connectedNodes":[10,3]},{"coordinate":[5,2],"connectedNodes":[3,11]},{"coordinate":[2,6],"connectedNodes":[18]},{"coordinate":[7,5],"connectedNodes":[12]},{"coordinate":[6,0],"connectedNodes":[15]},{"coordinate":[1,1],"connectedNodes":[20]}]',
            pythonEnabled=False, theme=snow, model_solution='[5]',
            traffic_lights='[{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":4,"y":4},"direction":"N","startTime":0,"startingState":"GREEN"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":4,"y":2},"direction":"S","startTime":0,"startingState":"GREEN"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":4,"y":3},"direction":"E","startTime":0,"startingState":"RED"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":2,"y":3},"direction":"E","startTime":0,"startingState":"RED"}]'
        )
        level70.save()
        set_decor(level70, json.loads('[{"url":"decor/snow/tree2.svg","height":100,"width":100,"y":418,"x":112,"decorName":"tree2"},{"url":"decor/snow/pond.svg","height":100,"width":150,"y":588,"x":302,"decorName":"pond"},{"url":"decor/snow/tree1.svg","height":100,"width":100,"y":418,"x":697,"decorName":"tree1"},{"url":"decor/snow/bush.svg","height":50,"width":50,"y":59,"x":560,"decorName":"bush"},{"url":"decor/snow/bush.svg","height":50,"width":50,"y":180,"x":297,"decorName":"bush"},{"url":"decor/snow/bush.svg","height":50,"width":50,"y":250,"x":371,"decorName":"bush"},{"url":"decor/snow/bush.svg","height":50,"width":50,"y":188,"x":358,"decorName":"bush"},{"url":"decor/snow/bush.svg","height":50,"width":50,"y":195,"x":493,"decorName":"bush"},{"url":"decor/snow/bush.svg","height":50,"width":50,"y":64,"x":116,"decorName":"bush"},{"url":"decor/snow/bush.svg","height":50,"width":50,"y":61,"x":176,"decorName":"bush"},{"url":"decor/snow/bush.svg","height":50,"width":50,"y":58,"x":243,"decorName":"bush"},{"url":"decor/snow/bush.svg","height":50,"width":50,"y":60,"x":307,"decorName":"bush"},{"url":"decor/snow/bush.svg","height":50,"width":50,"y":63,"x":370,"decorName":"bush"},{"url":"decor/snow/bush.svg","height":50,"width":50,"y":62,"x":434,"decorName":"bush"},{"url":"decor/snow/bush.svg","height":50,"width":50,"y":60,"x":494,"decorName":"bush"}]'))
        set_blocks(level70, json.loads('[{"type":"turn_left","number":1},{"type":"turn_right","number":2},{"type":"turn_around","number":1},{"type":"controls_repeat_while","number":null},{"type":"controls_repeat_until","number":1},{"type":"at_destination","number":1}]'))
        return level70

    def create_level71():
        level71 = Level(
            name='71',
            default=True,
            path='[{"coordinate":[1,2],"connectedNodes":[2]},{"coordinate":[2,4],"connectedNodes":[3,4,12]},{"coordinate":[1,3],"connectedNodes":[3,0]},{"coordinate":[1,4],"connectedNodes":[1,2]},{"coordinate":[2,5],"connectedNodes":[5,1]},{"coordinate":[2,6],"connectedNodes":[11,6,4]},{"coordinate":[3,6],"connectedNodes":[5,7]},{"coordinate":[4,6],"connectedNodes":[6,8]},{"coordinate":[4,5],"connectedNodes":[7,9]},{"coordinate":[4,4],"connectedNodes":[10,8]},{"coordinate":[3,4],"connectedNodes":[9]},{"coordinate":[1,6],"connectedNodes":[5]},{"coordinate":[2,3],"connectedNodes":[1]}]',
            traffic_lights='[]',
            destinations='[[3,4]]',
            origin='{"coordinate":[1,2],"direction":"N"}',
            max_fuel=50,
            theme=Theme.objects.get(id=2),
            character=Character.objects.get(name='Van'),
            blocklyEnabled=True,
            pythonEnabled=False,
            model_solution='[7]',
        )
        level71.save()
        set_decor(level71, json.loads('[{"x":658,"y":505,"decorName":"tree2"},{"x":619,"y":611,"decorName":"tree2"},{"x":687,"y":700,"decorName":"tree2"},{"x":716,"y":356,"decorName":"bush"},{"x":473,"y":54,"decorName":"bush"},{"x":337,"y":227,"decorName":"bush"},{"x":265,"y":159,"decorName":"bush"},{"x":411,"y":0,"decorName":"bush"},{"x":412,"y":127,"decorName":"bush"},{"x":354,"y":80,"decorName":"bush"},{"x":207,"y":85,"decorName":"bush"},{"x":297,"y":15,"decorName":"bush"}]'))
        set_blocks(level71, json.loads('[{"type":"move_forwards","number":1},{"type":"turn_left","number":1},{"type":"turn_right","number":1},{"type":"turn_around","number":1},{"type":"controls_repeat_until"},{"type":"controls_if"},{"type":"at_destination"},{"type":"road_exists","number":1}]'))
        return level71

    level59 = create_level59()
    level60 = create_level60()
    level68 = create_level68()
    level61 = create_level61()
    level70 = create_level70()
    level71 = create_level71()

    level68.next_level_id = level61.id
    level61.next_level_id = level70.id
    level70.next_level_id = level71.id
    level68.save()
    level61.save()
    level70.save()

    level51 = Level.objects.get(name="51", default=True)
    level51.next_level_id = level59.id
    level59.next_level_id = level60.id
    level51.save()
    level59.save()

    episode9 = Episode(name="Blockly Brain Teasers", first_level=level68, r_branchiness=0.5,
                       r_loopiness=0.1, r_num_tiles=35, r_curviness=0.2, r_pythonEnabled=0,
                       r_blocklyEnabled=1, r_trafficLights=1, in_development=True)
    episode9.save()


# Add new level 52 to 65
def add_levels_63_to_65(apps, schema_editor):

    Level = apps.get_model('game', 'Level')
    LevelDecor = apps.get_model('game', 'LevelDecor')
    LevelBlock = apps.get_model('game', 'LevelBlock')
    Block = apps.get_model('game', 'Block')
    Character = apps.get_model('game', 'Character')
    Theme = apps.get_model('game', 'Theme')

    def set_decor(level, decor):
        set_decor_inner(level, decor, LevelDecor)

    def set_blocks(level, blocks):
        set_blocks_inner(level, blocks, LevelBlock, Block)

    def create_level63():
        path = ('[{"coordinate":[0,1],"connectedNodes":[24]},'
                + '{"coordinate":[1,2],"connectedNodes":[2,24]},'
                + '{"coordinate":[1,3],"connectedNodes":[3,1]},'
                + '{"coordinate":[2,3],"connectedNodes":[2,4]},'
                + '{"coordinate":[2,2],"connectedNodes":[3,5]},'
                + '{"coordinate":[3,2],"connectedNodes":[4,6]},'
                + '{"coordinate":[4,2],"connectedNodes":[5,7]},'
                + '{"coordinate":[4,3],"connectedNodes":[8,6]},'
                + '{"coordinate":[4,4],"connectedNodes":[9,7]},'
                + '{"coordinate":[5,4],"connectedNodes":[8,10]},'
                + '{"coordinate":[5,3],"connectedNodes":[9,11]},'
                + '{"coordinate":[6,3],"connectedNodes":[10,12]},'
                + '{"coordinate":[6,4],"connectedNodes":[13,11]},'
                + '{"coordinate":[6,5],"connectedNodes":[14,12]},'
                + '{"coordinate":[7,5],"connectedNodes":[13,15]},'
                + '{"coordinate":[7,4],"connectedNodes":[14,16]},'
                + '{"coordinate":[8,4],"connectedNodes":[15,17]},'
                + '{"coordinate":[8,3],"connectedNodes":[16,18]},'
                + '{"coordinate":[8,2],"connectedNodes":[19,17]},'
                + '{"coordinate":[7,2],"connectedNodes":[18,20]},'
                + '{"coordinate":[7,1],"connectedNodes":[19,21]},'
                + '{"coordinate":[7,0],"connectedNodes":[22,20]},'
                + '{"coordinate":[6,0],"connectedNodes":[23,21]},'
                + '{"coordinate":[6,1],"connectedNodes":[25,22]},'
                + '{"coordinate":[1,1],"connectedNodes":[0,1]},'
                + '{"coordinate":[5,1],"connectedNodes":[23]}]')

        decor = json.loads('[{"url":"decor/city/hospital.svg","height":157,"width":140,"y":291,"x":280,'
                           + '"decorName":"pond"}, {"url":"decor/city/school.svg","height":100,'
                           + '"width":100,"y":300,"x":706,"decorName":"tree2"},'
                           + '{"url":"decor/city/shop.svg","height":70,"width":70,"y":490,"x":785,'
                           + '"decorName":"tree1"}, {"url":"decor/city/shop.svg","height":70,'
                           + '"width":70,"y":129,"x":789,"decorName":"tree1"},'
                           + '{"url":"decor/city/bush.svg","height":50,"width":50,"y":184,"x":600,'
                           + '"decorName":"bush"}, {"url":"decor/city/bush.svg","height":50,"width":50,'
                           + '"y":208,"x":662,"decorName":"bush"}, {"url":"decor/city/bush.svg",'
                           + '"height":50,"width":50,"y":277,"x":641,"decorName":"bush"},'
                           + '{"url":"decor/city/bush.svg","height":50,"width":50,"y":255,"x":570,'
                           + '"decorName":"bush"}, {"url":"decor/city/bush.svg","height":50,"width":50,'
                           + '"y":282,"x":497,"decorName":"bush"}, {"url":"decor/city/bush.svg",'
                           + '"height":50,"width":50,"y":455,"x":286,"decorName":"bush"},'
                           + '{"url":"decor/city/bush.svg","height":50,"width":50,"y":453,"x":215,'
                           + '"decorName":"bush"}, {"url":"decor/city/bush.svg","height":50,"width":50,'
                           + '"y":391,"x":216,"decorName":"bush"}, {"url":"decor/city/bush.svg",'
                           + '"height":50,"width":50,"y":456,"x":357,"decorName":"bush"}]')

        level63 = Level(
            name='63', path=path, default=True, blocklyEnabled=True, destinations='[[5,1]]',
            max_fuel='50', traffic_lights='[]', theme=Theme.objects.get(name='city'),
            origin='{"coordinate":[0,1],"direction":"E"}', character=Character.objects.get(name="Van"),
            pythonEnabled=False, model_solution='[14]')
        level63.save()
        blocks = Block.objects.filter(type__in=['move_forwards', 'turn_left', 'turn_right', 'call_proc',
                                                'declare_proc'])
        for block in blocks:
            levelblock = LevelBlock(level=level63, type=block)
            levelblock.save()

        set_decor(level63, decor)

        return level63

    def create_level67():
        path = ('[{"coordinate":[4,7],"connectedNodes":[18]},'
                + '{"coordinate":[2,5],"connectedNodes":[2,19]},'
                + '{"coordinate":[1,5],"connectedNodes":[1,3]},'
                + '{"coordinate":[1,4],"connectedNodes":[2,4]},'
                + '{"coordinate":[1,3],"connectedNodes":[3,5]},'
                + '{"coordinate":[2,3],"connectedNodes":[4,6]},'
                + '{"coordinate":[2,2],"connectedNodes":[5,7]},'
                + '{"coordinate":[3,2],"connectedNodes":[6,8]},'
                + '{"coordinate":[3,1],"connectedNodes":[7,9]},'
                + '{"coordinate":[4,1],"connectedNodes":[8,10]},'
                + '{"coordinate":[4,2],"connectedNodes":[11,9]},'
                + '{"coordinate":[4,3],"connectedNodes":[12,10]},'
                + '{"coordinate":[3,3],"connectedNodes":[13,11]},'
                + '{"coordinate":[3,4],"connectedNodes":[14,12]},'
                + '{"coordinate":[4,4],"connectedNodes":[13,15]},'
                + '{"coordinate":[4,5],"connectedNodes":[16,14]},'
                + '{"coordinate":[5,5],"connectedNodes":[15,20]},'
                + '{"coordinate":[3,6],"connectedNodes":[19,18]},'
                + '{"coordinate":[3,7],"connectedNodes":[0,17]},'
                + '{"coordinate":[2,6],"connectedNodes":[17,1]},'
                + '{"coordinate":[5,4],"connectedNodes":[16,21]},'
                + '{"coordinate":[6,4],"connectedNodes":[20,22]},'
                + '{"coordinate":[6,3],"connectedNodes":[21,23]},'
                + '{"coordinate":[7,3],"connectedNodes":[22,24]},'
                + '{"coordinate":[7,2],"connectedNodes":[23,25]},'
                + '{"coordinate":[8,2],"connectedNodes":[24,26]},'
                + '{"coordinate":[8,1],"connectedNodes":[25,27]},'
                + '{"coordinate":[9,1],"connectedNodes":[26,28]},'
                + '{"coordinate":[9,0],"connectedNodes":[27]}]')

        level67 = Level(
            name='67',
            default=True,
            path=path,
            traffic_lights='[]',
            destinations='[[9,0]]',
            origin='{"coordinate":[4,7],"direction":"W"}',
            max_fuel=50,
            theme=Theme.objects.get(id=3),
            character=Character.objects.get(id='1'),
            blocklyEnabled=True,
            pythonEnabled=False,
            model_solution='[18, 19]'
        )

        decor = ('[{"x":191,"y":407,"decorName":"tree2"},{"x":388,"y":595,"decorName":"pond"},'
                 + '{"x":182,"y":688,"decorName":"tree1"},{"x":81,"y":584,"decorName":"tree1"},'
                 + '{"x":212,"y":184,"decorName":"bush"},{"x":165,"y":230,"decorName":"bush"},'
                 + '{"x":125,"y":279,"decorName":"bush"},{"x":262,"y":143,"decorName":"bush"},'
                 + '{"x":693,"y":386,"decorName":"tree1"},{"x":592,"y":476,"decorName":"tree1"},'
                 + '{"x":498,"y":319,"decorName":"tree1"},{"x":575,"y":596,"decorName":"pond"},'
                 + '{"x":574,"y":700,"decorName":"pond"},{"x":900,"y":203,"decorName":"tree1"},'
                 + '{"x":712,"y":102,"decorName":"tree1"},{"x":609,"y":216,"decorName":"tree1"},'
                 + '{"x":793,"y":290,"decorName":"tree1"},{"x":812,"y":0,"decorName":"tree1"}]')

        blocks = ('[{"type":"move_forwards"},{"type":"turn_left"},{"type":"turn_right"},'
                  + '{"type":"controls_repeat"},{"type":"call_proc"},{"type":"declare_proc"}]')

        level67.save()
        set_decor(level67, json.loads(decor))
        set_blocks(level67, json.loads(blocks))
        return level67

    def create_level65():
        path = ('[{"coordinate":[1,4],"connectedNodes":[1]},'
                + '{"coordinate":[2,4],"connectedNodes":[0,2]},'
                + '{"coordinate":[2,5],"connectedNodes":[3,1]},'
                + '{"coordinate":[3,5],"connectedNodes":[2,4,20]},'
                + '{"coordinate":[4,5],"connectedNodes":[3,5]},'
                + '{"coordinate":[4,4],"connectedNodes":[4,6]},'
                + '{"coordinate":[5,4],"connectedNodes":[5,7]},'
                + '{"coordinate":[5,5],"connectedNodes":[8,6]},'
                + '{"coordinate":[6,5],"connectedNodes":[7,11,9]},'
                + '{"coordinate":[7,5],"connectedNodes":[8,10]},'
                + '{"coordinate":[8,5],"connectedNodes":[9]},'
                + '{"coordinate":[6,6],"connectedNodes":[21,12,8]},'
                + '{"coordinate":[7,6],"connectedNodes":[11,13]},'
                + '{"coordinate":[8,6],"connectedNodes":[12,14]},'
                + '{"coordinate":[9,6],"connectedNodes":[13,15]},'
                + '{"coordinate":[9,5],"connectedNodes":[14,16]},'
                + '{"coordinate":[9,4],"connectedNodes":[17,15]},'
                + '{"coordinate":[8,4],"connectedNodes":[16,18]},'
                + '{"coordinate":[8,3],"connectedNodes":[19,17]},'
                + '{"coordinate":[7,3],"connectedNodes":[18,25]},'
                + '{"coordinate":[3,4],"connectedNodes":[3]},'
                + '{"coordinate":[6,7],"connectedNodes":[22,11]},'
                + '{"coordinate":[5,7],"connectedNodes":[23,21]},'
                + '{"coordinate":[4,7],"connectedNodes":[24,22]},'
                + '{"coordinate":[3,7],"connectedNodes":[23]},'
                + '{"coordinate":[7,2],"connectedNodes":[26,19]},'
                + '{"coordinate":[6,2],"connectedNodes":[27,29,25]},'
                + '{"coordinate":[5,2],"connectedNodes":[28,26]},'
                + '{"coordinate":[4,2],"connectedNodes":[27]},'
                + '{"coordinate":[6,3],"connectedNodes":[30,26]},'
                + '{"coordinate":[5,3],"connectedNodes":[31,29]},'
                + '{"coordinate":[4,3],"connectedNodes":[32,30]},'
                + '{"coordinate":[3,3],"connectedNodes":[31,33]},'
                + '{"coordinate":[3,2],"connectedNodes":[45,32,34]},'
                + '{"coordinate":[3,1],"connectedNodes":[33,35]},'
                + '{"coordinate":[4,1],"connectedNodes":[34,36]},'
                + '{"coordinate":[4,0],"connectedNodes":[35,37]},'
                + '{"coordinate":[5,0],"connectedNodes":[36,38]},'
                + '{"coordinate":[5,1],"connectedNodes":[39,37]},'
                + '{"coordinate":[6,1],"connectedNodes":[38,40]},'
                + '{"coordinate":[7,1],"connectedNodes":[39,41]},'
                + '{"coordinate":[8,1],"connectedNodes":[40,42,44]},'
                + '{"coordinate":[8,2],"connectedNodes":[43,41]},'
                + '{"coordinate":[9,2],"connectedNodes":[42]},'
                + '{"coordinate":[8,0],"connectedNodes":[41]},'
                + '{"coordinate":[2,2],"connectedNodes":[46,33]},'
                + '{"coordinate":[1,2],"connectedNodes":[45]}]')

        level65 = Level(
            name='65',
            default=True,
            path=path,
            traffic_lights='[]',
            destinations='[[9,2]]',
            origin='{"coordinate":[1,4],"direction":"E"}',
            max_fuel=50,
            theme=Theme.objects.get(id=2),
            character=Character.objects.get(id='1'),
            blocklyEnabled=True,
            pythonEnabled=False,
            model_solution='[27]'
        )

        decor = ('[{"x":726,"y":408,"decorName":"tree2"},{"x":598,"y":400,"decorName":"tree2"},'
                 + '{"x":503,"y":610,"decorName":"tree1"},{"x":44,"y":607,"decorName":"pond"},'
                 + '{"x":700,"y":698,"decorName":"tree1"},{"x":361,"y":19,"decorName":"bush"},'
                 + '{"x":308,"y":56,"decorName":"bush"},{"x":261,"y":107,"decorName":"bush"},'
                 + '{"x":218,"y":159,"decorName":"bush"},{"x":629,"y":56,"decorName":"bush"},'
                 + '{"x":572,"y":13,"decorName":"bush"},{"x":5,"y":510,"decorName":"tree1"}]')

        block = ('[{"type":"move_forwards"},{"type":"turn_left"},{"type":"turn_right"},'
                 + '{"type":"controls_repeat"},{"type":"call_proc"},{"type":"declare_proc"}]')

        level65.save()
        set_decor(level65, json.loads(decor))
        set_blocks(level65, json.loads(block))
        return level65

    level63 = create_level63()
    level62 = Level.objects.get(name='62', default=True)
    level62.next_level = level63
    level62.save()

    level67 = create_level67()
    level63.next_level = level67
    level63.save()

    level65 = create_level65()
    level67.next_level = level65
    level67.save()


# Add levels 80-86, 100-107
# Add episodes 10, 11
def add_levels_80_to_107(apps, schema_editor):

    Level = apps.get_model('game', 'Level')
    Episode = apps.get_model('game', 'Episode')
    Theme = apps.get_model('game', 'Theme')
    Character = apps.get_model('game', 'Character')
    LevelDecor = apps.get_model('game', 'LevelDecor')
    LevelBlock = apps.get_model('game', 'LevelBlock')

    grass = Theme.objects.get(name='grass')
    snow = Theme.objects.get(name='snow')
    farm = Theme.objects.get(name='farm')
    city = Theme.objects.get(name='city')

    van = Character.objects.get(name='Van')

    # keep track of where we're copying the vague basis of the python levels
    levelPairs = []

    # from level6
    levelPairs.append(["6","80"])
    level80 = Level(name='80', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[6, 1]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    origin='{"coordinate":[0, 4], "direction":"E"}',
                    path='[{"coordinate":[0,4],"connectedNodes":[1]},{"coordinate":[1,4],"connectedNodes":[0,2]},{"coordinate":[2,4],"connectedNodes":[1,3]},{"coordinate":[3,4],"connectedNodes":[2,4]},{"coordinate":[3,5],"connectedNodes":[5,3]},{"coordinate":[4,5],"connectedNodes":[4,6]},{"coordinate":[5,5],"connectedNodes":[5,7]},{"coordinate":[5,4],"connectedNodes":[6,8]},{"coordinate":[5,3],"connectedNodes":[7,9]},{"coordinate":[5,2],"connectedNodes":[8,10]},{"coordinate":[5,1],"connectedNodes":[9,11]},{"coordinate":[6,1],"connectedNodes":[10]}]',
                    pythonEnabled=True, theme=grass, threads=1, traffic_lights='[]')

    # from level13
    levelPairs.append(["13","81"])
    level81 = Level(name='81', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[0, 1]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    origin='{"coordinate":[2, 7], "direction":"S"}',
                    path='[{"coordinate":[2,7],"connectedNodes":[1]},{"coordinate":[2,6],"connectedNodes":[0,2]},{"coordinate":[3,6],"connectedNodes":[1,3,10]},{"coordinate":[4,6],"connectedNodes":[2,4]},{"coordinate":[5,6],"connectedNodes":[3,5]},{"coordinate":[6,6],"connectedNodes":[4,6]},{"coordinate":[6,5],"connectedNodes":[5,7]},{"coordinate":[6,4],"connectedNodes":[13,6,8]},{"coordinate":[6,3],"connectedNodes":[7,9]},{"coordinate":[6,2],"connectedNodes":[8,14]},{"coordinate":[3,5],"connectedNodes":[2,11]},{"coordinate":[3,4],"connectedNodes":[10,12]},{"coordinate":[4,4],"connectedNodes":[11,13,18]},{"coordinate":[5,4],"connectedNodes":[12,7]},{"coordinate":[6,1],"connectedNodes":[15,9]},{"coordinate":[5,1],"connectedNodes":[16,14]},{"coordinate":[4,1],"connectedNodes":[19,17,15]},{"coordinate":[4,2],"connectedNodes":[18,16]},{"coordinate":[4,3],"connectedNodes":[12,17]},{"coordinate":[3,1],"connectedNodes":[20,16]},{"coordinate":[2,1],"connectedNodes":[21,19]},{"coordinate":[1,1],"connectedNodes":[22,20]},{"coordinate":[0,1],"connectedNodes":[21]}]',
                    pythonEnabled=True, theme=grass, threads=1, traffic_lights='[]')

    # from level21
    levelPairs.append(["21","82"])
    level82 = Level(name='82', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[3, 7]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    origin='{"coordinate":[1, 6], "direction":"S"}',
                    path='[{"coordinate":[1,6],"connectedNodes":[2]},{"coordinate":[1,4],"connectedNodes":[2,3]},{"coordinate":[1,5],"connectedNodes":[0,1]},{"coordinate":[2,4],"connectedNodes":[1,4]},{"coordinate":[2,3],"connectedNodes":[3,5]},{"coordinate":[3,3],"connectedNodes":[4,6]},{"coordinate":[4,3],"connectedNodes":[5,7]},{"coordinate":[4,4],"connectedNodes":[8,6]},{"coordinate":[5,4],"connectedNodes":[7,9]},{"coordinate":[5,5],"connectedNodes":[10,8]},{"coordinate":[5,6],"connectedNodes":[11,9]},{"coordinate":[4,6],"connectedNodes":[12,10]},{"coordinate":[4,7],"connectedNodes":[13,11]},{"coordinate":[3,7],"connectedNodes":[12]}]',
                    pythonEnabled=True, theme=grass, threads=1, traffic_lights='[]')

    # from level29
    levelPairs.append(["29","83"])
    level83 = Level(name='83', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[4, 3]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    origin='{"coordinate":[0, 3], "direction":"E"}',
                    path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[2,3],"connectedNodes":[1,3]},{"coordinate":[3,3],"connectedNodes":[2,4]},{"coordinate":[4,3],"connectedNodes":[3]}]',
                    pythonEnabled=True, theme=grass, threads=1, traffic_lights='[]')

    # from level35
    levelPairs.append(["35","84"])
    level84 = Level(name='84', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[1, 1]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    origin='{"coordinate":[8, 6], "direction":"W"}',
                    path='[{"coordinate":[8,6],"connectedNodes":[1]},{"coordinate":[7,6],"connectedNodes":[2,0]},{"coordinate":[6,6],"connectedNodes":[3,1]},{"coordinate":[5,6],"connectedNodes":[4,2]},{"coordinate":[4,6],"connectedNodes":[3,5]},{"coordinate":[4,5],"connectedNodes":[4,6]},{"coordinate":[4,4],"connectedNodes":[5,7]},{"coordinate":[5,4],"connectedNodes":[6,8]},{"coordinate":[6,4],"connectedNodes":[7,9]},{"coordinate":[7,4],"connectedNodes":[8,10]},{"coordinate":[8,4],"connectedNodes":[9,11]},{"coordinate":[8,3],"connectedNodes":[10,12]},{"coordinate":[8,2],"connectedNodes":[13,11]},{"coordinate":[7,2],"connectedNodes":[14,12]},{"coordinate":[6,2],"connectedNodes":[15,13]},{"coordinate":[5,2],"connectedNodes":[16,14]},{"coordinate":[4,2],"connectedNodes":[15,17]},{"coordinate":[4,1],"connectedNodes":[18,16]},{"coordinate":[3,1],"connectedNodes":[19,17]},{"coordinate":[2,1],"connectedNodes":[20,18]},{"coordinate":[1,1],"connectedNodes":[19]}]',
                    pythonEnabled=True, theme=grass, threads=1, traffic_lights='[]')

    # from level 36
    levelPairs.append(["36","85"])
    level85 = Level(name='85', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[5, 3]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    origin='{"coordinate":[0, 3], "direction":"E"}',
                    path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[1,4],"connectedNodes":[1,3]},{"coordinate":[1,5],"connectedNodes":[2,4]},{"coordinate":[1,6],"connectedNodes":[3,5]},{"coordinate":[2,6],"connectedNodes":[4,6]},{"coordinate":[2,5],"connectedNodes":[5,7]},{"coordinate":[3,5],"connectedNodes":[6,8]},{"coordinate":[3,4],"connectedNodes":[7,9]},{"coordinate":[3,3],"connectedNodes":[8,10]},{"coordinate":[3,2],"connectedNodes":[9,11]},{"coordinate":[4,2],"connectedNodes":[10,12]},{"coordinate":[4,3],"connectedNodes":[11,13]},{"coordinate":[5,3],"connectedNodes":[12]}] ',
                    pythonEnabled=True, theme=grass, threads=1, traffic_lights='[]')

    # from level47
    levelPairs.append(["47","86"])
    level86 = Level(name='86', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[4, 3]]', direct_drive=False, fuel_gauge=True, max_fuel=50,
                    origin='{"coordinate":[6, 1], "direction":"N"}',
                    path='[{"coordinate":[6,1],"connectedNodes":[1]},{"coordinate":[6,2],"connectedNodes":[2,0]},{"coordinate":[6,3],"connectedNodes":[3,1]},{"coordinate":[6,4],"connectedNodes":[4,2]},{"coordinate":[6,5],"connectedNodes":[5,3]},{"coordinate":[6,6],"connectedNodes":[6,4]},{"coordinate":[5,6],"connectedNodes":[7,5]},{"coordinate":[4,6],"connectedNodes":[8,6]},{"coordinate":[3,6],"connectedNodes":[9,7]},{"coordinate":[2,6],"connectedNodes":[8,10]},{"coordinate":[2,5],"connectedNodes":[9,11]},{"coordinate":[2,4],"connectedNodes":[10,12]},{"coordinate":[2,3],"connectedNodes":[11,13]},{"coordinate":[2,2],"connectedNodes":[12,14]},{"coordinate":[3,2],"connectedNodes":[13,15]},{"coordinate":[4,2],"connectedNodes":[14,16]},{"coordinate":[4,3],"connectedNodes":[15]}]',
                    pythonEnabled=True, theme=grass, threads=1,
                    traffic_lights='[{"direction": "N", "startTime": 0, "sourceCoordinate": {"y":3, "x": 6}, "greenDuration": 3, "startingState": "RED", "redDuration": 3}, {"direction":"W", "startTime": 0, "sourceCoordinate": {"y": 6, "x": 5}, "greenDuration":3, "startingState": "RED", "redDuration": 3}, {"direction": "S", "startTime":0, "sourceCoordinate": {"y": 5, "x": 2}, "greenDuration": 3, "startingState":"RED", "redDuration": 3}, {"direction": "E", "startTime": 0, "sourceCoordinate":{"y": 2, "x": 3}, "greenDuration": 3, "startingState": "GREEN", "redDuration":3}]')


    level80.save()
    level81.save()
    level82.save()
    level83.save()
    level84.save()
    level85.save()
    level86.save()
    level80.next_level_id = level81.id
    level81.next_level_id = level82.id
    level82.next_level_id = level83.id
    level83.next_level_id = level84.id
    level84.next_level_id = level85.id
    level85.next_level_id = level86.id
    level80.save()
    level81.save()
    level82.save()
    level83.save()
    level84.save()
    level85.save()
    level86.save()

    # from level7
    levelPairs.append(["7","100"])
    level100 = Level(name='100', anonymous=False, blocklyEnabled=False, character=van, default=True,
                     destinations='[[5, 3]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                     origin='{"coordinate":[0, 3], "direction":"E"}',
                     path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[1,4],"connectedNodes":[1,3]},{"coordinate":[1,5],"connectedNodes":[2,4]},{"coordinate":[1,6],"connectedNodes":[3,5]},{"coordinate":[2,6],"connectedNodes":[4,6]},{"coordinate":[2,5],"connectedNodes":[5,7]},{"coordinate":[3,5],"connectedNodes":[6,8]},{"coordinate":[3,4],"connectedNodes":[7,9]},{"coordinate":[3,3],"connectedNodes":[8,10]},{"coordinate":[3,2],"connectedNodes":[9,11]},{"coordinate":[4,2],"connectedNodes":[10,12]},{"coordinate":[4,3],"connectedNodes":[11,13]},{"coordinate":[5,3],"connectedNodes":[12]}]',
                     pythonEnabled=True, theme=grass, threads=1, traffic_lights='[]')

    # from level14
    levelPairs.append(["14","101"])
    level101 = Level(name='101', anonymous=False, blocklyEnabled=False, character=van, default=True,
                     destinations='[[2, 5]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                     origin='{"coordinate":[7, 2], "direction":"W"}',
                     path='[{"coordinate":[7,2],"connectedNodes":[27]},{"coordinate":[4,2],"connectedNodes":[4,14]},{"coordinate":[3,1],"connectedNodes":[3,14]},{"coordinate":[2,1],"connectedNodes":[7,2]},{"coordinate":[4,3],"connectedNodes":[10,5,1]},{"coordinate":[5,3],"connectedNodes":[4,6]},{"coordinate":[6,3],"connectedNodes":[5,11,27]},{"coordinate":[1,1],"connectedNodes":[8,3]},{"coordinate":[1,2],"connectedNodes":[21,7]},{"coordinate":[3,4],"connectedNodes":[16,10]},{"coordinate":[4,4],"connectedNodes":[9,4]},{"coordinate":[6,4],"connectedNodes":[12,6]},{"coordinate":[6,5],"connectedNodes":[20,11]},{"coordinate":[5,1],"connectedNodes":[14,15]},{"coordinate":[4,1],"connectedNodes":[2,1,13]},{"coordinate":[6,1],"connectedNodes":[13,27]},{"coordinate":[3,5],"connectedNodes":[26,17,9]},{"coordinate":[3,6],"connectedNodes":[18,16]},{"coordinate":[4,6],"connectedNodes":[17,19]},{"coordinate":[5,6],"connectedNodes":[18,20]},{"coordinate":[6,6],"connectedNodes":[19,12]},{"coordinate":[2,2],"connectedNodes":[8,22]},{"coordinate":[2,3],"connectedNodes":[23,21]},{"coordinate":[1,3],"connectedNodes":[24,22]},{"coordinate":[1,4],"connectedNodes":[25,23]},{"coordinate":[1,5],"connectedNodes":[26,24]},{"coordinate":[2,5],"connectedNodes":[25,16]},{"coordinate":[6,2],"connectedNodes":[6,0,15]}]',
                     pythonEnabled=True, theme=grass, threads=1, traffic_lights='[]')


    # from level26
    levelPairs.append(["26","102"])
    level102 = Level(name='102', anonymous=False, blocklyEnabled=False, character=van, default=True,
                     destinations='[[8, 3]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                     origin='{"coordinate":[4, 6], "direction":"S"}',
                     path='[{"coordinate":[4,6],"connectedNodes":[1]},{"coordinate":[4,5],"connectedNodes":[0,2]},{"coordinate":[4,4],"connectedNodes":[1,3]},{"coordinate":[4,3],"connectedNodes":[2,4]},{"coordinate":[5,3],"connectedNodes":[3,5]},{"coordinate":[6,3],"connectedNodes":[4,6]},{"coordinate":[7,3],"connectedNodes":[5,7]},{"coordinate":[8,3],"connectedNodes":[6]}]',
                     pythonEnabled=True, theme=snow, threads=1, traffic_lights='[]')

    # from level32
    levelPairs.append(["32","103"])
    level103 = Level(name='103', anonymous=False, blocklyEnabled=False, character=van, default=True,
                     destinations='[[5, 0]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                     origin='{"coordinate":[2, 7], "direction":"S"}',
                     path='[{"coordinate":[2,7],"connectedNodes":[1]},{"coordinate":[2,6],"connectedNodes":[0,2]},{"coordinate":[3,6],"connectedNodes":[1,3]},{"coordinate":[3,5],"connectedNodes":[2,4]},{"coordinate":[3,4],"connectedNodes":[3,5]},{"coordinate":[4,4],"connectedNodes":[4,6]},{"coordinate":[4,3],"connectedNodes":[5,7]},{"coordinate":[4,2],"connectedNodes":[6,8]},{"coordinate":[5,2],"connectedNodes":[7,9]},{"coordinate":[5,1],"connectedNodes":[8,10]},{"coordinate":[5,0],"connectedNodes":[9]}]',
                     pythonEnabled=True, theme=grass, threads=1, traffic_lights='[]')

    # from level 34
    levelPairs.append(["34","104"])
    level104 = Level(name='104', anonymous=False, blocklyEnabled=False, character=van, default=True,
                     destinations='[[6, 6]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                     origin='{"coordinate":[1, 2], "direction":"E"}',
                     path='[{"coordinate":[1,2],"connectedNodes":[1]},{"coordinate":[2,2],"connectedNodes":[0,2]},{"coordinate":[3,2],"connectedNodes":[1,3]},{"coordinate":[4,2],"connectedNodes":[2,4]},{"coordinate":[5,2],"connectedNodes":[3,5]},{"coordinate":[6,2],"connectedNodes":[4,6]},{"coordinate":[7,2],"connectedNodes":[5,7]},{"coordinate":[8,2],"connectedNodes":[6,8]},{"coordinate":[8,3],"connectedNodes":[9,7]},{"coordinate":[8,4],"connectedNodes":[10,8]},{"coordinate":[8,5],"connectedNodes":[11,9]},{"coordinate":[8,6],"connectedNodes":[12,10]},{"coordinate":[8,7],"connectedNodes":[13,11]},{"coordinate":[7,7],"connectedNodes":[14,12]},{"coordinate":[6,7],"connectedNodes":[15,13]},{"coordinate":[5,7],"connectedNodes":[16,14]},{"coordinate":[4,7],"connectedNodes":[17,15]},{"coordinate":[3,7],"connectedNodes":[16,18]},{"coordinate":[3,6],"connectedNodes":[17,19]},{"coordinate":[3,5],"connectedNodes":[18,20]},{"coordinate":[3,4],"connectedNodes":[19,21]},{"coordinate":[4,4],"connectedNodes":[20,22]},{"coordinate":[5,4],"connectedNodes":[21,23]},{"coordinate":[6,4],"connectedNodes":[22,24]},{"coordinate":[6,5],"connectedNodes":[25,23]},{"coordinate":[6,6],"connectedNodes":[24]}]',
                     pythonEnabled=True, theme=grass, threads=1, traffic_lights='[]')

    # from level38
    levelPairs.append(["38","105"])
    level105 = Level(name='105', anonymous=False, blocklyEnabled=False, character=van, default=True,
                     destinations='[[6, 0]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                     origin='{"coordinate":[7, 6], "direction":"W"}',
                     path='[{"coordinate":[7,6],"connectedNodes":[1]},{"coordinate":[6,6],"connectedNodes":[2,0]},{"coordinate":[5,6],"connectedNodes":[3,1]},{"coordinate":[4,6],"connectedNodes":[4,2]},{"coordinate":[3,6],"connectedNodes":[5,3]},{"coordinate":[2,6],"connectedNodes":[4,6]},{"coordinate":[2,5],"connectedNodes":[7,5]},{"coordinate":[1,5],"connectedNodes":[8,6]},{"coordinate":[1,6],"connectedNodes":[9,7]},{"coordinate":[0,6],"connectedNodes":[8,10]},{"coordinate":[0,5],"connectedNodes":[9,11]},{"coordinate":[0,4],"connectedNodes":[10,12]},{"coordinate":[1,4],"connectedNodes":[11,13]},{"coordinate":[2,4],"connectedNodes":[12,14]},{"coordinate":[3,4],"connectedNodes":[13,15]},{"coordinate":[3,5],"connectedNodes":[16,14]},{"coordinate":[4,5],"connectedNodes":[15,17]},{"coordinate":[5,5],"connectedNodes":[16,18]},{"coordinate":[6,5],"connectedNodes":[17,19]},{"coordinate":[7,5],"connectedNodes":[18,20]},{"coordinate":[7,4],"connectedNodes":[21,19]},{"coordinate":[6,4],"connectedNodes":[22,20]},{"coordinate":[5,4],"connectedNodes":[23,21]},{"coordinate":[4,4],"connectedNodes":[22,24]},{"coordinate":[4,3],"connectedNodes":[25,23]},{"coordinate":[3,3],"connectedNodes":[26,24]},{"coordinate":[2,3],"connectedNodes":[27,25]},{"coordinate":[1,3],"connectedNodes":[26,28]},{"coordinate":[1,2],"connectedNodes":[27,29]},{"coordinate":[2,2],"connectedNodes":[28,30]},{"coordinate":[3,2],"connectedNodes":[29,31]},{"coordinate":[3,1],"connectedNodes":[30,32]},{"coordinate":[3,0],"connectedNodes":[31,33]},{"coordinate":[4,0],"connectedNodes":[32,34]},{"coordinate":[4,1],"connectedNodes":[35,33]},{"coordinate":[4,2],"connectedNodes":[36,34]},{"coordinate":[5,2],"connectedNodes":[35,37]},{"coordinate":[6,2],"connectedNodes":[36,38]},{"coordinate":[6,1],"connectedNodes":[37,39]},{"coordinate":[6,0],"connectedNodes":[38]}]',
                     pythonEnabled=True, theme=grass, threads=1, traffic_lights='[]')

    # from level43
    levelPairs.append(["43","106"])
    level106 = Level(name='106', anonymous=False, blocklyEnabled=False, character=van, default=True,
                     destinations='[[5, 7]]', direct_drive=False, fuel_gauge=True, max_fuel=50,
                     origin='{"coordinate":[0, 5], "direction":"E"}',
                     path='[{"coordinate":[0,5],"connectedNodes":[1]},{"coordinate":[1,5],"connectedNodes":[0,2]},{"coordinate":[1,4],"connectedNodes":[1,3]},{"coordinate":[2,4],"connectedNodes":[2,4]},{"coordinate":[2,3],"connectedNodes":[5,3]},{"coordinate":[1,3],"connectedNodes":[4,6]},{"coordinate":[1,2],"connectedNodes":[5,7,8]},{"coordinate":[2,2],"connectedNodes":[6,9]},{"coordinate":[1,1],"connectedNodes":[6,9]},{"coordinate":[2,1],"connectedNodes":[8,7,10]},{"coordinate":[2,0],"connectedNodes":[9,11]},{"coordinate":[3,0],"connectedNodes":[10,12]},{"coordinate":[4,0],"connectedNodes":[11,13]},{"coordinate":[4,1],"connectedNodes":[14,12]},{"coordinate":[3,1],"connectedNodes":[15,13]},{"coordinate":[3,2],"connectedNodes":[16,14]},{"coordinate":[3,3],"connectedNodes":[17,15]},{"coordinate":[4,3],"connectedNodes":[16,18]},{"coordinate":[5,3],"connectedNodes":[17,19,28,20]},{"coordinate":[5,4],"connectedNodes":[29,18]},{"coordinate":[5,2],"connectedNodes":[18,21]},{"coordinate":[5,1],"connectedNodes":[20,22]},{"coordinate":[5,0],"connectedNodes":[21,23]},{"coordinate":[6,0],"connectedNodes":[22,24]},{"coordinate":[7,0],"connectedNodes":[23,25]},{"coordinate":[7,1],"connectedNodes":[26,24]},{"coordinate":[7,2],"connectedNodes":[27,25]},{"coordinate":[7,3],"connectedNodes":[28,26]},{"coordinate":[6,3],"connectedNodes":[18,27]},{"coordinate":[5,5],"connectedNodes":[30,40,19]},{"coordinate":[4,5],"connectedNodes":[31,29]},{"coordinate":[3,5],"connectedNodes":[32,30]},{"coordinate":[3,6],"connectedNodes":[33,31]},{"coordinate":[3,7],"connectedNodes":[41,34,32]},{"coordinate":[4,7],"connectedNodes":[33,35]},{"coordinate":[5,7],"connectedNodes":[34,36]},{"coordinate":[6,7],"connectedNodes":[35,37]},{"coordinate":[7,7],"connectedNodes":[36,38]},{"coordinate":[7,6],"connectedNodes":[37,39]},{"coordinate":[7,5],"connectedNodes":[40,38]},{"coordinate":[6,5],"connectedNodes":[29,39]},{"coordinate":[2,7],"connectedNodes":[42,33]},{"coordinate":[1,7],"connectedNodes":[41]}]',
                     pythonEnabled=True, theme=grass, threads=1, traffic_lights='[]')

    # from level50
    levelPairs.append(["50","107"])
    level107 = Level(name='107', anonymous=False, blocklyEnabled=False, character=van, default=True,
                     destinations='[[6, 4]]', direct_drive=False, fuel_gauge=True, max_fuel=50,
                     origin='{"coordinate":[0, 3], "direction":"E"}',
                     path='[{"coordinate":[0,3],"connectedNodes":[1]}, {"coordinate":[1,3],"connectedNodes":[0,27,2]},{"coordinate":[1,2],"connectedNodes":[1,3]}, {"coordinate":[1,1],"connectedNodes":[2,4]},{"coordinate":[2,1],"connectedNodes":[3,6,5]}, {"coordinate":[2,0],"connectedNodes":[4]},{"coordinate":[3,1],"connectedNodes":[4,7]}, {"coordinate":[4,1],"connectedNodes":[6,8]},{"coordinate":[4,2],"connectedNodes":[9,11,7]}, {"coordinate":[4,3],"connectedNodes":[10,36,8]},{"coordinate":[3,3],"connectedNodes":[9]}, {"coordinate":[5,2],"connectedNodes":[8,12]},{"coordinate":[6,2],"connectedNodes":[11,15,13]}, {"coordinate":[6,1],"connectedNodes":[12,14]},{"coordinate":[6,0],"connectedNodes":[13]}, {"coordinate":[7,2],"connectedNodes":[12,16]},{"coordinate":[8,2],"connectedNodes":[15,25,17]}, {"coordinate":[8,1],"connectedNodes":[16,18]},{"coordinate":[8,0],"connectedNodes":[17,19]}, {"coordinate":[9,0],"connectedNodes":[18,20]},{"coordinate":[9,1],"connectedNodes":[21,19]}, {"coordinate":[9,2],"connectedNodes":[22,20]},{"coordinate":[9,3],"connectedNodes":[23,21]}, {"coordinate":[9,4],"connectedNodes":[24,22]},{"coordinate":[8,4],"connectedNodes":[26,23,25]}, {"coordinate":[8,3],"connectedNodes":[24,16]},{"coordinate":[7,4],"connectedNodes":[42,28,24]}, {"coordinate":[1,4],"connectedNodes":[41,1]},{"coordinate":[7,5],"connectedNodes":[29,26]}, {"coordinate":[7,6],"connectedNodes":[32,30,28]},{"coordinate":[8,6],"connectedNodes":[29,31]}, {"coordinate":[9,6],"connectedNodes":[30]},{"coordinate":[6,6],"connectedNodes":[33,29]}, {"coordinate":[5,6],"connectedNodes":[34,32]},{"coordinate":[4,6],"connectedNodes":[33,35]}, {"coordinate":[4,5],"connectedNodes":[37,34,36]},{"coordinate":[4,4],"connectedNodes":[35,9]}, {"coordinate":[3,5],"connectedNodes":[38,35]},{"coordinate":[2,5],"connectedNodes":[39,37]}, {"coordinate":[2,6],"connectedNodes":[40,38]},{"coordinate":[1,6],"connectedNodes":[39,41]}, {"coordinate":[1,5],"connectedNodes":[40,27]},{"coordinate":[6,4],"connectedNodes":[26]} ]',
                     pythonEnabled=True, theme=city, threads=1,
                     traffic_lights='[{"direction": "E", "startTime": 0, "sourceCoordinate": {"y":1, "x": 1}, "greenDuration": 2, "startingState": "RED", "redDuration": 4}, {"direction":"N", "startTime": 2, "sourceCoordinate": {"y": 0, "x": 2}, "greenDuration":2, "startingState": "RED", "redDuration": 4}, {"direction": "W", "startTime":0, "sourceCoordinate": {"y": 1, "x": 3}, "greenDuration": 2, "startingState":"GREEN", "redDuration": 4}, {"direction": "N", "startTime": 0, "sourceCoordinate":{"y": 1, "x": 4}, "greenDuration": 2, "startingState": "RED", "redDuration":4}, {"direction": "S", "startTime": 2, "sourceCoordinate": {"y": 3, "x": 4},"greenDuration": 2, "startingState": "RED", "redDuration": 4}, {"direction":"W", "startTime": 0, "sourceCoordinate": {"y": 2, "x": 5}, "greenDuration":2, "startingState": "GREEN", "redDuration": 4}, {"direction": "E", "startTime":0, "sourceCoordinate": {"y": 5, "x": 3}, "greenDuration": 2, "startingState":"RED", "redDuration": 4}, {"direction": "S", "startTime": 2, "sourceCoordinate":{"y": 6, "x": 4}, "greenDuration": 2, "startingState": "RED", "redDuration":4}, {"direction": "N", "startTime": 0, "sourceCoordinate": {"y": 4, "x": 4},"greenDuration": 2, "startingState": "GREEN", "redDuration": 4}, {"direction":"W", "startTime": 0, "sourceCoordinate": {"y": 6, "x": 2}, "greenDuration":4, "startingState": "RED", "redDuration": 2}, {"direction": "W", "startTime":0, "sourceCoordinate": {"y": 4, "x": 9}, "greenDuration": 2, "startingState":"RED", "redDuration": 4}, {"direction": "N", "startTime": 2, "sourceCoordinate":{"y": 3, "x": 8}, "greenDuration": 2, "startingState": "RED", "redDuration":4}, {"direction": "E", "startTime": 0, "sourceCoordinate": {"y": 4, "x": 7},"greenDuration": 2, "startingState": "GREEN", "redDuration": 4}]')

    level100.save()
    level101.save()
    level102.save()
    level103.save()
    level104.save()
    level105.save()
    level106.save()
    level107.save()
    level100.next_level_id = level101.id
    level101.next_level_id = level102.id
    level102.next_level_id = level103.id
    level103.next_level_id = level104.id
    level104.next_level_id = level105.id
    level105.next_level_id = level106.id
    level106.next_level_id = level107.id
    level100.save()
    level101.save()
    level102.save()
    level103.save()
    level104.save()
    level105.save()
    level106.save()
    level107.save()

    # Add level decor
    for levelPair in levelPairs:
        oldName = levelPair[0]
        newName = levelPair[1]
        oldLevel = Level.objects.get(name=oldName, default=True)
        newLevel = Level.objects.get(name=newName, default=True)
        levelDecors = LevelDecor.objects.filter(level=oldLevel)
        for levelDecor in levelDecors:
            newDecor = LevelDecor(decorName=levelDecor.decorName, level=newLevel, x=levelDecor.x, y=levelDecor.y)
            newDecor.save()

    # Add level blocks for blockly and python levels
    count = 0
    while count < 7:
        levelPair = levelPairs[count]
        oldName = levelPair[0]
        newName = levelPair[1]
        oldLevel = Level.objects.get(name=oldName, default=True)
        newLevel = Level.objects.get(name=newName, default=True)
        levelBlocks = LevelBlock.objects.filter(level=oldLevel)
        for levelBlock in levelBlocks:
            newBlock = LevelBlock(type=levelBlock.type, number=levelBlock.number, level=newLevel)
            newBlock.save()
        count += 1

    blocklyAndPythonEpisode = Episode(name="Introduction to Python", first_level=level80, r_branchiness=0.5,
                                      r_loopiness=0.1, r_num_tiles=35, r_curviness=0.2, r_pythonEnabled=0,
                                      r_blocklyEnabled=1, r_trafficLights=1, in_development=True)
    blocklyAndPythonEpisode.save()

    pythonOnlyEpisode = Episode(name="Python", first_level=level100, r_branchiness=0.5,
                                r_loopiness=0.1, r_num_tiles=35, r_curviness=0.2, r_pythonEnabled=0,
                                r_blocklyEnabled=1, r_trafficLights=1, in_development=True)
    pythonOnlyEpisode.save()


def enable_random_levels_for_episodes_1_to_7(apps, schema_editor):
    Episode = apps.get_model('game', 'Episode')

    for i in range(1,7):
        episode = Episode.objects.get(id=i)
        episode.r_random_levels_enabled = True
        episode.save()


def change_decor_and_blocks_in_level_63_and_60(apps, schema_editor):

    Level = apps.get_model('game', 'Level')
    LevelDecor = apps.get_model('game', 'LevelDecor')
    LevelBlock = apps.get_model('game', 'LevelBlock')
    Block = apps.get_model('game', 'Block')

    def set_decor(level, decor):
        set_decor_inner(level, decor, LevelDecor)

    def set_blocks(level, blocks):
        set_blocks_inner(level, blocks, LevelBlock, Block)

    level71 = Level.objects.get(name="71")
    set_decor(level71, json.loads('[{"x":458,"y":456,"decorName":"bush"},{"x":466,"y":585,"decorName":"tree2"},{"x":562,"y":636,"decorName":"tree2"},{"x":140,"y":261,"decorName":"bush"},{"x":474,"y":700,"decorName":"tree2"},{"x":55,"y":195,"decorName":"bush"},{"x":324,"y":147,"decorName":"bush"},{"x":152,"y":173,"decorName":"bush"},{"x":381,"y":99,"decorName":"bush"},{"x":0,"y":145,"decorName":"bush"},{"x":91,"y":100,"decorName":"bush"},{"x":205,"y":33,"decorName":"bush"},{"x":115,"y":0,"decorName":"bush"}]'))
    set_blocks(level71, json.loads('[{"type":"move_forwards","number":1},{"type":"turn_left","number":1},{"type":"turn_right","number":1},{"type":"turn_around","number":1},{"type":"controls_repeat_until"},{"type":"controls_if"},{"type":"at_destination"},{"type":"road_exists","number":1}]'))
    level71.save()
    LevelBlock.objects.filter(level=level71, type=Block.objects.get(type="turn_around")).delete()

    level60 = Level.objects.get(name='60', default=True)

    set_decor(level60, json.loads('[{"x":261,"y":426,"decorName":"pond"},{"x":412,"y":368,"decorName":"tree2"},{"x":179,"y":300,"decorName":"tree2"},{"x":210,"y":496,"decorName":"tree2"},{"x":323,"y":288,"decorName":"tree1"},{"x":415,"y":514,"decorName":"tree1"},{"x":789,"y":359,"decorName":"tree1"},{"x":750,"y":308,"decorName":"tree1"},{"x":807,"y":317,"decorName":"tree1"},{"x":207,"y":693,"decorName":"bush"},{"x":427,"y":161,"decorName":"bush"},{"x":355,"y":159,"decorName":"bush"},{"x":284,"y":160,"decorName":"bush"},{"x":211,"y":160,"decorName":"bush"},{"x":137,"y":160,"decorName":"bush"},{"x":278,"y":694,"decorName":"bush"},{"x":348,"y":695,"decorName":"bush"},{"x":419,"y":695,"decorName":"bush"},{"x":490,"y":695,"decorName":"bush"},{"x":566,"y":697,"decorName":"bush"},{"x":636,"y":697,"decorName":"bush"}]'))
    set_blocks(level60, json.loads('[{"type":"move_forwards","number":1},{"type":"turn_right","number":1},{"type":"turn_around","number":1},{"type":"controls_repeat"}]'))


def set_next_episode(apps, schema_editor):

    Episode = apps.get_model('game', 'Episode')

    getting_started_episode = Episode.objects.get(name="Getting Started")
    shortest_route_episode = Episode.objects.get(name="Shortest Route")
    loops_and_repetitions_episode = Episode.objects.get(name="Loops and Repetitions")
    loops_and_conditions_episode = Episode.objects.get(name="Loops with Conditions")
    if_only_episode = Episode.objects.get(name="If... Only")
    traffic_lights_episode = Episode.objects.get(name="Traffic Lights")
    limited_blocks_episode = Episode.objects.get(name="Limited Blocks")
    procedures_episode = Episode.objects.get(name="Procedures")
    blockly_brain_teasers_episode = Episode.objects.get(name="Blockly Brain Teasers")
    introduction_to_python_episode = Episode.objects.get(name="Introduction to Python")
    python_episode = Episode.objects.get(name="Python")


    getting_started_episode.next_episode = shortest_route_episode
    shortest_route_episode.next_episode = loops_and_repetitions_episode
    loops_and_repetitions_episode.next_episode = loops_and_conditions_episode
    loops_and_conditions_episode.next_episode = if_only_episode
    if_only_episode.next_episode = traffic_lights_episode
    traffic_lights_episode.next_episode = limited_blocks_episode
    limited_blocks_episode.next_episode = procedures_episode
    procedures_episode.next_episode = blockly_brain_teasers_episode
    blockly_brain_teasers_episode.next_episode = introduction_to_python_episode
    introduction_to_python_episode.next_episode = python_episode

    getting_started_episode.save()
    shortest_route_episode.save()
    loops_and_repetitions_episode.save()
    loops_and_conditions_episode.save()
    if_only_episode.save()
    traffic_lights_episode.save()
    limited_blocks_episode.save()
    procedures_episode.save()
    blockly_brain_teasers_episode.save()
    introduction_to_python_episode.save()
    python_episode.save()


def add_and_reorder_levels(apps, schema_editor):

    Level = apps.get_model('game', 'Level')
    Character = apps.get_model('game', 'Character')
    Theme = apps.get_model('game', 'Theme')
    Episode = apps.get_model('game', 'Episode')
    LevelDecor = apps.get_model('game', 'LevelDecor')
    LevelBlock = apps.get_model('game', 'LevelBlock')
    Block = apps.get_model('game', 'Block')

    def set_decor(level, decor):
        set_decor_inner(level, decor, LevelDecor)

    def set_blocks(level, blocks):
        set_blocks_inner(level, blocks, LevelBlock, Block)

    def create_level52():
        level52 = Level(
            name='52',
            default=True,
            path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,8,2,18]},{"coordinate":[2,3],"connectedNodes":[1,3]},{"coordinate":[3,3],"connectedNodes":[2,4]},{"coordinate":[4,3],"connectedNodes":[3,5]},{"coordinate":[5,3],"connectedNodes":[4,6]},{"coordinate":[6,3],"connectedNodes":[5,17,7,25]},{"coordinate":[7,3],"connectedNodes":[6]},{"coordinate":[1,4],"connectedNodes":[9,1]},{"coordinate":[2,4],"connectedNodes":[8,10]},{"coordinate":[2,5],"connectedNodes":[11,9]},{"coordinate":[3,5],"connectedNodes":[10,12]},{"coordinate":[3,6],"connectedNodes":[13,11]},{"coordinate":[4,6],"connectedNodes":[12,14]},{"coordinate":[4,5],"connectedNodes":[13,15]},{"coordinate":[5,5],"connectedNodes":[14,16]},{"coordinate":[5,4],"connectedNodes":[15,17]},{"coordinate":[6,4],"connectedNodes":[16,6]},{"coordinate":[1,2],"connectedNodes":[1,19]},{"coordinate":[2,2],"connectedNodes":[18,20]},{"coordinate":[3,2],"connectedNodes":[19,21]},{"coordinate":[3,1],"connectedNodes":[20,22]},{"coordinate":[4,1],"connectedNodes":[21,23]},{"coordinate":[5,1],"connectedNodes":[22,24]},{"coordinate":[6,1],"connectedNodes":[23,25]},{"coordinate":[6,2],"connectedNodes":[6,24]}]',
            traffic_lights='[]',
            destinations='[[7,3]]',
            origin='{"coordinate":[0,3],"direction":"E"}',
            max_fuel=50,
            blocklyEnabled=True,
            pythonEnabled=False,
            theme=Theme.objects.get(id=2),
            character=Character.objects.get(id='1'),
            model_solution='[6]',
        )
        level52.save()
        set_decor(level52, json.loads('[{"x":29,"y":524,"decorName":"tree2"},{"x":193,"y":622,"decorName":"tree2"},{"x":521,"y":603,"decorName":"tree2"},{"x":651,"y":488,"decorName":"tree2"},{"x":74,"y":100,"decorName":"tree1"},{"x":266,"y":2,"decorName":"tree1"},{"x":533,"y":9,"decorName":"tree1"},{"x":701,"y":110,"decorName":"tree1"},{"x":268,"y":385,"decorName":"bush"},{"x":348,"y":386,"decorName":"bush"},{"x":420,"y":385,"decorName":"bush"},{"x":494,"y":386,"decorName":"bush"},{"x":424,"y":201,"decorName":"pond"}]'))
        set_blocks(level52, json.loads('[{"type":"turn_left","number":2},{"type":"turn_right","number":2},{"type":"controls_repeat"}]'))
        return level52

    def create_level53():
        level53 = Level(
            name='53',
            default=True,
            path='[{"coordinate":[1,3],"connectedNodes":[1]},{"coordinate":[2,3],"connectedNodes":[0,17,12,2]},{"coordinate":[2,2],"connectedNodes":[1,3]},{"coordinate":[2,1],"connectedNodes":[2,4]},{"coordinate":[3,1],"connectedNodes":[3,5]},{"coordinate":[4,1],"connectedNodes":[4,6]},{"coordinate":[5,1],"connectedNodes":[5,7]},{"coordinate":[6,1],"connectedNodes":[6,8]},{"coordinate":[6,2],"connectedNodes":[9,29,7]},{"coordinate":[6,3],"connectedNodes":[16,10,8]},{"coordinate":[6,4],"connectedNodes":[11,9]},{"coordinate":[6,5],"connectedNodes":[23,24,10]},{"coordinate":[3,3],"connectedNodes":[1,13]},{"coordinate":[4,3],"connectedNodes":[12,14]},{"coordinate":[4,4],"connectedNodes":[15,13]},{"coordinate":[5,4],"connectedNodes":[14,16]},{"coordinate":[5,3],"connectedNodes":[15,9]},{"coordinate":[2,4],"connectedNodes":[18,1]},{"coordinate":[2,5],"connectedNodes":[19,17]},{"coordinate":[2,6],"connectedNodes":[20,18]},{"coordinate":[3,6],"connectedNodes":[19,21]},{"coordinate":[4,6],"connectedNodes":[20,22]},{"coordinate":[5,6],"connectedNodes":[21,23]},{"coordinate":[6,6],"connectedNodes":[22,11]},{"coordinate":[7,5],"connectedNodes":[11,25]},{"coordinate":[8,5],"connectedNodes":[24,26]},{"coordinate":[8,4],"connectedNodes":[25,27]},{"coordinate":[8,3],"connectedNodes":[26,28]},{"coordinate":[8,2],"connectedNodes":[29,27]},{"coordinate":[7,2],"connectedNodes":[8,28]}]',
            traffic_lights='[]',
            destinations='[[8,3]]',
            origin='{"coordinate":[1,3],"direction":"E"}',
            max_fuel=50,
            blocklyEnabled=True,
            pythonEnabled=False,
            theme=Theme.objects.get(id=3),
            character=Character.objects.get(id='1'),
            model_solution='[9]',
        )
        level53.save()
        set_decor(level53, json.loads('[{"x":302,"y":199,"decorName":"pond"},{"x":481,"y":302,"decorName":"bush"},{"x":481,"y":252,"decorName":"bush"},{"x":481,"y":204,"decorName":"bush"},{"x":692,"y":292,"decorName":"tree1"},{"x":540,"y":503,"decorName":"tree2"},{"x":331,"y":499,"decorName":"pond"},{"x":254,"y":700,"decorName":"tree1"},{"x":0,"y":700,"decorName":"tree1"},{"x":97,"y":509,"decorName":"tree1"},{"x":42,"y":602,"decorName":"tree1"},{"x":123,"y":670,"decorName":"tree1"},{"x":4,"y":444,"decorName":"tree1"},{"x":357,"y":457,"decorName":"bush"},{"x":295,"y":414,"decorName":"bush"},{"x":296,"y":457,"decorName":"bush"},{"x":356,"y":414,"decorName":"bush"}]'))
        set_blocks(level53, json.loads('[{"type":"move_forwards","number":2},{"type":"turn_left","number":3},{"type":"turn_right","number":2},{"type":"controls_repeat"}]'))
        return level53

    def create_level54():
        level54 = Level(
            name='54',
            default=True,
            path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,9,2,18]},{"coordinate":[2,3],"connectedNodes":[1,10,3,19]},{"coordinate":[3,3],"connectedNodes":[2,11,4,20]},{"coordinate":[4,3],"connectedNodes":[3,12,5,21]},{"coordinate":[5,3],"connectedNodes":[4,13,6,22]},{"coordinate":[6,3],"connectedNodes":[5,14,7,23]},{"coordinate":[7,3],"connectedNodes":[6,15,8,24]},{"coordinate":[8,3],"connectedNodes":[7,16,17,25]},{"coordinate":[1,4],"connectedNodes":[10,1]},{"coordinate":[2,4],"connectedNodes":[9,2]},{"coordinate":[3,4],"connectedNodes":[12,3]},{"coordinate":[4,4],"connectedNodes":[11,4]},{"coordinate":[5,4],"connectedNodes":[14,5]},{"coordinate":[6,4],"connectedNodes":[13,6]},{"coordinate":[7,4],"connectedNodes":[16,7]},{"coordinate":[8,4],"connectedNodes":[15,8]},{"coordinate":[9,3],"connectedNodes":[8]},{"coordinate":[1,2],"connectedNodes":[1,19]},{"coordinate":[2,2],"connectedNodes":[18,2]},{"coordinate":[3,2],"connectedNodes":[3,21]},{"coordinate":[4,2],"connectedNodes":[20,4]},{"coordinate":[5,2],"connectedNodes":[5,23]},{"coordinate":[6,2],"connectedNodes":[22,6]},{"coordinate":[7,2],"connectedNodes":[7,25]},{"coordinate":[8,2],"connectedNodes":[24,8]}]',
            traffic_lights='[]',
            destinations='[[9,3]]',
            origin='{"coordinate":[0,3],"direction":"E"}',
            max_fuel=50,
            blocklyEnabled=True,
            pythonEnabled=False,
            theme=Theme.objects.get(id=1),
            character=Character.objects.get(id='1'),
            model_solution='[5]',
        )
        level54.save()
        set_decor(level54, json.loads('[{"x":29,"y":466,"decorName":"tree2"},{"x":40,"y":97,"decorName":"tree2"},{"x":296,"y":501,"decorName":"tree2"},{"x":719,"y":52,"decorName":"tree2"},{"x":650,"y":481,"decorName":"tree1"},{"x":122,"y":639,"decorName":"tree1"},{"x":416,"y":22,"decorName":"pond"},{"x":674,"y":417,"decorName":"bush"},{"x":475,"y":419,"decorName":"bush"},{"x":274,"y":421,"decorName":"bush"},{"x":275,"y":226,"decorName":"bush"},{"x":475,"y":226,"decorName":"bush"},{"x":675,"y":228,"decorName":"bush"},{"x":74,"y":224,"decorName":"bush"},{"x":75,"y":421,"decorName":"bush"},{"x":874,"y":227,"decorName":"bush"},{"x":876,"y":418,"decorName":"bush"}]'))
        set_blocks(level54, json.loads('[{"type":"turn_left","number":2},{"type":"turn_right","number":1},{"type":"controls_repeat"}]'))
        return level54

    def create_level55():
        level55 = Level(
            name='55',
            default=True,
            path='[{"coordinate":[2,6],"connectedNodes":[18]},{"coordinate":[3,6],"connectedNodes":[2,19]},{"coordinate":[4,6],"connectedNodes":[1,3]},{"coordinate":[4,7],"connectedNodes":[4,2]},{"coordinate":[5,7],"connectedNodes":[3,5]},{"coordinate":[5,6],"connectedNodes":[4,6]},{"coordinate":[6,6],"connectedNodes":[5,7]},{"coordinate":[6,5],"connectedNodes":[6,8]},{"coordinate":[7,5],"connectedNodes":[7,9]},{"coordinate":[7,4],"connectedNodes":[10,8]},{"coordinate":[6,4],"connectedNodes":[9,11]},{"coordinate":[6,3],"connectedNodes":[12,10]},{"coordinate":[5,3],"connectedNodes":[11,13]},{"coordinate":[5,2],"connectedNodes":[14,12]},{"coordinate":[4,2],"connectedNodes":[15,13]},{"coordinate":[4,3],"connectedNodes":[16,14]},{"coordinate":[3,3],"connectedNodes":[17,15]},{"coordinate":[3,4],"connectedNodes":[20,16]},{"coordinate":[2,5],"connectedNodes":[0,19]},{"coordinate":[3,5],"connectedNodes":[18,1]},{"coordinate":[2,4],"connectedNodes":[17,21]},{"coordinate":[2,3],"connectedNodes":[20]}]',
            traffic_lights='[]',
            destinations='[[2,3]]',
            origin='{"coordinate":[2,6],"direction":"S"}',
            max_fuel=50,
            blocklyEnabled=True,
            pythonEnabled=False,
            theme=Theme.objects.get(id=1),
            character=Character.objects.get(id='1'),
            model_solution='[6]',
        )
        level55.save()
        set_decor(level55, json.loads('[{"x":81,"y":559,"decorName":"tree1"},{"x":715,"y":700,"decorName":"tree1"},{"x":772,"y":588,"decorName":"tree1"},{"x":7,"y":462,"decorName":"tree1"},{"x":83,"y":349,"decorName":"tree1"},{"x":535,"y":478,"decorName":"tree2"},{"x":211,"y":472,"decorName":"bush"},{"x":144,"y":473,"decorName":"bush"},{"x":430,"y":379,"decorName":"pond"}]'))
        set_blocks(level55, json.loads('[{"type":"turn_left","number":1},{"type":"turn_right","number":1},{"type":"controls_repeat_until"},{"type":"controls_if"},{"type":"at_destination"},{"type":"road_exists","number":1}]'))
        return level55

    def create_level56():
        level56 = Level(
            name='56',
            default=True,
            path='[{"coordinate":[1,6],"connectedNodes":[25]},{"coordinate":[3,5],"connectedNodes":[26,2]},{"coordinate":[4,5],"connectedNodes":[1,3]},{"coordinate":[4,6],"connectedNodes":[4,2]},{"coordinate":[4,7],"connectedNodes":[5,3]},{"coordinate":[5,7],"connectedNodes":[4,6]},{"coordinate":[6,7],"connectedNodes":[5,7]},{"coordinate":[7,7],"connectedNodes":[6,8]},{"coordinate":[7,6],"connectedNodes":[7,9]},{"coordinate":[7,5],"connectedNodes":[8,10]},{"coordinate":[7,4],"connectedNodes":[9,11]},{"coordinate":[7,3],"connectedNodes":[12,10]},{"coordinate":[6,3],"connectedNodes":[13,11]},{"coordinate":[5,3],"connectedNodes":[14,12]},{"coordinate":[4,3],"connectedNodes":[15,13]},{"coordinate":[3,3],"connectedNodes":[16,14]},{"coordinate":[2,3],"connectedNodes":[15,17]},{"coordinate":[2,2],"connectedNodes":[16,18]},{"coordinate":[2,1],"connectedNodes":[17,19]},{"coordinate":[3,1],"connectedNodes":[18,20]},{"coordinate":[4,1],"connectedNodes":[19,21]},{"coordinate":[5,1],"connectedNodes":[20,22]},{"coordinate":[6,1],"connectedNodes":[21,23]},{"coordinate":[7,1],"connectedNodes":[22,24]},{"coordinate":[7,2],"connectedNodes":[23]},{"coordinate":[2,6],"connectedNodes":[0,26]},{"coordinate":[2,5],"connectedNodes":[25,1]}]',
            traffic_lights='[]',
            destinations='[[7,2]]',
            origin='{"coordinate":[1,6],"direction":"E"}',
            max_fuel=50,
            blocklyEnabled=True,
            pythonEnabled=False,
            theme=Theme.objects.get(id=4),
            character=Character.objects.get(id='1'),
            model_solution='[8]',
        )
        level56.save()
        set_decor(level56, json.loads('[{"x":295,"y":200,"decorName":"tree2"},{"x":658,"y":654,"decorName":"bush"},{"x":657,"y":589,"decorName":"bush"},{"x":656,"y":523,"decorName":"bush"},{"x":655,"y":463,"decorName":"bush"},{"x":655,"y":401,"decorName":"bush"},{"x":497,"y":561,"decorName":"pond"},{"x":782,"y":408,"decorName":"tree1"},{"x":415,"y":190,"decorName":"bush"},{"x":492,"y":191,"decorName":"bush"},{"x":567,"y":192,"decorName":"bush"},{"x":645,"y":192,"decorName":"bush"}]'))
        set_blocks(level56, json.loads('[{"type":"move_forwards","number":1},{"type":"turn_left","number":1},{"type":"turn_right","number":1},{"type":"controls_repeat_until"},{"type":"controls_if"},{"type":"at_destination"},{"type":"road_exists","number":2}]'))
        return level56

    def create_level57():
        level57 = Level(
            name='57',
            default=True,
            path='[{"coordinate":[1,6],"connectedNodes":[1]},{"coordinate":[2,6],"connectedNodes":[0,2]},{"coordinate":[2,5],"connectedNodes":[1,3]},{"coordinate":[2,4],"connectedNodes":[2,4]},{"coordinate":[3,4],"connectedNodes":[3,5]},{"coordinate":[4,4],"connectedNodes":[4,6]},{"coordinate":[4,5],"connectedNodes":[7,5]},{"coordinate":[4,6],"connectedNodes":[8,6]},{"coordinate":[4,7],"connectedNodes":[9,7]},{"coordinate":[5,7],"connectedNodes":[8,10]},{"coordinate":[5,6],"connectedNodes":[9,11]},{"coordinate":[5,5],"connectedNodes":[10,12]},{"coordinate":[6,5],"connectedNodes":[11,13]},{"coordinate":[6,6],"connectedNodes":[14,12]},{"coordinate":[7,6],"connectedNodes":[13,15]},{"coordinate":[7,5],"connectedNodes":[14,16]},{"coordinate":[8,5],"connectedNodes":[15,17]},{"coordinate":[8,4],"connectedNodes":[18,16]},{"coordinate":[7,4],"connectedNodes":[17,19]},{"coordinate":[7,3],"connectedNodes":[20,18]},{"coordinate":[6,3],"connectedNodes":[21,19]},{"coordinate":[5,3],"connectedNodes":[20,22]},{"coordinate":[5,2],"connectedNodes":[23,21]},{"coordinate":[4,2],"connectedNodes":[24,22]},{"coordinate":[3,2],"connectedNodes":[23]}]',
            traffic_lights='[]',
            destinations='[[3,2]]',
            origin='{"coordinate":[1,6],"direction":"E"}',
            max_fuel=50,
            blocklyEnabled=True,
            pythonEnabled=False,
            theme=Theme.objects.get(id=3),
            character=Character.objects.get(id='1'),
            model_solution='[9]',
        )
        level57.save()
        set_decor(level57, json.loads('[{"x":287,"y":493,"decorName":"tree2"},{"x":646,"y":451,"decorName":"tree1"},{"x":31,"y":111,"decorName":"pond"},{"x":32,"y":300,"decorName":"pond"},{"x":32,"y":205,"decorName":"pond"},{"x":190,"y":298,"decorName":"pond"},{"x":346,"y":298,"decorName":"pond"},{"x":596,"y":698,"decorName":"tree1"},{"x":757,"y":676,"decorName":"tree1"},{"x":900,"y":426,"decorName":"tree1"},{"x":897,"y":700,"decorName":"tree1"},{"x":852,"y":556,"decorName":"tree1"},{"x":159,"y":458,"decorName":"bush"},{"x":158,"y":507,"decorName":"bush"},{"x":159,"y":561,"decorName":"bush"},{"x":500,"y":184,"decorName":"bush"},{"x":566,"y":185,"decorName":"bush"},{"x":436,"y":184,"decorName":"bush"}]'))
        set_blocks(level57, json.loads('[{"type":"move_forwards","number":1},{"type":"turn_left","number":1},{"type":"turn_right","number":1},{"type":"controls_repeat_while"},{"type":"controls_if"},{"type":"logic_negate","number":1},{"type":"at_destination","number":1},{"type":"road_exists","number":2}]'))
        return level57

    def create_level58():
        level58 = Level(
            name='58',
            default=True,
            path='[{"coordinate":[6,6],"connectedNodes":[1]},{"coordinate":[5,6],"connectedNodes":[2,0]},{"coordinate":[4,6],"connectedNodes":[3,1]},{"coordinate":[3,6],"connectedNodes":[4,2]},{"coordinate":[2,6],"connectedNodes":[5,3]},{"coordinate":[1,6],"connectedNodes":[4,6]},{"coordinate":[1,5],"connectedNodes":[5,7]},{"coordinate":[2,5],"connectedNodes":[6,8]},{"coordinate":[3,5],"connectedNodes":[7,9]},{"coordinate":[4,5],"connectedNodes":[8,10]},{"coordinate":[5,5],"connectedNodes":[9,11]},{"coordinate":[6,5],"connectedNodes":[10,12]},{"coordinate":[6,4],"connectedNodes":[13,11]},{"coordinate":[5,4],"connectedNodes":[14,12]},{"coordinate":[4,4],"connectedNodes":[15,13]},{"coordinate":[3,4],"connectedNodes":[16,14]},{"coordinate":[2,4],"connectedNodes":[17,15]},{"coordinate":[1,4],"connectedNodes":[16,18]},{"coordinate":[1,3],"connectedNodes":[17,19]},{"coordinate":[2,3],"connectedNodes":[18,20]},{"coordinate":[3,3],"connectedNodes":[19,21]},{"coordinate":[4,3],"connectedNodes":[20,22]},{"coordinate":[5,3],"connectedNodes":[21,23]},{"coordinate":[6,3],"connectedNodes":[22,24]},{"coordinate":[6,2],"connectedNodes":[25,23]},{"coordinate":[5,2],"connectedNodes":[24]}]',
            traffic_lights='[]',
            destinations='[[5,2]]',
            origin='{"coordinate":[6,6],"direction":"W"}',
            max_fuel=50,
            blocklyEnabled=True,
            pythonEnabled=False,
            theme=Theme.objects.get(id=2),
            character=Character.objects.get(id='1'),
            model_solution='[11]',
        )
        level58.save()
        set_decor(level58, json.loads('[{"x":795,"y":680,"decorName":"tree1"},{"x":797,"y":527,"decorName":"tree1"},{"x":799,"y":365,"decorName":"tree1"},{"x":800,"y":187,"decorName":"tree1"},{"x":311,"y":74,"decorName":"pond"},{"x":171,"y":701,"decorName":"bush"},{"x":270,"y":701,"decorName":"bush"},{"x":369,"y":699,"decorName":"bush"},{"x":461,"y":699,"decorName":"bush"},{"x":551,"y":698,"decorName":"bush"},{"x":82,"y":254,"decorName":"bush"},{"x":177,"y":254,"decorName":"bush"},{"x":371,"y":254,"decorName":"bush"},{"x":275,"y":255,"decorName":"bush"},{"x":450,"y":251,"decorName":"bush"},{"x":799,"y":31,"decorName":"tree1"},{"x":74,"y":699,"decorName":"bush"}]'))
        set_blocks(level58, json.loads('[{"type":"move_forwards","number":2},{"type":"turn_left","number":1},{"type":"turn_right","number":1},{"type":"controls_repeat","number":4},{"type":"controls_repeat_while"},{"type":"logic_negate","number":1},{"type":"at_destination","number":1}]'))
        return level58

    def create_level61():
        level61 = Level(
            name='61',
            default=True,
            path='[{"coordinate":[0,5],"connectedNodes":[1]},{"coordinate":[1,5],"connectedNodes":[0,2]},{"coordinate":[2,5],"connectedNodes":[1,3]},{"coordinate":[2,6],"connectedNodes":[4,2]},{"coordinate":[3,6],"connectedNodes":[3,5]},{"coordinate":[3,5],"connectedNodes":[4,6]},{"coordinate":[4,5],"connectedNodes":[5,7]},{"coordinate":[5,5],"connectedNodes":[6,8]},{"coordinate":[6,5],"connectedNodes":[7,9]},{"coordinate":[6,6],"connectedNodes":[10,8]},{"coordinate":[7,6],"connectedNodes":[9,11]},{"coordinate":[7,5],"connectedNodes":[10,12]},{"coordinate":[8,5],"connectedNodes":[11]}]',
            traffic_lights='[]',
            destinations='[[8,5]]',
            origin='{"coordinate":[0,5],"direction":"E"}',
            max_fuel=50,
            blocklyEnabled=True,
            pythonEnabled=False,
            theme=Theme.objects.get(id=1),
            character=Character.objects.get(id='1'),
            model_solution='[8]',
        )
        level61.save()
        set_decor(level61, json.loads('[{"x":853,"y":70,"decorName":"tree2"},{"x":783,"y":250,"decorName":"tree2"},{"x":461,"y":115,"decorName":"tree2"},{"x":675,"y":25,"decorName":"tree2"},{"x":739,"y":0,"decorName":"tree2"},{"x":530,"y":67,"decorName":"tree1"},{"x":655,"y":127,"decorName":"tree1"},{"x":433,"y":16,"decorName":"tree1"},{"x":749,"y":93,"decorName":"tree1"},{"x":156,"y":64,"decorName":"tree1"},{"x":877,"y":182,"decorName":"tree1"},{"x":45,"y":125,"decorName":"tree1"},{"x":547,"y":182,"decorName":"tree2"},{"x":322,"y":56,"decorName":"tree2"},{"x":607,"y":0,"decorName":"tree2"},{"x":214,"y":3,"decorName":"tree2"},{"x":59,"y":24,"decorName":"tree2"},{"x":665,"y":245,"decorName":"tree1"},{"x":242,"y":150,"decorName":"tree1"},{"x":98,"y":451,"decorName":"bush"},{"x":598,"y":451,"decorName":"bush"},{"x":498,"y":451,"decorName":"bush"},{"x":397,"y":451,"decorName":"bush"},{"x":296,"y":452,"decorName":"bush"},{"x":197,"y":452,"decorName":"bush"},{"x":698,"y":451,"decorName":"bush"}]'))
        set_blocks(level61, json.loads('[{"type":"move_forwards"},{"type":"turn_left"},{"type":"turn_right"},{"type":"controls_repeat"},{"type":"call_proc"},{"type":"declare_proc"}]'))
        return level61

    def create_level64():
        level64 = Level(
            name='64',
            default=True,
            path='[{"coordinate":[1,4],"connectedNodes":[1]},{"coordinate":[2,4],"connectedNodes":[0,2]},{"coordinate":[2,5],"connectedNodes":[3,1]},{"coordinate":[3,5],"connectedNodes":[2,4]},{"coordinate":[4,5],"connectedNodes":[3,5]},{"coordinate":[4,4],"connectedNodes":[4,6]},{"coordinate":[5,4],"connectedNodes":[5,7]},{"coordinate":[6,4],"connectedNodes":[6,8]},{"coordinate":[6,5],"connectedNodes":[9,7]},{"coordinate":[7,5],"connectedNodes":[8,10]},{"coordinate":[8,5],"connectedNodes":[9,11]},{"coordinate":[8,4],"connectedNodes":[10,12]},{"coordinate":[9,4],"connectedNodes":[11,13]},{"coordinate":[9,3],"connectedNodes":[12,14]},{"coordinate":[9,2],"connectedNodes":[15,13]},{"coordinate":[8,2],"connectedNodes":[16,14]},{"coordinate":[7,2],"connectedNodes":[17,15]},{"coordinate":[7,3],"connectedNodes":[18,16]},{"coordinate":[6,3],"connectedNodes":[17,19]},{"coordinate":[6,2],"connectedNodes":[20,18]},{"coordinate":[5,2],"connectedNodes":[19,21]},{"coordinate":[5,1],"connectedNodes":[22,20]},{"coordinate":[4,1],"connectedNodes":[23,21]},{"coordinate":[3,1],"connectedNodes":[24,22]},{"coordinate":[3,2],"connectedNodes":[25,23]},{"coordinate":[2,2],"connectedNodes":[26,24]},{"coordinate":[2,3],"connectedNodes":[27,25]},{"coordinate":[1,3],"connectedNodes":[26,28]},{"coordinate":[1,2],"connectedNodes":[29,27]},{"coordinate":[0,2],"connectedNodes":[28]}]',
            traffic_lights='[]',
            destinations='[[0,2]]',
            origin='{"coordinate":[1,4],"direction":"E"}',
            max_fuel=50,
            blocklyEnabled=True,
            pythonEnabled=False,
            theme=Theme.objects.get(id=3),
            character=Character.objects.get(id='6'),
            model_solution='[20]',
        )
        level64.save()
        set_decor(level64, json.loads('[{"x":291,"y":295,"decorName":"pond"},{"x":452,"y":295,"decorName":"pond"},{"x":630,"y":108,"decorName":"tree1"},{"x":501,"y":498,"decorName":"tree1"},{"x":95,"y":500,"decorName":"tree1"},{"x":702,"y":408,"decorName":"tree1"},{"x":313,"y":415,"decorName":"tree2"},{"x":814,"y":302,"decorName":"tree2"},{"x":896,"y":494,"decorName":"tree1"},{"x":151,"y":106,"decorName":"tree1"},{"x":426,"y":237,"decorName":"bush"},{"x":456,"y":203,"decorName":"bush"},{"x":396,"y":204,"decorName":"bush"},{"x":41,"y":614,"decorName":"tree1"},{"x":219,"y":607,"decorName":"tree1"},{"x":532,"y":607,"decorName":"tree1"},{"x":366,"y":655,"decorName":"tree1"},{"x":900,"y":657,"decorName":"tree1"},{"x":671,"y":668,"decorName":"tree1"}]'))
        set_blocks(level64, json.loads('[{"type":"move_forwards"},{"type":"turn_left"},{"type":"turn_right"},{"type":"controls_repeat"},{"type":"call_proc"},{"type":"declare_proc"}]'))
        return level64

    def create_level66():
        level66 = Level(
            name='66',
            default=True,
            path='[{"coordinate":[1,5],"connectedNodes":[1]},{"coordinate":[2,5],"connectedNodes":[0,2]},{"coordinate":[3,5],"connectedNodes":[1,3]},{"coordinate":[4,5],"connectedNodes":[2,4]},{"coordinate":[4,4],"connectedNodes":[3,5]},{"coordinate":[5,4],"connectedNodes":[4,6]},{"coordinate":[6,4],"connectedNodes":[5,7]},{"coordinate":[7,4],"connectedNodes":[6,8]},{"coordinate":[8,4],"connectedNodes":[7,9]},{"coordinate":[8,3],"connectedNodes":[8,10]},{"coordinate":[8,2],"connectedNodes":[9,11]},{"coordinate":[8,1],"connectedNodes":[12,10]},{"coordinate":[7,1],"connectedNodes":[13,11]},{"coordinate":[6,1],"connectedNodes":[14,12]},{"coordinate":[5,1],"connectedNodes":[15,13]},{"coordinate":[4,1],"connectedNodes":[16,14]},{"coordinate":[4,2],"connectedNodes":[17,15]},{"coordinate":[3,2],"connectedNodes":[18,16]},{"coordinate":[2,2],"connectedNodes":[19,17]},{"coordinate":[1,2],"connectedNodes":[20,18]},{"coordinate":[1,3],"connectedNodes":[19]}]',
            traffic_lights='[]',
            destinations='[[1,3]]',
            origin='{"coordinate":[1,5],"direction":"E"}',
            max_fuel=50,
            blocklyEnabled=True,
            pythonEnabled=False,
            theme=Theme.objects.get(id=2),
            character=Character.objects.get(id='2'),
            model_solution='[14]',
        )
        level66.save()
        set_decor(level66, json.loads('[{"x":900,"y":305,"decorName":"tree2"},{"x":712,"y":700,"decorName":"tree2"},{"x":850,"y":514,"decorName":"tree2"},{"x":736,"y":605,"decorName":"tree2"},{"x":874,"y":700,"decorName":"tree2"},{"x":608,"y":700,"decorName":"tree2"},{"x":382,"y":688,"decorName":"tree2"},{"x":900,"y":597,"decorName":"tree1"},{"x":508,"y":700,"decorName":"tree1"},{"x":587,"y":578,"decorName":"tree1"},{"x":795,"y":666,"decorName":"tree1"},{"x":496,"y":202,"decorName":"bush"},{"x":460,"y":298,"decorName":"bush"},{"x":379,"y":298,"decorName":"bush"},{"x":300,"y":297,"decorName":"bush"},{"x":217,"y":297,"decorName":"bush"},{"x":740,"y":202,"decorName":"bush"},{"x":661,"y":201,"decorName":"bush"},{"x":579,"y":201,"decorName":"bush"}]'))
        set_blocks(level66, json.loads('[{"type":"move_forwards"},{"type":"turn_left"},{"type":"turn_right"},{"type":"controls_repeat"},{"type":"call_proc"},{"type":"declare_proc"}]'))
        return level66

    def create_level72():
        level72 = Level(
            name='72',
            default=True,
            path='[{"coordinate":[1,5],"connectedNodes":[1]},{"coordinate":[2,5],"connectedNodes":[0,2]},{"coordinate":[3,5],"connectedNodes":[1,3]},{"coordinate":[4,5],"connectedNodes":[2,17,4]},{"coordinate":[5,5],"connectedNodes":[3,5]},{"coordinate":[6,5],"connectedNodes":[4,28,19,6]},{"coordinate":[6,4],"connectedNodes":[5,7]},{"coordinate":[6,3],"connectedNodes":[6,8]},{"coordinate":[6,2],"connectedNodes":[7,9]},{"coordinate":[6,1],"connectedNodes":[10,8,25]},{"coordinate":[5,1],"connectedNodes":[11,9]},{"coordinate":[4,1],"connectedNodes":[12,10]},{"coordinate":[3,1],"connectedNodes":[13,11]},{"coordinate":[2,1],"connectedNodes":[14,12]},{"coordinate":[1,1],"connectedNodes":[29,15,13]},{"coordinate":[1,2],"connectedNodes":[35,16,14]},{"coordinate":[2,2],"connectedNodes":[15]},{"coordinate":[4,6],"connectedNodes":[18,3]},{"coordinate":[4,7],"connectedNodes":[26,17]},{"coordinate":[7,5],"connectedNodes":[5,20]},{"coordinate":[8,5],"connectedNodes":[19,21]},{"coordinate":[8,4],"connectedNodes":[20,22]},{"coordinate":[8,3],"connectedNodes":[21,23]},{"coordinate":[8,2],"connectedNodes":[22,24]},{"coordinate":[8,1],"connectedNodes":[25,23]},{"coordinate":[7,1],"connectedNodes":[9,24]},{"coordinate":[5,7],"connectedNodes":[18,27]},{"coordinate":[6,7],"connectedNodes":[26,28]},{"coordinate":[6,6],"connectedNodes":[27,5]},{"coordinate":[0,1],"connectedNodes":[14,30]},{"coordinate":[0,0],"connectedNodes":[29,31]},{"coordinate":[1,0],"connectedNodes":[30,32]},{"coordinate":[2,0],"connectedNodes":[31,33]},{"coordinate":[3,0],"connectedNodes":[32,34]},{"coordinate":[4,0],"connectedNodes":[33]},{"coordinate":[1,3],"connectedNodes":[36,15]},{"coordinate":[2,3],"connectedNodes":[35,37]},{"coordinate":[3,3],"connectedNodes":[36,38]},{"coordinate":[4,3],"connectedNodes":[37,39]},{"coordinate":[5,3],"connectedNodes":[38]}]',
            traffic_lights='[]',
            destinations='[[2,2]]',
            origin='{"coordinate":[1,5],"direction":"E"}',
            max_fuel=14,
            blocklyEnabled=True,
            pythonEnabled=False,
            theme=Theme.objects.get(id=1),
            character=Character.objects.get(id='5'),
            model_solution='[6]',
        )
        level72.save()
        set_decor(level72, json.loads('[{"x":704,"y":391,"decorName":"tree2"},{"x":688,"y":590,"decorName":"pond"},{"x":701,"y":287,"decorName":"tree2"},{"x":718,"y":184,"decorName":"tree2"},{"x":400,"y":200,"decorName":"bush"},{"x":399,"y":255,"decorName":"bush"}]'))
        set_blocks(level72, json.loads('[{"type":"move_forwards","number":1},{"type":"turn_left","number":1},{"type":"turn_right","number":1},{"type":"turn_around","number":2},{"type":"controls_repeat_until","number":2},{"type":"at_destination"},{"type":"road_exists"}]'))
        return level72

    def create_level73():
        level73 = Level(
            name='73',
            default=True,
            path='[{"coordinate":[8,1],"connectedNodes":[47]},{"coordinate":[5,5],"connectedNodes":[2,12]},{"coordinate":[4,5],"connectedNodes":[3,1,48]},{"coordinate":[3,5],"connectedNodes":[2,4]},{"coordinate":[3,4],"connectedNodes":[3,5]},{"coordinate":[3,3],"connectedNodes":[4,6]},{"coordinate":[4,3],"connectedNodes":[5,7,21]},{"coordinate":[5,3],"connectedNodes":[6,8]},{"coordinate":[6,3],"connectedNodes":[7,9]},{"coordinate":[6,4],"connectedNodes":[10,8]},{"coordinate":[6,5],"connectedNodes":[11,9]},{"coordinate":[6,6],"connectedNodes":[12,10]},{"coordinate":[5,6],"connectedNodes":[13,11,1]},{"coordinate":[4,6],"connectedNodes":[14,12]},{"coordinate":[3,6],"connectedNodes":[15,13]},{"coordinate":[2,6],"connectedNodes":[14,16]},{"coordinate":[2,5],"connectedNodes":[15,17]},{"coordinate":[2,4],"connectedNodes":[16,18]},{"coordinate":[2,3],"connectedNodes":[39,17,19]},{"coordinate":[2,2],"connectedNodes":[18,20]},{"coordinate":[3,2],"connectedNodes":[19,21]},{"coordinate":[4,2],"connectedNodes":[20,6,22]},{"coordinate":[5,2],"connectedNodes":[21,23]},{"coordinate":[6,2],"connectedNodes":[22,24]},{"coordinate":[7,2],"connectedNodes":[23,25]},{"coordinate":[7,3],"connectedNodes":[26,24]},{"coordinate":[7,4],"connectedNodes":[27,25]},{"coordinate":[7,5],"connectedNodes":[28,26]},{"coordinate":[7,6],"connectedNodes":[29,27]},{"coordinate":[7,7],"connectedNodes":[30,28]},{"coordinate":[6,7],"connectedNodes":[31,29]},{"coordinate":[5,7],"connectedNodes":[32,30]},{"coordinate":[4,7],"connectedNodes":[33,31]},{"coordinate":[3,7],"connectedNodes":[34,32]},{"coordinate":[2,7],"connectedNodes":[35,33]},{"coordinate":[1,7],"connectedNodes":[34,36]},{"coordinate":[1,6],"connectedNodes":[35,37]},{"coordinate":[1,5],"connectedNodes":[36,38]},{"coordinate":[1,4],"connectedNodes":[37,39]},{"coordinate":[1,3],"connectedNodes":[38,18,40]},{"coordinate":[1,2],"connectedNodes":[39,41]},{"coordinate":[1,1],"connectedNodes":[40,42]},{"coordinate":[2,1],"connectedNodes":[41,43]},{"coordinate":[3,1],"connectedNodes":[42,44]},{"coordinate":[4,1],"connectedNodes":[43,45]},{"coordinate":[5,1],"connectedNodes":[44,46]},{"coordinate":[6,1],"connectedNodes":[45,47]},{"coordinate":[7,1],"connectedNodes":[46,0]},{"coordinate":[4,4],"connectedNodes":[2,49]},{"coordinate":[5,4],"connectedNodes":[48]}]',
            traffic_lights='[]',
            destinations='[[5,4]]',
            origin='{"coordinate":[8,1],"direction":"W"}',
            max_fuel=50,
            blocklyEnabled=True,
            pythonEnabled=False,
            theme=Theme.objects.get(id=3),
            character=Character.objects.get(id='4'),
            model_solution='[14]'

        )
        level73.save()
        set_decor(level73, json.loads('[{"x":4,"y":692,"decorName":"tree1"},{"x":5,"y":78,"decorName":"tree1"},{"x":2,"y":222,"decorName":"tree1"},{"x":5,"y":392,"decorName":"tree1"},{"x":8,"y":554,"decorName":"tree1"},{"x":802,"y":648,"decorName":"tree2"},{"x":796,"y":533,"decorName":"pond"},{"x":896,"y":351,"decorName":"bush"},{"x":842,"y":351,"decorName":"bush"},{"x":788,"y":352,"decorName":"bush"},{"x":950,"y":352,"decorName":"bush"},{"x":924,"y":385,"decorName":"bush"},{"x":869,"y":384,"decorName":"bush"},{"x":815,"y":383,"decorName":"bush"},{"x":895,"y":417,"decorName":"bush"},{"x":839,"y":415,"decorName":"bush"},{"x":863,"y":448,"decorName":"bush"}]'))
        set_blocks(level73, json.loads('[{"type":"move_forwards","number":1},{"type":"turn_left","number":1},{"type":"turn_right","number":1},{"type":"controls_repeat","number":1},{"type":"controls_repeat_until"},{"type":"logic_negate"},{"type":"road_exists"},{"type":"dead_end"}]'))
        return level73

    def create_level74():
        level74 = Level(
            name='74',
            default=True,
            path='[{"coordinate":[9,2],"connectedNodes":[1]},{"coordinate":[8,2],"connectedNodes":[2,18,0]},{"coordinate":[7,2],"connectedNodes":[1,3]},{"coordinate":[7,1],"connectedNodes":[4,2]},{"coordinate":[6,1],"connectedNodes":[5,3,6]},{"coordinate":[5,1],"connectedNodes":[16,7,4]},{"coordinate":[6,0],"connectedNodes":[4]},{"coordinate":[5,2],"connectedNodes":[8,10,5]},{"coordinate":[4,2],"connectedNodes":[15,9,7,16]},{"coordinate":[4,3],"connectedNodes":[12,10,8]},{"coordinate":[5,3],"connectedNodes":[9,11,7]},{"coordinate":[5,4],"connectedNodes":[12,10]},{"coordinate":[4,4],"connectedNodes":[13,11,9]},{"coordinate":[3,4],"connectedNodes":[42,12,14]},{"coordinate":[3,3],"connectedNodes":[13,15]},{"coordinate":[3,2],"connectedNodes":[37,14,8]},{"coordinate":[4,1],"connectedNodes":[8,5,17]},{"coordinate":[4,0],"connectedNodes":[16]},{"coordinate":[8,3],"connectedNodes":[19,1]},{"coordinate":[8,4],"connectedNodes":[20,18]},{"coordinate":[8,5],"connectedNodes":[21,43,19]},{"coordinate":[8,6],"connectedNodes":[22,20]},{"coordinate":[7,6],"connectedNodes":[23,21]},{"coordinate":[6,6],"connectedNodes":[24,22]},{"coordinate":[5,6],"connectedNodes":[25,23,38]},{"coordinate":[4,6],"connectedNodes":[26,24]},{"coordinate":[3,6],"connectedNodes":[27,25]},{"coordinate":[2,6],"connectedNodes":[28,39,26]},{"coordinate":[1,6],"connectedNodes":[29,27]},{"coordinate":[0,6],"connectedNodes":[28,30]},{"coordinate":[0,5],"connectedNodes":[29,31]},{"coordinate":[0,4],"connectedNodes":[30,40,32]},{"coordinate":[0,3],"connectedNodes":[31,33]},{"coordinate":[0,2],"connectedNodes":[32,34]},{"coordinate":[0,1],"connectedNodes":[33,35]},{"coordinate":[1,1],"connectedNodes":[34,36,41]},{"coordinate":[2,1],"connectedNodes":[35,37]},{"coordinate":[2,2],"connectedNodes":[15,36]},{"coordinate":[5,5],"connectedNodes":[24]},{"coordinate":[2,7],"connectedNodes":[27]},{"coordinate":[1,4],"connectedNodes":[31]},{"coordinate":[1,0],"connectedNodes":[35]},{"coordinate":[3,5],"connectedNodes":[13]},{"coordinate":[9,5],"connectedNodes":[20]}]',
            traffic_lights='[]',
            destinations='[[4,0]]',
            origin='{"coordinate":[9,2],"direction":"W"}',
            max_fuel=50,
            blocklyEnabled=True,
            pythonEnabled=False,
            theme=Theme.objects.get(id=2),
            character=Character.objects.get(id='1'),
            model_solution='[10]',
        )
        level74.save()
        set_decor(level74, json.loads('[{"x":738,"y":33,"decorName":"tree1"},{"x":397,"y":495,"decorName":"tree2"},{"x":248,"y":39,"decorName":"pond"},{"x":94,"y":498,"decorName":"bush"},{"x":148,"y":558,"decorName":"bush"},{"x":96,"y":558,"decorName":"bush"}]'))
        set_blocks(level74, json.loads('[{"type":"move_forwards","number":1},{"type":"turn_left","number":3},{"type":"turn_right","number":1},{"type":"turn_around","number":2},{"type":"controls_repeat","number":1},{"type":"call_proc"},{"type":"declare_proc"}]'))
        return level74

    def create_level75():
        level75 = Level(
            name='75',
            default=True,
            path='[{"coordinate":[1,6],"connectedNodes":[18]},{"coordinate":[2,5],"connectedNodes":[18,2]},{"coordinate":[2,6],"connectedNodes":[3,1]},{"coordinate":[3,6],"connectedNodes":[2,4]},{"coordinate":[3,5],"connectedNodes":[3,5]},{"coordinate":[3,4],"connectedNodes":[4,6]},{"coordinate":[3,3],"connectedNodes":[5,7]},{"coordinate":[3,2],"connectedNodes":[6,8]},{"coordinate":[4,2],"connectedNodes":[7,9]},{"coordinate":[4,3],"connectedNodes":[10,8]},{"coordinate":[4,4],"connectedNodes":[11,9]},{"coordinate":[4,5],"connectedNodes":[12,10]},{"coordinate":[4,6],"connectedNodes":[13,11]},{"coordinate":[5,6],"connectedNodes":[12,14]},{"coordinate":[5,5],"connectedNodes":[13,15]},{"coordinate":[5,4],"connectedNodes":[14,16]},{"coordinate":[5,3],"connectedNodes":[15,17]},{"coordinate":[5,2],"connectedNodes":[16]},{"coordinate":[1,5],"connectedNodes":[0,1]}]',
            traffic_lights='[{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":3,"y":4},"direction":"S","startTime":0,"startingState":"GREEN"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":4,"y":4},"direction":"N","startTime":0,"startingState":"RED"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":5,"y":5},"direction":"S","startTime":0,"startingState":"RED"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":3,"y":5},"direction":"S","startTime":0,"startingState":"RED"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":5,"y":4},"direction":"S","startTime":0,"startingState":"GREEN"}]',
            destinations='[[5,2]]',
            origin='{"coordinate":[1,6],"direction":"S"}',
            max_fuel=50,
            blocklyEnabled=True,
            pythonEnabled=False,
            theme=Theme.objects.get(id=2),
            character=Character.objects.get(id='1'),
            model_solution='[26]',
        )
        level75.save()
        set_decor(level75, json.loads('[{"x":259,"y":477,"decorName":"bush"},{"x":258,"y":416,"decorName":"bush"},{"x":258,"y":352,"decorName":"bush"},{"x":258,"y":282,"decorName":"bush"},{"x":777,"y":507,"decorName":"tree1"},{"x":413,"y":686,"decorName":"tree1"},{"x":859,"y":220,"decorName":"tree1"},{"x":639,"y":700,"decorName":"tree1"},{"x":699,"y":298,"decorName":"tree1"},{"x":900,"y":378,"decorName":"tree2"},{"x":736,"y":700,"decorName":"tree2"},{"x":900,"y":695,"decorName":"tree2"},{"x":728,"y":628,"decorName":"tree1"},{"x":884,"y":577,"decorName":"tree2"},{"x":834,"y":655,"decorName":"tree1"},{"x":900,"y":502,"decorName":"tree1"},{"x":658,"y":525,"decorName":"tree2"},{"x":793,"y":399,"decorName":"tree2"}]'))
        set_blocks(level75, json.loads('[{"type":"move_forwards","number":1},{"type":"turn_left","number":1},{"type":"turn_right","number":1},{"type":"wait","number":1},{"type":"controls_repeat_until"},{"type":"controls_if"},{"type":"road_exists"},{"type":"dead_end"},{"type":"traffic_light"},{"type":"call_proc"},{"type":"declare_proc"}]'))
        return level75

    def create_level79():
        level79 = Level(
            name='79',
            default=True,
            path='[{"coordinate":[9,0],"connectedNodes":[76]},{"coordinate":[2,5],"connectedNodes":[77,2]},{"coordinate":[2,4],"connectedNodes":[1,5]},{"coordinate":[1,4],"connectedNodes":[15,4]},{"coordinate":[1,3],"connectedNodes":[3,5]},{"coordinate":[2,3],"connectedNodes":[4,2,6]},{"coordinate":[3,3],"connectedNodes":[5,7]},{"coordinate":[3,4],"connectedNodes":[8,6]},{"coordinate":[3,5],"connectedNodes":[10,22,7]},{"coordinate":[2,6],"connectedNodes":[11,10]},{"coordinate":[3,6],"connectedNodes":[9,8]},{"coordinate":[1,6],"connectedNodes":[12,9]},{"coordinate":[1,7],"connectedNodes":[13,18,11]},{"coordinate":[0,7],"connectedNodes":[12,14]},{"coordinate":[0,6],"connectedNodes":[13,17]},{"coordinate":[0,4],"connectedNodes":[3,16]},{"coordinate":[0,3],"connectedNodes":[15,73]},{"coordinate":[0,5],"connectedNodes":[14,77]},{"coordinate":[2,7],"connectedNodes":[12,19]},{"coordinate":[3,7],"connectedNodes":[18,20]},{"coordinate":[4,7],"connectedNodes":[19,21]},{"coordinate":[4,6],"connectedNodes":[20,24]},{"coordinate":[4,5],"connectedNodes":[8,23]},{"coordinate":[5,5],"connectedNodes":[22,28,43]},{"coordinate":[5,6],"connectedNodes":[21,25]},{"coordinate":[5,7],"connectedNodes":[26,24]},{"coordinate":[6,7],"connectedNodes":[25,27]},{"coordinate":[6,6],"connectedNodes":[26,30]},{"coordinate":[6,5],"connectedNodes":[23,29]},{"coordinate":[6,4],"connectedNodes":[28,39]},{"coordinate":[7,6],"connectedNodes":[27,31]},{"coordinate":[8,6],"connectedNodes":[30,35]},{"coordinate":[8,7],"connectedNodes":[33,34]},{"coordinate":[7,7],"connectedNodes":[32]},{"coordinate":[9,7],"connectedNodes":[32,35]},{"coordinate":[9,6],"connectedNodes":[31,34,36]},{"coordinate":[9,5],"connectedNodes":[35,37]},{"coordinate":[9,4],"connectedNodes":[38,36,49]},{"coordinate":[8,4],"connectedNodes":[39,41,37]},{"coordinate":[7,4],"connectedNodes":[29,38]},{"coordinate":[7,5],"connectedNodes":[41]},{"coordinate":[8,5],"connectedNodes":[40,38]},{"coordinate":[4,4],"connectedNodes":[43,45]},{"coordinate":[5,4],"connectedNodes":[42,23]},{"coordinate":[5,3],"connectedNodes":[45,46,54]},{"coordinate":[4,3],"connectedNodes":[42,44]},{"coordinate":[6,3],"connectedNodes":[44,47,53]},{"coordinate":[7,3],"connectedNodes":[46,48]},{"coordinate":[8,3],"connectedNodes":[47,49]},{"coordinate":[9,3],"connectedNodes":[48,37,50]},{"coordinate":[9,2],"connectedNodes":[51,49,76]},{"coordinate":[8,2],"connectedNodes":[50]},{"coordinate":[7,2],"connectedNodes":[53]},{"coordinate":[6,2],"connectedNodes":[46,52]},{"coordinate":[5,2],"connectedNodes":[55,44]},{"coordinate":[4,2],"connectedNodes":[54]},{"coordinate":[3,2],"connectedNodes":[69,57]},{"coordinate":[3,1],"connectedNodes":[56,58]},{"coordinate":[4,1],"connectedNodes":[57,59]},{"coordinate":[5,1],"connectedNodes":[58,60]},{"coordinate":[6,1],"connectedNodes":[59,63]},{"coordinate":[7,1],"connectedNodes":[78,62]},{"coordinate":[7,0],"connectedNodes":[63,61]},{"coordinate":[6,0],"connectedNodes":[64,60,62]},{"coordinate":[5,0],"connectedNodes":[65,63]},{"coordinate":[4,0],"connectedNodes":[66,64]},{"coordinate":[3,0],"connectedNodes":[68,65]},{"coordinate":[2,1],"connectedNodes":[68]},{"coordinate":[2,0],"connectedNodes":[75,67,66]},{"coordinate":[2,2],"connectedNodes":[70,56]},{"coordinate":[1,2],"connectedNodes":[73,69,71]},{"coordinate":[1,1],"connectedNodes":[72,70]},{"coordinate":[0,1],"connectedNodes":[71,74]},{"coordinate":[0,2],"connectedNodes":[16,70]},{"coordinate":[0,0],"connectedNodes":[72,75]},{"coordinate":[1,0],"connectedNodes":[74,68]},{"coordinate":[9,1],"connectedNodes":[50,0]},{"coordinate":[1,5],"connectedNodes":[17,1]},{"coordinate":[8,1],"connectedNodes":[61,79]},{"coordinate":[8,0],"connectedNodes":[78]}]',
            traffic_lights='[]',
            destinations='[[8,0]]',
            origin='{"coordinate":[9,0],"direction":"N"}',
            max_fuel=50,
            blocklyEnabled=True,
            pythonEnabled=False,
            theme=Theme.objects.get(id=1),
            character=Character.objects.get(id='2'),
            model_solution='[55]',
        )
        level79.save()
        set_decor(level79, json.loads('[]'))
        set_blocks(level79, json.loads('[{"type":"move_forwards","number":7},{"type":"turn_left","number":4},{"type":"turn_right","number":1},{"type":"controls_if"},{"type":"logic_negate"},{"type":"road_exists"},{"type":"call_proc"},{"type":"declare_proc","number":1}]'))
        return level79

    def create_level80():
        level80 = Level(
            name='80',
            default=True,
            path='[{"coordinate":[1,3],"connectedNodes":[1]},{"coordinate":[2,3],"connectedNodes":[0,2]},{"coordinate":[3,3],"connectedNodes":[1,3]},{"coordinate":[3,4],"connectedNodes":[4,2]},{"coordinate":[3,5],"connectedNodes":[5,3]},{"coordinate":[4,5],"connectedNodes":[4,6]},{"coordinate":[5,5],"connectedNodes":[5]}]',
            traffic_lights='[]',
            destinations='[[5,5]]',
            origin='{"coordinate":[1,3],"direction":"E"}',
            max_fuel=50,
            blocklyEnabled=True,
            pythonEnabled=True,
            theme=Theme.objects.get(id=3),
            character=Character.objects.get(id='1'),
        )
        level80.save()
        set_decor(level80, json.loads('[{"x":436,"y":374,"decorName":"pond"},{"x":437,"y":283,"decorName":"pond"},{"x":872,"y":331,"decorName":"tree1"},{"x":720,"y":193,"decorName":"tree1"},{"x":81,"y":623,"decorName":"tree1"},{"x":190,"y":669,"decorName":"tree1"},{"x":25,"y":521,"decorName":"tree1"},{"x":442,"y":590,"decorName":"bush"},{"x":375,"y":591,"decorName":"bush"},{"x":410,"y":628,"decorName":"bush"},{"x":723,"y":73,"decorName":"tree1"},{"x":603,"y":17,"decorName":"tree1"},{"x":862,"y":169,"decorName":"tree1"},{"x":830,"y":14,"decorName":"tree1"},{"x":0,"y":697,"decorName":"tree1"}]'))
        set_blocks(level80, json.loads('[{"type":"move_forwards"},{"type":"turn_left"},{"type":"turn_right"}]'))
        return level80

    def create_level84():
        level84 = Level(
            name='84',
            default=True,
            path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[1,4],"connectedNodes":[3,1]},{"coordinate":[2,4],"connectedNodes":[2,4]},{"coordinate":[2,3],"connectedNodes":[3,5]},{"coordinate":[3,3],"connectedNodes":[4,6]},{"coordinate":[3,4],"connectedNodes":[7,5]},{"coordinate":[4,4],"connectedNodes":[6,8]},{"coordinate":[4,3],"connectedNodes":[7,9]},{"coordinate":[5,3],"connectedNodes":[8,10]},{"coordinate":[5,4],"connectedNodes":[11,9]},{"coordinate":[6,4],"connectedNodes":[10,12]},{"coordinate":[6,3],"connectedNodes":[11,13]},{"coordinate":[7,3],"connectedNodes":[12,14]},{"coordinate":[7,4],"connectedNodes":[15,13]},{"coordinate":[8,4],"connectedNodes":[14,16]},{"coordinate":[8,3],"connectedNodes":[15,17]},{"coordinate":[9,3],"connectedNodes":[16]}]',
            traffic_lights='[]',
            destinations='[[9,3]]',
            origin='{"coordinate":[0,3],"direction":"E"}',
            max_fuel=50,
            blocklyEnabled=True,
            pythonEnabled=True,
            theme=Theme.objects.get(id=2),
            character=Character.objects.get(id='1'),
        )
        level84.save()
        set_decor(level84, json.loads('[{"x":156,"y":584,"decorName":"tree1"},{"x":181,"y":169,"decorName":"tree2"},{"x":750,"y":225,"decorName":"tree1"},{"x":311,"y":615,"decorName":"tree2"},{"x":225,"y":509,"decorName":"pond"},{"x":37,"y":483,"decorName":"tree2"},{"x":472,"y":487,"decorName":"tree1"},{"x":54,"y":675,"decorName":"tree1"}]'))
        set_blocks(level84, json.loads('[{"type":"move_forwards"},{"type":"turn_left"},{"type":"turn_right"},{"type":"controls_repeat"}]'))
        return level84

    def create_level88():
        level88 = Level(
            name='88',
            default=True,
            path='[{"coordinate":[2,6],"connectedNodes":[1]},{"coordinate":[2,5],"connectedNodes":[0,2]},{"coordinate":[2,4],"connectedNodes":[10,1,3]},{"coordinate":[2,3],"connectedNodes":[2,4]},{"coordinate":[3,3],"connectedNodes":[3,5]},{"coordinate":[4,3],"connectedNodes":[4,6]},{"coordinate":[4,2],"connectedNodes":[5,14,7]},{"coordinate":[4,1],"connectedNodes":[8,6]},{"coordinate":[3,1],"connectedNodes":[9,7]},{"coordinate":[2,1],"connectedNodes":[8]},{"coordinate":[1,4],"connectedNodes":[11,2]},{"coordinate":[0,4],"connectedNodes":[10,12]},{"coordinate":[0,3],"connectedNodes":[11,13]},{"coordinate":[0,2],"connectedNodes":[12]},{"coordinate":[5,2],"connectedNodes":[6,15]},{"coordinate":[6,2],"connectedNodes":[14,16]},{"coordinate":[6,3],"connectedNodes":[17,15]},{"coordinate":[6,4],"connectedNodes":[18,20,16]},{"coordinate":[5,4],"connectedNodes":[19,17]},{"coordinate":[5,5],"connectedNodes":[18]},{"coordinate":[7,4],"connectedNodes":[17,21]},{"coordinate":[8,4],"connectedNodes":[20,22]},{"coordinate":[8,5],"connectedNodes":[23,21]},{"coordinate":[8,6],"connectedNodes":[22]}]',
            traffic_lights='[{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":2,"y":3},"direction":"E","startTime":0,"startingState":"GREEN"}]',
            destinations='[[2,1]]',
            origin='{"coordinate":[2,6],"direction":"S"}',
            max_fuel=50,
            blocklyEnabled=True,
            pythonEnabled=True,
            theme=Theme.objects.get(id=4),
            character=Character.objects.get(id='1'),
        )
        level88.save()
        set_decor(level88, json.loads('[{"x":0,"y":117,"decorName":"tree2"},{"x":630,"y":484,"decorName":"pond"},{"x":289,"y":458,"decorName":"bush"},{"x":288,"y":395,"decorName":"bush"},{"x":289,"y":525,"decorName":"bush"},{"x":695,"y":355,"decorName":"bush"},{"x":694,"y":152,"decorName":"bush"},{"x":695,"y":214,"decorName":"bush"},{"x":694,"y":285,"decorName":"bush"},{"x":551,"y":152,"decorName":"bush"},{"x":622,"y":152,"decorName":"bush"},{"x":487,"y":152,"decorName":"bush"},{"x":496,"y":286,"decorName":"tree1"}]'))
        set_blocks(level88, json.loads('[{"type":"move_forwards"},{"type":"turn_left"},{"type":"turn_right"},{"type":"controls_repeat_while"},{"type":"controls_if"},{"type":"logic_negate"},{"type":"at_destination"},{"type":"road_exists"},{"type":"traffic_light"}]'))
        return level88

    def create_level90():
        level90 = Level(
            name='90',
            default=True,
            path='[{"coordinate":[1,6],"connectedNodes":[1]},{"coordinate":[2,6],"connectedNodes":[0,2]},{"coordinate":[2,5],"connectedNodes":[1,3]},{"coordinate":[3,5],"connectedNodes":[2,4]},{"coordinate":[4,5],"connectedNodes":[3,5]},{"coordinate":[4,4],"connectedNodes":[4,6]},{"coordinate":[5,4],"connectedNodes":[5,7]},{"coordinate":[5,3],"connectedNodes":[6,8]},{"coordinate":[6,3],"connectedNodes":[7,9]},{"coordinate":[7,3],"connectedNodes":[8,10]},{"coordinate":[7,2],"connectedNodes":[9,11]},{"coordinate":[8,2],"connectedNodes":[10,12]},{"coordinate":[8,1],"connectedNodes":[13,11]},{"coordinate":[7,1],"connectedNodes":[14,12]},{"coordinate":[6,1],"connectedNodes":[15,13]},{"coordinate":[5,1],"connectedNodes":[16,14]},{"coordinate":[4,1],"connectedNodes":[17,15]},{"coordinate":[3,1],"connectedNodes":[18,16]},{"coordinate":[3,2],"connectedNodes":[19,17]},{"coordinate":[2,2],"connectedNodes":[20,18]},{"coordinate":[2,3],"connectedNodes":[21,19]},{"coordinate":[1,3],"connectedNodes":[20]}]',
            traffic_lights='[]',
            destinations='[[1,3]]',
            origin='{"coordinate":[1,6],"direction":"E"}',
            max_fuel=50,
            blocklyEnabled=True,
            pythonEnabled=True,
            theme=Theme.objects.get(id=4),
            character=Character.objects.get(id='1'),
        )
        level90.save()
        set_decor(level90, json.loads('[{"x":607,"y":213,"decorName":"tree2"},{"x":276,"y":357,"decorName":"pond"},{"x":295,"y":594,"decorName":"bush"},{"x":360,"y":594,"decorName":"bush"},{"x":424,"y":592,"decorName":"bush"},{"x":482,"y":592,"decorName":"bush"},{"x":484,"y":532,"decorName":"bush"},{"x":712,"y":393,"decorName":"bush"},{"x":771,"y":391,"decorName":"bush"},{"x":649,"y":394,"decorName":"bush"},{"x":592,"y":395,"decorName":"bush"},{"x":708,"y":186,"decorName":"bush"},{"x":772,"y":334,"decorName":"bush"},{"x":540,"y":528,"decorName":"bush"},{"x":594,"y":458,"decorName":"bush"},{"x":596,"y":524,"decorName":"bush"}]'))
        set_blocks(level90, json.loads('[{"type":"move_forwards"},{"type":"turn_left"},{"type":"turn_right"},{"type":"controls_repeat"},{"type":"call_proc"},{"type":"declare_proc"}]'))
        return level90

    def create_level91():
        level91 = Level(
            name='91',
            default=True,
            path='[{"coordinate":[1,6],"connectedNodes":[1]},{"coordinate":[2,6],"connectedNodes":[0,2]},{"coordinate":[3,6],"connectedNodes":[1,3]},{"coordinate":[3,5],"connectedNodes":[2,4]},{"coordinate":[3,4],"connectedNodes":[3,5]},{"coordinate":[3,3],"connectedNodes":[6,4]},{"coordinate":[2,3],"connectedNodes":[5,7]},{"coordinate":[2,2],"connectedNodes":[6,8]},{"coordinate":[3,2],"connectedNodes":[7,9]},{"coordinate":[4,2],"connectedNodes":[8,10]},{"coordinate":[5,2],"connectedNodes":[9,11]},{"coordinate":[5,1],"connectedNodes":[10,12]},{"coordinate":[6,1],"connectedNodes":[11,13]},{"coordinate":[6,2],"connectedNodes":[14,12]},{"coordinate":[6,3],"connectedNodes":[15,13]},{"coordinate":[6,4],"connectedNodes":[16,14]},{"coordinate":[6,5],"connectedNodes":[17,15]},{"coordinate":[7,5],"connectedNodes":[16,18]},{"coordinate":[7,6],"connectedNodes":[19,17]},{"coordinate":[6,6],"connectedNodes":[20,18]},{"coordinate":[5,6],"connectedNodes":[21,19]},{"coordinate":[4,6],"connectedNodes":[22,20]},{"coordinate":[4,7],"connectedNodes":[21]}]',
            traffic_lights='[]',
            destinations='[[4,7]]',
            origin='{"coordinate":[1,6],"direction":"E"}',
            max_fuel=50,
            blocklyEnabled=True,
            pythonEnabled=True,
            theme=Theme.objects.get(id=2),
            character=Character.objects.get(id='1'),
        )
        level91.save()
        set_decor(level91, json.loads('[{"x":152,"y":498,"decorName":"tree1"},{"x":103,"y":377,"decorName":"tree1"},{"x":782,"y":329,"decorName":"pond"},{"x":551,"y":482,"decorName":"bush"},{"x":554,"y":545,"decorName":"bush"},{"x":551,"y":286,"decorName":"bush"},{"x":551,"y":349,"decorName":"bush"},{"x":550,"y":414,"decorName":"bush"},{"x":732,"y":221,"decorName":"tree2"},{"x":894,"y":437,"decorName":"tree2"},{"x":0,"y":273,"decorName":"tree1"},{"x":0,"y":502,"decorName":"tree1"}]'))
        set_blocks(level91, json.loads('[{"type":"move_forwards"},{"type":"turn_left"},{"type":"turn_right"},{"type":"controls_repeat"},{"type":"call_proc"},{"type":"declare_proc"}]'))
        return level91

    def create_level92():
        level92 = Level(
            name='92',
            default=True,
            path='[{"coordinate":[3,6],"connectedNodes":[1]},{"coordinate":[3,5],"connectedNodes":[0,2]},{"coordinate":[3,4],"connectedNodes":[3,1]},{"coordinate":[2,4],"connectedNodes":[2,4]},{"coordinate":[2,3],"connectedNodes":[3,5]},{"coordinate":[2,2],"connectedNodes":[4]}]',
            traffic_lights='[]',
            destinations='[[2,2]]',
            origin='{"coordinate":[3,6],"direction":"S"}',
            max_fuel=50,
            blocklyEnabled=False,
            pythonEnabled=True,
            theme=Theme.objects.get(id=3),
            character=Character.objects.get(id='1'),
        )
        level92.save()
        set_decor(level92, json.loads('[{"x":291,"y":329,"decorName":"tree2"},{"x":106,"y":604,"decorName":"pond"},{"x":106,"y":502,"decorName":"pond"},{"x":764,"y":664,"decorName":"tree1"},{"x":882,"y":622,"decorName":"tree1"},{"x":799,"y":575,"decorName":"tree1"},{"x":751,"y":404,"decorName":"tree1"},{"x":665,"y":560,"decorName":"tree1"},{"x":880,"y":473,"decorName":"tree1"},{"x":579,"y":659,"decorName":"tree1"},{"x":529,"y":431,"decorName":"tree1"},{"x":772,"y":0,"decorName":"pond"},{"x":772,"y":101,"decorName":"pond"},{"x":605,"y":101,"decorName":"pond"},{"x":430,"y":102,"decorName":"pond"},{"x":605,"y":3,"decorName":"pond"},{"x":430,"y":3,"decorName":"pond"},{"x":150,"y":339,"decorName":"bush"},{"x":94,"y":338,"decorName":"bush"},{"x":36,"y":338,"decorName":"bush"},{"x":99,"y":409,"decorName":"bush"},{"x":126,"y":370,"decorName":"bush"},{"x":65,"y":372,"decorName":"bush"}]'))
        return level92

    def create_level97():
        level97 = Level(
            name='97',
            default=True,
            path='[{"coordinate":[1,6],"connectedNodes":[1]},{"coordinate":[1,5],"connectedNodes":[0,2]},{"coordinate":[1,4],"connectedNodes":[1,3]},{"coordinate":[1,3],"connectedNodes":[2,4]},{"coordinate":[1,2],"connectedNodes":[3,5]},{"coordinate":[1,1],"connectedNodes":[4,6]},{"coordinate":[2,1],"connectedNodes":[5,7]},{"coordinate":[2,2],"connectedNodes":[8,6]},{"coordinate":[2,3],"connectedNodes":[9,7]},{"coordinate":[2,4],"connectedNodes":[10,8]},{"coordinate":[2,5],"connectedNodes":[11,9]},{"coordinate":[2,6],"connectedNodes":[12,10]},{"coordinate":[3,6],"connectedNodes":[11,17]},{"coordinate":[3,1],"connectedNodes":[14,18]},{"coordinate":[3,2],"connectedNodes":[15,13]},{"coordinate":[3,3],"connectedNodes":[16,14]},{"coordinate":[3,4],"connectedNodes":[17,15]},{"coordinate":[3,5],"connectedNodes":[12,16]},{"coordinate":[4,1],"connectedNodes":[13,19]},{"coordinate":[4,2],"connectedNodes":[20,18]},{"coordinate":[4,3],"connectedNodes":[21,19]},{"coordinate":[4,4],"connectedNodes":[22,20]},{"coordinate":[4,5],"connectedNodes":[23,21]},{"coordinate":[4,6],"connectedNodes":[24,22]},{"coordinate":[5,6],"connectedNodes":[23,25]},{"coordinate":[5,5],"connectedNodes":[24,26]},{"coordinate":[5,4],"connectedNodes":[25,27]},{"coordinate":[5,3],"connectedNodes":[26,28]},{"coordinate":[5,2],"connectedNodes":[27,29]},{"coordinate":[5,1],"connectedNodes":[28,30]},{"coordinate":[6,1],"connectedNodes":[29,31]},{"coordinate":[6,2],"connectedNodes":[32,30]},{"coordinate":[6,3],"connectedNodes":[33,31]},{"coordinate":[6,4],"connectedNodes":[34,32]},{"coordinate":[6,5],"connectedNodes":[35,33]},{"coordinate":[6,6],"connectedNodes":[36,34]},{"coordinate":[7,6],"connectedNodes":[35,37]},{"coordinate":[7,5],"connectedNodes":[36]}]',
            traffic_lights='[]',
            destinations='[[7,5]]',
            origin='{"coordinate":[1,6],"direction":"S"}',
            max_fuel=50,
            blocklyEnabled=False,
            pythonEnabled=True,
            theme=Theme.objects.get(id=2),
            character=Character.objects.get(id='1'),
        )
        level97.save()
        set_decor(level97, json.loads('[{"x":0,"y":4,"decorName":"tree1"},{"x":296,"y":695,"decorName":"tree1"},{"x":102,"y":700,"decorName":"tree1"},{"x":0,"y":599,"decorName":"tree1"},{"x":0,"y":395,"decorName":"tree1"},{"x":0,"y":198,"decorName":"tree1"},{"x":900,"y":700,"decorName":"tree1"},{"x":700,"y":700,"decorName":"tree1"},{"x":503,"y":700,"decorName":"tree1"},{"x":900,"y":99,"decorName":"tree1"},{"x":803,"y":0,"decorName":"tree1"},{"x":600,"y":0,"decorName":"tree1"},{"x":399,"y":0,"decorName":"tree1"},{"x":199,"y":0,"decorName":"tree1"},{"x":900,"y":499,"decorName":"tree1"},{"x":897,"y":300,"decorName":"tree1"},{"x":687,"y":422,"decorName":"bush"},{"x":685,"y":338,"decorName":"bush"},{"x":686,"y":264,"decorName":"bush"},{"x":685,"y":185,"decorName":"bush"},{"x":684,"y":112,"decorName":"bush"}]'))
        return level97

    def create_level100():
        level100 = Level(
            name='100',
            default=True,
            path='[{"coordinate":[8,6],"connectedNodes":[1]},{"coordinate":[7,6],"connectedNodes":[2,0]},{"coordinate":[6,6],"connectedNodes":[1,3]},{"coordinate":[6,5],"connectedNodes":[2,4]},{"coordinate":[7,5],"connectedNodes":[3,5]},{"coordinate":[7,4],"connectedNodes":[6,4]},{"coordinate":[6,4],"connectedNodes":[7,5]},{"coordinate":[5,4],"connectedNodes":[8,6]},{"coordinate":[5,5],"connectedNodes":[9,7]},{"coordinate":[5,6],"connectedNodes":[10,8]},{"coordinate":[4,6],"connectedNodes":[11,9]},{"coordinate":[3,6],"connectedNodes":[12,10]},{"coordinate":[2,6],"connectedNodes":[11,13]},{"coordinate":[2,5],"connectedNodes":[12,14]},{"coordinate":[3,5],"connectedNodes":[13,15]},{"coordinate":[3,4],"connectedNodes":[16,14]},{"coordinate":[2,4],"connectedNodes":[17,15]},{"coordinate":[1,4],"connectedNodes":[18,16]},{"coordinate":[1,5],"connectedNodes":[19,17]},{"coordinate":[1,6],"connectedNodes":[20,18]},{"coordinate":[0,6],"connectedNodes":[19,21]},{"coordinate":[0,5],"connectedNodes":[20,22]},{"coordinate":[0,4],"connectedNodes":[21,23]},{"coordinate":[0,3],"connectedNodes":[22,24]},{"coordinate":[0,2],"connectedNodes":[23,25]},{"coordinate":[0,1],"connectedNodes":[24,26]},{"coordinate":[1,1],"connectedNodes":[25,27]},{"coordinate":[2,1],"connectedNodes":[26,28]},{"coordinate":[3,1],"connectedNodes":[27,29]},{"coordinate":[4,1],"connectedNodes":[28,30]},{"coordinate":[5,1],"connectedNodes":[29,33]},{"coordinate":[6,3],"connectedNodes":[32]},{"coordinate":[6,2],"connectedNodes":[31,33]},{"coordinate":[6,1],"connectedNodes":[30,32,34]},{"coordinate":[7,1],"connectedNodes":[33,35]},{"coordinate":[8,1],"connectedNodes":[34]}]',
            traffic_lights='[]',
            destinations='[[8,1]]',
            origin='{"coordinate":[8,6],"direction":"W"}',
            max_fuel=50,
            blocklyEnabled=False,
            pythonEnabled=True,
            theme=Theme.objects.get(id=4),
            character=Character.objects.get(id='1'),
        )
        level100.save()
        set_decor(level100, json.loads('[{"x":682,"y":228,"decorName":"tree1"},{"x":186,"y":189,"decorName":"pond"},{"x":332,"y":571,"decorName":"bush"},{"x":404,"y":506,"decorName":"tree2"},{"x":98,"y":191,"decorName":"bush"},{"x":97,"y":251,"decorName":"bush"},{"x":98,"y":315,"decorName":"bush"},{"x":354,"y":192,"decorName":"bush"},{"x":354,"y":252,"decorName":"bush"},{"x":354,"y":317,"decorName":"bush"},{"x":676,"y":698,"decorName":"bush"},{"x":750,"y":700,"decorName":"bush"},{"x":297,"y":357,"decorName":"bush"},{"x":230,"y":357,"decorName":"bush"},{"x":160,"y":356,"decorName":"bush"},{"x":902,"y":550,"decorName":"bush"},{"x":827,"y":550,"decorName":"bush"},{"x":754,"y":552,"decorName":"bush"},{"x":901,"y":697,"decorName":"bush"},{"x":826,"y":699,"decorName":"bush"},{"x":904,"y":627,"decorName":"bush"}]'))
        return level100

    def create_level101():
        level101 = Level(
            name='101',
            default=True,
            path='[{"coordinate":[1,6],"connectedNodes":[1]},{"coordinate":[2,6],"connectedNodes":[0,2]},{"coordinate":[2,5],"connectedNodes":[1,3,19]},{"coordinate":[3,5],"connectedNodes":[2,4]},{"coordinate":[4,5],"connectedNodes":[3,5]},{"coordinate":[4,4],"connectedNodes":[4,6]},{"coordinate":[5,4],"connectedNodes":[5,7]},{"coordinate":[6,4],"connectedNodes":[6,14,8]},{"coordinate":[7,4],"connectedNodes":[7,9]},{"coordinate":[7,3],"connectedNodes":[8,10]},{"coordinate":[8,3],"connectedNodes":[9,18,11]},{"coordinate":[8,2],"connectedNodes":[12,10]},{"coordinate":[7,2],"connectedNodes":[11,13]},{"coordinate":[7,1],"connectedNodes":[26,12]},{"coordinate":[6,5],"connectedNodes":[15,7]},{"coordinate":[6,6],"connectedNodes":[16,14]},{"coordinate":[7,6],"connectedNodes":[15,17]},{"coordinate":[8,6],"connectedNodes":[16]},{"coordinate":[9,3],"connectedNodes":[10]},{"coordinate":[2,4],"connectedNodes":[20,2]},{"coordinate":[1,4],"connectedNodes":[19,21]},{"coordinate":[1,3],"connectedNodes":[24,20,22]},{"coordinate":[2,3],"connectedNodes":[21,23]},{"coordinate":[3,3],"connectedNodes":[22]},{"coordinate":[0,3],"connectedNodes":[21,25]},{"coordinate":[0,2],"connectedNodes":[24]},{"coordinate":[6,1],"connectedNodes":[27,13]},{"coordinate":[5,1],"connectedNodes":[26]}]',
            traffic_lights='[]',
            destinations='[[5,1]]',
            origin='{"coordinate":[1,6],"direction":"E"}',
            max_fuel=50,
            blocklyEnabled=True,
            pythonEnabled=True,
            theme=Theme.objects.get(id=4),
            character=Character.objects.get(id='1'),
        )
        level101.save()
        set_decor(level101, json.loads('[{"x":739,"y":509,"decorName":"tree2"},{"x":117,"y":162,"decorName":"pond"},{"x":290,"y":458,"decorName":"bush"},{"x":358,"y":457,"decorName":"bush"},{"x":358,"y":397,"decorName":"bush"},{"x":422,"y":352,"decorName":"bush"},{"x":495,"y":352,"decorName":"bush"},{"x":566,"y":353,"decorName":"bush"},{"x":638,"y":354,"decorName":"bush"},{"x":792,"y":380,"decorName":"tree1"},{"x":692,"y":689,"decorName":"bush"},{"x":627,"y":688,"decorName":"bush"},{"x":824,"y":692,"decorName":"bush"},{"x":756,"y":690,"decorName":"bush"}]'))
        return level101

    def create_level102():
        level102 = Level(
            name='102',
            default=True,
            path='[{"coordinate":[1,4],"connectedNodes":[1]},{"coordinate":[2,4],"connectedNodes":[0,2]},{"coordinate":[2,5],"connectedNodes":[3,1]},{"coordinate":[3,5],"connectedNodes":[2,4]},{"coordinate":[3,6],"connectedNodes":[5,3]},{"coordinate":[4,6],"connectedNodes":[4,6]},{"coordinate":[4,5],"connectedNodes":[5,7]},{"coordinate":[5,5],"connectedNodes":[6,8]},{"coordinate":[5,4],"connectedNodes":[7,9]},{"coordinate":[6,4],"connectedNodes":[8,10]},{"coordinate":[7,4],"connectedNodes":[9,11]},{"coordinate":[7,3],"connectedNodes":[10,12]},{"coordinate":[7,2],"connectedNodes":[11,13]},{"coordinate":[7,1],"connectedNodes":[14,12]},{"coordinate":[6,1],"connectedNodes":[15,13]},{"coordinate":[6,2],"connectedNodes":[16,14]},{"coordinate":[5,2],"connectedNodes":[17,15]},{"coordinate":[5,3],"connectedNodes":[18,16]},{"coordinate":[4,3],"connectedNodes":[17,19]},{"coordinate":[4,2],"connectedNodes":[20,18]},{"coordinate":[3,2],"connectedNodes":[19,21]},{"coordinate":[3,1],"connectedNodes":[22,20]},{"coordinate":[2,1],"connectedNodes":[23,21]},{"coordinate":[1,1],"connectedNodes":[22]}]',
            traffic_lights='[]',
            destinations='[[1,1]]',
            origin='{"coordinate":[1,4],"direction":"E"}',
            max_fuel=50,
            blocklyEnabled=False,
            pythonEnabled=True,
            theme=Theme.objects.get(id=3),
            character=Character.objects.get(id='1'),
        )
        level102.save()
        set_decor(level102, json.loads('[{"x":815,"y":697,"decorName":"pond"},{"x":816,"y":597,"decorName":"pond"},{"x":817,"y":498,"decorName":"pond"},{"x":817,"y":397,"decorName":"pond"},{"x":818,"y":296,"decorName":"pond"},{"x":820,"y":197,"decorName":"pond"},{"x":820,"y":98,"decorName":"pond"},{"x":818,"y":0,"decorName":"pond"},{"x":101,"y":508,"decorName":"tree1"},{"x":210,"y":599,"decorName":"tree1"},{"x":500,"y":589,"decorName":"tree1"},{"x":597,"y":508,"decorName":"tree1"},{"x":641,"y":321,"decorName":"tree2"},{"x":446,"y":140,"decorName":"tree1"},{"x":228,"y":202,"decorName":"bush"},{"x":354,"y":505,"decorName":"bush"},{"x":315,"y":467,"decorName":"bush"},{"x":276,"y":431,"decorName":"bush"},{"x":241,"y":395,"decorName":"bush"},{"x":417,"y":388,"decorName":"bush"},{"x":381,"y":352,"decorName":"bush"},{"x":344,"y":315,"decorName":"bush"},{"x":305,"y":279,"decorName":"bush"},{"x":266,"y":239,"decorName":"bush"}]'))
        return level102

    def create_level103():
        level103 = Level(
            name='103',
            default=True,
            path='[{"coordinate":[1,5],"connectedNodes":[1]},{"coordinate":[2,5],"connectedNodes":[0,2]},{"coordinate":[3,5],"connectedNodes":[1,3]},{"coordinate":[3,6],"connectedNodes":[4,2]},{"coordinate":[3,7],"connectedNodes":[5,3]},{"coordinate":[4,7],"connectedNodes":[4,6]},{"coordinate":[5,7],"connectedNodes":[5,7]},{"coordinate":[5,6],"connectedNodes":[6,26,8]},{"coordinate":[5,5],"connectedNodes":[7,9]},{"coordinate":[5,4],"connectedNodes":[8,10]},{"coordinate":[6,4],"connectedNodes":[9,11]},{"coordinate":[7,4],"connectedNodes":[10,12]},{"coordinate":[7,3],"connectedNodes":[11,13]},{"coordinate":[7,2],"connectedNodes":[14,12]},{"coordinate":[6,2],"connectedNodes":[15,13]},{"coordinate":[5,2],"connectedNodes":[14,16]},{"coordinate":[5,1],"connectedNodes":[15,17]},{"coordinate":[5,0],"connectedNodes":[18,16]},{"coordinate":[4,0],"connectedNodes":[19,17]},{"coordinate":[3,0],"connectedNodes":[20,18]},{"coordinate":[2,0],"connectedNodes":[21,19]},{"coordinate":[2,1],"connectedNodes":[22,20]},{"coordinate":[2,2],"connectedNodes":[23,21]},{"coordinate":[2,3],"connectedNodes":[25,24,22]},{"coordinate":[3,3],"connectedNodes":[23,28]},{"coordinate":[1,3],"connectedNodes":[23]},{"coordinate":[6,6],"connectedNodes":[7,27]},{"coordinate":[7,6],"connectedNodes":[26]},{"coordinate":[4,3],"connectedNodes":[24,29]},{"coordinate":[4,4],"connectedNodes":[28]}]',
            traffic_lights='[]',
            destinations='[[1,3]]',
            origin='{"coordinate":[1,5],"direction":"E"}',
            max_fuel=50,
            blocklyEnabled=False,
            pythonEnabled=True,
            theme=Theme.objects.get(id=2),
            character=Character.objects.get(id='1'),
        )
        level103.save()
        set_decor(level103, json.loads('[{"x":180,"y":653,"decorName":"tree2"},{"x":4,"y":602,"decorName":"tree2"},{"x":81,"y":700,"decorName":"tree2"},{"x":755,"y":558,"decorName":"pond"},{"x":304,"y":237,"decorName":"bush"},{"x":304,"y":170,"decorName":"bush"},{"x":302,"y":104,"decorName":"bush"},{"x":372,"y":104,"decorName":"bush"},{"x":440,"y":106,"decorName":"bush"},{"x":440,"y":172,"decorName":"bush"},{"x":438,"y":236,"decorName":"bush"},{"x":757,"y":167,"decorName":"tree1"},{"x":865,"y":209,"decorName":"tree1"},{"x":666,"y":82,"decorName":"tree1"},{"x":826,"y":350,"decorName":"tree1"},{"x":890,"y":67,"decorName":"tree1"},{"x":842,"y":665,"decorName":"bush"}]'))
        return level103

    def create_level104():
        level104 = Level(
            name='104',
            default=True,
            path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[2,3],"connectedNodes":[1,3]},{"coordinate":[2,4],"connectedNodes":[4,2]},{"coordinate":[2,5],"connectedNodes":[5,3]},{"coordinate":[1,5],"connectedNodes":[6,4]},{"coordinate":[0,5],"connectedNodes":[7,5]},{"coordinate":[0,6],"connectedNodes":[8,6]},{"coordinate":[0,7],"connectedNodes":[9,7]},{"coordinate":[1,7],"connectedNodes":[8,10]},{"coordinate":[2,7],"connectedNodes":[9,11]},{"coordinate":[3,7],"connectedNodes":[10,12]},{"coordinate":[4,7],"connectedNodes":[11,13]},{"coordinate":[5,7],"connectedNodes":[12,14]},{"coordinate":[6,7],"connectedNodes":[13,15]},{"coordinate":[6,6],"connectedNodes":[14,16]},{"coordinate":[6,5],"connectedNodes":[17,15]},{"coordinate":[5,5],"connectedNodes":[18,16]},{"coordinate":[4,5],"connectedNodes":[17,19]},{"coordinate":[4,4],"connectedNodes":[18,20]},{"coordinate":[4,3],"connectedNodes":[19,21]},{"coordinate":[5,3],"connectedNodes":[20,22]},{"coordinate":[6,3],"connectedNodes":[21,23]},{"coordinate":[6,2],"connectedNodes":[22,24]},{"coordinate":[6,1],"connectedNodes":[25,23]},{"coordinate":[5,1],"connectedNodes":[26,24]},{"coordinate":[4,1],"connectedNodes":[27,25]},{"coordinate":[3,1],"connectedNodes":[28,26]},{"coordinate":[2,1],"connectedNodes":[29,27]},{"coordinate":[2,2],"connectedNodes":[30,28]},{"coordinate":[1,2],"connectedNodes":[31,29]},{"coordinate":[0,2],"connectedNodes":[30,32]},{"coordinate":[0,1],"connectedNodes":[31,33]},{"coordinate":[0,0],"connectedNodes":[32,34]},{"coordinate":[1,0],"connectedNodes":[33,35]},{"coordinate":[2,0],"connectedNodes":[34]}]',
            traffic_lights='[]',
            destinations='[[2,0]]',
            origin='{"coordinate":[0,3],"direction":"E"}',
            max_fuel=50,
            blocklyEnabled=False,
            pythonEnabled=True,
            theme=Theme.objects.get(id=4),
            character=Character.objects.get(id='1'),
        )
        level104.save()
        set_decor(level104, json.loads('[{"x":277,"y":554,"decorName":"pond"},{"x":100,"y":664,"decorName":"bush"},{"x":196,"y":663,"decorName":"bush"},{"x":451,"y":662,"decorName":"bush"},{"x":551,"y":660,"decorName":"bush"},{"x":495,"y":196,"decorName":"tree2"},{"x":289,"y":476,"decorName":"bush"},{"x":365,"y":475,"decorName":"bush"},{"x":291,"y":372,"decorName":"bush"},{"x":366,"y":370,"decorName":"bush"},{"x":289,"y":273,"decorName":"bush"},{"x":362,"y":272,"decorName":"bush"},{"x":287,"y":185,"decorName":"bush"},{"x":360,"y":187,"decorName":"bush"},{"x":495,"y":423,"decorName":"tree1"},{"x":97,"y":121,"decorName":"tree1"}]'))
        return level104

    def create_level105():
        level105 = Level(
            name='105',
            default=True,
            path='[{"coordinate":[6,7],"connectedNodes":[1]},{"coordinate":[6,6],"connectedNodes":[0,2]},{"coordinate":[6,5],"connectedNodes":[3,1]},{"coordinate":[5,5],"connectedNodes":[4,2]},{"coordinate":[4,5],"connectedNodes":[5,3]},{"coordinate":[3,5],"connectedNodes":[8,4,6]},{"coordinate":[3,4],"connectedNodes":[5,7]},{"coordinate":[3,3],"connectedNodes":[19,6,9]},{"coordinate":[2,5],"connectedNodes":[14,5]},{"coordinate":[3,2],"connectedNodes":[7,10]},{"coordinate":[4,2],"connectedNodes":[9,11]},{"coordinate":[5,2],"connectedNodes":[10,12]},{"coordinate":[6,2],"connectedNodes":[11,13]},{"coordinate":[6,3],"connectedNodes":[21,12]},{"coordinate":[1,5],"connectedNodes":[16,15,8]},{"coordinate":[1,6],"connectedNodes":[23,14]},{"coordinate":[0,5],"connectedNodes":[14,17]},{"coordinate":[0,4],"connectedNodes":[16,18]},{"coordinate":[0,3],"connectedNodes":[17]},{"coordinate":[2,3],"connectedNodes":[7,20]},{"coordinate":[2,2],"connectedNodes":[19]},{"coordinate":[7,3],"connectedNodes":[13,22]},{"coordinate":[7,4],"connectedNodes":[21]},{"coordinate":[1,7],"connectedNodes":[15]}]',
            traffic_lights='[{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":4,"y":5},"direction":"W","startTime":0,"startingState":"RED"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":2,"y":5},"direction":"E","startTime":0,"startingState":"RED"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":3,"y":4},"direction":"N","startTime":0,"startingState":"GREEN"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":3,"y":4},"direction":"S","startTime":0,"startingState":"RED"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":3,"y":2},"direction":"N","startTime":0,"startingState":"RED"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":2,"y":3},"direction":"E","startTime":0,"startingState":"GREEN"}]',
            destinations='[[7,4]]',
            origin='{"coordinate":[6,7],"direction":"S"}',
            max_fuel=50,
            blocklyEnabled=False,
            pythonEnabled=True,
            theme=Theme.objects.get(id=4),
            character=Character.objects.get(id='1'),
        )
        level105.save()
        set_decor(level105, json.loads('[{"x":452,"y":360,"decorName":"pond"},{"x":230,"y":640,"decorName":"tree2"},{"x":212,"y":587,"decorName":"bush"},{"x":301,"y":750,"decorName":"bush"},{"x":216,"y":750,"decorName":"bush"},{"x":296,"y":586,"decorName":"bush"},{"x":328,"y":157,"decorName":"bush"},{"x":551,"y":586,"decorName":"bush"},{"x":383,"y":587,"decorName":"bush"},{"x":464,"y":586,"decorName":"bush"},{"x":99,"y":383,"decorName":"tree1"},{"x":107,"y":459,"decorName":"bush"},{"x":176,"y":459,"decorName":"bush"},{"x":243,"y":459,"decorName":"bush"},{"x":243,"y":393,"decorName":"bush"},{"x":107,"y":327,"decorName":"bush"},{"x":243,"y":157,"decorName":"bush"},{"x":659,"y":159,"decorName":"bush"},{"x":577,"y":157,"decorName":"bush"},{"x":492,"y":157,"decorName":"bush"},{"x":408,"y":157,"decorName":"bush"}]'))
        return level105

    def create_level106():
        level106 = Level(
            name='106',
            default=True,
            path='[{"coordinate":[3,4],"connectedNodes":[1]},{"coordinate":[4,4],"connectedNodes":[0,2]},{"coordinate":[4,3],"connectedNodes":[1,3]},{"coordinate":[4,2],"connectedNodes":[4,2]},{"coordinate":[3,2],"connectedNodes":[5,3]},{"coordinate":[2,2],"connectedNodes":[6,4]},{"coordinate":[1,2],"connectedNodes":[7,5]},{"coordinate":[1,3],"connectedNodes":[8,6]},{"coordinate":[1,4],"connectedNodes":[9,7]},{"coordinate":[1,5],"connectedNodes":[10,8]},{"coordinate":[1,6],"connectedNodes":[11,9]},{"coordinate":[2,6],"connectedNodes":[10,12]},{"coordinate":[3,6],"connectedNodes":[11,13]},{"coordinate":[4,6],"connectedNodes":[12,14]},{"coordinate":[5,6],"connectedNodes":[13,15]},{"coordinate":[6,6],"connectedNodes":[14,16]},{"coordinate":[6,5],"connectedNodes":[15,17]},{"coordinate":[6,4],"connectedNodes":[16,18]},{"coordinate":[6,3],"connectedNodes":[17,19]},{"coordinate":[6,2],"connectedNodes":[18,20]},{"coordinate":[6,1],"connectedNodes":[19,21]},{"coordinate":[6,0],"connectedNodes":[20]}]',
            traffic_lights='[]',
            destinations='[[6,0]]',
            origin='{"coordinate":[3,4],"direction":"E"}',
            max_fuel=50,
            blocklyEnabled=False,
            pythonEnabled=True,
            theme=Theme.objects.get(id=2),
            character=Character.objects.get(id='1'),
        )
        level106.save()
        set_decor(level106, json.loads('[{"x":210,"y":505,"decorName":"tree1"},{"x":474,"y":505,"decorName":"tree1"},{"x":697,"y":593,"decorName":"bush"},{"x":697,"y":282,"decorName":"bush"},{"x":697,"y":362,"decorName":"bush"},{"x":697,"y":435,"decorName":"bush"},{"x":697,"y":515,"decorName":"bush"},{"x":695,"y":137,"decorName":"bush"},{"x":696,"y":210,"decorName":"bush"},{"x":209,"y":15,"decorName":"pond"},{"x":72,"y":71,"decorName":"tree2"},{"x":354,"y":95,"decorName":"tree2"},{"x":392,"y":0,"decorName":"tree2"}]'))
        return level106

    def create_level107():
        level107 = Level(
            name='107',
            default=True,
            path='[{"coordinate":[2,4],"connectedNodes":[19]},{"coordinate":[8,1],"connectedNodes":[2,20]},{"coordinate":[7,1],"connectedNodes":[3,1]},{"coordinate":[6,1],"connectedNodes":[4,2]},{"coordinate":[5,1],"connectedNodes":[5,3]},{"coordinate":[4,1],"connectedNodes":[6,4]},{"coordinate":[3,1],"connectedNodes":[7,5]},{"coordinate":[2,1],"connectedNodes":[8,6]},{"coordinate":[1,1],"connectedNodes":[9,7]},{"coordinate":[0,1],"connectedNodes":[10,8]},{"coordinate":[0,2],"connectedNodes":[11,9]},{"coordinate":[0,3],"connectedNodes":[12,10]},{"coordinate":[0,4],"connectedNodes":[13,11]},{"coordinate":[0,5],"connectedNodes":[14,12]},{"coordinate":[0,6],"connectedNodes":[15,13]},{"coordinate":[1,6],"connectedNodes":[14,16]},{"coordinate":[2,6],"connectedNodes":[15,17]},{"coordinate":[3,6],"connectedNodes":[16,18]},{"coordinate":[3,5],"connectedNodes":[17,19]},{"coordinate":[3,4],"connectedNodes":[0,18]},{"coordinate":[9,1],"connectedNodes":[1]}]',
            traffic_lights='[]',
            destinations='[[9,1]]',
            origin='{"coordinate":[2,4],"direction":"E"}',
            max_fuel=50,
            blocklyEnabled=False,
            pythonEnabled=True,
            theme=Theme.objects.get(id=1),
            character=Character.objects.get(id='1'),
        )
        level107.save()
        set_decor(level107, json.loads('[{"x":639,"y":534,"decorName":"pond"},{"x":515,"y":624,"decorName":"tree1"},{"x":812,"y":700,"decorName":"tree1"},{"x":755,"y":462,"decorName":"tree1"},{"x":792,"y":589,"decorName":"tree1"},{"x":95,"y":550,"decorName":"bush"},{"x":95,"y":477,"decorName":"bush"},{"x":96,"y":398,"decorName":"bush"},{"x":96,"y":327,"decorName":"bush"},{"x":97,"y":189,"decorName":"bush"},{"x":96,"y":257,"decorName":"bush"},{"x":553,"y":191,"decorName":"bush"},{"x":405,"y":191,"decorName":"bush"},{"x":332,"y":190,"decorName":"bush"},{"x":177,"y":189,"decorName":"bush"},{"x":256,"y":190,"decorName":"bush"},{"x":479,"y":191,"decorName":"bush"},{"x":627,"y":191,"decorName":"bush"},{"x":701,"y":190,"decorName":"bush"},{"x":775,"y":191,"decorName":"bush"},{"x":900,"y":654,"decorName":"tree2"},{"x":459,"y":700,"decorName":"tree2"},{"x":900,"y":528,"decorName":"tree2"},{"x":678,"y":700,"decorName":"tree2"},{"x":883,"y":324,"decorName":"tree1"},{"x":171,"y":551,"decorName":"bush"},{"x":249,"y":547,"decorName":"bush"},{"x":76,"y":700,"decorName":"tree1"}]'))
        return level107

    def create_level108():
        level108 = Level(
            name='108',
            default=True,
            path='[{"coordinate":[8,6],"connectedNodes":[7]},{"coordinate":[6,6],"connectedNodes":[2,7]},{"coordinate":[5,6],"connectedNodes":[3,1]},{"coordinate":[4,6],"connectedNodes":[4,2]},{"coordinate":[3,6],"connectedNodes":[5,3]},{"coordinate":[2,6],"connectedNodes":[6,4]},{"coordinate":[1,6],"connectedNodes":[5,8]},{"coordinate":[7,6],"connectedNodes":[1,0]},{"coordinate":[1,5],"connectedNodes":[6,9]},{"coordinate":[1,4],"connectedNodes":[8,10]},{"coordinate":[1,3],"connectedNodes":[9,11]},{"coordinate":[1,2],"connectedNodes":[10,12]},{"coordinate":[1,1],"connectedNodes":[11,13]},{"coordinate":[2,1],"connectedNodes":[12,14]},{"coordinate":[3,1],"connectedNodes":[13,15]},{"coordinate":[4,1],"connectedNodes":[14,16]},{"coordinate":[4,2],"connectedNodes":[17,15]},{"coordinate":[3,2],"connectedNodes":[16]}]',
            traffic_lights='[]',
            destinations='[[3,2]]',
            origin='{"coordinate":[8,6],"direction":"W"}',
            max_fuel=50,
            blocklyEnabled=False,
            pythonEnabled=True,
            theme=Theme.objects.get(id=3),
            character=Character.objects.get(id='1'),
        )
        level108.save()
        set_decor(level108, json.loads('[{"x":235,"y":501,"decorName":"pond"},{"x":235,"y":402,"decorName":"pond"},{"x":237,"y":298,"decorName":"pond"},{"x":397,"y":500,"decorName":"pond"},{"x":398,"y":401,"decorName":"pond"},{"x":399,"y":298,"decorName":"pond"},{"x":2,"y":492,"decorName":"tree1"},{"x":406,"y":3,"decorName":"tree1"},{"x":76,"y":28,"decorName":"tree1"},{"x":14,"y":246,"decorName":"tree1"},{"x":550,"y":176,"decorName":"tree1"},{"x":27,"y":666,"decorName":"tree1"},{"x":495,"y":688,"decorName":"tree1"},{"x":236,"y":700,"decorName":"tree1"},{"x":715,"y":700,"decorName":"tree1"},{"x":677,"y":285,"decorName":"bush"},{"x":677,"y":338,"decorName":"bush"},{"x":675,"y":397,"decorName":"bush"},{"x":675,"y":452,"decorName":"bush"},{"x":672,"y":512,"decorName":"bush"},{"x":673,"y":571,"decorName":"bush"},{"x":677,"y":229,"decorName":"bush"},{"x":679,"y":169,"decorName":"bush"}]'))
        return level108

    def create_level109():
        level109 = Level(
            name='109',
            default=True,
            path='[{"coordinate":[2,5],"connectedNodes":[1]},{"coordinate":[3,5],"connectedNodes":[0,2]},{"coordinate":[3,4],"connectedNodes":[3,1]},{"coordinate":[2,4],"connectedNodes":[4,2]},{"coordinate":[1,4],"connectedNodes":[5,3]},{"coordinate":[1,5],"connectedNodes":[6,4]},{"coordinate":[1,6],"connectedNodes":[7,5]},{"coordinate":[1,7],"connectedNodes":[8,6]},{"coordinate":[2,7],"connectedNodes":[7,9]},{"coordinate":[3,7],"connectedNodes":[8,10]},{"coordinate":[4,7],"connectedNodes":[9,11]},{"coordinate":[5,7],"connectedNodes":[10,12]},{"coordinate":[5,6],"connectedNodes":[11,13]},{"coordinate":[5,5],"connectedNodes":[12,14]},{"coordinate":[5,4],"connectedNodes":[13,15]},{"coordinate":[5,3],"connectedNodes":[14,16]},{"coordinate":[5,2],"connectedNodes":[15,17]},{"coordinate":[6,2],"connectedNodes":[16,18]},{"coordinate":[7,2],"connectedNodes":[17,19]},{"coordinate":[8,2],"connectedNodes":[18,20]},{"coordinate":[8,3],"connectedNodes":[21,19]},{"coordinate":[8,4],"connectedNodes":[22,20]},{"coordinate":[7,4],"connectedNodes":[21]}]',
            traffic_lights='[]',
            destinations='[[7,4]]',
            origin='{"coordinate":[2,5],"direction":"E"}',
            max_fuel=50,
            blocklyEnabled=False,
            pythonEnabled=True,
            theme=Theme.objects.get(id=2),
            character=Character.objects.get(id='1'),
        )
        level109.save()
        set_decor(level109, json.loads('[{"x":398,"y":600,"decorName":"tree2"},{"x":627,"y":632,"decorName":"tree1"},{"x":876,"y":697,"decorName":"tree1"},{"x":800,"y":521,"decorName":"tree1"},{"x":402,"y":441,"decorName":"tree2"},{"x":394,"y":277,"decorName":"tree2"},{"x":215,"y":604,"decorName":"tree2"},{"x":391,"y":97,"decorName":"tree2"},{"x":568,"y":96,"decorName":"tree2"},{"x":756,"y":99,"decorName":"tree2"},{"x":900,"y":197,"decorName":"tree2"},{"x":900,"y":369,"decorName":"tree2"}]'))
        return level109

    # Limited Blocks
    level51 = Level.objects.get(name='51', default=1)
    level59 = Level.objects.get(name='59', default=1)
    level60 = Level.objects.get(name='60', default=1)

    # Procedures
    level62 = Level.objects.get(name='62', default=1)
    level63 = Level.objects.get(name='63', default=1)
    level65 = Level.objects.get(name='65', default=1)
    level67 = Level.objects.get(name='67', default=1)

    # Blockly Brain Teasers
    level68 = Level.objects.get(name='68', default=1)
    level69 = Level.objects.get(name='61', default=1)
    level70 = Level.objects.get(name='70', default=1)
    level71 = Level.objects.get(name='71', default=1)
    level76 = None
    level77 = None
    level78 = None

    # Introduction to Python
    level81 = Level.objects.get(name='80', default=1)
    level82 = Level.objects.get(name='81', default=1)
    level83 = Level.objects.get(name='82', default=1)
    level85 = Level.objects.get(name='83', default=1)
    level86 = Level.objects.get(name='84', default=1)
    level87 = Level.objects.get(name='85', default=1)
    level89 = Level.objects.get(name='86')

    # Python
    level93 = Level.objects.get(name='100', default=1)
    level94 = Level.objects.get(name='102', default=1)
    level95 = Level.objects.get(name='101', default=1)
    level96 = Level.objects.get(name='103', default=1)
    level98 = Level.objects.get(name='104', default=1)
    level99 = Level.objects.get(name='105', default=1)

    # Limited Blocks
    level52 = create_level52()
    level53 = create_level53()
    level54 = create_level54()
    level55 = create_level55()
    level56 = create_level56()
    level57 = create_level57()
    level58 = create_level58()

    level51.next_level = level52
    level52.next_level = level53
    level53.next_level = level54
    level54.next_level = level55
    level55.next_level = level56
    level56.next_level = level57
    level57.next_level = level58
    level58.next_level = level59
    level59.next_level = level60

    level51.save()
    level52.save()
    level53.save()
    level54.save()
    level55.save()
    level56.save()
    level57.save()
    level58.save()
    level59.save()
    level60.save()

    limited_blocks_episode = Episode.objects.get(name="Limited Blocks")
    limited_blocks_episode.first_level = level51
    limited_blocks_episode.save()

    # Procedures
    level61 = create_level61()
    level64 = create_level64()
    level66 = create_level66()

    level61.next_level = level62
    level62.next_level = level63
    level63.next_level = level64
    level64.next_level = level65
    level65.next_level = level66
    level66.next_level = level67
    level67.next_level = None

    level62.name = '62'

    level61.save()
    level62.save()
    level63.save()
    level64.save()
    level65.save()
    level66.save()
    level67.save()

    procedures_episode = Episode.objects.get(name="Procedures")
    procedures_episode.first_level = level61
    procedures_episode.save()

    # Puzzles
    level72 = create_level72()
    level73 = create_level73()
    level74 = create_level74()
    level75 = create_level75()

    level79 = create_level79()

    level69.name = '69'
    level71.name = '71'

    level68.next_level = level69
    level69.next_level = level70
    level70.next_level = level71
    level71.next_level = level72
    level72.next_level = level73
    level73.next_level = level74
    level74.next_level = level75

    level68.save()
    level69.save()
    level70.save()
    level71.save()
    level72.save()
    level73.save()
    level74.save()
    level75.save()

    blockly_brain_teasers_episode = Episode.objects.get(name="Blockly Brain Teasers")
    blockly_brain_teasers_episode.first_level = level68
    blockly_brain_teasers_episode.save()

    # Introduction to Python
    level80 = create_level80()
    level84 = create_level84()
    level88 = create_level88()
    level90 = create_level90()
    level91 = create_level91()

    level80.next_level = level81
    level81.next_level = level82
    level82.next_level = level83
    level83.next_level = level84
    level84.next_level = level85
    level85.next_level = level86
    level86.next_level = level87
    level87.next_level = level88
    level88.next_level = level89
    level89.next_level = level90
    level90.next_level = level91
    level91.next_level = None

    level80.model_solution = '[]'
    level81.model_solution = '[]'
    level82.model_solution = '[]'
    level83.model_solution = '[]'
    level84.model_solution = '[]'
    level85.model_solution = '[]'
    level86.model_solution = '[]'
    level87.model_solution = '[]'
    level88.model_solution = '[]'
    level89.model_solution = '[]'
    level90.model_solution = '[]'
    level91.model_solution = '[]'

    level81.name = '81'
    level82.name = '82'
    level83.name = '83'
    level85.name = '85'
    level86.name = '86'
    level87.name = '87'
    level89.name = '89'

    level80.save()
    level81.save()
    level82.save()
    level83.save()
    level84.save()
    level85.save()
    level86.save()
    level87.save()
    level88.save()
    level89.save()
    level90.save()
    level91.save()

    introduction_to_python_episode = Episode.objects.get(name="Introduction to Python")
    introduction_to_python_episode.first_level = level80
    introduction_to_python_episode.save()

    # Python
    level92 = create_level92()
    level97 = create_level97()
    level100 = create_level100()
    level101 = create_level101()
    level102 = create_level102()
    level103 = create_level103()
    level104 = create_level104()
    level105 = create_level105()
    level106 = create_level106()
    level107 = create_level107()
    level108 = create_level108()
    level109 = create_level109()

    level92.next_level = level93
    level93.next_level = level94
    level94.next_level = level95
    level95.next_level = level96
    level96.next_level = level97
    level97.next_level = level98
    level98.next_level = level99
    level99.next_level = level100
    level100.next_level = level101
    level101.next_level = level102
    level102.next_level = level103
    level103.next_level = level104
    level104.next_level = level105
    level105.next_level = level106
    level106.next_level = level107
    level107.next_level = level108
    level108.next_level = level109
    level109.next_level = None

    level93.name = '93'
    level94.name = '94'
    level95.name = '95'
    level96.name = '96'
    level98.name = '98'
    level99.name = '99'

    level92.save()
    level93.save()
    level94.save()
    level95.save()
    level96.save()
    level97.save()
    level98.save()
    level99.save()
    level100.save()
    level101.save()
    level102.save()
    level103.save()
    level104.save()
    level105.save()
    level106.save()
    level107.save()
    level108.save()
    level109.save()

    python_episode = Episode.objects.get(name="Python")
    python_episode.first_level = level92
    python_episode.save()

    dead_end = Block.objects.get(type='dead_end')
    LevelBlock.objects.get(level=level59, type=dead_end).delete()


class Migration(migrations.Migration):

    replaces = [(b'game', '0001_initial'), (b'game', '0002_characters_theme_decor_block'), (b'game', '0003_levels_and_episodes'), (b'game', '0004_leveldecor'), (b'game', '0005_auto_20140903_1456'), (b'game', '0006_change_27_solution'), (b'game', '0007_added_block__limits'), (b'game', '0008_fix_dee'), (b'game', '0009_auto_20140905_1201'), (b'game', '0010_episode_in_development'), (b'game', '0011_add_new_episodes'), (b'game', '0012_remove_level_blocks'), (b'game', '0013_delete_orig_limit_level'), (b'game', '0014_correct_old_episode_link'), (b'game', '0015_remove_level_decor'), (b'game', '0016_first_puzzle_levels'), (b'game', '0017_change_episode_names'), (b'game', '0018_method_levels'), (b'game', '0019_sort_scores_and_add_initial_python_episodes'), (b'game', '0020_auto_20140912_1021'), (b'game', '0021_fix_level_63'), (b'game', '0022_add_python_contents_and_python_workspace'), (b'game', '0023_add_solutions_to_level_43'), (b'game', '0024_fix_levels_54_63'), (b'game', '0025_levels_ordering_pt1')]

    dependencies = [
        ('portal', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('en_face', models.CharField(max_length=500)),
                ('top_down', models.CharField(max_length=500)),
                ('width', models.IntegerField(default=40)),
                ('height', models.IntegerField(default=20)),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('background', models.CharField(default=b'#eff8ff', max_length=7)),
                ('border', models.CharField(default=b'#bce369', max_length=7)),
                ('selected', models.CharField(default=b'#70961f', max_length=7)),
                ],
        ),
        migrations.CreateModel(
            name='Decor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=500)),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('theme', models.ForeignKey(related_name=b'decor', to='game.Theme'))
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('path', models.TextField(max_length=10000)),
                ('traffic_lights', models.TextField(default=b'[]', max_length=10000)),
                ('origin', models.CharField(default=b'[]', max_length=50)),
                ('destinations', models.CharField(default=b'[[]]', max_length=50)),
                ('default', models.BooleanField(default=False)),
                ('fuel_gauge', models.BooleanField(default=True)),
                ('max_fuel', models.IntegerField(default=50)),
                ('direct_drive', models.BooleanField(default=False)),
                ('model_solution', models.CharField(default=b'[]', max_length=20, blank=True)),
                ('threads', models.IntegerField(default=1)),
                ('blocklyEnabled', models.BooleanField(default=True)),
                ('pythonEnabled', models.BooleanField(default=True)),
                ('anonymous', models.BooleanField(default=False)),
                ('character', models.ForeignKey(default=1, to='game.Character')),
                ('next_level', models.ForeignKey(default=None, to='game.Level', null=True)),
                ('owner', models.ForeignKey(related_name=b'levels', blank=True, to='portal.UserProfile', null=True)),
                ('shared_with', models.ManyToManyField(related_name='shared', to=settings.AUTH_USER_MODEL, null=True, blank=True)),
                ('theme', models.ForeignKey(default=None, blank=True, to='game.Theme', null=True))
                ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('r_branchiness', models.FloatField(default=0, null=True)),
                ('r_loopiness', models.FloatField(default=0, null=True)),
                ('r_curviness', models.FloatField(default=0, null=True)),
                ('r_num_tiles', models.IntegerField(default=5, null=True)),
                ('r_blocklyEnabled', models.BooleanField(default=True)),
                ('r_pythonEnabled', models.BooleanField(default=False)),
                ('r_trafficLights', models.BooleanField(default=False)),
                ('next_episode', models.ForeignKey(default=None, to='game.Episode', null=True)),
                ('r_blocks', models.ManyToManyField(related_name=b'episodes', null=True, to=b'game.Block')),
                ('in_development', models.BooleanField(default=False)),
                ('r_random_levels_enabled', models.BooleanField(default=False)),
                ('first_level', models.ForeignKey(to='game.Level'))
            ],
        ),
        migrations.CreateModel(
            name='LevelDecor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('decorName', models.CharField(default=b'tree1', max_length=100)),
                ('level', models.ForeignKey(to='game.Level')),
            ],
        ),
        migrations.CreateModel(
            name='Workspace',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('contents', models.TextField(default=b'')),
                ('owner', models.ForeignKey(related_name=b'workspaces', blank=True, to='portal.UserProfile', null=True)),
                ('python_contents', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='LevelBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.PositiveIntegerField(default=None, null=True)),
                ('level', models.ForeignKey(to='game.Level')),
                ('type', models.ForeignKey(to='game.Block')),
            ],
        ),
        migrations.CreateModel(
            name='Attempt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('finish_time', models.DateTimeField(auto_now=True)),
                ('score', models.FloatField(default=0, null=True)),
                ('workspace', models.TextField(default=b'')),
                ('student', models.ForeignKey(blank=True, to='portal.Student', null=True)),
                ('python_workspace', models.TextField(default=b'')),
                ('level', models.ForeignKey(related_name=b'attempts', to='game.Level')),
                ('student', models.ForeignKey(related_name=b'attempts', blank=True, to='portal.Student', null=True))
                ],
        ),
        migrations.RunPython(
            code=add_characters,
        ),
        migrations.RunPython(
            code=add_theme_and_decor,
        ),
        migrations.RunPython(
            code=add_blocks,
        ),
        migrations.RunPython(
            code=add_levels,
        ),
        migrations.RunPython(
            code=setup_blocks,
        ),
        migrations.RunPython(
            code=add_episodes_1_to_6,
        ),
        migrations.RunPython(
            code=add_leveldecor,
        ),
        migrations.RunPython(
            code=addTestLevel,
        ),
        migrations.RunPython(
            code=delete_old_limit_level,
        ),
        migrations.RunPython(
            code=add_episode_7_to_9,
        ),
        migrations.RunPython(
            code=add_levels_63_to_65,
        ),
        migrations.RunPython(
            code=add_levels_80_to_107,
        ),
        migrations.RunPython(
            code=enable_random_levels_for_episodes_1_to_7,
        ),
        migrations.RunPython(
            code=change_decor_and_blocks_in_level_63_and_60,
        ),
        migrations.RunPython(
            code=set_next_episode,
        ),
        migrations.RunPython(
            code=add_and_reorder_levels,
        ),
    ]
