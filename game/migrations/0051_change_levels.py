# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def change_levels(apps, schema_editor):

    Level = apps.get_model('game', 'Level')
    Block = apps.get_model('game', 'Block')

    blocks = Block.objects.filter(type__in=["move_forwards", "turn_left", "turn_right",
                                            "controls_whileUntil", "controls_if", "logic_negate",
                                            "road_exists", "at_destination"])

    blocks_around = Block.objects.filter(type__in=["move_forwards", "turn_left", "turn_right",
                                                   "controls_whileUntil", "controls_if",
                                                   "logic_negate", "road_exists", "at_destination",
                                                   "turn_around", "controls_repeat", "road_exists",
                                                   "dead_end"])

    level43 = Level.objects.get(pk=43)
    level41 = Level.objects.get(pk=41)
    level36 = Level.objects.get(pk=36)
    level35 = Level.objects.get(pk=35)

    level35.next_level = None
    level35.save()

    level43.path = level41.path
    level43.decor = level41.decor
    level43.model_solution = level41.model_solution
    level43.blocks = blocks_around

    level43.save()

    level41.path = level36.path
    level41.decor = level36.decor
    level41.model_solution = level36.model_solution
    level41.blocks = blocks_around

    level41.save()

    level36 = Level.objects.get(pk=36)
    level36.delete()

    level36 = Level.objects.get(pk=37)
    level36.pk = 36
    level36.name = 36

    level36.save()

    level35.next_level = level36
    level35.save()

    level37 = Level.objects.get(pk=38)
    level37.pk = 37
    level37.name = 37
    level37.save()

    level38 = Level(pk=38, name=38, default=1, model_solution=11,
                    path='[{"coordinate":[7,6],"connectedNodes":[1]},{"coordinate":[6,6],"connectedNodes":[2,0]},{"coordinate":[5,6],"connectedNodes":[3,1]},{"coordinate":[4,6],"connectedNodes":[4,2]},{"coordinate":[3,6],"connectedNodes":[5,3]},{"coordinate":[2,6],"connectedNodes":[4,6]},{"coordinate":[2,5],"connectedNodes":[7,5]},{"coordinate":[1,5],"connectedNodes":[8,6]},{"coordinate":[1,6],"connectedNodes":[9,7]},{"coordinate":[0,6],"connectedNodes":[8,10]},{"coordinate":[0,5],"connectedNodes":[9,11]},{"coordinate":[0,4],"connectedNodes":[10,12]},{"coordinate":[1,4],"connectedNodes":[11,13]},{"coordinate":[2,4],"connectedNodes":[12,14]},{"coordinate":[3,4],"connectedNodes":[13,15]},{"coordinate":[3,5],"connectedNodes":[16,14]},{"coordinate":[4,5],"connectedNodes":[15,17]},{"coordinate":[5,5],"connectedNodes":[16,18]},{"coordinate":[6,5],"connectedNodes":[17,19]},{"coordinate":[7,5],"connectedNodes":[18,20]},{"coordinate":[7,4],"connectedNodes":[21,19]},{"coordinate":[6,4],"connectedNodes":[22,20]},{"coordinate":[5,4],"connectedNodes":[23,21]},{"coordinate":[4,4],"connectedNodes":[22,24]},{"coordinate":[4,3],"connectedNodes":[25,23]},{"coordinate":[3,3],"connectedNodes":[26,24]},{"coordinate":[2,3],"connectedNodes":[27,25]},{"coordinate":[1,3],"connectedNodes":[26,28]},{"coordinate":[1,2],"connectedNodes":[27,29]},{"coordinate":[2,2],"connectedNodes":[28,30]},{"coordinate":[3,2],"connectedNodes":[29,31]},{"coordinate":[3,1],"connectedNodes":[30,32]},{"coordinate":[3,0],"connectedNodes":[31,33]},{"coordinate":[4,0],"connectedNodes":[32,34]},{"coordinate":[4,1],"connectedNodes":[35,33]},{"coordinate":[4,2],"connectedNodes":[36,34]},{"coordinate":[5,2],"connectedNodes":[35,37]},{"coordinate":[6,2],"connectedNodes":[36,38]},{"coordinate":[6,1],"connectedNodes":[37,39]},{"coordinate":[6,0],"connectedNodes":[38]}]',
                    decor='[{"coordinate":{"x":865,"y":655},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":867,"y":457},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":867,"y":275},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":864,"y":91},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":668,"y":307},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":542,"y":301},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":194,"y":695},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":340,"y":704},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":87,"y":671},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":187,"y":50},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":62,"y":86},"url":"/static/game/image/tree2.svg"}]')
    level38.save()

    level36.next_level = level37
    level37.next_level = level38
    level38.next_level = Level.objects.get(pk=39)

    level36.blocks = blocks
    level37.blocks = blocks
    level38.blocks = blocks

    level36.save()
    level37.save()
    level38.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0050_rename_destination(s)'),
    ]

    operations = [
        migrations.RunPython(change_levels)
    ]
