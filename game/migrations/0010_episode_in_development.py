# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def add_episodes(apps, schema_editor):
    Level = apps.get_model('game', 'Level')
    Episode = apps.get_model('game', 'Episode')
    Block = apps.get_model('game', 'Block')
    LevelBlock = apps.get_model('game', 'LevelBlock')
    Theme = apps.get_model('game', 'Theme')
    Character = apps.get_model('game', 'Character')

    level51 = Level.objects.get(id=51).delete()

    level51 = Level(blocklyEnabled=True,
                    character=Character.objects.get(name="Van"),
                    decor='[{"coordinate":{"x":413,"y":374},"name":"pond","height":100},{"coordinate":{"x":352,"y":594},"name":"tree2","height":100},{"coordinate":{"x":396,"y":438},"name":"bush","height":50},{"coordinate":{"x":530,"y":428},"name":"tree2","height":100},{"coordinate":{"x":134,"y":605},"name":"bush","height":50},{"coordinate":{"x":221,"y":395},"name":"tree2","height":100},{"coordinate":{"x":658,"y":528},"name":"tree2","height":100}]',
                    destinations="[[6,2]]",
                    max_fuel="50",
                    name="51",
                    origin='{"coordinate":[1,5],"direction":"E"}',
                    path='[{"coordinate":[1,5],"connectedNodes":[1]},{"coordinate":[2,5],"connectedNodes":[0,2]},{"coordinate":[3,5],"connectedNodes":[1,3]},{"coordinate":[4,5],"connectedNodes":[2,4]},{"coordinate":[5,5],"connectedNodes":[3,5]},{"coordinate":[6,5],"connectedNodes":[4,6]},{"coordinate":[6,4],"connectedNodes":[5,7]},{"coordinate":[6,3],"connectedNodes":[6,8]},{"coordinate":[6,2],"connectedNodes":[7]}]',
                    pythonEnabled=False,
                    theme=Theme.objects.get(id=2),
                    default=True,
                    traffic_lights='[{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":4,"y":5},"direction":"E","startTime":0,"startingState":"GREEN"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":5,"y":5},"direction":"E","startTime":0,"startingState":"GREEN"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":6,"y":5},"direction":"S","startTime":0,"startingState":"GREEN"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":6,"y":3},"direction":"S","startTime":0,"startingState":"RED"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":2,"y":5},"direction":"E","startTime":0,"startingState":"RED"}]')
    level51.save()

    move_forwards = LevelBlock(level=level51, type=Block.objects.get(type="move_forwards"))
    turn_left = LevelBlock(level=level51, type=Block.objects.get(type="turn_left"))
    turn_right = LevelBlock(level=level51, type=Block.objects.get(type="turn_right"))
    wait = LevelBlock(level=level51, type=Block.objects.get(type="wait"))
    controls_repeat_until = LevelBlock(level=level51, type=Block.objects.get(type="controls_repeat_until"))
    at_destination = LevelBlock(level=level51, type=Block.objects.get(type="at_destination"))
    traffic_light = LevelBlock(level=level51, type=Block.objects.get(type="traffic_light"))
    call_proc = LevelBlock(level=level51, type=Block.objects.get(type="call_proc"))
    declare_proc = LevelBlock(level=level51, type=Block.objects.get(type="declare_proc"))
    move_forwards.save()
    turn_left.save()
    turn_right.save()
    wait.save()
    controls_repeat_until.save()
    at_destination.save()
    traffic_light.save()
    call_proc.save()
    declare_proc.save()


    level52 = Level(blocklyEnabled=True,
                    character=Character.objects.get(name="Van"),
                    decor='[{"coordinate":{"x":271,"y":463},"name":"tree2","height":100},{"coordinate":{"x":535,"y":431},"name":"tree2","height":100},{"coordinate":{"x":144,"y":301},"name":"tree2","height":100},{"coordinate":{"x":404,"y":293},"name":"tree2","height":100},{"coordinate":{"x":200,"y":262},"name":"tree2","height":100},{"coordinate":{"x":423,"y":611},"name":"pond","height":100},{"coordinate":{"x":375,"y":670},"name":"tree2","height":100},{"coordinate":{"x":521,"y":583},"name":"tree2","height":100}]',
                    destinations="[[8,6]]",
                    max_fuel="52",
                    name="Block scarcity",
                    origin='{"coordinate":[0,4],"direction":"E"}',
                    path='[{"coordinate":[0,4],"connectedNodes":[1]},{"coordinate":[1,4],"connectedNodes":[0,2]},{"coordinate":[2,4],"connectedNodes":[1,3,11]},{"coordinate":[2,5],"connectedNodes":[5,2]},{"coordinate":[4,5],"connectedNodes":[10,7]},{"coordinate":[2,6],"connectedNodes":[6,3]},{"coordinate":[3,6],"connectedNodes":[5,10]},{"coordinate":[5,5],"connectedNodes":[4,8]},{"coordinate":[6,5],"connectedNodes":[7,20,16,9]},{"coordinate":[6,4],"connectedNodes":[8,15]},{"coordinate":[3,5],"connectedNodes":[6,4]},{"coordinate":[3,4],"connectedNodes":[2,12]},{"coordinate":[4,4],"connectedNodes":[11,13]},{"coordinate":[5,4],"connectedNodes":[12,14]},{"coordinate":[5,3],"connectedNodes":[13,15]},{"coordinate":[6,3],"connectedNodes":[14,9]},{"coordinate":[7,5],"connectedNodes":[8,17]},{"coordinate":[7,4],"connectedNodes":[16,18]},{"coordinate":[8,4],"connectedNodes":[17,19]},{"coordinate":[8,5],"connectedNodes":[24,18]},{"coordinate":[6,6],"connectedNodes":[21,8]},{"coordinate":[6,7],"connectedNodes":[22,20]},{"coordinate":[7,7],"connectedNodes":[21,23]},{"coordinate":[8,7],"connectedNodes":[22,24]},{"coordinate":[8,6],"connectedNodes":[23,19]}]',
                    pythonEnabled=False,
                    theme=Theme.objects.get(id=1),
                    default=True,
                    traffic_lights= "[]")
    level52.save()

    forwards = LevelBlock(level=level52, type=Block.objects.get(type="move_forwards"))
    left = LevelBlock(level=level52, type=Block.objects.get(type="turn_left"), number=4)
    right = LevelBlock(level=level52, type=Block.objects.get(type="turn_right"), number=2)
    forwards.save()
    left.save()
    right.save()



    episode6 = Episode.objects.get(id=6)

    episode7 = Episode(pk=7, name="Functions", first_level=level51, r_branchiness=0.5,
                       r_loopiness=0.1, r_num_tiles=35, r_curviness=0.2, r_pythonEnabled=0,
                       r_blocklyEnabled=1, r_trafficLights=1, in_development=True)
    episode7.save()

    episode8 = Episode(pk=8, name="Limited blocks", first_level=level52, r_branchiness=0.5,
                       r_loopiness=0.1, r_num_tiles=35, r_curviness=0.2, r_pythonEnabled=0,
                       r_blocklyEnabled=1, r_trafficLights=1, in_development=True)
    episode8.save()


    episode6.next_episode = episode7
    episode7.next_episode = episode8
    episode6.save()
    episode7.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0009_auto_20140905_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='in_development',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),

        migrations.RunPython(add_episodes),
    ]
