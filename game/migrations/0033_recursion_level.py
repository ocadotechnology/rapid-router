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
from django.db import migrations
from game.level_management import set_decor_inner, set_blocks_inner
import json

def new_level(apps, schema_editor):
    Level = apps.get_model('game', 'Level')
    Character = apps.get_model('game', 'Character')
    Theme = apps.get_model('game', 'Theme')
    LevelDecor = apps.get_model('game', 'LevelDecor')
    LevelBlock = apps.get_model('game', 'LevelBlock')
    Block = apps.get_model('game', 'Block')
    LevelDecor = apps.get_model('game', 'LevelDecor')
    LevelBlock = apps.get_model('game', 'LevelBlock')
    Block = apps.get_model('game', 'Block')

    def set_decor(level, decor):
        set_decor_inner(level, decor, LevelDecor)

    def set_blocks(level, blocks):
        set_blocks_inner(level, blocks, LevelBlock, Block)

    level77 = Level(
        name='77',
        default=True,
        path='[{"coordinate":[2,2],"connectedNodes":[1]},{"coordinate":[3,2],"connectedNodes":[0,2]},{"coordinate":[4,2],"connectedNodes":[1,3]},{"coordinate":[5,2],"connectedNodes":[2,4]},{"coordinate":[6,2],"connectedNodes":[3,5]},{"coordinate":[7,2],"connectedNodes":[4,6]},{"coordinate":[8,2],"connectedNodes":[5,7]},{"coordinate":[8,3],"connectedNodes":[8,6]},{"coordinate":[8,4],"connectedNodes":[9,7]},{"coordinate":[8,5],"connectedNodes":[10,8]},{"coordinate":[8,6],"connectedNodes":[11,9]},{"coordinate":[7,6],"connectedNodes":[12,10]},{"coordinate":[6,6],"connectedNodes":[13,11]},{"coordinate":[5,6],"connectedNodes":[14,12]},{"coordinate":[4,6],"connectedNodes":[15,13]},{"coordinate":[3,6],"connectedNodes":[14,16]},{"coordinate":[3,5],"connectedNodes":[15,17]},{"coordinate":[3,4],"connectedNodes":[16,18]},{"coordinate":[4,4],"connectedNodes":[17,19]},{"coordinate":[5,4],"connectedNodes":[18,20]},{"coordinate":[6,4],"connectedNodes":[19]}]',
        traffic_lights='[]',
        destinations='[[6,4]]',
        origin='{"coordinate":[2,2],"direction":"E"}',
        max_fuel=50,
        blocklyEnabled=True,
        pythonEnabled=False,
        theme=Theme.objects.get(id=1),
        character=Character.objects.get(id='1'),
        model_solution='[9]',
        next_level=None,
        disable_route_score=True
    )
    level77.save()
    set_decor(level77, json.loads('[{"x":900,"y":410,"decorName":"tree1"},{"x":480,"y":490,"decorName":"tree1"},{"x":388,"y":284,"decorName":"tree1"},{"x":330,"y":318,"decorName":"tree1"},{"x":629,"y":292,"decorName":"tree1"},{"x":205,"y":622,"decorName":"tree2"},{"x":440,"y":290,"decorName":"tree2"},{"x":688,"y":469,"decorName":"tree2"},{"x":387,"y":518,"decorName":"tree2"},{"x":220,"y":314,"decorName":"tree2"},{"x":78,"y":259,"decorName":"bush"},{"x":82,"y":177,"decorName":"bush"},{"x":139,"y":117,"decorName":"bush"},{"x":232,"y":127,"decorName":"bush"},{"x":320,"y":135,"decorName":"bush"},{"x":397,"y":138,"decorName":"bush"},{"x":75,"y":490,"decorName":"tree1"},{"x":656,"y":17,"decorName":"tree2"}]'))
    set_blocks(level77, json.loads('[{"type":"move_forwards","number":1},{"type":"turn_left","number":1},{"type":"wait"},{"type":"controls_if"},{"type":"road_exists"},{"type":"call_proc"},{"type":"declare_proc","number":2}]'))

    level76 = Level.objects.get(name='76', default=1)
    level76.next_level = level77
    level76.save()
 

class Migration(migrations.Migration):
    dependencies = [
        ('game', '0032_cannot_turn_left_level'),
    ]

    operations = [
        migrations.RunPython(new_level)
    ]
