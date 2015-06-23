# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

import json

from game.level_management import set_decor_inner, set_blocks_inner

def fix_level_63(apps, schema_editor):

    Level = apps.get_model('game', 'Level')
    LevelDecor = apps.get_model('game', 'LevelDecor')
    LevelBlock = apps.get_model('game', 'LevelBlock')
    Block = apps.get_model('game', 'Block')

    def set_decor(level, decor):
        set_decor_inner(level, decor, LevelDecor)

    def set_blocks(level, blocks):
        set_blocks_inner(level, blocks, LevelBlock, Block)

    level63 = Level.objects.get(name="63")
    level63.path=str('[{"coordinate":[1,2],"connectedNodes":[2]},{"coordinate":[2,4],"connectedNodes":[3,4,12]},{"coordinate":[1,3],"connectedNodes":[3,0]},{"coordinate":[1,4],"connectedNodes":[1,2]},{"coordinate":[2,5],"connectedNodes":[5,1]},{"coordinate":[2,6],"connectedNodes":[11,6,4]},{"coordinate":[3,6],"connectedNodes":[5,7]},{"coordinate":[4,6],"connectedNodes":[6,8]},{"coordinate":[4,5],"connectedNodes":[7,9]},{"coordinate":[4,4],"connectedNodes":[10,8]},{"coordinate":[3,4],"connectedNodes":[9]},{"coordinate":[1,6],"connectedNodes":[5]},{"coordinate":[2,3],"connectedNodes":[1]}]')
    level63.model_solution='[7]'
    level63.destinations='[[3,4]]'
    level63.origin='{"coordinate":[1,2],"direction":"N"}'
    set_decor(level63, json.loads('[{"x":458,"y":456,"decorName":"bush"},{"x":466,"y":585,"decorName":"tree2"},{"x":562,"y":636,"decorName":"tree2"},{"x":140,"y":261,"decorName":"bush"},{"x":474,"y":700,"decorName":"tree2"},{"x":55,"y":195,"decorName":"bush"},{"x":324,"y":147,"decorName":"bush"},{"x":152,"y":173,"decorName":"bush"},{"x":381,"y":99,"decorName":"bush"},{"x":0,"y":145,"decorName":"bush"},{"x":91,"y":100,"decorName":"bush"},{"x":205,"y":33,"decorName":"bush"},{"x":115,"y":0,"decorName":"bush"}]'))
    set_blocks(level63, json.loads('[{"type":"move_forwards","number":1},{"type":"turn_left","number":1},{"type":"turn_right","number":1},{"type":"turn_around","number":1},{"type":"controls_repeat_until"},{"type":"controls_if"},{"type":"at_destination"},{"type":"road_exists","number":2}]'))
    level63.save()
    
class Migration(migrations.Migration):

    dependencies = [
        ('game', '0020_auto_20140912_1021'),
    ]

    operations = [
        migrations.RunPython(fix_level_63),
    ]
