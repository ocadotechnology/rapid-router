# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.db import migrations
from game.level_management import set_decor_inner, set_blocks_inner


def create_method_levels(apps, schema_editor):

    Level = apps.get_model('game', 'Level')
    LevelDecor = apps.get_model('game', 'LevelDecor')
    LevelBlock = apps.get_model('game', 'LevelBlock')
    Block = apps.get_model('game', 'Block')
    Character = apps.get_model('game', 'Character')
    Theme = apps.get_model('game', 'Theme')

    def set_decor(level, decor):
        set_decor_inner(level, decor, LevelDecor)

    def set_blocks(level, blocks):
        set_blocks_inner(level, blocks, LevelBlock, Block)

    level51 = Level.objects.get(name='51', default=True)
    level55 = Level.objects.get(name='52', default=True)
    level56 = Level.objects.get(name='53', default=True)
    level57 = Level.objects.get(name='54', default=True)

    level55.name = '55'
    level55.save()
    level56.name = '56'
    level56.save()
    level57.name = '57'
    level57.save()

    path = ('[{"coordinate":[0,1],"connectedNodes":[24]},'
            + '{"coordinate":[1,2],"connectedNodes":[2,24]},'
            + '{"coordinate":[1,3],"connectedNodes":[3,1]},'
            + '{"coordinate":[2,3],"connectedNodes":[2,4]},'
            + '{"coordinate":[2,2],"connectedNodes":[3,5]},'
            + '{"coordinate":[3,2],"connectedNodes":[4,6]},'
            + '{"coordinate":[4,2],"connectedNodes":[5,7]},'
            + '{"coordinate":[4,3],"connectedNodes":[8,6]},'
            + '{"coordinate":[4,4],"connectedNodes":[9,7]},'
            + '{"coordinate":[5,4],"connectedNodes":[8,10]},'
            + '{"coordinate":[5,3],"connectedNodes":[9,11]},'
            + '{"coordinate":[6,3],"connectedNodes":[10,12]},'
            + '{"coordinate":[6,4],"connectedNodes":[13,11]},'
            + '{"coordinate":[6,5],"connectedNodes":[14,12]},'
            + '{"coordinate":[7,5],"connectedNodes":[13,15]},'
            + '{"coordinate":[7,4],"connectedNodes":[14,16]},'
            + '{"coordinate":[8,4],"connectedNodes":[15,17]},'
            + '{"coordinate":[8,3],"connectedNodes":[16,18]},'
            + '{"coordinate":[8,2],"connectedNodes":[19,17]},'
            + '{"coordinate":[7,2],"connectedNodes":[18,20]},'
            + '{"coordinate":[7,1],"connectedNodes":[19,21]},'
            + '{"coordinate":[7,0],"connectedNodes":[22,20]},'
            + '{"coordinate":[6,0],"connectedNodes":[23,21]},'
            + '{"coordinate":[6,1],"connectedNodes":[25,22]},'
            + '{"coordinate":[1,1],"connectedNodes":[0,1]},'
            + '{"coordinate":[5,1],"connectedNodes":[23]}]')

    decor = json.loads('[{"url":"decor/city/hospital.svg","height":157,"width":140,"y":291,"x":280,'
                       + '"decorName":"pond"}, {"url":"decor/city/school.svg","height":100,'
                       + '"width":100,"y":300,"x":706,"decorName":"tree2"},'
                       + '{"url":"decor/city/shop.svg","height":70,"width":70,"y":490,"x":785,'
                       + '"decorName":"tree1"}, {"url":"decor/city/shop.svg","height":70,'
                       + '"width":70,"y":129,"x":789,"decorName":"tree1"},'
                       + '{"url":"decor/city/bush.svg","height":50,"width":50,"y":184,"x":600,'
                       + '"decorName":"bush"}, {"url":"decor/city/bush.svg","height":50,"width":50,'
                       + '"y":208,"x":662,"decorName":"bush"}, {"url":"decor/city/bush.svg",'
                       + '"height":50,"width":50,"y":277,"x":641,"decorName":"bush"},'
                       + '{"url":"decor/city/bush.svg","height":50,"width":50,"y":255,"x":570,'
                       + '"decorName":"bush"}, {"url":"decor/city/bush.svg","height":50,"width":50,'
                       + '"y":282,"x":497,"decorName":"bush"}, {"url":"decor/city/bush.svg",'
                       + '"height":50,"width":50,"y":455,"x":286,"decorName":"bush"},'
                       + '{"url":"decor/city/bush.svg","height":50,"width":50,"y":453,"x":215,'
                       + '"decorName":"bush"}, {"url":"decor/city/bush.svg","height":50,"width":50,'
                       + '"y":391,"x":216,"decorName":"bush"}, {"url":"decor/city/bush.svg",'
                       + '"height":50,"width":50,"y":456,"x":357,"decorName":"bush"}]')

    level52 = Level(
        name='52', path=path, default=True, blocklyEnabled=True, destinations='[[5,1]]',
        max_fuel='50', traffic_lights='[]', theme=Theme.objects.get(name='city'),
        origin='{"coordinate":[0,1],"direction":"E"}', character=Character.objects.get(name="Van"),
        pythonEnabled=False, model_solution='[14]')
    level52.save()

    level51.next_level = level52
    level51.save()

    blocks = Block.objects.filter(type__in=['move_forwards', 'turn_left', 'turn_right', 'call_proc',
                                            'declare_proc'])

    for block in blocks:
        levelblock = LevelBlock(level=level52, type=block)
        levelblock.save()

    set_decor(level52, decor)

    path = ('[{"coordinate":[4,7],"connectedNodes":[18]},'
            + '{"coordinate":[2,5],"connectedNodes":[2,19]},'
            + '{"coordinate":[1,5],"connectedNodes":[1,3]},'
            + '{"coordinate":[1,4],"connectedNodes":[2,4]},'
            + '{"coordinate":[1,3],"connectedNodes":[3,5]},'
            + '{"coordinate":[2,3],"connectedNodes":[4,6]},'
            + '{"coordinate":[2,2],"connectedNodes":[5,7]},'
            + '{"coordinate":[3,2],"connectedNodes":[6,8]},'
            + '{"coordinate":[3,1],"connectedNodes":[7,9]},'
            + '{"coordinate":[4,1],"connectedNodes":[8,10]},'
            + '{"coordinate":[4,2],"connectedNodes":[11,9]},'
            + '{"coordinate":[4,3],"connectedNodes":[12,10]},'
            + '{"coordinate":[3,3],"connectedNodes":[13,11]},'
            + '{"coordinate":[3,4],"connectedNodes":[14,12]},'
            + '{"coordinate":[4,4],"connectedNodes":[13,15]},'
            + '{"coordinate":[4,5],"connectedNodes":[16,14]},'
            + '{"coordinate":[5,5],"connectedNodes":[15,20]},'
            + '{"coordinate":[3,6],"connectedNodes":[19,18]},'
            + '{"coordinate":[3,7],"connectedNodes":[0,17]},'
            + '{"coordinate":[2,6],"connectedNodes":[17,1]},'
            + '{"coordinate":[5,4],"connectedNodes":[16,21]},'
            + '{"coordinate":[6,4],"connectedNodes":[20,22]},'
            + '{"coordinate":[6,3],"connectedNodes":[21,23]},'
            + '{"coordinate":[7,3],"connectedNodes":[22,24]},'
            + '{"coordinate":[7,2],"connectedNodes":[23,25]},'
            + '{"coordinate":[8,2],"connectedNodes":[24,26]},'
            + '{"coordinate":[8,1],"connectedNodes":[25,27]},'
            + '{"coordinate":[9,1],"connectedNodes":[26,28]},'
            + '{"coordinate":[9,0],"connectedNodes":[27]}]')

    level53 = Level(
        name='53',
        default=True,
        path=path,
        traffic_lights='[]',
        destinations='[[9,0]]',
        origin='{"coordinate":[4,7],"direction":"W"}',
        max_fuel=50,
        theme=Theme.objects.get(id=3),
        character=Character.objects.get(id='1'),
        blocklyEnabled=True,
        pythonEnabled=False,
        model_solution='[19]'
    )

    decor = ('[{"x":191,"y":407,"decorName":"tree2"},{"x":388,"y":595,"decorName":"pond"},'
             + '{"x":182,"y":688,"decorName":"tree1"},{"x":81,"y":584,"decorName":"tree1"},'
             + '{"x":212,"y":184,"decorName":"bush"},{"x":165,"y":230,"decorName":"bush"},'
             + '{"x":125,"y":279,"decorName":"bush"},{"x":262,"y":143,"decorName":"bush"},'
             + '{"x":693,"y":386,"decorName":"tree1"},{"x":592,"y":476,"decorName":"tree1"},'
             + '{"x":498,"y":319,"decorName":"tree1"},{"x":575,"y":596,"decorName":"pond"},'
             + '{"x":574,"y":700,"decorName":"pond"},{"x":900,"y":203,"decorName":"tree1"},'
             + '{"x":712,"y":102,"decorName":"tree1"},{"x":609,"y":216,"decorName":"tree1"},'
             + '{"x":793,"y":290,"decorName":"tree1"},{"x":812,"y":0,"decorName":"tree1"}]')

    blocks = ('[{"type":"move_forwards"},{"type":"turn_left"},{"type":"turn_right"},'
            + '{"type":"controls_repeat"},{"type":"call_proc"},{"type":"declare_proc"}]')

    level53.save()
    set_decor(level53, json.loads(decor))
    set_blocks(level53, json.loads(blocks))

    level52.next_level = level53
    level52.save()

    path = ('[{"coordinate":[1,4],"connectedNodes":[1]},'
            + '{"coordinate":[2,4],"connectedNodes":[0,2]},'
            + '{"coordinate":[2,5],"connectedNodes":[3,1]},'
            + '{"coordinate":[3,5],"connectedNodes":[2,4,20]},'
            + '{"coordinate":[4,5],"connectedNodes":[3,5]},'
            + '{"coordinate":[4,4],"connectedNodes":[4,6]},'
            + '{"coordinate":[5,4],"connectedNodes":[5,7]},'
            + '{"coordinate":[5,5],"connectedNodes":[8,6]},'
            + '{"coordinate":[6,5],"connectedNodes":[7,11,9]},'
            + '{"coordinate":[7,5],"connectedNodes":[8,10]},'
            + '{"coordinate":[8,5],"connectedNodes":[9]},'
            + '{"coordinate":[6,6],"connectedNodes":[21,12,8]},'
            + '{"coordinate":[7,6],"connectedNodes":[11,13]},'
            + '{"coordinate":[8,6],"connectedNodes":[12,14]},'
            + '{"coordinate":[9,6],"connectedNodes":[13,15]},'
            + '{"coordinate":[9,5],"connectedNodes":[14,16]},'
            + '{"coordinate":[9,4],"connectedNodes":[17,15]},'
            + '{"coordinate":[8,4],"connectedNodes":[16,18]},'
            + '{"coordinate":[8,3],"connectedNodes":[19,17]},'
            + '{"coordinate":[7,3],"connectedNodes":[18,25]},'
            + '{"coordinate":[3,4],"connectedNodes":[3]},'
            + '{"coordinate":[6,7],"connectedNodes":[22,11]},'
            + '{"coordinate":[5,7],"connectedNodes":[23,21]},'
            + '{"coordinate":[4,7],"connectedNodes":[24,22]},'
            + '{"coordinate":[3,7],"connectedNodes":[23]},'
            + '{"coordinate":[7,2],"connectedNodes":[26,19]},'
            + '{"coordinate":[6,2],"connectedNodes":[27,29,25]},'
            + '{"coordinate":[5,2],"connectedNodes":[28,26]},'
            + '{"coordinate":[4,2],"connectedNodes":[27]},'
            + '{"coordinate":[6,3],"connectedNodes":[30,26]},'
            + '{"coordinate":[5,3],"connectedNodes":[31,29]},'
            + '{"coordinate":[4,3],"connectedNodes":[32,30]},'
            + '{"coordinate":[3,3],"connectedNodes":[31,33]},'
            + '{"coordinate":[3,2],"connectedNodes":[45,32,34]},'
            + '{"coordinate":[3,1],"connectedNodes":[33,35]},'
            + '{"coordinate":[4,1],"connectedNodes":[34,36]},'
            + '{"coordinate":[4,0],"connectedNodes":[35,37]},'
            + '{"coordinate":[5,0],"connectedNodes":[36,38]},'
            + '{"coordinate":[5,1],"connectedNodes":[39,37]},'
            + '{"coordinate":[6,1],"connectedNodes":[38,40]},'
            + '{"coordinate":[7,1],"connectedNodes":[39,41]},'
            + '{"coordinate":[8,1],"connectedNodes":[40,42,44]},'
            + '{"coordinate":[8,2],"connectedNodes":[43,41]},'
            + '{"coordinate":[9,2],"connectedNodes":[42]},'
            + '{"coordinate":[8,0],"connectedNodes":[41]},'
            + '{"coordinate":[2,2],"connectedNodes":[46,33]},'
            + '{"coordinate":[1,2],"connectedNodes":[45]}]')

    level54 = Level(
        name='54',
        default=True,
        path=path,
        traffic_lights='[]',
        destinations='[[9,2]]',
        origin='{"coordinate":[1,4],"direction":"E"}',
        max_fuel=50,
        theme=Theme.objects.get(id=2),
        character=Character.objects.get(id='1'),
        blocklyEnabled=True,
        pythonEnabled=False,
        model_solution='[29]'
    )

    decor = ('[{"x":726,"y":408,"decorName":"tree2"},{"x":598,"y":400,"decorName":"tree2"},'
             + '{"x":503,"y":610,"decorName":"tree1"},{"x":44,"y":607,"decorName":"pond"},'
             + '{"x":700,"y":698,"decorName":"tree1"},{"x":361,"y":19,"decorName":"bush"},'
             + '{"x":308,"y":56,"decorName":"bush"},{"x":261,"y":107,"decorName":"bush"},'
             + '{"x":218,"y":159,"decorName":"bush"},{"x":629,"y":56,"decorName":"bush"},'
             + '{"x":572,"y":13,"decorName":"bush"},{"x":5,"y":510,"decorName":"tree1"}]')

    block = ('[{"type":"move_forwards"},{"type":"turn_left"},{"type":"turn_right"},'
             + '{"type":"controls_repeat"},{"type":"call_proc"},{"type":"declare_proc"}]')

    level54.save()
    set_decor(level54, json.loads(decor))
    set_blocks(level54, json.loads(block))

    level53.next_level = level54
    level53.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0017_change_episode_names'),
    ]

    operations = [
        migrations.RunPython(create_method_levels)
    ]
