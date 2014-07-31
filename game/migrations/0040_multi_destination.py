
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def add_multiple_destinations(apps, schema_editor):

    Block = apps.get_model('game', 'Block')
    Level = apps.get_model('game', 'Level')
    Episode = apps.get_model('game', 'Episode')

    levels = Level.objects.all();

    for level in levels:
        level.destination = '[' + level.destination + ']';
        level.save();

    deliverBlock = Block(type='deliver')
    deliverBlock.save()

    level54 = Level(pk=54, name=54, default=1, destination=[[4,2], [4,4]], model_solution=8,
                    decor='[{"coordinate":{"x":0,"y":595},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":2,"y":502},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":6,"y":398},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":0,"y":700},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":5,"y":201},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":8,"y":104},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":0,"y":5},"url":"/static/game/image/tree1.svg"}]',
                    path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[2,27,26,0]},{"coordinate":[1,4],"connectedNodes":[1,3]},{"coordinate":[1,5],"connectedNodes":[2,4]},{"coordinate":[1,6],"connectedNodes":[3,5]},{"coordinate":[1,7],"connectedNodes":[4,6]},{"coordinate":[2,7],"connectedNodes":[5,7]},{"coordinate":[3,7],"connectedNodes":[6,8]},{"coordinate":[4,7],"connectedNodes":[7,9]},{"coordinate":[5,7],"connectedNodes":[8,10]},{"coordinate":[6,7],"connectedNodes":[9,11]},{"coordinate":[7,7],"connectedNodes":[10,12]},{"coordinate":[7,6],"connectedNodes":[11,13]},{"coordinate":[7,5],"connectedNodes":[12,14]},{"coordinate":[7,4],"connectedNodes":[13,15]},{"coordinate":[7,3],"connectedNodes":[14,16]},{"coordinate":[7,2],"connectedNodes":[15,17]},{"coordinate":[7,1],"connectedNodes":[16,18]},{"coordinate":[7,0],"connectedNodes":[17,19]},{"coordinate":[6,0],"connectedNodes":[18,20]},{"coordinate":[5,0],"connectedNodes":[19,21]},{"coordinate":[4,0],"connectedNodes":[20,22]},{"coordinate":[3,0],"connectedNodes":[21,23]},{"coordinate":[2,0],"connectedNodes":[22,24]},{"coordinate":[1,0],"connectedNodes":[23,25]},{"coordinate":[1,1],"connectedNodes":[24,26]},{"coordinate":[1,2],"connectedNodes":[25,1]},{"coordinate":[2,3],"connectedNodes":[28,45,44,1]},{"coordinate":[2,4],"connectedNodes":[27,29]},{"coordinate":[2,5],"connectedNodes":[28,30]},{"coordinate":[2,6],"connectedNodes":[29,31]},{"coordinate":[3,6],"connectedNodes":[30,32]},{"coordinate":[4,6],"connectedNodes":[31,33]},{"coordinate":[5,6],"connectedNodes":[32,34]},{"coordinate":[6,6],"connectedNodes":[33,35]},{"coordinate":[6,5],"connectedNodes":[34,36]},{"coordinate":[6,4],"connectedNodes":[35,37]},{"coordinate":[6,3],"connectedNodes":[36,38]},{"coordinate":[6,2],"connectedNodes":[37,39]},{"coordinate":[6,1],"connectedNodes":[38,40]},{"coordinate":[5,1],"connectedNodes":[39,41]},{"coordinate":[4,1],"connectedNodes":[40,42]},{"coordinate":[3,1],"connectedNodes":[41,43]},{"coordinate":[2,1],"connectedNodes":[42,44]},{"coordinate":[2,2],"connectedNodes":[43,27]},{"coordinate":[3,3],"connectedNodes":[46,54,53,27]},{"coordinate":[3,4],"connectedNodes":[45,47]},{"coordinate":[3,5],"connectedNodes":[46,48]},{"coordinate":[4,5],"connectedNodes":[47,49]},{"coordinate":[5,5],"connectedNodes":[48,50]},{"coordinate":[5,4],"connectedNodes":[49,51]},{"coordinate":[5,3],"connectedNodes":[50,52]},{"coordinate":[5,2],"connectedNodes":[51,56]},{"coordinate":[3,2],"connectedNodes":[45,56]},{"coordinate":[4,3],"connectedNodes":[45,55]},{"coordinate":[4,4],"connectedNodes":[54]},{"coordinate":[4,2],"connectedNodes":[52,53]}]')
    level54.save()

    blocks = Block.objects.filter(type__in=["move_forwards", "turn_left", "turn_right",
                                            "controls_whileUntil", "controls_if", "logic_negate",
                                            "road_exists", "at_destination", "turn_around",
                                            "controls_repeat", "road_exists", "dead_end",
                                            "turn_around", "call_proc", "declare_proc", "text", "deliver"])
    level54.blocks = blocks;
    level54.save();

class Migration(migrations.Migration):

    dependencies = [
        ('game', '0039_auto_20140724_1628'),
    ]

    operations = [
        migrations.RunPython(add_multiple_destinations),
    ]
