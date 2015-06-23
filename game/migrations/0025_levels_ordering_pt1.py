# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from game.level_management import set_decor_inner, set_blocks_inner
import json


def reorder_episodes(apps, schema_editor):

    Episode = apps.get_model('game', 'Episode')

    traffic_lights_episode = Episode.objects.get(name="Traffic Lights")
    limited_blocks_episode = Episode.objects.get(name="Limited blocks")
    procedures_episode = Episode.objects.get(name="Procedures")
    blockly_brain_teasers_episode = Episode.objects.get(name="Puzzles!")
    introduction_to_python_episode = Episode.objects.get(name="Introduction to Python")
    python_episode = Episode.objects.get(name="Python!")

    limited_blocks_episode.name = "Limited Blocks"
    blockly_brain_teasers_episode.name = "Blockly Brain Teasers"
    python_episode.name = "Python"

    traffic_lights_episode.next_episode = limited_blocks_episode
    limited_blocks_episode.next_episode = procedures_episode
    procedures_episode.next_episode = blockly_brain_teasers_episode
    blockly_brain_teasers_episode.next_episode = introduction_to_python_episode
    introduction_to_python_episode.next_episode = python_episode

    traffic_lights_episode.save()
    limited_blocks_episode.save()
    procedures_episode.save()
    blockly_brain_teasers_episode.save()
    introduction_to_python_episode.save()
    python_episode.save()


