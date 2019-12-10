# -*- coding: utf-8 -*-
# Code for Life
#
# Copyright (C) 2019, Ocado Innovation Limited
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
    Level = apps.get_model("game", "Level")
    Character = apps.get_model("game", "Character")
    Theme = apps.get_model("game", "Theme")
    LevelDecor = apps.get_model("game", "LevelDecor")
    LevelBlock = apps.get_model("game", "LevelBlock")
    Block = apps.get_model("game", "Block")

    def set_decor(level, decor):
        set_decor_inner(level, decor, LevelDecor)

    def set_blocks(level, blocks):
        set_blocks_inner(level, blocks, LevelBlock, Block)

    level76 = Level(
        name="76",
        default=True,
        path='[{"coordinate":[2,6],"connectedNodes":[1]},{"coordinate":[3,6],"connectedNodes":[0,2]},{"coordinate":[4,6],"connectedNodes":[1,3,5]},{"coordinate":[5,6],"connectedNodes":[2,4]},{"coordinate":[5,5],"connectedNodes":[5,3,6]},{"coordinate":[4,5],"connectedNodes":[2,4,7]},{"coordinate":[5,4],"connectedNodes":[7,4,8]},{"coordinate":[4,4],"connectedNodes":[5,6,9]},{"coordinate":[5,3],"connectedNodes":[9,6,10]},{"coordinate":[4,3],"connectedNodes":[7,8,11]},{"coordinate":[5,2],"connectedNodes":[11,8,12]},{"coordinate":[4,2],"connectedNodes":[9,10,13]},{"coordinate":[5,1],"connectedNodes":[13,10,14,17]},{"coordinate":[4,1],"connectedNodes":[11,12,16]},{"coordinate":[6,1],"connectedNodes":[12,15]},{"coordinate":[7,1],"connectedNodes":[14]},{"coordinate":[4,0],"connectedNodes":[13,17]},{"coordinate":[5,0],"connectedNodes":[16,12]}]',
        traffic_lights="[]",
        destinations="[[7,1]]",
        origin='{"coordinate":[2,6],"direction":"E"}',
        max_fuel=50,
        blocklyEnabled=True,
        pythonEnabled=False,
        theme=Theme.objects.get(id=3),
        character=Character.objects.get(id="1"),
        model_solution="[9]",
        next_level=None,
        disable_route_score=True,
    )
    level76.save()
    set_decor(
        level76,
        json.loads(
            '[{"x":277,"y":382,"decorName":"tree2"},{"x":124,"y":381,"decorName":"tree2"},{"x":731,"y":547,"decorName":"pond"},{"x":639,"y":228,"decorName":"tree1"},{"x":227,"y":328,"decorName":"bush"},{"x":171,"y":191,"decorName":"pond"}]'
        ),
    )
    set_blocks(
        level76,
        json.loads(
            '[{"type":"move_forwards","number":1},{"type":"turn_right","number":3},{"type":"wait"},{"type":"controls_repeat_while","number":1},{"type":"controls_if"},{"type":"logic_negate"},{"type":"at_destination"},{"type":"road_exists"}]'
        ),
    )

    level75 = Level.objects.get(name="75", default=1)
    level75.next_level = level76
    level75.model_solution = "[11]"
    level75.save()


class Migration(migrations.Migration):
    dependencies = [("game", "0031_python_view")]

    operations = [migrations.RunPython(new_level)]
