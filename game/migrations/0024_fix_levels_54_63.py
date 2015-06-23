# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from game.level_management import set_decor_inner, set_blocks_inner

import json


def fix_new_levels(apps, schema_editor):

    Level = apps.get_model('game', 'Level')
    Theme = apps.get_model('game', 'Theme')

    LevelDecor = apps.get_model('game', 'LevelDecor')
    LevelBlock = apps.get_model('game', 'LevelBlock')
    Block = apps.get_model('game', 'Block')

    def set_decor(level, decor):
        set_decor_inner(level, decor, LevelDecor)

    def set_blocks(level, blocks):
        set_blocks_inner(level, blocks, LevelBlock, Block)

    right = Block.objects.get(type="turn_right")
    turn_around = Block.objects.get(type="turn_around")
    road_exists = Block.objects.get(type="road_exists")

    level51 = Level.objects.get(name='51', default=True)
    level51.traffic_lights = '[{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":4,"y":5},"direction":"E","startTime":0,"startingState":"GREEN"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":5,"y":5},"direction":"E","startTime":0,"startingState":"GREEN"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":6,"y":5},"direction":"S","startTime":0,"startingState":"GREEN"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":2,"y":5},"direction":"E","startTime":0,"startingState":"RED"}]'
    level51.model_solution = '[15]'
    level51.save()

    level54 = Level.objects.get(name='54', default=True)
    level54.model_solution = '[27]'
    level54.save()

    level54 = Level.objects.get(name='54', default=True)
    level54.model_solution = '[27]'
    level54.save()

    level55 = Level.objects.get(name='55', default=True)
    left = Block.objects.get(type="turn_left")
    level_block = LevelBlock.objects.get(level=level55, type=left)
    level_block.number = 2
    level_block.save()

    level57 = Level.objects.get(name='57', default=True)

    LevelDecor.objects.filter(level=level57).delete()
    LevelBlock.objects.filter(level=level57).delete()

    level57.path = '[{"coordinate":[0,2],"connectedNodes":[18]},{"coordinate":[5,3],"connectedNodes":[16,2]},{"coordinate":[5,2],"connectedNodes":[5,1,12]},{"coordinate":[2,2],"connectedNodes":[18,4]},{"coordinate":[3,2],"connectedNodes":[3,5]},{"coordinate":[4,2],"connectedNodes":[4,2]},{"coordinate":[5,5],"connectedNodes":[7,16]},{"coordinate":[5,6],"connectedNodes":[9,8,6]},{"coordinate":[6,6],"connectedNodes":[7]},{"coordinate":[4,6],"connectedNodes":[10,7]},{"coordinate":[3,6],"connectedNodes":[11,9]},{"coordinate":[2,6],"connectedNodes":[14,10]},{"coordinate":[5,1],"connectedNodes":[2]},{"coordinate":[1,7],"connectedNodes":[14]},{"coordinate":[1,6],"connectedNodes":[13,11,15]},{"coordinate":[1,5],"connectedNodes":[14,17]},{"coordinate":[5,4],"connectedNodes":[6,1]},{"coordinate":[1,4],"connectedNodes":[15]},{"coordinate":[1,2],"connectedNodes":[0,3]}]'
    level57.destinations = '[[1,6]]'
    level57.origin = '{"coordinate":[0,2],"direction":"E"}'
    level57.theme = Theme.objects.get(id=1)
    level57.model_solution = '[5]'

    level57.save()

    set_decor(level57, json.loads('[{"x":261,"y":426,"decorName":"pond"},{"x":412,"y":368,"decorName":"tree2"},{"x":179,"y":300,"decorName":"tree2"},{"x":210,"y":496,"decorName":"tree2"},{"x":323,"y":288,"decorName":"tree1"},{"x":415,"y":514,"decorName":"tree1"},{"x":789,"y":359,"decorName":"tree1"},{"x":750,"y":308,"decorName":"tree1"},{"x":807,"y":317,"decorName":"tree1"},{"x":207,"y":693,"decorName":"bush"},{"x":427,"y":161,"decorName":"bush"},{"x":355,"y":159,"decorName":"bush"},{"x":284,"y":160,"decorName":"bush"},{"x":211,"y":160,"decorName":"bush"},{"x":137,"y":160,"decorName":"bush"},{"x":278,"y":694,"decorName":"bush"},{"x":348,"y":695,"decorName":"bush"},{"x":419,"y":695,"decorName":"bush"},{"x":490,"y":695,"decorName":"bush"},{"x":566,"y":697,"decorName":"bush"},{"x":636,"y":697,"decorName":"bush"}]'))
    set_blocks(level57, json.loads('[{"type":"move_forwards","number":1},{"type":"turn_right","number":1},{"type":"turn_around","number":1},{"type":"controls_repeat"}]'))

    level61 = Level.objects.get(name='61', default=True)
    level61.model_solution = '[6]'
    level61.save()

    level62 = Level.objects.get(name='62', default=True)
    level62.model_solution = '[5]'
    level_block = LevelBlock.objects.get(level=level62, type=left)
    level_block.number = 1
    level_block.save()
    level_block = LevelBlock.objects.get(level=level62, type=right)
    level_block.number = 2
    level_block.save()

    level63 = Level.objects.get(name='63', default=True)
    LevelBlock.objects.filter(level=level63, type=turn_around).delete()
    level_block = LevelBlock.objects.get(level=level63, type=road_exists)
    level_block.number = 1
    level_block.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0023_add_solutions_to_level_43'),
    ]

    operations = [
        migrations.RunPython(fix_new_levels)
    ]
