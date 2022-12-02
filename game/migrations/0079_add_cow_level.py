from __future__ import unicode_literals

from builtins import range
from django.db import models, migrations
from django.conf import settings
import json
from game.level_management import set_decor_inner, set_blocks_inner


# Functions from the following migrations need manual copying.
# Move them and any dependencies into this file, then update the
# RunPython operations to refer to the local versions:
# game.migrations.0001_squashed_0024_fix_levels_54_63
# game.migrations.0025_levels_ordering_pt1


def add_cow_levels(apps, schema_editor):

    Level = apps.get_model("game", "Level")

    level110 = Level(
        name="110",
        episode_id=11,
        path='[{"coordinate":[0,0],"connectedNodes":[1]},{"coordinate":[1,0],"connectedNodes":[0,2]},{"coordinate":[2,0],"connectedNodes":[1,3]},{"coordinate":[3,0],"connectedNodes":[2,4]},{"coordinate":[4,0],"connectedNodes":[3,5]},{"coordinate":[5,0],"connectedNodes":[4,6]},{"coordinate":[6,0],"connectedNodes":[5,7]},{"coordinate":[7,0],"connectedNodes":[6,8]},{"coordinate":[8,0],"connectedNodes":[7,9]},{"coordinate":[9,0],"connectedNodes":[8,10]},{"coordinate":[9,1],"connectedNodes":[11,9]},{"coordinate":[9,2],"connectedNodes":[12,10]},{"coordinate":[9,3],"connectedNodes":[13,11]},{"coordinate":[9,4],"connectedNodes":[14,12]},{"coordinate":[9,5],"connectedNodes":[15,13]},{"coordinate":[9,6],"connectedNodes":[16,14]},{"coordinate":[9,7],"connectedNodes":[17,15]},{"coordinate":[8,7],"connectedNodes":[18,16]},{"coordinate":[7,7],"connectedNodes":[19,17]},{"coordinate":[6,7],"connectedNodes":[20,18]},{"coordinate":[5,7],"connectedNodes":[21,19]},{"coordinate":[4,7],"connectedNodes":[22,20]},{"coordinate":[3,7],"connectedNodes":[23,21]},{"coordinate":[2,7],"connectedNodes":[24,22]},{"coordinate":[1,7],"connectedNodes":[25,23]},{"coordinate":[0,7],"connectedNodes":[24,26]},{"coordinate":[0,6],"connectedNodes":[25,27]},{"coordinate":[0,5],"connectedNodes":[26,28]},{"coordinate":[1,5],"connectedNodes":[27,29]},{"coordinate":[2,5],"connectedNodes":[28,30]},{"coordinate":[3,5],"connectedNodes":[29,31]},{"coordinate":[4,5],"connectedNodes":[30,32]},{"coordinate":[5,5],"connectedNodes":[31,33]},{"coordinate":[6,5],"connectedNodes":[32,34]},{"coordinate":[7,5],"connectedNodes":[33,35]},{"coordinate":[7,4],"connectedNodes":[36,34]},{"coordinate":[6,4],"connectedNodes":[37,35]},{"coordinate":[5,4],"connectedNodes":[38,36]},{"coordinate":[4,4],"connectedNodes":[39,37]},{"coordinate":[3,4],"connectedNodes":[40,38]},{"coordinate":[2,4],"connectedNodes":[41,39]},{"coordinate":[1,4],"connectedNodes":[40]}]',
        traffic_lights="[]",
        cows='[{"minCows":1,"maxCows":1,"potentialCoordinates":[{"x":1,"y":0},{"x":9,"y":2},{"x":9,"y":3}],"type":"WHITE"}]',
        origin='{"coordinate":[0,0],"direction":"E"}',
        destinations="[[1,4]]",
        default=True,
        owner_id=None,
        fuel_gauge=True,
        max_fuel=50,
        direct_drive=False,
        next_level_id=None,
        model_solution="[11]",
        disable_route_score=False,
        threads=1,
        blocklyEnabled=True,
        pythonEnabled=False,
        pythonViewEnabled=False,
        theme_name="grass",
        character_name="Van",
        anonymous=False,
    )

    level110.save()

    level109 = Level.objects.get(name="109")
    level109.next_level = level110
    level109.save()


def setup_blocks(apps, schema_editor):

    Level = apps.get_model("game", "Level")
    Block = apps.get_model("game", "Block")

    LevelBlock = apps.get_model("game", "LevelBlock")
    level = Level.objects.get(name="110")

    for block in Block.objects.all():
        newBlock = LevelBlock(type=block, number=None, level=level)
        newBlock.save()


def add_leveldecor(apps, schema_editor):
    Level = apps.get_model("game", "Level")
    LevelDecor = apps.get_model("game", "LevelDecor")
    level110 = Level.objects.get(name="110")

    LevelDecor.objects.bulk_create(
        [
            LevelDecor(decorName="tree2", level=level110, x=797, y=491),
            LevelDecor(decorName="bush", level=level110, x=494, y=492),
            LevelDecor(decorName="bush", level=level110, x=494, y=558),
            LevelDecor(decorName="bush", level=level110, x=494, y=426),
            LevelDecor(decorName="bush", level=level110, x=495, y=356),
            LevelDecor(decorName="bush", level=level110, x=495, y=291),
            LevelDecor(decorName="tree1", level=level110, x=284, y=584),
            LevelDecor(decorName="bush", level=level110, x=686, y=39),
            LevelDecor(decorName="bush", level=level110, x=686, y=98),
            LevelDecor(decorName="bush", level=level110, x=684, y=160),
        ]
    )


class Migration(migrations.Migration):

    dependencies = [
        ("game", "0078_populate_block_type_add_cow_blocks"),
    ]

    operations = [
        migrations.RunPython(code=add_cow_levels),
        migrations.RunPython(code=setup_blocks),
        migrations.RunPython(code=add_leveldecor),
    ]
