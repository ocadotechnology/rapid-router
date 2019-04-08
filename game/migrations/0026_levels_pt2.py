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
from __future__ import unicode_literals

from django.db import migrations
from game.level_management import set_decor_inner, set_blocks_inner
import json


def change_levels(apps, schema_editor):

    Level = apps.get_model("game", "Level")
    LevelDecor = apps.get_model("game", "LevelDecor")
    LevelBlock = apps.get_model("game", "LevelBlock")
    Block = apps.get_model("game", "Block")

    def set_decor(level, decor):
        set_decor_inner(level, decor, LevelDecor)

    def set_blocks(level, blocks):
        set_blocks_inner(level, blocks, LevelBlock, Block)

    level61 = Level.objects.get(name="61", default=1)
    level61.model_solution = "[9]"
    level61.save()

    level75 = Level.objects.get(name="75", default=1)
    level73 = Level.objects.get(name="73", default=1)
    level72 = Level.objects.get(name="72", default=1)
    level74 = Level.objects.get(name="74", default=1)
    level79 = Level.objects.get(name="79", default=1)

    level72.next_level = level75
    level75.next_level = level74
    level74.next_level = level73
    level73.next_level = level79
    level79.next_level = None

    level74.path = (
        '[{"coordinate":[9,2],"connectedNodes":[1]},'
        + '{"coordinate":[8,2],"connectedNodes":[2,9,0]},'
        + '{"coordinate":[7,2],"connectedNodes":[1,3]},'
        + '{"coordinate":[7,1],"connectedNodes":[4,2]},'
        + '{"coordinate":[6,1],"connectedNodes":[5,3,6]},'
        + '{"coordinate":[5,1],"connectedNodes":[8,4,34]},'
        + '{"coordinate":[6,0],"connectedNodes":[4]},'
        + '{"coordinate":[3,2],"connectedNodes":[28,37,35]},'
        + '{"coordinate":[4,1],"connectedNodes":[35,5]},'
        + '{"coordinate":[8,3],"connectedNodes":[10,1]},'
        + '{"coordinate":[8,4],"connectedNodes":[11,9]},'
        + '{"coordinate":[8,5],"connectedNodes":[12,33,10]},'
        + '{"coordinate":[8,6],"connectedNodes":[13,11]},'
        + '{"coordinate":[7,6],"connectedNodes":[14,12]},'
        + '{"coordinate":[6,6],"connectedNodes":[15,13]},'
        + '{"coordinate":[5,6],"connectedNodes":[16,14,29]},'
        + '{"coordinate":[4,6],"connectedNodes":[17,15,39]},'
        + '{"coordinate":[3,6],"connectedNodes":[18,16]},'
        + '{"coordinate":[2,6],"connectedNodes":[19,30,17]},'
        + '{"coordinate":[1,6],"connectedNodes":[20,18]},'
        + '{"coordinate":[0,6],"connectedNodes":[19,21]},'
        + '{"coordinate":[0,5],"connectedNodes":[20,22]},'
        + '{"coordinate":[0,4],"connectedNodes":[21,31,23]},'
        + '{"coordinate":[0,3],"connectedNodes":[22,24]},'
        + '{"coordinate":[0,2],"connectedNodes":[23,25]},'
        + '{"coordinate":[0,1],"connectedNodes":[24,26]},'
        + '{"coordinate":[1,1],"connectedNodes":[25,27,32]},'
        + '{"coordinate":[2,1],"connectedNodes":[26,28]},'
        + '{"coordinate":[2,2],"connectedNodes":[7,27]},'
        + '{"coordinate":[5,5],"connectedNodes":[15]},'
        + '{"coordinate":[2,7],"connectedNodes":[18]},'
        + '{"coordinate":[1,4],"connectedNodes":[22]},'
        + '{"coordinate":[1,0],"connectedNodes":[26]},'
        + '{"coordinate":[9,5],"connectedNodes":[11]},'
        + '{"coordinate":[5,0],"connectedNodes":[5]},'
        + '{"coordinate":[4,2],"connectedNodes":[7,36,8]},'
        + '{"coordinate":[4,3],"connectedNodes":[37,38,35]},'
        + '{"coordinate":[3,3],"connectedNodes":[36,7]},'
        + '{"coordinate":[4,4],"connectedNodes":[39,36]},'
        + '{"coordinate":[4,5],"connectedNodes":[40,16,38]},'
        + '{"coordinate":[3,5],"connectedNodes":[41,39]},'
        + '{"coordinate":[2,5],"connectedNodes":[40,42]},'
        + '{"coordinate":[2,4],"connectedNodes":[41]}]'
    )
    level74.traffic_lights = "[]"
    level74.destinations = "[[2,4]]"
    level74.origin = '{"coordinate":[9,2],"direction":"W"}'
    level74.model_solution = "[13]"

    level74.save()

    LevelDecor.objects.filter(level=level74).delete()

    set_decor(
        level74,
        json.loads(
            '[{"x":738,"y":33,"decorName":"tree1"},'
            + '{"x":496,"y":404,"decorName":"tree2"},'
            + '{"x":248,"y":39,"decorName":"pond"},'
            + '{"x":101,"y":500,"decorName":"bush"},'
            + '{"x":148,"y":561,"decorName":"bush"},'
            + '{"x":97,"y":565,"decorName":"bush"}]'
        ),
    )
    set_blocks(
        level74,
        json.loads(
            '[{"type":"move_forwards","number":1},'
            + '{"type":"turn_left","number":2},'
            + '{"type":"turn_right","number":1},'
            + '{"type":"turn_around","number":2},'
            + '{"type":"controls_repeat","number":1},'
            + '{"type":"call_proc"},{"type":"declare_proc"}]'
        ),
    )

    level73.model_solution = "[15]"
    level75.model_solution = "[10, 26]"

    level75.name = "73"
    level73.name = "75"

    level72.save()
    level75.save()
    level74.save()
    level73.save()
    level79.save()

    level88 = Level.objects.get(name="88", default=1)
    levelBlock = LevelBlock(level=level88, type=Block.objects.get(type="wait"))
    levelBlock.save()

    level89 = Level.objects.get(name="89", default=1)
    levelBlock = LevelBlock(level=level89, type=Block.objects.get(type="logic_negate"))
    levelBlock.save()

    levelBlock = LevelBlock.objects.get(
        type=Block.objects.get(type="controls_repeat_until"), level=level89
    )
    levelBlock.delete()

    level90 = Level.objects.get(name="90", default=1)
    level90.path = (
        '[{"coordinate":[1,6],"connectedNodes":[1]},'
        + '{"coordinate":[2,6],"connectedNodes":[0,2]},'
        + '{"coordinate":[2,5],"connectedNodes":[1,3]},'
        + '{"coordinate":[3,5],"connectedNodes":[2,4]},'
        + '{"coordinate":[4,5],"connectedNodes":[3,5]},'
        + '{"coordinate":[4,4],"connectedNodes":[4,6]},'
        + '{"coordinate":[5,4],"connectedNodes":[5,7]},'
        + '{"coordinate":[5,3],"connectedNodes":[6,8]},'
        + '{"coordinate":[6,3],"connectedNodes":[7,9]},'
        + '{"coordinate":[7,3],"connectedNodes":[8,10]},'
        + '{"coordinate":[7,2],"connectedNodes":[9,11]},'
        + '{"coordinate":[8,2],"connectedNodes":[10,12]},'
        + '{"coordinate":[8,1],"connectedNodes":[13,11]},'
        + '{"coordinate":[7,1],"connectedNodes":[14,12]},'
        + '{"coordinate":[6,1],"connectedNodes":[15,13]},'
        + '{"coordinate":[5,1],"connectedNodes":[16,14]},'
        + '{"coordinate":[4,1],"connectedNodes":[17,15]},'
        + '{"coordinate":[3,1],"connectedNodes":[18,16]},'
        + '{"coordinate":[3,2],"connectedNodes":[19,17]},'
        + '{"coordinate":[2,2],"connectedNodes":[20,18]},'
        + '{"coordinate":[2,3],"connectedNodes":[21,19]},'
        + '{"coordinate":[1,3],"connectedNodes":[22,20]},'
        + '{"coordinate":[1,4],"connectedNodes":[23,21]},'
        + '{"coordinate":[0,4],"connectedNodes":[22]}]'
    )
    level90.destinations = "[[0,4]]"
    level90.save()

    level101 = Level.objects.get(name="101", default=1)
    level101.blocklyEnabled = False
    level101.save()

    level105 = Level.objects.get(name="105", default=1)
    Level.objects.filter(name="106", default=1).exclude(
        pk=level105.next_level.id
    ).delete()

    level106 = Level.objects.get(name="106", default=1)
    Level.objects.filter(name="107", default=1).exclude(
        pk=level106.next_level.id
    ).delete()


class Migration(migrations.Migration):

    dependencies = [("game", "0001_squashed_0025_levels_ordering_pt1")]

    operations = [migrations.RunPython(change_levels)]