def fix_levels(apps, schema_editor):

    Level = apps.get_model('game', 'Level')
    Character = apps.get_model('game', 'Character')
    Theme = apps.get_model('game', 'Theme')
    Episode = apps.get_model('game', 'Episode')
    LevelDecor = apps.get_model('game', 'LevelDecor')
    LevelBlock = apps.get_model('game', 'LevelBlock')
    Block = apps.get_model('game', 'Block')

    def set_decor(level, decor):
        set_decor_inner(level, decor, LevelDecor)

    def set_blocks(level, blocks):
        set_blocks_inner(level, blocks, LevelBlock, Block)

    def level52():
        level52 = Level(
            name='52',
            default=True,
            path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,8,2,18]},{"coordinate":[2,3],"connectedNodes":[1,3]},{"coordinate":[3,3],"connectedNodes":[2,4]},{"coordinate":[4,3],"connectedNodes":[3,5]},{"coordinate":[5,3],"connectedNodes":[4,6]},{"coordinate":[6,3],"connectedNodes":[5,17,7,25]},{"coordinate":[7,3],"connectedNodes":[6]},{"coordinate":[1,4],"connectedNodes":[9,1]},{"coordinate":[2,4],"connectedNodes":[8,10]},{"coordinate":[2,5],"connectedNodes":[11,9]},{"coordinate":[3,5],"connectedNodes":[10,12]},{"coordinate":[3,6],"connectedNodes":[13,11]},{"coordinate":[4,6],"connectedNodes":[12,14]},{"coordinate":[4,5],"connectedNodes":[13,15]},{"coordinate":[5,5],"connectedNodes":[14,16]},{"coordinate":[5,4],"connectedNodes":[15,17]},{"coordinate":[6,4],"connectedNodes":[16,6]},{"coordinate":[1,2],"connectedNodes":[1,19]},{"coordinate":[2,2],"connectedNodes":[18,20]},{"coordinate":[3,2],"connectedNodes":[19,21]},{"coordinate":[3,1],"connectedNodes":[20,22]},{"coordinate":[4,1],"connectedNodes":[21,23]},{"coordinate":[5,1],"connectedNodes":[22,24]},{"coordinate":[6,1],"connectedNodes":[23,25]},{"coordinate":[6,2],"connectedNodes":[6,24]}]',
            traffic_lights='[]',
            destinations='[[7,3]]',
            origin='{"coordinate":[0,3],"direction":"E"}',
            max_fuel=50,
            blocklyEnabled=True,
            pythonEnabled=False,
            theme=Theme.objects.get(id=2),
            character=Character.objects.get(id='1'),
            model_solution='[6]',
        )
        level52.save()
        set_decor(level52, json.loads('[{"x":29,"y":524,"decorName":"tree2"},{"x":193,"y":622,"decorName":"tree2"},{"x":521,"y":603,"decorName":"tree2"},{"x":651,"y":488,"decorName":"tree2"},{"x":74,"y":100,"decorName":"tree1"},{"x":266,"y":2,"decorName":"tree1"},{"x":533,"y":9,"decorName":"tree1"},{"x":701,"y":110,"decorName":"tree1"},{"x":268,"y":385,"decorName":"bush"},{"x":348,"y":386,"decorName":"bush"},{"x":420,"y":385,"decorName":"bush"},{"x":494,"y":386,"decorName":"bush"},{"x":424,"y":201,"decorName":"pond"}]'))
        set_blocks(level52, json.loads('[{"type":"turn_left","number":2},{"type":"turn_right","number":2},{"type":"controls_repeat"}]'))
        return level52

    def level53():
        level53 = Level(
            name='53',
            default=True,
            path='[{"coordinate":[1,3],"connectedNodes":[1]},{"coordinate":[2,3],"connectedNodes":[0,17,12,2]},{"coordinate":[2,2],"connectedNodes":[1,3]},{"coordinate":[2,1],"connectedNodes":[2,4]},{"coordinate":[3,1],"connectedNodes":[3,5]},{"coordinate":[4,1],"connectedNodes":[4,6]},{"coordinate":[5,1],"connectedNodes":[5,7]},{"coordinate":[6,1],"connectedNodes":[6,8]},{"coordinate":[6,2],"connectedNodes":[9,29,7]},{"coordinate":[6,3],"connectedNodes":[16,10,8]},{"coordinate":[6,4],"connectedNodes":[11,9]},{"coordinate":[6,5],"connectedNodes":[23,24,10]},{"coordinate":[3,3],"connectedNodes":[1,13]},{"coordinate":[4,3],"connectedNodes":[12,14]},{"coordinate":[4,4],"connectedNodes":[15,13]},{"coordinate":[5,4],"connectedNodes":[14,16]},{"coordinate":[5,3],"connectedNodes":[15,9]},{"coordinate":[2,4],"connectedNodes":[18,1]},{"coordinate":[2,5],"connectedNodes":[19,17]},{"coordinate":[2,6],"connectedNodes":[20,18]},{"coordinate":[3,6],"connectedNodes":[19,21]},{"coordinate":[4,6],"connectedNodes":[20,22]},{"coordinate":[5,6],"connectedNodes":[21,23]},{"coordinate":[6,6],"connectedNodes":[22,11]},{"coordinate":[7,5],"connectedNodes":[11,25]},{"coordinate":[8,5],"connectedNodes":[24,26]},{"coordinate":[8,4],"connectedNodes":[25,27]},{"coordinate":[8,3],"connectedNodes":[26,28]},{"coordinate":[8,2],"connectedNodes":[29,27]},{"coordinate":[7,2],"connectedNodes":[8,28]}]',
            traffic_lights='[]',
            destinations='[[8,3]]',
            origin='{"coordinate":[1,3],"direction":"E"}',
            max_fuel=50,
            blocklyEnabled=True,
            pythonEnabled=False,
            theme=Theme.objects.get(id=3),
            character=Character.objects.get(id='1'),
            model_solution='[9]',
        )
        level53.save()
        set_decor(level53, json.loads('[{"x":302,"y":199,"decorName":"pond"},{"x":481,"y":302,"decorName":"bush"},{"x":481,"y":252,"decorName":"bush"},{"x":481,"y":204,"decorName":"bush"},{"x":692,"y":292,"decorName":"tree1"},{"x":540,"y":503,"decorName":"tree2"},{"x":331,"y":499,"decorName":"pond"},{"x":254,"y":700,"decorName":"tree1"},{"x":0,"y":700,"decorName":"tree1"},{"x":97,"y":509,"decorName":"tree1"},{"x":42,"y":602,"decorName":"tree1"},{"x":123,"y":670,"decorName":"tree1"},{"x":4,"y":444,"decorName":"tree1"},{"x":357,"y":457,"decorName":"bush"},{"x":295,"y":414,"decorName":"bush"},{"x":296,"y":457,"decorName":"bush"},{"x":356,"y":414,"decorName":"bush"}]'))
        set_blocks(level53, json.loads('[{"type":"move_forwards","number":2},{"type":"turn_left","number":3},{"type":"turn_right","number":2},{"type":"controls_repeat"}]'))
        return level53

    def level54():
        level54 = Level(
            name='54',
            default=True,
            path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,9,2,18]},{"coordinate":[2,3],"connectedNodes":[1,10,3,19]},{"coordinate":[3,3],"connectedNodes":[2,11,4,20]},{"coordinate":[4,3],"connectedNodes":[3,12,5,21]},{"coordinate":[5,3],"connectedNodes":[4,13,6,22]},{"coordinate":[6,3],"connectedNodes":[5,14,7,23]},{"coordinate":[7,3],"connectedNodes":[6,15,8,24]},{"coordinate":[8,3],"connectedNodes":[7,16,17,25]},{"coordinate":[1,4],"connectedNodes":[10,1]},{"coordinate":[2,4],"connectedNodes":[9,2]},{"coordinate":[3,4],"connectedNodes":[12,3]},{"coordinate":[4,4],"connectedNodes":[11,4]},{"coordinate":[5,4],"connectedNodes":[14,5]},{"coordinate":[6,4],"connectedNodes":[13,6]},{"coordinate":[7,4],"connectedNodes":[16,7]},{"coordinate":[8,4],"connectedNodes":[15,8]},{"coordinate":[9,3],"connectedNodes":[8]},{"coordinate":[1,2],"connectedNodes":[1,19]},{"coordinate":[2,2],"connectedNodes":[18,2]},{"coordinate":[3,2],"connectedNodes":[3,21]},{"coordinate":[4,2],"connectedNodes":[20,4]},{"coordinate":[5,2],"connectedNodes":[5,23]},{"coordinate":[6,2],"connectedNodes":[22,6]},{"coordinate":[7,2],"connectedNodes":[7,25]},{"coordinate":[8,2],"connectedNodes":[24,8]}]',
            traffic_lights='[]',
            destinations='[[9,3]]',
            origin='{"coordinate":[0,3],"direction":"E"}',
            max_fuel=50,
            blocklyEnabled=True,
            pythonEnabled=False,
            theme=Theme.objects.get(id=1),
            character=Character.objects.get(id='1'),
            model_solution='[5]',
        )
        level54.save()
        set_decor(level54, json.loads('[{"x":29,"y":466,"decorName":"tree2"},{"x":40,"y":97,"decorName":"tree2"},{"x":296,"y":501,"decorName":"tree2"},{"x":719,"y":52,"decorName":"tree2"},{"x":650,"y":481,"decorName":"tree1"},{"x":122,"y":639,"decorName":"tree1"},{"x":416,"y":22,"decorName":"pond"},{"x":674,"y":417,"decorName":"bush"},{"x":475,"y":419,"decorName":"bush"},{"x":274,"y":421,"decorName":"bush"},{"x":275,"y":226,"decorName":"bush"},{"x":475,"y":226,"decorName":"bush"},{"x":675,"y":228,"decorName":"bush"},{"x":74,"y":224,"decorName":"bush"},{"x":75,"y":421,"decorName":"bush"},{"x":874,"y":227,"decorName":"bush"},{"x":876,"y":418,"decorName":"bush"}]'))
        set_blocks(level54, json.loads('[{"type":"turn_left","number":2},{"type":"turn_right","number":1},{"type":"controls_repeat"}]'))
        return level54

    def level55():
        level55 = Level(
            name='55',
            default=True,
            path='[{"coordinate":[2,6],"connectedNodes":[18]},{"coordinate":[3,6],"connectedNodes":[2,19]},{"coordinate":[4,6],"connectedNodes":[1,3]},{"coordinate":[4,7],"connectedNodes":[4,2]},{"coordinate":[5,7],"connectedNodes":[3,5]},{"coordinate":[5,6],"connectedNodes":[4,6]},{"coordinate":[6,6],"connectedNodes":[5,7]},{"coordinate":[6,5],"connectedNodes":[6,8]},{"coordinate":[7,5],"connectedNodes":[7,9]},{"coordinate":[7,4],"connectedNodes":[10,8]},{"coordinate":[6,4],"connectedNodes":[9,11]},{"coordinate":[6,3],"connectedNodes":[12,10]},{"coordinate":[5,3],"connectedNodes":[11,13]},{"coordinate":[5,2],"connectedNodes":[14,12]},{"coordinate":[4,2],"connectedNodes":[15,13]},{"coordinate":[4,3],"connectedNodes":[16,14]},{"coordinate":[3,3],"connectedNodes":[17,15]},{"coordinate":[3,4],"connectedNodes":[20,16]},{"coordinate":[2,5],"connectedNodes":[0,19]},{"coordinate":[3,5],"connectedNodes":[18,1]},{"coordinate":[2,4],"connectedNodes":[17,21]},{"coordinate":[2,3],"connectedNodes":[20]}]',
            traffic_lights='[]',
            destinations='[[2,3]]',
            origin='{"coordinate":[2,6],"direction":"S"}',
            max_fuel=50,
            blocklyEnabled=True,
            pythonEnabled=False,
            theme=Theme.objects.get(id=1),
            character=Character.objects.get(id='1'),
            model_solution='[6]',
        )
        level55.save()
        set_decor(level55, json.loads('[{"x":81,"y":559,"decorName":"tree1"},{"x":715,"y":700,"decorName":"tree1"},{"x":772,"y":588,"decorName":"tree1"},{"x":7,"y":462,"decorName":"tree1"},{"x":83,"y":349,"decorName":"tree1"},{"x":535,"y":478,"decorName":"tree2"},{"x":211,"y":472,"decorName":"bush"},{"x":144,"y":473,"decorName":"bush"},{"x":430,"y":379,"decorName":"pond"}]'))
        set_blocks(level55, json.loads('[{"type":"turn_left","number":1},{"type":"turn_right","number":1},{"type":"controls_repeat_until"},{"type":"controls_if"},{"type":"at_destination"},{"type":"road_exists","number":1}]'))
        return level55

    def level56():
        level56 = Level(
            name='56',
            default=True,
            path='[{"coordinate":[1,6],"connectedNodes":[25]},{"coordinate":[3,5],"connectedNodes":[26,2]},{"coordinate":[4,5],"connectedNodes":[1,3]},{"coordinate":[4,6],"connectedNodes":[4,2]},{"coordinate":[4,7],"connectedNodes":[5,3]},{"coordinate":[5,7],"connectedNodes":[4,6]},{"coordinate":[6,7],"connectedNodes":[5,7]},{"coordinate":[7,7],"connectedNodes":[6,8]},{"coordinate":[7,6],"connectedNodes":[7,9]},{"coordinate":[7,5],"connectedNodes":[8,10]},{"coordinate":[7,4],"connectedNodes":[9,11]},{"coordinate":[7,3],"connectedNodes":[12,10]},{"coordinate":[6,3],"connectedNodes":[13,11]},{"coordinate":[5,3],"connectedNodes":[14,12]},{"coordinate":[4,3],"connectedNodes":[15,13]},{"coordinate":[3,3],"connectedNodes":[16,14]},{"coordinate":[2,3],"connectedNodes":[15,17]},{"coordinate":[2,2],"connectedNodes":[16,18]},{"coordinate":[2,1],"connectedNodes":[17,19]},{"coordinate":[3,1],"connectedNodes":[18,20]},{"coordinate":[4,1],"connectedNodes":[19,21]},{"coordinate":[5,1],"connectedNodes":[20,22]},{"coordinate":[6,1],"connectedNodes":[21,23]},{"coordinate":[7,1],"connectedNodes":[22,24]},{"coordinate":[7,2],"connectedNodes":[23]},{"coordinate":[2,6],"connectedNodes":[0,26]},{"coordinate":[2,5],"connectedNodes":[25,1]}]',
            traffic_lights='[]',
            destinations='[[7,2]]',
            origin='{"coordinate":[1,6],"direction":"E"}',
            max_fuel=50,
            blocklyEnabled=True,
            pythonEnabled=False,
            theme=Theme.objects.get(id=4),
            character=Character.objects.get(id='1'),
            model_solution='[8]',
        )
        level56.save()
        set_decor(level56, json.loads('[{"x":295,"y":200,"decorName":"tree2"},{"x":658,"y":654,"decorName":"bush"},{"x":657,"y":589,"decorName":"bush"},{"x":656,"y":523,"decorName":"bush"},{"x":655,"y":463,"decorName":"bush"},{"x":655,"y":401,"decorName":"bush"},{"x":497,"y":561,"decorName":"pond"},{"x":782,"y":408,"decorName":"tree1"},{"x":415,"y":190,"decorName":"bush"},{"x":492,"y":191,"decorName":"bush"},{"x":567,"y":192,"decorName":"bush"},{"x":645,"y":192,"decorName":"bush"}]'))
        set_blocks(level56, json.loads('[{"type":"move_forwards","number":1},{"type":"turn_left","number":1},{"type":"turn_right","number":1},{"type":"controls_repeat_until"},{"type":"controls_if"},{"type":"at_destination"},{"type":"road_exists","number":2}]'))
        return level56

    def level57():
        level57 = Level(
            name='57',
            default=True,
            path='[{"coordinate":[1,6],"connectedNodes":[1]},{"coordinate":[2,6],"connectedNodes":[0,2]},{"coordinate":[2,5],"connectedNodes":[1,3]},{"coordinate":[2,4],"connectedNodes":[2,4]},{"coordinate":[3,4],"connectedNodes":[3,5]},{"coordinate":[4,4],"connectedNodes":[4,6]},{"coordinate":[4,5],"connectedNodes":[7,5]},{"coordinate":[4,6],"connectedNodes":[8,6]},{"coordinate":[4,7],"connectedNodes":[9,7]},{"coordinate":[5,7],"connectedNodes":[8,10]},{"coordinate":[5,6],"connectedNodes":[9,11]},{"coordinate":[5,5],"connectedNodes":[10,12]},{"coordinate":[6,5],"connectedNodes":[11,13]},{"coordinate":[6,6],"connectedNodes":[14,12]},{"coordinate":[7,6],"connectedNodes":[13,15]},{"coordinate":[7,5],"connectedNodes":[14,16]},{"coordinate":[8,5],"connectedNodes":[15,17]},{"coordinate":[8,4],"connectedNodes":[18,16]},{"coordinate":[7,4],"connectedNodes":[17,19]},{"coordinate":[7,3],"connectedNodes":[20,18]},{"coordinate":[6,3],"connectedNodes":[21,19]},{"coordinate":[5,3],"connectedNodes":[20,22]},{"coordinate":[5,2],"connectedNodes":[23,21]},{"coordinate":[4,2],"connectedNodes":[24,22]},{"coordinate":[3,2],"connectedNodes":[23]}]',
            traffic_lights='[]',
            destinations='[[3,2]]',
            origin='{"coordinate":[1,6],"direction":"E"}',
            max_fuel=50,
            blocklyEnabled=True,
            pythonEnabled=False,
            theme=Theme.objects.get(id=3),
            character=Character.objects.get(id='1'),
            model_solution='[9]',
        )
        level57.save()
        set_decor(level57, json.loads('[{"x":287,"y":493,"decorName":"tree2"},{"x":646,"y":451,"decorName":"tree1"},{"x":31,"y":111,"decorName":"pond"},{"x":32,"y":300,"decorName":"pond"},{"x":32,"y":205,"decorName":"pond"},{"x":190,"y":298,"decorName":"pond"},{"x":346,"y":298,"decorName":"pond"},{"x":596,"y":698,"decorName":"tree1"},{"x":757,"y":676,"decorName":"tree1"},{"x":900,"y":426,"decorName":"tree1"},{"x":897,"y":700,"decorName":"tree1"},{"x":852,"y":556,"decorName":"tree1"},{"x":159,"y":458,"decorName":"bush"},{"x":158,"y":507,"decorName":"bush"},{"x":159,"y":561,"decorName":"bush"},{"x":500,"y":184,"decorName":"bush"},{"x":566,"y":185,"decorName":"bush"},{"x":436,"y":184,"decorName":"bush"}]'))
        set_blocks(level57, json.loads('[{"type":"move_forwards","number":1},{"type":"turn_left","number":1},{"type":"turn_right","number":1},{"type":"controls_repeat_while"},{"type":"controls_if"},{"type":"logic_negate","number":1},{"type":"at_destination","number":1},{"type":"road_exists","number":2}]'))
        return level57

    def level58():
        level58 = Level(
            name='58',
            default=True,
            path='[{"coordinate":[6,6],"connectedNodes":[1]},{"coordinate":[5,6],"connectedNodes":[2,0]},{"coordinate":[4,6],"connectedNodes":[3,1]},{"coordinate":[3,6],"connectedNodes":[4,2]},{"coordinate":[2,6],"connectedNodes":[5,3]},{"coordinate":[1,6],"connectedNodes":[4,6]},{"coordinate":[1,5],"connectedNodes":[5,7]},{"coordinate":[2,5],"connectedNodes":[6,8]},{"coordinate":[3,5],"connectedNodes":[7,9]},{"coordinate":[4,5],"connectedNodes":[8,10]},{"coordinate":[5,5],"connectedNodes":[9,11]},{"coordinate":[6,5],"connectedNodes":[10,12]},{"coordinate":[6,4],"connectedNodes":[13,11]},{"coordinate":[5,4],"connectedNodes":[14,12]},{"coordinate":[4,4],"connectedNodes":[15,13]},{"coordinate":[3,4],"connectedNodes":[16,14]},{"coordinate":[2,4],"connectedNodes":[17,15]},{"coordinate":[1,4],"connectedNodes":[16,18]},{"coordinate":[1,3],"connectedNodes":[17,19]},{"coordinate":[2,3],"connectedNodes":[18,20]},{"coordinate":[3,3],"connectedNodes":[19,21]},{"coordinate":[4,3],"connectedNodes":[20,22]},{"coordinate":[5,3],"connectedNodes":[21,23]},{"coordinate":[6,3],"connectedNodes":[22,24]},{"coordinate":[6,2],"connectedNodes":[25,23]},{"coordinate":[5,2],"connectedNodes":[24]}]',
            traffic_lights='[]',
            destinations='[[5,2]]',
            origin='{"coordinate":[6,6],"direction":"W"}',
            max_fuel=50,
            blocklyEnabled=True,
            pythonEnabled=False,
            theme=Theme.objects.get(id=2),
            character=Character.objects.get(id='1'),
            model_solution='[11]',
        )
        level58.save()
        set_decor(level58, json.loads('[{"x":795,"y":680,"decorName":"tree1"},{"x":797,"y":527,"decorName":"tree1"},{"x":799,"y":365,"decorName":"tree1"},{"x":800,"y":187,"decorName":"tree1"},{"x":311,"y":74,"decorName":"pond"},{"x":171,"y":701,"decorName":"bush"},{"x":270,"y":701,"decorName":"bush"},{"x":369,"y":699,"decorName":"bush"},{"x":461,"y":699,"decorName":"bush"},{"x":551,"y":698,"decorName":"bush"},{"x":82,"y":254,"decorName":"bush"},{"x":177,"y":254,"decorName":"bush"},{"x":371,"y":254,"decorName":"bush"},{"x":275,"y":255,"decorName":"bush"},{"x":450,"y":251,"decorName":"bush"},{"x":799,"y":31,"decorName":"tree1"},{"x":74,"y":699,"decorName":"bush"}]'))
        set_blocks(level58, json.loads('[{"type":"move_forwards","number":2},{"type":"turn_left","number":1},{"type":"turn_right","number":1},{"type":"controls_repeat","number":4},{"type":"controls_repeat_while"},{"type":"logic_negate","number":1},{"type":"at_destination","number":1}]'))
        return level58

    def level61():
        level61 = Level(
            name='61',
            default=True,
            path='[{"coordinate":[0,5],"connectedNodes":[1]},{"coordinate":[1,5],"connectedNodes":[0,2]},{"coordinate":[2,5],"connectedNodes":[1,3]},{"coordinate":[2,6],"connectedNodes":[4,2]},{"coordinate":[3,6],"connectedNodes":[3,5]},{"coordinate":[3,5],"connectedNodes":[4,6]},{"coordinate":[4,5],"connectedNodes":[5,7]},{"coordinate":[5,5],"connectedNodes":[6,8]},{"coordinate":[6,5],"connectedNodes":[7,9]},{"coordinate":[6,6],"connectedNodes":[10,8]},{"coordinate":[7,6],"connectedNodes":[9,11]},{"coordinate":[7,5],"connectedNodes":[10,12]},{"coordinate":[8,5],"connectedNodes":[11]}]',
            traffic_lights='[]',
            destinations='[[8,5]]',
            origin='{"coordinate":[0,5],"direction":"E"}',
            max_fuel=50,
            blocklyEnabled=True,
            pythonEnabled=False,
            theme=Theme.objects.get(id=1),
            character=Character.objects.get(id='1'),
            model_solution='[8]',
        )
        level61.save()
        set_decor(level61, json.loads('[{"x":853,"y":70,"decorName":"tree2"},{"x":783,"y":250,"decorName":"tree2"},{"x":461,"y":115,"decorName":"tree2"},{"x":675,"y":25,"decorName":"tree2"},{"x":739,"y":0,"decorName":"tree2"},{"x":530,"y":67,"decorName":"tree1"},{"x":655,"y":127,"decorName":"tree1"},{"x":433,"y":16,"decorName":"tree1"},{"x":749,"y":93,"decorName":"tree1"},{"x":156,"y":64,"decorName":"tree1"},{"x":877,"y":182,"decorName":"tree1"},{"x":45,"y":125,"decorName":"tree1"},{"x":547,"y":182,"decorName":"tree2"},{"x":322,"y":56,"decorName":"tree2"},{"x":607,"y":0,"decorName":"tree2"},{"x":214,"y":3,"decorName":"tree2"},{"x":59,"y":24,"decorName":"tree2"},{"x":665,"y":245,"decorName":"tree1"},{"x":242,"y":150,"decorName":"tree1"},{"x":98,"y":451,"decorName":"bush"},{"x":598,"y":451,"decorName":"bush"},{"x":498,"y":451,"decorName":"bush"},{"x":397,"y":451,"decorName":"bush"},{"x":296,"y":452,"decorName":"bush"},{"x":197,"y":452,"decorName":"bush"},{"x":698,"y":451,"decorName":"bush"}]'))
        set_blocks(level61, json.loads('[{"type":"move_forwards"},{"type":"turn_left"},{"type":"turn_right"},{"type":"controls_repeat"},{"type":"call_proc"},{"type":"declare_proc"}]'))
        return level61

    def level64():
        level64 = Level(
            name='64',
            default=True,
            path='[{"coordinate":[1,4],"connectedNodes":[1]},{"coordinate":[2,4],"connectedNodes":[0,2]},{"coordinate":[2,5],"connectedNodes":[3,1]},{"coordinate":[3,5],"connectedNodes":[2,4]},{"coordinate":[4,5],"connectedNodes":[3,5]},{"coordinate":[4,4],"connectedNodes":[4,6]},{"coordinate":[5,4],"connectedNodes":[5,7]},{"coordinate":[6,4],"connectedNodes":[6,8]},{"coordinate":[6,5],"connectedNodes":[9,7]},{"coordinate":[7,5],"connectedNodes":[8,10]},{"coordinate":[8,5],"connectedNodes":[9,11]},{"coordinate":[8,4],"connectedNodes":[10,12]},{"coordinate":[9,4],"connectedNodes":[11,13]},{"coordinate":[9,3],"connectedNodes":[12,14]},{"coordinate":[9,2],"connectedNodes":[15,13]},{"coordinate":[8,2],"connectedNodes":[16,14]},{"coordinate":[7,2],"connectedNodes":[17,15]},{"coordinate":[7,3],"connectedNodes":[18,16]},{"coordinate":[6,3],"connectedNodes":[17,19]},{"coordinate":[6,2],"connectedNodes":[20,18]},{"coordinate":[5,2],"connectedNodes":[19,21]},{"coordinate":[5,1],"connectedNodes":[22,20]},{"coordinate":[4,1],"connectedNodes":[23,21]},{"coordinate":[3,1],"connectedNodes":[24,22]},{"coordinate":[3,2],"connectedNodes":[25,23]},{"coordinate":[2,2],"connectedNodes":[26,24]},{"coordinate":[2,3],"connectedNodes":[27,25]},{"coordinate":[1,3],"connectedNodes":[26,28]},{"coordinate":[1,2],"connectedNodes":[29,27]},{"coordinate":[0,2],"connectedNodes":[28]}]',
            traffic_lights='[]',
            destinations='[[0,2]]',
            origin='{"coordinate":[1,4],"direction":"E"}',
            max_fuel=50,
            blocklyEnabled=True,
            pythonEnabled=False,
            theme=Theme.objects.get(id=3),
            character=Character.objects.get(id='6'),
            model_solution='[20]',
        )
        level64.save()
        set_decor(level64, json.loads('[{"x":291,"y":295,"decorName":"pond"},{"x":452,"y":295,"decorName":"pond"},{"x":630,"y":108,"decorName":"tree1"},{"x":501,"y":498,"decorName":"tree1"},{"x":95,"y":500,"decorName":"tree1"},{"x":702,"y":408,"decorName":"tree1"},{"x":313,"y":415,"decorName":"tree2"},{"x":814,"y":302,"decorName":"tree2"},{"x":896,"y":494,"decorName":"tree1"},{"x":151,"y":106,"decorName":"tree1"},{"x":426,"y":237,"decorName":"bush"},{"x":456,"y":203,"decorName":"bush"},{"x":396,"y":204,"decorName":"bush"},{"x":41,"y":614,"decorName":"tree1"},{"x":219,"y":607,"decorName":"tree1"},{"x":532,"y":607,"decorName":"tree1"},{"x":366,"y":655,"decorName":"tree1"},{"x":900,"y":657,"decorName":"tree1"},{"x":671,"y":668,"decorName":"tree1"}]'))
        set_blocks(level64, json.loads('[{"type":"move_forwards"},{"type":"turn_left"},{"type":"turn_right"},{"type":"controls_repeat"},{"type":"call_proc"},{"type":"declare_proc"}]'))
        return level64

    def level66():
        level66 = Level(
            name='66',
            default=True,
            path='[{"coordinate":[1,5],"connectedNodes":[1]},{"coordinate":[2,5],"connectedNodes":[0,2]},{"coordinate":[3,5],"connectedNodes":[1,3]},{"coordinate":[4,5],"connectedNodes":[2,4]},{"coordinate":[4,4],"connectedNodes":[3,5]},{"coordinate":[5,4],"connectedNodes":[4,6]},{"coordinate":[6,4],"connectedNodes":[5,7]},{"coordinate":[7,4],"connectedNodes":[6,8]},{"coordinate":[8,4],"connectedNodes":[7,9]},{"coordinate":[8,3],"connectedNodes":[8,10]},{"coordinate":[8,2],"connectedNodes":[9,11]},{"coordinate":[8,1],"connectedNodes":[12,10]},{"coordinate":[7,1],"connectedNodes":[13,11]},{"coordinate":[6,1],"connectedNodes":[14,12]},{"coordinate":[5,1],"connectedNodes":[15,13]},{"coordinate":[4,1],"connectedNodes":[16,14]},{"coordinate":[4,2],"connectedNodes":[17,15]},{"coordinate":[3,2],"connectedNodes":[18,16]},{"coordinate":[2,2],"connectedNodes":[19,17]},{"coordinate":[1,2],"connectedNodes":[20,18]},{"coordinate":[1,3],"connectedNodes":[19]}]',
            traffic_lights='[]',
            destinations='[[1,3]]',
            origin='{"coordinate":[1,5],"direction":"E"}',
            max_fuel=50,
            blocklyEnabled=True,
            pythonEnabled=False,
            theme=Theme.objects.get(id=2),
            character=Character.objects.get(id='2'),
            model_solution='[14]',
        )
        level66.save()
        set_decor(level66, json.loads('[{"x":900,"y":305,"decorName":"tree2"},{"x":712,"y":700,"decorName":"tree2"},{"x":850,"y":514,"decorName":"tree2"},{"x":736,"y":605,"decorName":"tree2"},{"x":874,"y":700,"decorName":"tree2"},{"x":608,"y":700,"decorName":"tree2"},{"x":382,"y":688,"decorName":"tree2"},{"x":900,"y":597,"decorName":"tree1"},{"x":508,"y":700,"decorName":"tree1"},{"x":587,"y":578,"decorName":"tree1"},{"x":795,"y":666,"decorName":"tree1"},{"x":496,"y":202,"decorName":"bush"},{"x":460,"y":298,"decorName":"bush"},{"x":379,"y":298,"decorName":"bush"},{"x":300,"y":297,"decorName":"bush"},{"x":217,"y":297,"decorName":"bush"},{"x":740,"y":202,"decorName":"bush"},{"x":661,"y":201,"decorName":"bush"},{"x":579,"y":201,"decorName":"bush"}]'))
        set_blocks(level66, json.loads('[{"type":"move_forwards"},{"type":"turn_left"},{"type":"turn_right"},{"type":"controls_repeat"},{"type":"call_proc"},{"type":"declare_proc"}]'))
        return level66

    def level72():
        level72 = Level(
            name='72',
            default=True,
            path='[{"coordinate":[1,5],"connectedNodes":[1]},{"coordinate":[2,5],"connectedNodes":[0,2]},{"coordinate":[3,5],"connectedNodes":[1,3]},{"coordinate":[4,5],"connectedNodes":[2,17,4]},{"coordinate":[5,5],"connectedNodes":[3,5]},{"coordinate":[6,5],"connectedNodes":[4,28,19,6]},{"coordinate":[6,4],"connectedNodes":[5,7]},{"coordinate":[6,3],"connectedNodes":[6,8]},{"coordinate":[6,2],"connectedNodes":[7,9]},{"coordinate":[6,1],"connectedNodes":[10,8,25]},{"coordinate":[5,1],"connectedNodes":[11,9]},{"coordinate":[4,1],"connectedNodes":[12,10]},{"coordinate":[3,1],"connectedNodes":[13,11]},{"coordinate":[2,1],"connectedNodes":[14,12]},{"coordinate":[1,1],"connectedNodes":[29,15,13]},{"coordinate":[1,2],"connectedNodes":[35,16,14]},{"coordinate":[2,2],"connectedNodes":[15]},{"coordinate":[4,6],"connectedNodes":[18,3]},{"coordinate":[4,7],"connectedNodes":[26,17]},{"coordinate":[7,5],"connectedNodes":[5,20]},{"coordinate":[8,5],"connectedNodes":[19,21]},{"coordinate":[8,4],"connectedNodes":[20,22]},{"coordinate":[8,3],"connectedNodes":[21,23]},{"coordinate":[8,2],"connectedNodes":[22,24]},{"coordinate":[8,1],"connectedNodes":[25,23]},{"coordinate":[7,1],"connectedNodes":[9,24]},{"coordinate":[5,7],"connectedNodes":[18,27]},{"coordinate":[6,7],"connectedNodes":[26,28]},{"coordinate":[6,6],"connectedNodes":[27,5]},{"coordinate":[0,1],"connectedNodes":[14,30]},{"coordinate":[0,0],"connectedNodes":[29,31]},{"coordinate":[1,0],"connectedNodes":[30,32]},{"coordinate":[2,0],"connectedNodes":[31,33]},{"coordinate":[3,0],"connectedNodes":[32,34]},{"coordinate":[4,0],"connectedNodes":[33]},{"coordinate":[1,3],"connectedNodes":[36,15]},{"coordinate":[2,3],"connectedNodes":[35,37]},{"coordinate":[3,3],"connectedNodes":[36,38]},{"coordinate":[4,3],"connectedNodes":[37,39]},{"coordinate":[5,3],"connectedNodes":[38]}]',
            traffic_lights='[]',
            destinations='[[2,2]]',
            origin='{"coordinate":[1,5],"direction":"E"}',
            max_fuel=14,
            blocklyEnabled=True,
            pythonEnabled=False,
            theme=Theme.objects.get(id=1),
            character=Character.objects.get(id='5'),
            model_solution='[6]',
        )
        level72.save()
        set_decor(level72, json.loads('[{"x":704,"y":391,"decorName":"tree2"},{"x":688,"y":590,"decorName":"pond"},{"x":701,"y":287,"decorName":"tree2"},{"x":718,"y":184,"decorName":"tree2"},{"x":400,"y":200,"decorName":"bush"},{"x":399,"y":255,"decorName":"bush"}]'))
        set_blocks(level72, json.loads('[{"type":"move_forwards","number":1},{"type":"turn_left","number":1},{"type":"turn_right","number":1},{"type":"turn_around","number":2},{"type":"controls_repeat_until","number":2},{"type":"at_destination"},{"type":"road_exists"}]'))
        return level72

    def level73():
        level73 = Level(
            name='73',
            default=True,
            path='[{"coordinate":[8,1],"connectedNodes":[47]},{"coordinate":[5,5],"connectedNodes":[2,12]},{"coordinate":[4,5],"connectedNodes":[3,1,48]},{"coordinate":[3,5],"connectedNodes":[2,4]},{"coordinate":[3,4],"connectedNodes":[3,5]},{"coordinate":[3,3],"connectedNodes":[4,6]},{"coordinate":[4,3],"connectedNodes":[5,7,21]},{"coordinate":[5,3],"connectedNodes":[6,8]},{"coordinate":[6,3],"connectedNodes":[7,9]},{"coordinate":[6,4],"connectedNodes":[10,8]},{"coordinate":[6,5],"connectedNodes":[11,9]},{"coordinate":[6,6],"connectedNodes":[12,10]},{"coordinate":[5,6],"connectedNodes":[13,11,1]},{"coordinate":[4,6],"connectedNodes":[14,12]},{"coordinate":[3,6],"connectedNodes":[15,13]},{"coordinate":[2,6],"connectedNodes":[14,16]},{"coordinate":[2,5],"connectedNodes":[15,17]},{"coordinate":[2,4],"connectedNodes":[16,18]},{"coordinate":[2,3],"connectedNodes":[39,17,19]},{"coordinate":[2,2],"connectedNodes":[18,20]},{"coordinate":[3,2],"connectedNodes":[19,21]},{"coordinate":[4,2],"connectedNodes":[20,6,22]},{"coordinate":[5,2],"connectedNodes":[21,23]},{"coordinate":[6,2],"connectedNodes":[22,24]},{"coordinate":[7,2],"connectedNodes":[23,25]},{"coordinate":[7,3],"connectedNodes":[26,24]},{"coordinate":[7,4],"connectedNodes":[27,25]},{"coordinate":[7,5],"connectedNodes":[28,26]},{"coordinate":[7,6],"connectedNodes":[29,27]},{"coordinate":[7,7],"connectedNodes":[30,28]},{"coordinate":[6,7],"connectedNodes":[31,29]},{"coordinate":[5,7],"connectedNodes":[32,30]},{"coordinate":[4,7],"connectedNodes":[33,31]},{"coordinate":[3,7],"connectedNodes":[34,32]},{"coordinate":[2,7],"connectedNodes":[35,33]},{"coordinate":[1,7],"connectedNodes":[34,36]},{"coordinate":[1,6],"connectedNodes":[35,37]},{"coordinate":[1,5],"connectedNodes":[36,38]},{"coordinate":[1,4],"connectedNodes":[37,39]},{"coordinate":[1,3],"connectedNodes":[38,18,40]},{"coordinate":[1,2],"connectedNodes":[39,41]},{"coordinate":[1,1],"connectedNodes":[40,42]},{"coordinate":[2,1],"connectedNodes":[41,43]},{"coordinate":[3,1],"connectedNodes":[42,44]},{"coordinate":[4,1],"connectedNodes":[43,45]},{"coordinate":[5,1],"connectedNodes":[44,46]},{"coordinate":[6,1],"connectedNodes":[45,47]},{"coordinate":[7,1],"connectedNodes":[46,0]},{"coordinate":[4,4],"connectedNodes":[2,49]},{"coordinate":[5,4],"connectedNodes":[48]}]',
            traffic_lights='[]',
            destinations='[[5,4]]',
            origin='{"coordinate":[8,1],"direction":"W"}',
            max_fuel=50,
            blocklyEnabled=True,
            pythonEnabled=False,
            theme=Theme.objects.get(id=3),
            character=Character.objects.get(id='4'),
            model_solution='[14]'

        )
        level73.save()
        set_decor(level73, json.loads('[{"x":4,"y":692,"decorName":"tree1"},{"x":5,"y":78,"decorName":"tree1"},{"x":2,"y":222,"decorName":"tree1"},{"x":5,"y":392,"decorName":"tree1"},{"x":8,"y":554,"decorName":"tree1"},{"x":802,"y":648,"decorName":"tree2"},{"x":796,"y":533,"decorName":"pond"},{"x":896,"y":351,"decorName":"bush"},{"x":842,"y":351,"decorName":"bush"},{"x":788,"y":352,"decorName":"bush"},{"x":950,"y":352,"decorName":"bush"},{"x":924,"y":385,"decorName":"bush"},{"x":869,"y":384,"decorName":"bush"},{"x":815,"y":383,"decorName":"bush"},{"x":895,"y":417,"decorName":"bush"},{"x":839,"y":415,"decorName":"bush"},{"x":863,"y":448,"decorName":"bush"}]'))
        set_blocks(level73, json.loads('[{"type":"move_forwards","number":1},{"type":"turn_left","number":1},{"type":"turn_right","number":1},{"type":"controls_repeat","number":1},{"type":"controls_repeat_until"},{"type":"logic_negate"},{"type":"road_exists"},{"type":"dead_end"}]'))
        return level73

    def level74():
        level74 = Level(
            name='74',
            default=True,
            path='[{"coordinate":[9,2],"connectedNodes":[1]},{"coordinate":[8,2],"connectedNodes":[2,18,0]},{"coordinate":[7,2],"connectedNodes":[1,3]},{"coordinate":[7,1],"connectedNodes":[4,2]},{"coordinate":[6,1],"connectedNodes":[5,3,6]},{"coordinate":[5,1],"connectedNodes":[16,7,4]},{"coordinate":[6,0],"connectedNodes":[4]},{"coordinate":[5,2],"connectedNodes":[8,10,5]},{"coordinate":[4,2],"connectedNodes":[15,9,7,16]},{"coordinate":[4,3],"connectedNodes":[12,10,8]},{"coordinate":[5,3],"connectedNodes":[9,11,7]},{"coordinate":[5,4],"connectedNodes":[12,10]},{"coordinate":[4,4],"connectedNodes":[13,11,9]},{"coordinate":[3,4],"connectedNodes":[42,12,14]},{"coordinate":[3,3],"connectedNodes":[13,15]},{"coordinate":[3,2],"connectedNodes":[37,14,8]},{"coordinate":[4,1],"connectedNodes":[8,5,17]},{"coordinate":[4,0],"connectedNodes":[16]},{"coordinate":[8,3],"connectedNodes":[19,1]},{"coordinate":[8,4],"connectedNodes":[20,18]},{"coordinate":[8,5],"connectedNodes":[21,43,19]},{"coordinate":[8,6],"connectedNodes":[22,20]},{"coordinate":[7,6],"connectedNodes":[23,21]},{"coordinate":[6,6],"connectedNodes":[24,22]},{"coordinate":[5,6],"connectedNodes":[25,23,38]},{"coordinate":[4,6],"connectedNodes":[26,24]},{"coordinate":[3,6],"connectedNodes":[27,25]},{"coordinate":[2,6],"connectedNodes":[28,39,26]},{"coordinate":[1,6],"connectedNodes":[29,27]},{"coordinate":[0,6],"connectedNodes":[28,30]},{"coordinate":[0,5],"connectedNodes":[29,31]},{"coordinate":[0,4],"connectedNodes":[30,40,32]},{"coordinate":[0,3],"connectedNodes":[31,33]},{"coordinate":[0,2],"connectedNodes":[32,34]},{"coordinate":[0,1],"connectedNodes":[33,35]},{"coordinate":[1,1],"connectedNodes":[34,36,41]},{"coordinate":[2,1],"connectedNodes":[35,37]},{"coordinate":[2,2],"connectedNodes":[15,36]},{"coordinate":[5,5],"connectedNodes":[24]},{"coordinate":[2,7],"connectedNodes":[27]},{"coordinate":[1,4],"connectedNodes":[31]},{"coordinate":[1,0],"connectedNodes":[35]},{"coordinate":[3,5],"connectedNodes":[13]},{"coordinate":[9,5],"connectedNodes":[20]}]',
            traffic_lights='[]',
            destinations='[[4,0]]',
            origin='{"coordinate":[9,2],"direction":"W"}',
            max_fuel=50,
            blocklyEnabled=True,
            pythonEnabled=False,
            theme=Theme.objects.get(id=2),
            character=Character.objects.get(id='1'),
            model_solution='[10]',
        )
        level74.save()
        set_decor(level74, json.loads('[{"x":738,"y":33,"decorName":"tree1"},{"x":397,"y":495,"decorName":"tree2"},{"x":248,"y":39,"decorName":"pond"},{"x":94,"y":498,"decorName":"bush"},{"x":148,"y":558,"decorName":"bush"},{"x":96,"y":558,"decorName":"bush"}]'))
        set_blocks(level74, json.loads('[{"type":"move_forwards","number":1},{"type":"turn_left","number":3},{"type":"turn_right","number":1},{"type":"turn_around","number":2},{"type":"controls_repeat","number":1},{"type":"call_proc"},{"type":"declare_proc"}]'))
        return level74

    def level75():
        level75 = Level(
            name='75',
            default=True,
            path='[{"coordinate":[1,6],"connectedNodes":[18]},{"coordinate":[2,5],"connectedNodes":[18,2]},{"coordinate":[2,6],"connectedNodes":[3,1]},{"coordinate":[3,6],"connectedNodes":[2,4]},{"coordinate":[3,5],"connectedNodes":[3,5]},{"coordinate":[3,4],"connectedNodes":[4,6]},{"coordinate":[3,3],"connectedNodes":[5,7]},{"coordinate":[3,2],"connectedNodes":[6,8]},{"coordinate":[4,2],"connectedNodes":[7,9]},{"coordinate":[4,3],"connectedNodes":[10,8]},{"coordinate":[4,4],"connectedNodes":[11,9]},{"coordinate":[4,5],"connectedNodes":[12,10]},{"coordinate":[4,6],"connectedNodes":[13,11]},{"coordinate":[5,6],"connectedNodes":[12,14]},{"coordinate":[5,5],"connectedNodes":[13,15]},{"coordinate":[5,4],"connectedNodes":[14,16]},{"coordinate":[5,3],"connectedNodes":[15,17]},{"coordinate":[5,2],"connectedNodes":[16]},{"coordinate":[1,5],"connectedNodes":[0,1]}]',
            traffic_lights='[{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":3,"y":4},"direction":"S","startTime":0,"startingState":"GREEN"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":4,"y":4},"direction":"N","startTime":0,"startingState":"RED"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":5,"y":5},"direction":"S","startTime":0,"startingState":"RED"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":3,"y":5},"direction":"S","startTime":0,"startingState":"RED"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":5,"y":4},"direction":"S","startTime":0,"startingState":"GREEN"}]',
            destinations='[[5,2]]',
            origin='{"coordinate":[1,6],"direction":"S"}',
            max_fuel=50,
            blocklyEnabled=True,
            pythonEnabled=False,
            theme=Theme.objects.get(id=2),
            character=Character.objects.get(id='1'),
            model_solution='[26]',
        )
        level75.save()
        set_decor(level75, json.loads('[{"x":259,"y":477,"decorName":"bush"},{"x":258,"y":416,"decorName":"bush"},{"x":258,"y":352,"decorName":"bush"},{"x":258,"y":282,"decorName":"bush"},{"x":777,"y":507,"decorName":"tree1"},{"x":413,"y":686,"decorName":"tree1"},{"x":859,"y":220,"decorName":"tree1"},{"x":639,"y":700,"decorName":"tree1"},{"x":699,"y":298,"decorName":"tree1"},{"x":900,"y":378,"decorName":"tree2"},{"x":736,"y":700,"decorName":"tree2"},{"x":900,"y":695,"decorName":"tree2"},{"x":728,"y":628,"decorName":"tree1"},{"x":884,"y":577,"decorName":"tree2"},{"x":834,"y":655,"decorName":"tree1"},{"x":900,"y":502,"decorName":"tree1"},{"x":658,"y":525,"decorName":"tree2"},{"x":793,"y":399,"decorName":"tree2"}]'))
        set_blocks(level75, json.loads('[{"type":"move_forwards","number":1},{"type":"turn_left","number":1},{"type":"turn_right","number":1},{"type":"wait","number":1},{"type":"controls_repeat_until"},{"type":"controls_if"},{"type":"road_exists"},{"type":"dead_end"},{"type":"traffic_light"},{"type":"call_proc"},{"type":"declare_proc"}]'))
        return level75

    def level79():
        level79 = Level(
            name='79',
            default=True,
            path='[{"coordinate":[9,0],"connectedNodes":[76]},{"coordinate":[2,5],"connectedNodes":[77,2]},{"coordinate":[2,4],"connectedNodes":[1,5]},{"coordinate":[1,4],"connectedNodes":[15,4]},{"coordinate":[1,3],"connectedNodes":[3,5]},{"coordinate":[2,3],"connectedNodes":[4,2,6]},{"coordinate":[3,3],"connectedNodes":[5,7]},{"coordinate":[3,4],"connectedNodes":[8,6]},{"coordinate":[3,5],"connectedNodes":[10,22,7]},{"coordinate":[2,6],"connectedNodes":[11,10]},{"coordinate":[3,6],"connectedNodes":[9,8]},{"coordinate":[1,6],"connectedNodes":[12,9]},{"coordinate":[1,7],"connectedNodes":[13,18,11]},{"coordinate":[0,7],"connectedNodes":[12,14]},{"coordinate":[0,6],"connectedNodes":[13,17]},{"coordinate":[0,4],"connectedNodes":[3,16]},{"coordinate":[0,3],"connectedNodes":[15,73]},{"coordinate":[0,5],"connectedNodes":[14,77]},{"coordinate":[2,7],"connectedNodes":[12,19]},{"coordinate":[3,7],"connectedNodes":[18,20]},{"coordinate":[4,7],"connectedNodes":[19,21]},{"coordinate":[4,6],"connectedNodes":[20,24]},{"coordinate":[4,5],"connectedNodes":[8,23]},{"coordinate":[5,5],"connectedNodes":[22,28,43]},{"coordinate":[5,6],"connectedNodes":[21,25]},{"coordinate":[5,7],"connectedNodes":[26,24]},{"coordinate":[6,7],"connectedNodes":[25,27]},{"coordinate":[6,6],"connectedNodes":[26,30]},{"coordinate":[6,5],"connectedNodes":[23,29]},{"coordinate":[6,4],"connectedNodes":[28,39]},{"coordinate":[7,6],"connectedNodes":[27,31]},{"coordinate":[8,6],"connectedNodes":[30,35]},{"coordinate":[8,7],"connectedNodes":[33,34]},{"coordinate":[7,7],"connectedNodes":[32]},{"coordinate":[9,7],"connectedNodes":[32,35]},{"coordinate":[9,6],"connectedNodes":[31,34,36]},{"coordinate":[9,5],"connectedNodes":[35,37]},{"coordinate":[9,4],"connectedNodes":[38,36,49]},{"coordinate":[8,4],"connectedNodes":[39,41,37]},{"coordinate":[7,4],"connectedNodes":[29,38]},{"coordinate":[7,5],"connectedNodes":[41]},{"coordinate":[8,5],"connectedNodes":[40,38]},{"coordinate":[4,4],"connectedNodes":[43,45]},{"coordinate":[5,4],"connectedNodes":[42,23]},{"coordinate":[5,3],"connectedNodes":[45,46,54]},{"coordinate":[4,3],"connectedNodes":[42,44]},{"coordinate":[6,3],"connectedNodes":[44,47,53]},{"coordinate":[7,3],"connectedNodes":[46,48]},{"coordinate":[8,3],"connectedNodes":[47,49]},{"coordinate":[9,3],"connectedNodes":[48,37,50]},{"coordinate":[9,2],"connectedNodes":[51,49,76]},{"coordinate":[8,2],"connectedNodes":[50]},{"coordinate":[7,2],"connectedNodes":[53]},{"coordinate":[6,2],"connectedNodes":[46,52]},{"coordinate":[5,2],"connectedNodes":[55,44]},{"coordinate":[4,2],"connectedNodes":[54]},{"coordinate":[3,2],"connectedNodes":[69,57]},{"coordinate":[3,1],"connectedNodes":[56,58]},{"coordinate":[4,1],"connectedNodes":[57,59]},{"coordinate":[5,1],"connectedNodes":[58,60]},{"coordinate":[6,1],"connectedNodes":[59,63]},{"coordinate":[7,1],"connectedNodes":[78,62]},{"coordinate":[7,0],"connectedNodes":[63,61]},{"coordinate":[6,0],"connectedNodes":[64,60,62]},{"coordinate":[5,0],"connectedNodes":[65,63]},{"coordinate":[4,0],"connectedNodes":[66,64]},{"coordinate":[3,0],"connectedNodes":[68,65]},{"coordinate":[2,1],"connectedNodes":[68]},{"coordinate":[2,0],"connectedNodes":[75,67,66]},{"coordinate":[2,2],"connectedNodes":[70,56]},{"coordinate":[1,2],"connectedNodes":[73,69,71]},{"coordinate":[1,1],"connectedNodes":[72,70]},{"coordinate":[0,1],"connectedNodes":[71,74]},{"coordinate":[0,2],"connectedNodes":[16,70]},{"coordinate":[0,0],"connectedNodes":[72,75]},{"coordinate":[1,0],"connectedNodes":[74,68]},{"coordinate":[9,1],"connectedNodes":[50,0]},{"coordinate":[1,5],"connectedNodes":[17,1]},{"coordinate":[8,1],"connectedNodes":[61,79]},{"coordinate":[8,0],"connectedNodes":[78]}]',
            traffic_lights='[]',
            destinations='[[8,0]]',
            origin='{"coordinate":[9,0],"direction":"N"}',
            max_fuel=50,
            blocklyEnabled=True,
            pythonEnabled=False,
            theme=Theme.objects.get(id=1),
            character=Character.objects.get(id='2'),
            model_solution='[55]',
        )
        level79.save()
        set_decor(level79, json.loads('[]'))
        set_blocks(level79, json.loads('[{"type":"move_forwards","number":7},{"type":"turn_left","number":4},{"type":"turn_right","number":1},{"type":"controls_if"},{"type":"logic_negate"},{"type":"road_exists"},{"type":"call_proc"},{"type":"declare_proc","number":1}]'))
        return level79

    def level80():
        level80 = Level(
            name='80',
            default=True,
            path='[{"coordinate":[1,3],"connectedNodes":[1]},{"coordinate":[2,3],"connectedNodes":[0,2]},{"coordinate":[3,3],"connectedNodes":[1,3]},{"coordinate":[3,4],"connectedNodes":[4,2]},{"coordinate":[3,5],"connectedNodes":[5,3]},{"coordinate":[4,5],"connectedNodes":[4,6]},{"coordinate":[5,5],"connectedNodes":[5]}]',
            traffic_lights='[]',
            destinations='[[5,5]]',
            origin='{"coordinate":[1,3],"direction":"E"}',
            max_fuel=50,
            blocklyEnabled=True,
            pythonEnabled=True,
            theme=Theme.objects.get(id=3),
            character=Character.objects.get(id='1'),
        )
        level80.save()
        set_decor(level80, json.loads('[{"x":436,"y":374,"decorName":"pond"},{"x":437,"y":283,"decorName":"pond"},{"x":872,"y":331,"decorName":"tree1"},{"x":720,"y":193,"decorName":"tree1"},{"x":81,"y":623,"decorName":"tree1"},{"x":190,"y":669,"decorName":"tree1"},{"x":25,"y":521,"decorName":"tree1"},{"x":442,"y":590,"decorName":"bush"},{"x":375,"y":591,"decorName":"bush"},{"x":410,"y":628,"decorName":"bush"},{"x":723,"y":73,"decorName":"tree1"},{"x":603,"y":17,"decorName":"tree1"},{"x":862,"y":169,"decorName":"tree1"},{"x":830,"y":14,"decorName":"tree1"},{"x":0,"y":697,"decorName":"tree1"}]'))
        set_blocks(level80, json.loads('[{"type":"move_forwards"},{"type":"turn_left"},{"type":"turn_right"}]'))
        return level80

    def level84():
        level84 = Level(
            name='84',
            default=True,
            path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[1,4],"connectedNodes":[3,1]},{"coordinate":[2,4],"connectedNodes":[2,4]},{"coordinate":[2,3],"connectedNodes":[3,5]},{"coordinate":[3,3],"connectedNodes":[4,6]},{"coordinate":[3,4],"connectedNodes":[7,5]},{"coordinate":[4,4],"connectedNodes":[6,8]},{"coordinate":[4,3],"connectedNodes":[7,9]},{"coordinate":[5,3],"connectedNodes":[8,10]},{"coordinate":[5,4],"connectedNodes":[11,9]},{"coordinate":[6,4],"connectedNodes":[10,12]},{"coordinate":[6,3],"connectedNodes":[11,13]},{"coordinate":[7,3],"connectedNodes":[12,14]},{"coordinate":[7,4],"connectedNodes":[15,13]},{"coordinate":[8,4],"connectedNodes":[14,16]},{"coordinate":[8,3],"connectedNodes":[15,17]},{"coordinate":[9,3],"connectedNodes":[16]}]',
            traffic_lights='[]',
            destinations='[[9,3]]',
            origin='{"coordinate":[0,3],"direction":"E"}',
            max_fuel=50,
            blocklyEnabled=True,
            pythonEnabled=True,
            theme=Theme.objects.get(id=2),
            character=Character.objects.get(id='1'),
        )
        level84.save()
        set_decor(level84, json.loads('[{"x":156,"y":584,"decorName":"tree1"},{"x":181,"y":169,"decorName":"tree2"},{"x":750,"y":225,"decorName":"tree1"},{"x":311,"y":615,"decorName":"tree2"},{"x":225,"y":509,"decorName":"pond"},{"x":37,"y":483,"decorName":"tree2"},{"x":472,"y":487,"decorName":"tree1"},{"x":54,"y":675,"decorName":"tree1"}]'))
        set_blocks(level84, json.loads('[{"type":"move_forwards"},{"type":"turn_left"},{"type":"turn_right"},{"type":"controls_repeat"}]'))
        return level84

    def level88():
        level88 = Level(
            name='88',
            default=True,
            path='[{"coordinate":[2,6],"connectedNodes":[1]},{"coordinate":[2,5],"connectedNodes":[0,2]},{"coordinate":[2,4],"connectedNodes":[10,1,3]},{"coordinate":[2,3],"connectedNodes":[2,4]},{"coordinate":[3,3],"connectedNodes":[3,5]},{"coordinate":[4,3],"connectedNodes":[4,6]},{"coordinate":[4,2],"connectedNodes":[5,14,7]},{"coordinate":[4,1],"connectedNodes":[8,6]},{"coordinate":[3,1],"connectedNodes":[9,7]},{"coordinate":[2,1],"connectedNodes":[8]},{"coordinate":[1,4],"connectedNodes":[11,2]},{"coordinate":[0,4],"connectedNodes":[10,12]},{"coordinate":[0,3],"connectedNodes":[11,13]},{"coordinate":[0,2],"connectedNodes":[12]},{"coordinate":[5,2],"connectedNodes":[6,15]},{"coordinate":[6,2],"connectedNodes":[14,16]},{"coordinate":[6,3],"connectedNodes":[17,15]},{"coordinate":[6,4],"connectedNodes":[18,20,16]},{"coordinate":[5,4],"connectedNodes":[19,17]},{"coordinate":[5,5],"connectedNodes":[18]},{"coordinate":[7,4],"connectedNodes":[17,21]},{"coordinate":[8,4],"connectedNodes":[20,22]},{"coordinate":[8,5],"connectedNodes":[23,21]},{"coordinate":[8,6],"connectedNodes":[22]}]',
            traffic_lights='[{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":2,"y":3},"direction":"E","startTime":0,"startingState":"GREEN"}]',
            destinations='[[2,1]]',
            origin='{"coordinate":[2,6],"direction":"S"}',
            max_fuel=50,
            blocklyEnabled=True,
            pythonEnabled=True,
            theme=Theme.objects.get(id=4),
            character=Character.objects.get(id='1'),
        )
        level88.save()
        set_decor(level88, json.loads('[{"x":0,"y":117,"decorName":"tree2"},{"x":630,"y":484,"decorName":"pond"},{"x":289,"y":458,"decorName":"bush"},{"x":288,"y":395,"decorName":"bush"},{"x":289,"y":525,"decorName":"bush"},{"x":695,"y":355,"decorName":"bush"},{"x":694,"y":152,"decorName":"bush"},{"x":695,"y":214,"decorName":"bush"},{"x":694,"y":285,"decorName":"bush"},{"x":551,"y":152,"decorName":"bush"},{"x":622,"y":152,"decorName":"bush"},{"x":487,"y":152,"decorName":"bush"},{"x":496,"y":286,"decorName":"tree1"}]'))
        set_blocks(level88, json.loads('[{"type":"move_forwards"},{"type":"turn_left"},{"type":"turn_right"},{"type":"controls_repeat_while"},{"type":"controls_if"},{"type":"logic_negate"},{"type":"at_destination"},{"type":"road_exists"},{"type":"traffic_light"}]'))
        return level88

    def level90():
        level90 = Level(
            name='90',
            default=True,
            path='[{"coordinate":[1,6],"connectedNodes":[1]},{"coordinate":[2,6],"connectedNodes":[0,2]},{"coordinate":[2,5],"connectedNodes":[1,3]},{"coordinate":[3,5],"connectedNodes":[2,4]},{"coordinate":[4,5],"connectedNodes":[3,5]},{"coordinate":[4,4],"connectedNodes":[4,6]},{"coordinate":[5,4],"connectedNodes":[5,7]},{"coordinate":[5,3],"connectedNodes":[6,8]},{"coordinate":[6,3],"connectedNodes":[7,9]},{"coordinate":[7,3],"connectedNodes":[8,10]},{"coordinate":[7,2],"connectedNodes":[9,11]},{"coordinate":[8,2],"connectedNodes":[10,12]},{"coordinate":[8,1],"connectedNodes":[13,11]},{"coordinate":[7,1],"connectedNodes":[14,12]},{"coordinate":[6,1],"connectedNodes":[15,13]},{"coordinate":[5,1],"connectedNodes":[16,14]},{"coordinate":[4,1],"connectedNodes":[17,15]},{"coordinate":[3,1],"connectedNodes":[18,16]},{"coordinate":[3,2],"connectedNodes":[19,17]},{"coordinate":[2,2],"connectedNodes":[20,18]},{"coordinate":[2,3],"connectedNodes":[21,19]},{"coordinate":[1,3],"connectedNodes":[20]}]',
            traffic_lights='[]',
            destinations='[[1,3]]',
            origin='{"coordinate":[1,6],"direction":"E"}',
            max_fuel=50,
            blocklyEnabled=True,
            pythonEnabled=True,
            theme=Theme.objects.get(id=4),
            character=Character.objects.get(id='1'),
        )
        level90.save()
        set_decor(level90, json.loads('[{"x":607,"y":213,"decorName":"tree2"},{"x":276,"y":357,"decorName":"pond"},{"x":295,"y":594,"decorName":"bush"},{"x":360,"y":594,"decorName":"bush"},{"x":424,"y":592,"decorName":"bush"},{"x":482,"y":592,"decorName":"bush"},{"x":484,"y":532,"decorName":"bush"},{"x":712,"y":393,"decorName":"bush"},{"x":771,"y":391,"decorName":"bush"},{"x":649,"y":394,"decorName":"bush"},{"x":592,"y":395,"decorName":"bush"},{"x":708,"y":186,"decorName":"bush"},{"x":772,"y":334,"decorName":"bush"},{"x":540,"y":528,"decorName":"bush"},{"x":594,"y":458,"decorName":"bush"},{"x":596,"y":524,"decorName":"bush"}]'))
        set_blocks(level90, json.loads('[{"type":"move_forwards"},{"type":"turn_left"},{"type":"turn_right"},{"type":"controls_repeat"},{"type":"call_proc"},{"type":"declare_proc"}]'))
        return level90

    def level91():
        level91 = Level(
            name='91',
            default=True,
            path='[{"coordinate":[1,6],"connectedNodes":[1]},{"coordinate":[2,6],"connectedNodes":[0,2]},{"coordinate":[3,6],"connectedNodes":[1,3]},{"coordinate":[3,5],"connectedNodes":[2,4]},{"coordinate":[3,4],"connectedNodes":[3,5]},{"coordinate":[3,3],"connectedNodes":[6,4]},{"coordinate":[2,3],"connectedNodes":[5,7]},{"coordinate":[2,2],"connectedNodes":[6,8]},{"coordinate":[3,2],"connectedNodes":[7,9]},{"coordinate":[4,2],"connectedNodes":[8,10]},{"coordinate":[5,2],"connectedNodes":[9,11]},{"coordinate":[5,1],"connectedNodes":[10,12]},{"coordinate":[6,1],"connectedNodes":[11,13]},{"coordinate":[6,2],"connectedNodes":[14,12]},{"coordinate":[6,3],"connectedNodes":[15,13]},{"coordinate":[6,4],"connectedNodes":[16,14]},{"coordinate":[6,5],"connectedNodes":[17,15]},{"coordinate":[7,5],"connectedNodes":[16,18]},{"coordinate":[7,6],"connectedNodes":[19,17]},{"coordinate":[6,6],"connectedNodes":[20,18]},{"coordinate":[5,6],"connectedNodes":[21,19]},{"coordinate":[4,6],"connectedNodes":[22,20]},{"coordinate":[4,7],"connectedNodes":[21]}]',
            traffic_lights='[]',
            destinations='[[4,7]]',
            origin='{"coordinate":[1,6],"direction":"E"}',
            max_fuel=50,
            blocklyEnabled=True,
            pythonEnabled=True,
            theme=Theme.objects.get(id=2),
            character=Character.objects.get(id='1'),
        )
        level91.save()
        set_decor(level91, json.loads('[{"x":152,"y":498,"decorName":"tree1"},{"x":103,"y":377,"decorName":"tree1"},{"x":782,"y":329,"decorName":"pond"},{"x":551,"y":482,"decorName":"bush"},{"x":554,"y":545,"decorName":"bush"},{"x":551,"y":286,"decorName":"bush"},{"x":551,"y":349,"decorName":"bush"},{"x":550,"y":414,"decorName":"bush"},{"x":732,"y":221,"decorName":"tree2"},{"x":894,"y":437,"decorName":"tree2"},{"x":0,"y":273,"decorName":"tree1"},{"x":0,"y":502,"decorName":"tree1"}]'))
        set_blocks(level91, json.loads('[{"type":"move_forwards"},{"type":"turn_left"},{"type":"turn_right"},{"type":"controls_repeat"},{"type":"call_proc"},{"type":"declare_proc"}]'))
        return level91

    def level92():
        level92 = Level(
            name='92',
            default=True,
            path='[{"coordinate":[3,6],"connectedNodes":[1]},{"coordinate":[3,5],"connectedNodes":[0,2]},{"coordinate":[3,4],"connectedNodes":[3,1]},{"coordinate":[2,4],"connectedNodes":[2,4]},{"coordinate":[2,3],"connectedNodes":[3,5]},{"coordinate":[2,2],"connectedNodes":[4]}]',
            traffic_lights='[]',
            destinations='[[2,2]]',
            origin='{"coordinate":[3,6],"direction":"S"}',
            max_fuel=50,
            blocklyEnabled=False,
            pythonEnabled=True,
            theme=Theme.objects.get(id=3),
            character=Character.objects.get(id='1'),
        )
        level92.save()
        set_decor(level92, json.loads('[{"x":291,"y":329,"decorName":"tree2"},{"x":106,"y":604,"decorName":"pond"},{"x":106,"y":502,"decorName":"pond"},{"x":764,"y":664,"decorName":"tree1"},{"x":882,"y":622,"decorName":"tree1"},{"x":799,"y":575,"decorName":"tree1"},{"x":751,"y":404,"decorName":"tree1"},{"x":665,"y":560,"decorName":"tree1"},{"x":880,"y":473,"decorName":"tree1"},{"x":579,"y":659,"decorName":"tree1"},{"x":529,"y":431,"decorName":"tree1"},{"x":772,"y":0,"decorName":"pond"},{"x":772,"y":101,"decorName":"pond"},{"x":605,"y":101,"decorName":"pond"},{"x":430,"y":102,"decorName":"pond"},{"x":605,"y":3,"decorName":"pond"},{"x":430,"y":3,"decorName":"pond"},{"x":150,"y":339,"decorName":"bush"},{"x":94,"y":338,"decorName":"bush"},{"x":36,"y":338,"decorName":"bush"},{"x":99,"y":409,"decorName":"bush"},{"x":126,"y":370,"decorName":"bush"},{"x":65,"y":372,"decorName":"bush"}]'))
        return level92

    def level97():
        level97 = Level(
            name='97',
            default=True,
            path='[{"coordinate":[1,6],"connectedNodes":[1]},{"coordinate":[1,5],"connectedNodes":[0,2]},{"coordinate":[1,4],"connectedNodes":[1,3]},{"coordinate":[1,3],"connectedNodes":[2,4]},{"coordinate":[1,2],"connectedNodes":[3,5]},{"coordinate":[1,1],"connectedNodes":[4,6]},{"coordinate":[2,1],"connectedNodes":[5,7]},{"coordinate":[2,2],"connectedNodes":[8,6]},{"coordinate":[2,3],"connectedNodes":[9,7]},{"coordinate":[2,4],"connectedNodes":[10,8]},{"coordinate":[2,5],"connectedNodes":[11,9]},{"coordinate":[2,6],"connectedNodes":[12,10]},{"coordinate":[3,6],"connectedNodes":[11,17]},{"coordinate":[3,1],"connectedNodes":[14,18]},{"coordinate":[3,2],"connectedNodes":[15,13]},{"coordinate":[3,3],"connectedNodes":[16,14]},{"coordinate":[3,4],"connectedNodes":[17,15]},{"coordinate":[3,5],"connectedNodes":[12,16]},{"coordinate":[4,1],"connectedNodes":[13,19]},{"coordinate":[4,2],"connectedNodes":[20,18]},{"coordinate":[4,3],"connectedNodes":[21,19]},{"coordinate":[4,4],"connectedNodes":[22,20]},{"coordinate":[4,5],"connectedNodes":[23,21]},{"coordinate":[4,6],"connectedNodes":[24,22]},{"coordinate":[5,6],"connectedNodes":[23,25]},{"coordinate":[5,5],"connectedNodes":[24,26]},{"coordinate":[5,4],"connectedNodes":[25,27]},{"coordinate":[5,3],"connectedNodes":[26,28]},{"coordinate":[5,2],"connectedNodes":[27,29]},{"coordinate":[5,1],"connectedNodes":[28,30]},{"coordinate":[6,1],"connectedNodes":[29,31]},{"coordinate":[6,2],"connectedNodes":[32,30]},{"coordinate":[6,3],"connectedNodes":[33,31]},{"coordinate":[6,4],"connectedNodes":[34,32]},{"coordinate":[6,5],"connectedNodes":[35,33]},{"coordinate":[6,6],"connectedNodes":[36,34]},{"coordinate":[7,6],"connectedNodes":[35,37]},{"coordinate":[7,5],"connectedNodes":[36]}]',
            traffic_lights='[]',
            destinations='[[7,5]]',
            origin='{"coordinate":[1,6],"direction":"S"}',
            max_fuel=50,
            blocklyEnabled=False,
            pythonEnabled=True,
            theme=Theme.objects.get(id=2),
            character=Character.objects.get(id='1'),
        )
        level97.save()
        set_decor(level97, json.loads('[{"x":0,"y":4,"decorName":"tree1"},{"x":296,"y":695,"decorName":"tree1"},{"x":102,"y":700,"decorName":"tree1"},{"x":0,"y":599,"decorName":"tree1"},{"x":0,"y":395,"decorName":"tree1"},{"x":0,"y":198,"decorName":"tree1"},{"x":900,"y":700,"decorName":"tree1"},{"x":700,"y":700,"decorName":"tree1"},{"x":503,"y":700,"decorName":"tree1"},{"x":900,"y":99,"decorName":"tree1"},{"x":803,"y":0,"decorName":"tree1"},{"x":600,"y":0,"decorName":"tree1"},{"x":399,"y":0,"decorName":"tree1"},{"x":199,"y":0,"decorName":"tree1"},{"x":900,"y":499,"decorName":"tree1"},{"x":897,"y":300,"decorName":"tree1"},{"x":687,"y":422,"decorName":"bush"},{"x":685,"y":338,"decorName":"bush"},{"x":686,"y":264,"decorName":"bush"},{"x":685,"y":185,"decorName":"bush"},{"x":684,"y":112,"decorName":"bush"}]'))
        return level97

    def level100():
        level100 = Level(
            name='100',
            default=True,
            path='[{"coordinate":[8,6],"connectedNodes":[1]},{"coordinate":[7,6],"connectedNodes":[2,0]},{"coordinate":[6,6],"connectedNodes":[1,3]},{"coordinate":[6,5],"connectedNodes":[2,4]},{"coordinate":[7,5],"connectedNodes":[3,5]},{"coordinate":[7,4],"connectedNodes":[6,4]},{"coordinate":[6,4],"connectedNodes":[7,5]},{"coordinate":[5,4],"connectedNodes":[8,6]},{"coordinate":[5,5],"connectedNodes":[9,7]},{"coordinate":[5,6],"connectedNodes":[10,8]},{"coordinate":[4,6],"connectedNodes":[11,9]},{"coordinate":[3,6],"connectedNodes":[12,10]},{"coordinate":[2,6],"connectedNodes":[11,13]},{"coordinate":[2,5],"connectedNodes":[12,14]},{"coordinate":[3,5],"connectedNodes":[13,15]},{"coordinate":[3,4],"connectedNodes":[16,14]},{"coordinate":[2,4],"connectedNodes":[17,15]},{"coordinate":[1,4],"connectedNodes":[18,16]},{"coordinate":[1,5],"connectedNodes":[19,17]},{"coordinate":[1,6],"connectedNodes":[20,18]},{"coordinate":[0,6],"connectedNodes":[19,21]},{"coordinate":[0,5],"connectedNodes":[20,22]},{"coordinate":[0,4],"connectedNodes":[21,23]},{"coordinate":[0,3],"connectedNodes":[22,24]},{"coordinate":[0,2],"connectedNodes":[23,25]},{"coordinate":[0,1],"connectedNodes":[24,26]},{"coordinate":[1,1],"connectedNodes":[25,27]},{"coordinate":[2,1],"connectedNodes":[26,28]},{"coordinate":[3,1],"connectedNodes":[27,29]},{"coordinate":[4,1],"connectedNodes":[28,30]},{"coordinate":[5,1],"connectedNodes":[29,33]},{"coordinate":[6,3],"connectedNodes":[32]},{"coordinate":[6,2],"connectedNodes":[31,33]},{"coordinate":[6,1],"connectedNodes":[30,32,34]},{"coordinate":[7,1],"connectedNodes":[33,35]},{"coordinate":[8,1],"connectedNodes":[34]}]',
            traffic_lights='[]',
            destinations='[[8,1]]',
            origin='{"coordinate":[8,6],"direction":"W"}',
            max_fuel=50,
            blocklyEnabled=False,
            pythonEnabled=True,
            theme=Theme.objects.get(id=4),
            character=Character.objects.get(id='1'),
        )
        level100.save()
        set_decor(level100, json.loads('[{"x":682,"y":228,"decorName":"tree1"},{"x":186,"y":189,"decorName":"pond"},{"x":332,"y":571,"decorName":"bush"},{"x":404,"y":506,"decorName":"tree2"},{"x":98,"y":191,"decorName":"bush"},{"x":97,"y":251,"decorName":"bush"},{"x":98,"y":315,"decorName":"bush"},{"x":354,"y":192,"decorName":"bush"},{"x":354,"y":252,"decorName":"bush"},{"x":354,"y":317,"decorName":"bush"},{"x":676,"y":698,"decorName":"bush"},{"x":750,"y":700,"decorName":"bush"},{"x":297,"y":357,"decorName":"bush"},{"x":230,"y":357,"decorName":"bush"},{"x":160,"y":356,"decorName":"bush"},{"x":902,"y":550,"decorName":"bush"},{"x":827,"y":550,"decorName":"bush"},{"x":754,"y":552,"decorName":"bush"},{"x":901,"y":697,"decorName":"bush"},{"x":826,"y":699,"decorName":"bush"},{"x":904,"y":627,"decorName":"bush"}]'))
        return level100

    def level101():
        level101 = Level(
            name='101',
            default=True,
            path='[{"coordinate":[1,6],"connectedNodes":[1]},{"coordinate":[2,6],"connectedNodes":[0,2]},{"coordinate":[2,5],"connectedNodes":[1,3,19]},{"coordinate":[3,5],"connectedNodes":[2,4]},{"coordinate":[4,5],"connectedNodes":[3,5]},{"coordinate":[4,4],"connectedNodes":[4,6]},{"coordinate":[5,4],"connectedNodes":[5,7]},{"coordinate":[6,4],"connectedNodes":[6,14,8]},{"coordinate":[7,4],"connectedNodes":[7,9]},{"coordinate":[7,3],"connectedNodes":[8,10]},{"coordinate":[8,3],"connectedNodes":[9,18,11]},{"coordinate":[8,2],"connectedNodes":[12,10]},{"coordinate":[7,2],"connectedNodes":[11,13]},{"coordinate":[7,1],"connectedNodes":[26,12]},{"coordinate":[6,5],"connectedNodes":[15,7]},{"coordinate":[6,6],"connectedNodes":[16,14]},{"coordinate":[7,6],"connectedNodes":[15,17]},{"coordinate":[8,6],"connectedNodes":[16]},{"coordinate":[9,3],"connectedNodes":[10]},{"coordinate":[2,4],"connectedNodes":[20,2]},{"coordinate":[1,4],"connectedNodes":[19,21]},{"coordinate":[1,3],"connectedNodes":[24,20,22]},{"coordinate":[2,3],"connectedNodes":[21,23]},{"coordinate":[3,3],"connectedNodes":[22]},{"coordinate":[0,3],"connectedNodes":[21,25]},{"coordinate":[0,2],"connectedNodes":[24]},{"coordinate":[6,1],"connectedNodes":[27,13]},{"coordinate":[5,1],"connectedNodes":[26]}]',
            traffic_lights='[]',
            destinations='[[5,1]]',
            origin='{"coordinate":[1,6],"direction":"E"}',
            max_fuel=50,
            blocklyEnabled=True,
            pythonEnabled=True,
            theme=Theme.objects.get(id=4),
            character=Character.objects.get(id='1'),
        )
        level101.save()
        set_decor(level101, json.loads('[{"x":739,"y":509,"decorName":"tree2"},{"x":117,"y":162,"decorName":"pond"},{"x":290,"y":458,"decorName":"bush"},{"x":358,"y":457,"decorName":"bush"},{"x":358,"y":397,"decorName":"bush"},{"x":422,"y":352,"decorName":"bush"},{"x":495,"y":352,"decorName":"bush"},{"x":566,"y":353,"decorName":"bush"},{"x":638,"y":354,"decorName":"bush"},{"x":792,"y":380,"decorName":"tree1"},{"x":692,"y":689,"decorName":"bush"},{"x":627,"y":688,"decorName":"bush"},{"x":824,"y":692,"decorName":"bush"},{"x":756,"y":690,"decorName":"bush"}]'))
        return level101

    def level102():
        level102 = Level(
            name='102',
            default=True,
            path='[{"coordinate":[1,4],"connectedNodes":[1]},{"coordinate":[2,4],"connectedNodes":[0,2]},{"coordinate":[2,5],"connectedNodes":[3,1]},{"coordinate":[3,5],"connectedNodes":[2,4]},{"coordinate":[3,6],"connectedNodes":[5,3]},{"coordinate":[4,6],"connectedNodes":[4,6]},{"coordinate":[4,5],"connectedNodes":[5,7]},{"coordinate":[5,5],"connectedNodes":[6,8]},{"coordinate":[5,4],"connectedNodes":[7,9]},{"coordinate":[6,4],"connectedNodes":[8,10]},{"coordinate":[7,4],"connectedNodes":[9,11]},{"coordinate":[7,3],"connectedNodes":[10,12]},{"coordinate":[7,2],"connectedNodes":[11,13]},{"coordinate":[7,1],"connectedNodes":[14,12]},{"coordinate":[6,1],"connectedNodes":[15,13]},{"coordinate":[6,2],"connectedNodes":[16,14]},{"coordinate":[5,2],"connectedNodes":[17,15]},{"coordinate":[5,3],"connectedNodes":[18,16]},{"coordinate":[4,3],"connectedNodes":[17,19]},{"coordinate":[4,2],"connectedNodes":[20,18]},{"coordinate":[3,2],"connectedNodes":[19,21]},{"coordinate":[3,1],"connectedNodes":[22,20]},{"coordinate":[2,1],"connectedNodes":[23,21]},{"coordinate":[1,1],"connectedNodes":[22]}]',
            traffic_lights='[]',
            destinations='[[1,1]]',
            origin='{"coordinate":[1,4],"direction":"E"}',
            max_fuel=50,
            blocklyEnabled=False,
            pythonEnabled=True,
            theme=Theme.objects.get(id=3),
            character=Character.objects.get(id='1'),
        )
        level102.save()
        set_decor(level102, json.loads('[{"x":815,"y":697,"decorName":"pond"},{"x":816,"y":597,"decorName":"pond"},{"x":817,"y":498,"decorName":"pond"},{"x":817,"y":397,"decorName":"pond"},{"x":818,"y":296,"decorName":"pond"},{"x":820,"y":197,"decorName":"pond"},{"x":820,"y":98,"decorName":"pond"},{"x":818,"y":0,"decorName":"pond"},{"x":101,"y":508,"decorName":"tree1"},{"x":210,"y":599,"decorName":"tree1"},{"x":500,"y":589,"decorName":"tree1"},{"x":597,"y":508,"decorName":"tree1"},{"x":641,"y":321,"decorName":"tree2"},{"x":446,"y":140,"decorName":"tree1"},{"x":228,"y":202,"decorName":"bush"},{"x":354,"y":505,"decorName":"bush"},{"x":315,"y":467,"decorName":"bush"},{"x":276,"y":431,"decorName":"bush"},{"x":241,"y":395,"decorName":"bush"},{"x":417,"y":388,"decorName":"bush"},{"x":381,"y":352,"decorName":"bush"},{"x":344,"y":315,"decorName":"bush"},{"x":305,"y":279,"decorName":"bush"},{"x":266,"y":239,"decorName":"bush"}]'))
        return level102

    def level103():
        level103 = Level(
            name='103',
            default=True,
            path='[{"coordinate":[1,5],"connectedNodes":[1]},{"coordinate":[2,5],"connectedNodes":[0,2]},{"coordinate":[3,5],"connectedNodes":[1,3]},{"coordinate":[3,6],"connectedNodes":[4,2]},{"coordinate":[3,7],"connectedNodes":[5,3]},{"coordinate":[4,7],"connectedNodes":[4,6]},{"coordinate":[5,7],"connectedNodes":[5,7]},{"coordinate":[5,6],"connectedNodes":[6,26,8]},{"coordinate":[5,5],"connectedNodes":[7,9]},{"coordinate":[5,4],"connectedNodes":[8,10]},{"coordinate":[6,4],"connectedNodes":[9,11]},{"coordinate":[7,4],"connectedNodes":[10,12]},{"coordinate":[7,3],"connectedNodes":[11,13]},{"coordinate":[7,2],"connectedNodes":[14,12]},{"coordinate":[6,2],"connectedNodes":[15,13]},{"coordinate":[5,2],"connectedNodes":[14,16]},{"coordinate":[5,1],"connectedNodes":[15,17]},{"coordinate":[5,0],"connectedNodes":[18,16]},{"coordinate":[4,0],"connectedNodes":[19,17]},{"coordinate":[3,0],"connectedNodes":[20,18]},{"coordinate":[2,0],"connectedNodes":[21,19]},{"coordinate":[2,1],"connectedNodes":[22,20]},{"coordinate":[2,2],"connectedNodes":[23,21]},{"coordinate":[2,3],"connectedNodes":[25,24,22]},{"coordinate":[3,3],"connectedNodes":[23,28]},{"coordinate":[1,3],"connectedNodes":[23]},{"coordinate":[6,6],"connectedNodes":[7,27]},{"coordinate":[7,6],"connectedNodes":[26]},{"coordinate":[4,3],"connectedNodes":[24,29]},{"coordinate":[4,4],"connectedNodes":[28]}]',
            traffic_lights='[]',
            destinations='[[1,3]]',
            origin='{"coordinate":[1,5],"direction":"E"}',
            max_fuel=50,
            blocklyEnabled=False,
            pythonEnabled=True,
            theme=Theme.objects.get(id=2),
            character=Character.objects.get(id='1'),
        )
        level103.save()
        set_decor(level103, json.loads('[{"x":180,"y":653,"decorName":"tree2"},{"x":4,"y":602,"decorName":"tree2"},{"x":81,"y":700,"decorName":"tree2"},{"x":755,"y":558,"decorName":"pond"},{"x":304,"y":237,"decorName":"bush"},{"x":304,"y":170,"decorName":"bush"},{"x":302,"y":104,"decorName":"bush"},{"x":372,"y":104,"decorName":"bush"},{"x":440,"y":106,"decorName":"bush"},{"x":440,"y":172,"decorName":"bush"},{"x":438,"y":236,"decorName":"bush"},{"x":757,"y":167,"decorName":"tree1"},{"x":865,"y":209,"decorName":"tree1"},{"x":666,"y":82,"decorName":"tree1"},{"x":826,"y":350,"decorName":"tree1"},{"x":890,"y":67,"decorName":"tree1"},{"x":842,"y":665,"decorName":"bush"}]'))
        return level103

    def level104():
        level104 = Level(
            name='104',
            default=True,
            path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[2,3],"connectedNodes":[1,3]},{"coordinate":[2,4],"connectedNodes":[4,2]},{"coordinate":[2,5],"connectedNodes":[5,3]},{"coordinate":[1,5],"connectedNodes":[6,4]},{"coordinate":[0,5],"connectedNodes":[7,5]},{"coordinate":[0,6],"connectedNodes":[8,6]},{"coordinate":[0,7],"connectedNodes":[9,7]},{"coordinate":[1,7],"connectedNodes":[8,10]},{"coordinate":[2,7],"connectedNodes":[9,11]},{"coordinate":[3,7],"connectedNodes":[10,12]},{"coordinate":[4,7],"connectedNodes":[11,13]},{"coordinate":[5,7],"connectedNodes":[12,14]},{"coordinate":[6,7],"connectedNodes":[13,15]},{"coordinate":[6,6],"connectedNodes":[14,16]},{"coordinate":[6,5],"connectedNodes":[17,15]},{"coordinate":[5,5],"connectedNodes":[18,16]},{"coordinate":[4,5],"connectedNodes":[17,19]},{"coordinate":[4,4],"connectedNodes":[18,20]},{"coordinate":[4,3],"connectedNodes":[19,21]},{"coordinate":[5,3],"connectedNodes":[20,22]},{"coordinate":[6,3],"connectedNodes":[21,23]},{"coordinate":[6,2],"connectedNodes":[22,24]},{"coordinate":[6,1],"connectedNodes":[25,23]},{"coordinate":[5,1],"connectedNodes":[26,24]},{"coordinate":[4,1],"connectedNodes":[27,25]},{"coordinate":[3,1],"connectedNodes":[28,26]},{"coordinate":[2,1],"connectedNodes":[29,27]},{"coordinate":[2,2],"connectedNodes":[30,28]},{"coordinate":[1,2],"connectedNodes":[31,29]},{"coordinate":[0,2],"connectedNodes":[30,32]},{"coordinate":[0,1],"connectedNodes":[31,33]},{"coordinate":[0,0],"connectedNodes":[32,34]},{"coordinate":[1,0],"connectedNodes":[33,35]},{"coordinate":[2,0],"connectedNodes":[34]}]',
            traffic_lights='[]',
            destinations='[[2,0]]',
            origin='{"coordinate":[0,3],"direction":"E"}',
            max_fuel=50,
            blocklyEnabled=False,
            pythonEnabled=True,
            theme=Theme.objects.get(id=4),
            character=Character.objects.get(id='1'),
        )
        level104.save()
        set_decor(level104, json.loads('[{"x":277,"y":554,"decorName":"pond"},{"x":100,"y":664,"decorName":"bush"},{"x":196,"y":663,"decorName":"bush"},{"x":451,"y":662,"decorName":"bush"},{"x":551,"y":660,"decorName":"bush"},{"x":495,"y":196,"decorName":"tree2"},{"x":289,"y":476,"decorName":"bush"},{"x":365,"y":475,"decorName":"bush"},{"x":291,"y":372,"decorName":"bush"},{"x":366,"y":370,"decorName":"bush"},{"x":289,"y":273,"decorName":"bush"},{"x":362,"y":272,"decorName":"bush"},{"x":287,"y":185,"decorName":"bush"},{"x":360,"y":187,"decorName":"bush"},{"x":495,"y":423,"decorName":"tree1"},{"x":97,"y":121,"decorName":"tree1"}]'))
        return level104

    def level105():
        level105 = Level(
            name='105',
            default=True,
            path='[{"coordinate":[6,7],"connectedNodes":[1]},{"coordinate":[6,6],"connectedNodes":[0,2]},{"coordinate":[6,5],"connectedNodes":[3,1]},{"coordinate":[5,5],"connectedNodes":[4,2]},{"coordinate":[4,5],"connectedNodes":[5,3]},{"coordinate":[3,5],"connectedNodes":[8,4,6]},{"coordinate":[3,4],"connectedNodes":[5,7]},{"coordinate":[3,3],"connectedNodes":[19,6,9]},{"coordinate":[2,5],"connectedNodes":[14,5]},{"coordinate":[3,2],"connectedNodes":[7,10]},{"coordinate":[4,2],"connectedNodes":[9,11]},{"coordinate":[5,2],"connectedNodes":[10,12]},{"coordinate":[6,2],"connectedNodes":[11,13]},{"coordinate":[6,3],"connectedNodes":[21,12]},{"coordinate":[1,5],"connectedNodes":[16,15,8]},{"coordinate":[1,6],"connectedNodes":[23,14]},{"coordinate":[0,5],"connectedNodes":[14,17]},{"coordinate":[0,4],"connectedNodes":[16,18]},{"coordinate":[0,3],"connectedNodes":[17]},{"coordinate":[2,3],"connectedNodes":[7,20]},{"coordinate":[2,2],"connectedNodes":[19]},{"coordinate":[7,3],"connectedNodes":[13,22]},{"coordinate":[7,4],"connectedNodes":[21]},{"coordinate":[1,7],"connectedNodes":[15]}]',
            traffic_lights='[{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":4,"y":5},"direction":"W","startTime":0,"startingState":"RED"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":2,"y":5},"direction":"E","startTime":0,"startingState":"RED"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":3,"y":4},"direction":"N","startTime":0,"startingState":"GREEN"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":3,"y":4},"direction":"S","startTime":0,"startingState":"RED"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":3,"y":2},"direction":"N","startTime":0,"startingState":"RED"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":2,"y":3},"direction":"E","startTime":0,"startingState":"GREEN"}]',
            destinations='[[7,4]]',
            origin='{"coordinate":[6,7],"direction":"S"}',
            max_fuel=50,
            blocklyEnabled=False,
            pythonEnabled=True,
            theme=Theme.objects.get(id=4),
            character=Character.objects.get(id='1'),
        )
        level105.save()
        set_decor(level105, json.loads('[{"x":452,"y":360,"decorName":"pond"},{"x":230,"y":640,"decorName":"tree2"},{"x":212,"y":587,"decorName":"bush"},{"x":301,"y":750,"decorName":"bush"},{"x":216,"y":750,"decorName":"bush"},{"x":296,"y":586,"decorName":"bush"},{"x":328,"y":157,"decorName":"bush"},{"x":551,"y":586,"decorName":"bush"},{"x":383,"y":587,"decorName":"bush"},{"x":464,"y":586,"decorName":"bush"},{"x":99,"y":383,"decorName":"tree1"},{"x":107,"y":459,"decorName":"bush"},{"x":176,"y":459,"decorName":"bush"},{"x":243,"y":459,"decorName":"bush"},{"x":243,"y":393,"decorName":"bush"},{"x":107,"y":327,"decorName":"bush"},{"x":243,"y":157,"decorName":"bush"},{"x":659,"y":159,"decorName":"bush"},{"x":577,"y":157,"decorName":"bush"},{"x":492,"y":157,"decorName":"bush"},{"x":408,"y":157,"decorName":"bush"}]'))
        return level105

    def level106():
        level106 = Level(
            name='106',
            default=True,
            path='[{"coordinate":[3,4],"connectedNodes":[1]},{"coordinate":[4,4],"connectedNodes":[0,2]},{"coordinate":[4,3],"connectedNodes":[1,3]},{"coordinate":[4,2],"connectedNodes":[4,2]},{"coordinate":[3,2],"connectedNodes":[5,3]},{"coordinate":[2,2],"connectedNodes":[6,4]},{"coordinate":[1,2],"connectedNodes":[7,5]},{"coordinate":[1,3],"connectedNodes":[8,6]},{"coordinate":[1,4],"connectedNodes":[9,7]},{"coordinate":[1,5],"connectedNodes":[10,8]},{"coordinate":[1,6],"connectedNodes":[11,9]},{"coordinate":[2,6],"connectedNodes":[10,12]},{"coordinate":[3,6],"connectedNodes":[11,13]},{"coordinate":[4,6],"connectedNodes":[12,14]},{"coordinate":[5,6],"connectedNodes":[13,15]},{"coordinate":[6,6],"connectedNodes":[14,16]},{"coordinate":[6,5],"connectedNodes":[15,17]},{"coordinate":[6,4],"connectedNodes":[16,18]},{"coordinate":[6,3],"connectedNodes":[17,19]},{"coordinate":[6,2],"connectedNodes":[18,20]},{"coordinate":[6,1],"connectedNodes":[19,21]},{"coordinate":[6,0],"connectedNodes":[20]}]',
            traffic_lights='[]',
            destinations='[[6,0]]',
            origin='{"coordinate":[3,4],"direction":"E"}',
            max_fuel=50,
            blocklyEnabled=False,
            pythonEnabled=True,
            theme=Theme.objects.get(id=2),
            character=Character.objects.get(id='1'),
        )
        level106.save()
        set_decor(level106, json.loads('[{"x":210,"y":505,"decorName":"tree1"},{"x":474,"y":505,"decorName":"tree1"},{"x":697,"y":593,"decorName":"bush"},{"x":697,"y":282,"decorName":"bush"},{"x":697,"y":362,"decorName":"bush"},{"x":697,"y":435,"decorName":"bush"},{"x":697,"y":515,"decorName":"bush"},{"x":695,"y":137,"decorName":"bush"},{"x":696,"y":210,"decorName":"bush"},{"x":209,"y":15,"decorName":"pond"},{"x":72,"y":71,"decorName":"tree2"},{"x":354,"y":95,"decorName":"tree2"},{"x":392,"y":0,"decorName":"tree2"}]'))
        return level106

    def level107():
        level107 = Level(
            name='107',
            default=True,
            path='[{"coordinate":[2,4],"connectedNodes":[19]},{"coordinate":[8,1],"connectedNodes":[2,20]},{"coordinate":[7,1],"connectedNodes":[3,1]},{"coordinate":[6,1],"connectedNodes":[4,2]},{"coordinate":[5,1],"connectedNodes":[5,3]},{"coordinate":[4,1],"connectedNodes":[6,4]},{"coordinate":[3,1],"connectedNodes":[7,5]},{"coordinate":[2,1],"connectedNodes":[8,6]},{"coordinate":[1,1],"connectedNodes":[9,7]},{"coordinate":[0,1],"connectedNodes":[10,8]},{"coordinate":[0,2],"connectedNodes":[11,9]},{"coordinate":[0,3],"connectedNodes":[12,10]},{"coordinate":[0,4],"connectedNodes":[13,11]},{"coordinate":[0,5],"connectedNodes":[14,12]},{"coordinate":[0,6],"connectedNodes":[15,13]},{"coordinate":[1,6],"connectedNodes":[14,16]},{"coordinate":[2,6],"connectedNodes":[15,17]},{"coordinate":[3,6],"connectedNodes":[16,18]},{"coordinate":[3,5],"connectedNodes":[17,19]},{"coordinate":[3,4],"connectedNodes":[0,18]},{"coordinate":[9,1],"connectedNodes":[1]}]',
            traffic_lights='[]',
            destinations='[[9,1]]',
            origin='{"coordinate":[2,4],"direction":"E"}',
            max_fuel=50,
            blocklyEnabled=False,
            pythonEnabled=True,
            theme=Theme.objects.get(id=1),
            character=Character.objects.get(id='1'),
        )
        level107.save()
        set_decor(level107, json.loads('[{"x":639,"y":534,"decorName":"pond"},{"x":515,"y":624,"decorName":"tree1"},{"x":812,"y":700,"decorName":"tree1"},{"x":755,"y":462,"decorName":"tree1"},{"x":792,"y":589,"decorName":"tree1"},{"x":95,"y":550,"decorName":"bush"},{"x":95,"y":477,"decorName":"bush"},{"x":96,"y":398,"decorName":"bush"},{"x":96,"y":327,"decorName":"bush"},{"x":97,"y":189,"decorName":"bush"},{"x":96,"y":257,"decorName":"bush"},{"x":553,"y":191,"decorName":"bush"},{"x":405,"y":191,"decorName":"bush"},{"x":332,"y":190,"decorName":"bush"},{"x":177,"y":189,"decorName":"bush"},{"x":256,"y":190,"decorName":"bush"},{"x":479,"y":191,"decorName":"bush"},{"x":627,"y":191,"decorName":"bush"},{"x":701,"y":190,"decorName":"bush"},{"x":775,"y":191,"decorName":"bush"},{"x":900,"y":654,"decorName":"tree2"},{"x":459,"y":700,"decorName":"tree2"},{"x":900,"y":528,"decorName":"tree2"},{"x":678,"y":700,"decorName":"tree2"},{"x":883,"y":324,"decorName":"tree1"},{"x":171,"y":551,"decorName":"bush"},{"x":249,"y":547,"decorName":"bush"},{"x":76,"y":700,"decorName":"tree1"}]'))
        return level107

    def level108():
        level108 = Level(
            name='108',
            default=True,
            path='[{"coordinate":[8,6],"connectedNodes":[7]},{"coordinate":[6,6],"connectedNodes":[2,7]},{"coordinate":[5,6],"connectedNodes":[3,1]},{"coordinate":[4,6],"connectedNodes":[4,2]},{"coordinate":[3,6],"connectedNodes":[5,3]},{"coordinate":[2,6],"connectedNodes":[6,4]},{"coordinate":[1,6],"connectedNodes":[5,8]},{"coordinate":[7,6],"connectedNodes":[1,0]},{"coordinate":[1,5],"connectedNodes":[6,9]},{"coordinate":[1,4],"connectedNodes":[8,10]},{"coordinate":[1,3],"connectedNodes":[9,11]},{"coordinate":[1,2],"connectedNodes":[10,12]},{"coordinate":[1,1],"connectedNodes":[11,13]},{"coordinate":[2,1],"connectedNodes":[12,14]},{"coordinate":[3,1],"connectedNodes":[13,15]},{"coordinate":[4,1],"connectedNodes":[14,16]},{"coordinate":[4,2],"connectedNodes":[17,15]},{"coordinate":[3,2],"connectedNodes":[16]}]',
            traffic_lights='[]',
            destinations='[[3,2]]',
            origin='{"coordinate":[8,6],"direction":"W"}',
            max_fuel=50,
            blocklyEnabled=False,
            pythonEnabled=True,
            theme=Theme.objects.get(id=3),
            character=Character.objects.get(id='1'),
        )
        level108.save()
        set_decor(level108, json.loads('[{"x":235,"y":501,"decorName":"pond"},{"x":235,"y":402,"decorName":"pond"},{"x":237,"y":298,"decorName":"pond"},{"x":397,"y":500,"decorName":"pond"},{"x":398,"y":401,"decorName":"pond"},{"x":399,"y":298,"decorName":"pond"},{"x":2,"y":492,"decorName":"tree1"},{"x":406,"y":3,"decorName":"tree1"},{"x":76,"y":28,"decorName":"tree1"},{"x":14,"y":246,"decorName":"tree1"},{"x":550,"y":176,"decorName":"tree1"},{"x":27,"y":666,"decorName":"tree1"},{"x":495,"y":688,"decorName":"tree1"},{"x":236,"y":700,"decorName":"tree1"},{"x":715,"y":700,"decorName":"tree1"},{"x":677,"y":285,"decorName":"bush"},{"x":677,"y":338,"decorName":"bush"},{"x":675,"y":397,"decorName":"bush"},{"x":675,"y":452,"decorName":"bush"},{"x":672,"y":512,"decorName":"bush"},{"x":673,"y":571,"decorName":"bush"},{"x":677,"y":229,"decorName":"bush"},{"x":679,"y":169,"decorName":"bush"}]'))
        return level108

    def level109():
        level109 = Level(
            name='109',
            default=True,
            path='[{"coordinate":[2,5],"connectedNodes":[1]},{"coordinate":[3,5],"connectedNodes":[0,2]},{"coordinate":[3,4],"connectedNodes":[3,1]},{"coordinate":[2,4],"connectedNodes":[4,2]},{"coordinate":[1,4],"connectedNodes":[5,3]},{"coordinate":[1,5],"connectedNodes":[6,4]},{"coordinate":[1,6],"connectedNodes":[7,5]},{"coordinate":[1,7],"connectedNodes":[8,6]},{"coordinate":[2,7],"connectedNodes":[7,9]},{"coordinate":[3,7],"connectedNodes":[8,10]},{"coordinate":[4,7],"connectedNodes":[9,11]},{"coordinate":[5,7],"connectedNodes":[10,12]},{"coordinate":[5,6],"connectedNodes":[11,13]},{"coordinate":[5,5],"connectedNodes":[12,14]},{"coordinate":[5,4],"connectedNodes":[13,15]},{"coordinate":[5,3],"connectedNodes":[14,16]},{"coordinate":[5,2],"connectedNodes":[15,17]},{"coordinate":[6,2],"connectedNodes":[16,18]},{"coordinate":[7,2],"connectedNodes":[17,19]},{"coordinate":[8,2],"connectedNodes":[18,20]},{"coordinate":[8,3],"connectedNodes":[21,19]},{"coordinate":[8,4],"connectedNodes":[22,20]},{"coordinate":[7,4],"connectedNodes":[21]}]',
            traffic_lights='[]',
            destinations='[[7,4]]',
            origin='{"coordinate":[2,5],"direction":"E"}',
            max_fuel=50,
            blocklyEnabled=False,
            pythonEnabled=True,
            theme=Theme.objects.get(id=2),
            character=Character.objects.get(id='1'),
        )
        level109.save()
        set_decor(level109, json.loads('[{"x":398,"y":600,"decorName":"tree2"},{"x":627,"y":632,"decorName":"tree1"},{"x":876,"y":697,"decorName":"tree1"},{"x":800,"y":521,"decorName":"tree1"},{"x":402,"y":441,"decorName":"tree2"},{"x":394,"y":277,"decorName":"tree2"},{"x":215,"y":604,"decorName":"tree2"},{"x":391,"y":97,"decorName":"tree2"},{"x":568,"y":96,"decorName":"tree2"},{"x":756,"y":99,"decorName":"tree2"},{"x":900,"y":197,"decorName":"tree2"},{"x":900,"y":369,"decorName":"tree2"}]'))
        return level109

    # Limited Blocks
    level51 = Level.objects.get(name='55', default=1)
    level59 = Level.objects.get(name='56', default=1)
    level60 = Level.objects.get(name='57', default=1)
  
    # Procedures
    level62 = Level.objects.get(name='51', default=1)
    level63 = Level.objects.get(name='52', default=1)
    level65 = Level.objects.get(name='54', default=1)
    level67 = Level.objects.get(name='53', default=1)

    # Blockly Brain Teasers
    level68 = Level.objects.get(name='60', default=1)
    level69 = Level.objects.get(name='61', default=1)
    level70 = Level.objects.get(name='62', default=1)
    level71 = Level.objects.get(name='63', default=1)
    level76 = None
    level77 = None
    level78 = None

    # Introduction to Python
    level81 = Level.objects.get(name='80', default=1)
    level82 = Level.objects.get(name='81', default=1)
    level83 = Level.objects.get(name='82', default=1)
    level85 = Level.objects.get(name='83', default=1)
    level86 = Level.objects.get(name='84', default=1)
    level87 = Level.objects.get(name='85', default=1)
    level89 = Level.objects.get(name='86')

    # Python
    level93 = Level.objects.get(name='100', default=1)
    level94 = Level.objects.get(name='102', default=1)
    level95 = Level.objects.get(name='101', default=1)
    level96 = Level.objects.get(name='103', default=1)
    level98 = Level.objects.get(name='104', default=1)
    level99 = Level.objects.get(name='105', default=1)

    # Limited Blocks
    level52 = level52()
    level53 = level53()
    level54 = level54()
    level55 = level55()
    level56 = level56()
    level57 = level57()
    level58 = level58()
   
    level51.next_level = level52
    level52.next_level = level53
    level53.next_level = level54
    level54.next_level = level55
    level55.next_level = level56
    level56.next_level = level57
    level57.next_level = level58
    level58.next_level = level59
    level59.next_level = level60

    level51.name = '51'
    level59.name = '59'
    level60.name = '60'

    level51.save()
    level52.save()
    level53.save()
    level54.save()
    level55.save()
    level56.save()
    level57.save()
    level58.save()
    level59.save()
    level60.save()

    limited_blocks_episode = Episode.objects.get(name="Limited Blocks")
    limited_blocks_episode.first_level = level51
    limited_blocks_episode.save()
   
    # Procedures
    level61 = level61()
    level64 = level64()
    level66 = level66()

    level61.next_level = level62
    level62.next_level = level63
    level63.next_level = level64
    level64.next_level = level65
    level65.next_level = level66
    level66.next_level = level67
    level67.next_level = None

    level62.name = '62'
    level63.name = '63'
    level65.name = '65'
    level67.name = '67'

    level61.save()
    level62.save()
    level63.save()
    level64.save()
    level65.save()
    level66.save()
    level67.save()

    procedures_episode = Episode.objects.get(name="Procedures")
    procedures_episode.first_level = level61
    procedures_episode.save()

    # Puzzles
    level72 = level72()
    level73 = level73()
    level74 = level74()
    level75 = level75()

    level79 = level79()

    level68.name = '68'
    level69.name = '69'
    level70.name = '70'
    level71.name = '71'

    level68.next_level = level69
    level69.next_level = level70
    level70.next_level = level71
    level71.next_level = level72
    level72.next_level = level73
    level73.next_level = level74
    level74.next_level = level75

    level68.save()
    level69.save()
    level70.save()
    level71.save()
    level72.save()
    level73.save()
    level74.save()
    level75.save()

    blockly_brain_teasers_episode = Episode.objects.get(name="Blockly Brain Teasers")
    blockly_brain_teasers_episode.first_level = level68
    blockly_brain_teasers_episode.save()

    # Introduction to Python
    level80 = level80()
    level84 = level84()
    level88 = level88()
    level90 = level90()
    level91 = level91()

    level80.next_level = level81
    level81.next_level = level82
    level82.next_level = level83
    level83.next_level = level84
    level84.next_level = level85
    level85.next_level = level86
    level86.next_level = level87
    level87.next_level = level88
    level88.next_level = level89
    level89.next_level = level90
    level90.next_level = level91
    level91.next_level = None

    level80.model_solution = '[]'
    level81.model_solution = '[]'
    level82.model_solution = '[]'
    level83.model_solution = '[]'
    level84.model_solution = '[]'
    level85.model_solution = '[]'
    level86.model_solution = '[]'
    level87.model_solution = '[]'
    level88.model_solution = '[]'
    level89.model_solution = '[]'
    level90.model_solution = '[]'
    level91.model_solution = '[]'

    level81.name = '81'
    level82.name = '82'
    level83.name = '83'
    level85.name = '85'
    level86.name = '86'
    level87.name = '87'
    level89.name = '89'

    level80.save()
    level81.save()
    level82.save()
    level83.save()
    level84.save()
    level85.save()
    level86.save()
    level87.save()
    level88.save()
    level89.save()
    level90.save()
    level91.save()

    introduction_to_python_episode = Episode.objects.get(name="Introduction to Python")
    introduction_to_python_episode.first_level = level80
    introduction_to_python_episode.save()

    # Python
    level92 = level92()
    level97 = level97()
    level100 = level100()
    level101 = level101()
    level102 = level102()
    level103 = level103()
    level104 = level104()
    level105 = level105()
    level106 = level106()
    level107 = level107()
    level108 = level108()
    level109 = level109()

    level92.next_level = level93
    level93.next_level = level94
    level94.next_level = level95
    level95.next_level = level96
    level96.next_level = level97
    level97.next_level = level98
    level98.next_level = level99
    level99.next_level = level100
    level100.next_level = level101
    level101.next_level = level102
    level102.next_level = level103
    level103.next_level = level104
    level104.next_level = level105
    level105.next_level = level106
    level106.next_level = level107
    level107.next_level = level108
    level108.next_level = level109
    level109.next_level = None

    level93.name = '93'
    level94.name = '94'
    level95.name = '95'
    level96.name = '96'
    level98.name = '98'
    level99.name = '99'

    level92.save()
    level93.save()
    level94.save()
    level95.save()
    level96.save()
    level97.save()
    level98.save()
    level99.save()
    level100.save()
    level101.save()
    level102.save()
    level103.save()
    level104.save()
    level105.save()
    level106.save()
    level107.save()
    level108.save()
    level109.save()

    python_episode = Episode.objects.get(name="Python")
    python_episode.first_level = level92
    python_episode.save()

    dead_end = Block.objects.get(type='dead_end')
    LevelBlock.objects.get(level=level59, type=dead_end).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0024_fix_levels_54_63'),
    ]

    operations = [
        migrations.RunPython(reorder_episodes),
        migrations.RunPython(fix_levels)
    ]
