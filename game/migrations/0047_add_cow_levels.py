# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.db import models, migrations
from game.level_management import set_blocks_inner, set_decor_inner


def add_cows_block(apps, schema_editor):

    Block = apps.get_model('game', 'Block')

    cow_crossing = Block.objects.create(type='cow_crossing')
    cow_crossing.save()
    declare_event = Block.objects.create(type='declare_event')
    declare_event.save()


def add_levels(apps, schema_editor):
    def set_decor(level, decor):
        set_decor_inner(level, decor, LevelDecor)

    def set_blocks(level, blocks):
        set_blocks_inner(level, blocks, LevelBlock, Block)

    Episode = apps.get_model('game', 'Episode')
    Level = apps.get_model('game', 'Level')
    Theme = apps.get_model('game', 'Theme')
    Character = apps.get_model('game', 'Character')
    LevelDecor = apps.get_model('game', 'LevelDecor')
    LevelBlock = apps.get_model('game', 'LevelBlock')
    Block = apps.get_model('game', 'Block')

    episode12 = Episode(pk=12, name="Cows", r_branchiness=0,
                        r_loopiness=0, r_num_tiles=10, r_curviness=0.5, r_pythonEnabled=0,
                        r_blocklyEnabled=1, r_trafficLights=0)
    episode12.save()

    episode11 = Episode.objects.get(pk=11)
    episode11.next_episode = episode12
    episode11.save()

    level110 = Level(
        name='110',
        episode=episode12,
        default=True,
        path='[{"coordinate":[0,5],"connectedNodes":[1]},{"coordinate":[1,5],"connectedNodes":[0,2]},{"coordinate":[2,5],"connectedNodes":[1,3]},{"coordinate":[3,5],"connectedNodes":[2,4]},{"coordinate":[4,5],"connectedNodes":[3,5]},{"coordinate":[5,5],"connectedNodes":[4]}]',
        traffic_lights='[]',
        cows='[{"minCows":1,"maxCows":1,"potentialCoordinates":[{"x":3,"y":5}]}]',
        destinations='[[5,5]]',
        origin='{"coordinate":[0,5],"direction":"E"}',
        max_fuel=50,
        blocklyEnabled=True,
        pythonEnabled=False,
        theme=Theme.objects.get(id=1),
        character=Character.objects.get(id='1'),
        model_solution='[6]',
    )
    level110.save()
    set_decor(level110, json.loads(
        '[{"x":401,"y":397,"decorName":"tree1"},{"x":250,"y":397,"decorName":"tree1"},{"x":100,"y":397,"decorName":"tree1"},{"x":400,"y":596,"decorName":"tree1"},{"x":247,"y":596,"decorName":"tree1"},{"x":100,"y":596,"decorName":"tree1"}]'))
    set_blocks(level110, json.loads(
        '[{"type":"move_forwards"},{"type":"turn_left"},{"type":"turn_right"},{"type":"wait"},{"type":"controls_repeat_while"},{"type":"controls_if"},{"type":"road_exists"},{"type":"cow_crossing"}]'))

    level111 = Level(
        name='111',
        episode=episode12,
        default=True,
        path='[{"coordinate":[0,5],"connectedNodes":[1]},{"coordinate":[1,5],"connectedNodes":[0,2]},{"coordinate":[2,5],"connectedNodes":[1,3]},{"coordinate":[3,5],"connectedNodes":[2,4]},{"coordinate":[4,5],"connectedNodes":[3,5]},{"coordinate":[5,5],"connectedNodes":[4]}]',
        traffic_lights='[]',
        cows='[{"minCows":1,"maxCows":1,"potentialCoordinates":[{"x":3,"y":5},{"x":2,"y":5},{"x":4,"y":5}]}]',
        destinations='[[5,5]]',
        origin='{"coordinate":[0,5],"direction":"E"}',
        max_fuel=50,
        blocklyEnabled=True,
        pythonEnabled=False,
        theme=Theme.objects.get(id=1),
        character=Character.objects.get(id='1'),
        model_solution='[6]',
    )

    level111.save()
    set_decor(level111, json.loads(
        '[{"x":401,"y":397,"decorName":"tree1"},{"x":250,"y":397,"decorName":"tree1"},{"x":100,"y":397,"decorName":"tree1"},{"x":400,"y":596,"decorName":"tree1"},{"x":247,"y":596,"decorName":"tree1"},{"x":100,"y":596,"decorName":"tree1"}]'))
    set_blocks(level111, json.loads(
        '[{"type":"move_forwards"},{"type":"turn_left"},{"type":"turn_right"},{"type":"wait"},{"type":"controls_if"},{"type":"controls_repeat_while"},{"type":"road_exists"},{"type":"cow_crossing"}]'))

    level112 = Level(
        name='112',
        episode=episode12,
        default=True,
        path='[{"coordinate":[0,5],"connectedNodes":[1]},{"coordinate":[1,5],"connectedNodes":[0,2]},{"coordinate":[2,5],"connectedNodes":[1,3]},{"coordinate":[3,5],"connectedNodes":[2,4]},{"coordinate":[4,5],"connectedNodes":[3,5]},{"coordinate":[5,5],"connectedNodes":[4]}]',
        traffic_lights='[]',
        cows='[{"minCows":1,"maxCows":1,"potentialCoordinates":[{"x":3,"y":5},{"x":2,"y":5},{"x":4,"y":5}]}]',
        destinations='[[5,5]]',
        origin='{"coordinate":[0,5],"direction":"E"}',
        max_fuel=50,
        blocklyEnabled=True,
        pythonEnabled=False,
        theme=Theme.objects.get(id=1),
        character=Character.objects.get(id='1'),
        model_solution='[6]',
    )
    level112.save()
    set_decor(level112, json.loads(
        '[{"x":401,"y":397,"decorName":"tree1"},{"x":250,"y":397,"decorName":"tree1"},{"x":100,"y":397,"decorName":"tree1"},{"x":400,"y":596,"decorName":"tree1"},{"x":247,"y":596,"decorName":"tree1"},{"x":100,"y":596,"decorName":"tree1"}]'))
    set_blocks(level112, json.loads(
        '[{"type":"move_forwards"},{"type":"turn_left"},{"type":"turn_right"},{"type":"turn_around"},{"type":"wait"},{"type":"controls_repeat"},{"type":"controls_repeat_while"},{"type":"controls_repeat_until"},{"type":"controls_if"},{"type":"at_destination"},{"type":"road_exists"},{"type":"dead_end"},{"type":"traffic_light"},{"type":"cow_crossing"},{"type":"declare_event"}]'))

    level113 = Level(
        name='113',
        episode=episode12,
        default=True,
        path='[{"coordinate":[0,5],"connectedNodes":[1]},{"coordinate":[1,5],"connectedNodes":[0,2]},{"coordinate":[2,5],"connectedNodes":[1,3]},{"coordinate":[3,5],"connectedNodes":[2,4]},{"coordinate":[4,5],"connectedNodes":[3,5]},{"coordinate":[5,5],"connectedNodes":[4,6]},{"coordinate":[5,6],"connectedNodes":[7,5]},{"coordinate":[5,7],"connectedNodes":[8,6]},{"coordinate":[6,7],"connectedNodes":[7]}]',
        traffic_lights='[{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":3,"y":5},"direction":"E","startTime":0,"startingState":"RED"}]',
        cows='[{"minCows":1,"maxCows":1,"potentialCoordinates":[{"x":5,"y":5},{"x":5,"y":6}]}]',
        destinations='[[6,7]]',
        origin='{"coordinate":[0,5],"direction":"E"}',
        max_fuel=50,
        blocklyEnabled=True,
        pythonEnabled=False,
        theme=Theme.objects.get(id=1),
        character=Character.objects.get(id='1'),
        model_solution='[11]',
    )
    level113.save()
    set_decor(level113, json.loads(
        '[{"x":335,"y":471,"decorName":"bush"},{"x":286,"y":470,"decorName":"bush"},{"x":237,"y":470,"decorName":"bush"},{"x":188,"y":470,"decorName":"bush"},{"x":138,"y":470,"decorName":"bush"},{"x":335,"y":582,"decorName":"bush"},{"x":286,"y":582,"decorName":"bush"},{"x":237,"y":583,"decorName":"bush"},{"x":187,"y":582,"decorName":"bush"},{"x":138,"y":582,"decorName":"bush"},{"x":432,"y":568,"decorName":"tree1"},{"x":527,"y":463,"decorName":"tree1"},{"x":565,"y":606,"decorName":"tree1"}]'))
    set_blocks(level113, json.loads(
        '[{"type":"move_forwards"},{"type":"turn_left"},{"type":"turn_right"},{"type":"turn_around"},{"type":"wait"},{"type":"controls_repeat"},{"type":"controls_repeat_while"},{"type":"controls_repeat_until"},{"type":"at_destination"},{"type":"road_exists"},{"type":"traffic_light"},{"type":"cow_crossing"},{"type":"declare_event"}]'))

    level114 = Level(
        name='114',
        episode=episode12,
        default=True,
        path='[{"coordinate":[0,7],"connectedNodes":[1]},{"coordinate":[1,7],"connectedNodes":[0,2]},{"coordinate":[2,7],"connectedNodes":[1,3]},{"coordinate":[3,7],"connectedNodes":[2,4,11]},{"coordinate":[4,7],"connectedNodes":[3,5]},{"coordinate":[5,7],"connectedNodes":[4,6]},{"coordinate":[5,6],"connectedNodes":[5,7]},{"coordinate":[5,5],"connectedNodes":[9,6,8]},{"coordinate":[5,4],"connectedNodes":[7,12]},{"coordinate":[4,5],"connectedNodes":[10,7]},{"coordinate":[3,5],"connectedNodes":[13,11,9]},{"coordinate":[3,6],"connectedNodes":[3,10]},{"coordinate":[5,3],"connectedNodes":[8]},{"coordinate":[2,5],"connectedNodes":[14,10]},{"coordinate":[1,5],"connectedNodes":[15,13]},{"coordinate":[0,5],"connectedNodes":[14]}]',
        traffic_lights='[{"redDuration":3,"greenDuration":2,"sourceCoordinate":{"x":2,"y":7},"direction":"E","startTime":0,"startingState":"GREEN"}]',
        cows='[{"minCows":1,"maxCows":1,"potentialCoordinates":[{"x":5,"y":6},{"x":5,"y":7},{"x":4,"y":7}]},{"minCows":1,"maxCows":1,"potentialCoordinates":[{"x":3,"y":6},{"x":3,"y":5}]},{"minCows":1,"maxCows":1,"potentialCoordinates":[{"x":5,"y":4},{"x":5,"y":5}]}]',
        destinations='[[5,3]]',
        origin='{"coordinate":[0,7],"direction":"E"}',
        max_fuel=50,
        blocklyEnabled=True,
        pythonEnabled=False,
        theme=Theme.objects.get(id=1),
        character=Character.objects.get(id='1'),
        model_solution='[11]',
    )

    level114.save()
    set_decor(level114, json.loads(
        '[{"x":47,"y":439,"decorName":"tree2"},{"x":0,"y":527,"decorName":"tree2"},{"x":0,"y":579,"decorName":"tree2"},{"x":57,"y":548,"decorName":"tree2"},{"x":0,"y":457,"decorName":"tree2"},{"x":0,"y":348,"decorName":"tree2"},{"x":12,"y":400,"decorName":"tree2"},{"x":407,"y":593,"decorName":"tree1"},{"x":446,"y":572,"decorName":"tree1"},{"x":449,"y":611,"decorName":"tree1"},{"x":250,"y":544,"decorName":"tree1"},{"x":130,"y":610,"decorName":"pond"}]'))
    set_blocks(level114, json.loads(
        '[{"type":"move_forwards"},{"type":"turn_left"},{"type":"turn_right"},{"type":"turn_around"},{"type":"wait"},{"type":"controls_repeat"},{"type":"controls_repeat_while"},{"type":"controls_repeat_until"},{"type":"controls_if"},{"type":"at_destination"},{"type":"road_exists"},{"type":"dead_end"},{"type":"traffic_light"},{"type":"cow_crossing"},{"type":"declare_event"}]'))

    level109 = Level.objects.get(name='109')
    level109.next_level=level110
    level110.next_level=level111
    level111.next_level=level112
    level112.next_level=level113
    level113.next_level=level114

    level109.save()
    level110.save()
    level111.save()
    level112.save()
    level113.save()
    level114.save()

class Migration(migrations.Migration):

    dependencies = [
        ('game', '0046_set_img_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='r_cows',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='level',
            name='cows',
            field=models.TextField(default=b'[]', max_length=10000),
            preserve_default=True,
        ),
        migrations.RunPython(add_cows_block),
        migrations.RunPython(add_levels)
    ]
