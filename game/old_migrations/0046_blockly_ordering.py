
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def reorder_blocks(apps, schema_editor):

    Block = apps.get_model('game', 'Block')

    moveForwards = Block.objects.get(type="move_forwards")
    turnLeft = Block.objects.get(type="turn_left")
    turnRight = Block.objects.get(type="turn_right")
    turnAround = Block.objects.get(type="turn_around")
    wait = Block.objects.get(type="wait")
    deliver = Block.objects.get(type="deliver")
    whileUntil = Block.objects.get(type="controls_whileUntil")
    repeat = Block.objects.get(type="controls_repeat")
    iff = Block.objects.get(type="controls_if")
    negate = Block.objects.get(type="logic_negate")
    atDestination = Block.objects.get(type="at_destination")
    roadExists = Block.objects.get(type="road_exists")
    deadEnd = Block.objects.get(type="dead_end")
    trafficLight = Block.objects.get(type="traffic_light")
    callProc = Block.objects.get(type="call_proc")
    declareProc = Block.objects.get(type="declare_proc")
    text = Block.objects.get(type="text")

    moveForwards.id = 1
    turnLeft.id = 2
    turnRight.id = 3
    turnAround.id = 4
    wait.id = 5
    deliver.id = 6
    whileUntil.id = 7
    repeat.id = 8
    iff.id = 9
    negate.id = 10
    atDestination.id = 11
    roadExists.id = 12
    deadEnd.id = 13
    trafficLight.id = 14
    callProc.id = 15
    declareProc.id = 16
    text.id = 17

    moveForwards.save()
    turnLeft.save()
    turnRight.save()
    turnAround.save()
    wait.save()
    deliver.save()
    whileUntil.save()
    repeat.save()
    iff.save()
    negate.save()
    atDestination.save()
    roadExists.save()
    deadEnd.save()
    trafficLight.save()
    callProc.save()
    declareProc.save()
    text.save()

class Migration(migrations.Migration):

    dependencies = [
        ('game', '0045_level_theme'),
    ]

    operations = [
        migrations.RunPython(reorder_blocks),
    ]
