# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def change_levels(apps, schema_editor):

    Level = apps.get_model('game', 'Level')
    Block = apps.get_model('game', 'Block')

    blocks_around = Block.objects.filter(type__in=["move_forwards", "turn_left", "turn_right",
                                                   "controls_whileUntil", "controls_if",
                                                   "logic_negate", "road_exists", "at_destination",
                                                   "turn_around", "controls_repeat", "road_exists",
                                                   "dead_end"])

    blocks_traffic = Block.objects.filter(type__in=["move_forwards", "turn_left", "turn_right", "wait",
                                                    "controls_repeat", "controls_whileUntil", "controls_if",
                                                    "logic_negate", "road_exists", "at_destination",
                                                    "traffic_light", "dead_end", "turn_around"])

    level34 = Level.objects.get(id=34)
    level34.model_solution += 1

    level35 = Level.objects.get(id=35)
    level35.model_solution += 1

    level36 = Level.objects.get(id=36)
    level36.model_solution += 1

    level37 = Level.objects.get(id=37)
    level37.model_solution += 1

    level38 = Level.objects.get(id=38)
    level38.model_solution += 1

    level39 = Level.objects.get(id=39)
    level39.model_solution = 11
    level39.blocks = blocks_around

    level40 = Level.objects.get(id=40)
    level40.model_solution += 11

    level45 = Level.objects.get(id=45)
    level45.traffic_lights = '[{"node":3,"sourceNode":4,"redDuration":4,"greenDuration":1,"startTime":0,"startingState":"GREEN"},{"node":4,"sourceNode":5,"redDuration":3,"greenDuration":1,"startTime":0,"startingState":"RED"}]'

    level46 = Level.objects.get(id=46)
    level46.model_solution = 9

    level47 = Level.objects.get(id=47)
    level47.model_solution = 9
    level47.path = '[{"coordinate":[6,1],"connectedNodes":[1]},{"coordinate":[6,2],"connectedNodes":[2,0]},{"coordinate":[6,3],"connectedNodes":[3,1]},{"coordinate":[6,4],"connectedNodes":[4,2]},{"coordinate":[6,5],"connectedNodes":[5,3]},{"coordinate":[6,6],"connectedNodes":[6,4]},{"coordinate":[5,6],"connectedNodes":[7,5]},{"coordinate":[4,6],"connectedNodes":[8,6]},{"coordinate":[3,6],"connectedNodes":[9,7]},{"coordinate":[2,6],"connectedNodes":[8,10]},{"coordinate":[2,5],"connectedNodes":[9,11]},{"coordinate":[2,4],"connectedNodes":[10,12]},{"coordinate":[2,3],"connectedNodes":[11,13]},{"coordinate":[2,2],"connectedNodes":[12,14]},{"coordinate":[3,2],"connectedNodes":[13,15]},{"coordinate":[4,2],"connectedNodes":[14,16]},{"coordinate":[4,3],"connectedNodes":[15]}]'
    level47.destination = [4, 3]
    level47.decor = '[{"coordinate":{"x":46,"y":683},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":8,"y":589},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":149,"y":716},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":106,"y":568},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":806,"y":262},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":760,"y":165},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":852,"y":86},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":761,"y":51},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":865,"y":175},"url":"/static/game/image/tree2.svg"}]'
    level47.traffic_lights = '[{"id":0,"node":3,"sourceNode":2,"redDuration":3,"greenDuration":3,"startTime":0,"startingState":"RED"},{"id":1,"node":7,"sourceNode":6,"redDuration":3,"greenDuration":3,"startTime":0,"startingState":"RED"},{"id":2,"node":11,"sourceNode":10,"redDuration":3,"greenDuration":3,"startTime":0,"startingState":"RED"},{"id":3,"node":15,"sourceNode":14,"redDuration":3,"greenDuration":3,"startTime":0,"startingState":"GREEN"}]'

    level48 = Level.objects.get(id=48)
    level48.model_solution = 11
    level48.destination = [1, 2]
    level48.blocks = blocks_traffic

    level34.save()
    level35.save()
    level36.save()
    level37.save()
    level38.save()
    level39.save()
    level40.save()
    level45.save()
    level46.save()
    level47.save()
    level48.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0036_merge'),
    ]

    operations = [
        migrations.RunPython(change_levels),
    ]
