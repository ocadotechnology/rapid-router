# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

import json

from game.level_management import set_decor, set_blocks

def add_levels(apps, schema_editor):

    Level = apps.get_model('game', 'Level')
    Episode = apps.get_model('game', 'Episode')
    Theme = apps.get_model('game', 'Theme')
    Character = apps.get_model('game', 'Character')

    grass = Theme.objects.get(name='grass')
    snow = Theme.objects.get(name='snow')
    farm = Theme.objects.get(name='farm')
    city = Theme.objects.get(name='city')

    van = Character.objects.get(name='Van')

    level53 = Level(
        name="53", blocklyEnabled=True, character=van, default=True,
        destinations="[[7,4]]", direct_drive=False, fuel_gauge=True,
        max_fuel=50, origin='{"coordinate":[0,4],"direction":"E"}',
        path='[{"coordinate":[0,4],"connectedNodes":[1]},{"coordinate":[1,4],"connectedNodes":[0,3,2,14]},{"coordinate":[2,4],"connectedNodes":[1,9,4]},{"coordinate":[1,5],"connectedNodes":[17,1]},{"coordinate":[3,4],"connectedNodes":[2,10,5,15]},{"coordinate":[4,4],"connectedNodes":[4,11,6]},{"coordinate":[5,4],"connectedNodes":[5,12,7,16]},{"coordinate":[6,4],"connectedNodes":[6,13,8,29]},{"coordinate":[7,4],"connectedNodes":[7]},{"coordinate":[2,5],"connectedNodes":[2]},{"coordinate":[3,5],"connectedNodes":[19,4]},{"coordinate":[4,5],"connectedNodes":[5]},{"coordinate":[5,5],"connectedNodes":[21,6]},{"coordinate":[6,5],"connectedNodes":[7]},{"coordinate":[1,3],"connectedNodes":[1,22]},{"coordinate":[3,3],"connectedNodes":[4]},{"coordinate":[5,3],"connectedNodes":[6]},{"coordinate":[1,6],"connectedNodes":[18,3]},{"coordinate":[2,6],"connectedNodes":[17,19]},{"coordinate":[3,6],"connectedNodes":[18,20,10]},{"coordinate":[4,6],"connectedNodes":[19,21]},{"coordinate":[5,6],"connectedNodes":[20,12]},{"coordinate":[1,2],"connectedNodes":[14,23]},{"coordinate":[2,2],"connectedNodes":[22,24]},{"coordinate":[3,2],"connectedNodes":[23,25]},{"coordinate":[4,2],"connectedNodes":[24,26]},{"coordinate":[5,2],"connectedNodes":[25,27]},{"coordinate":[6,2],"connectedNodes":[26,29,28]},{"coordinate":[7,2],"connectedNodes":[27]},{"coordinate":[6,3],"connectedNodes":[7,27]}]',
        pythonEnabled=False, theme=farm, model_solution='[5]',
        traffic_lights='[]',
    )
    level53.save()
    set_decor(level53, json.loads('[{"url":"decor/farm/tree1.svg","height":100,"width":100,"y":511,"x":9,"decorName":"tree1"},{"url":"decor/farm/tree1.svg","height":100,"width":100,"y":400,"x":813,"decorName":"tree1"},{"url":"decor/farm/crops.svg","height":100,"width":150,"y":507,"x":712,"decorName":"pond"},{"url":"decor/farm/crops.svg","height":100,"width":150,"y":290,"x":701,"decorName":"pond"},{"url":"decor/farm/bush.svg","height":30,"width":50,"y":373,"x":191,"decorName":"bush"},{"url":"decor/farm/bush.svg","height":30,"width":50,"y":373,"x":257,"decorName":"bush"}]'))
    set_blocks(level53, json.loads('[{"type":"turn_left","number":2},{"type":"turn_around","number":1},{"type":"controls_repeat_until","number":1},{"type":"at_destination","number":1},{"type":"dead_end","number":1}]'))

    level54 = Level(
        name='54',
        default=True,
        path='[{"coordinate":[2,3],"connectedNodes":[4]},{"coordinate":[4,3],"connectedNodes":[4,2]},{"coordinate":[5,3],"connectedNodes":[1,5,3]},{"coordinate":[5,2],"connectedNodes":[2]},{"coordinate":[3,3],"connectedNodes":[0,11,1]},{"coordinate":[5,4],"connectedNodes":[6,2]},{"coordinate":[5,5],"connectedNodes":[8,7,5]},{"coordinate":[6,5],"connectedNodes":[6]},{"coordinate":[4,5],"connectedNodes":[9,6]},{"coordinate":[3,5],"connectedNodes":[10,8,11]},{"coordinate":[3,6],"connectedNodes":[9]},{"coordinate":[3,4],"connectedNodes":[9,4]}]',
        traffic_lights='[]',
        destinations='[[3,5]]',
        origin='{"coordinate":[2,3],"direction":"E"}',
        max_fuel=50,
        theme=Theme.objects.get(id=1),
        character=Character.objects.get(name='Van'),
        blocklyEnabled=True,
        pythonEnabled=False,
        model_solution='[5]',
    )
    level54.save()
    set_decor(level54, json.loads('[{"x":400,"y":408,"decorName":"tree2"},{"x":99,"y":482,"decorName":"bush"},{"x":190,"y":437,"decorName":"tree2"},{"x":151,"y":496,"decorName":"tree2"},{"x":116,"y":430,"decorName":"tree2"},{"x":357,"y":185,"decorName":"tree2"},{"x":283,"y":153,"decorName":"tree2"},{"x":602,"y":367,"decorName":"tree2"},{"x":683,"y":394,"decorName":"tree2"},{"x":455,"y":633,"decorName":"tree2"},{"x":528,"y":625,"decorName":"tree2"},{"x":495,"y":691,"decorName":"tree2"},{"x":610,"y":599,"decorName":"tree2"},{"x":45,"y":210,"decorName":"bush"},{"x":377,"y":747,"decorName":"bush"},{"x":673,"y":224,"decorName":"bush"},{"x":576,"y":92,"decorName":"bush"},{"x":111,"y":102,"decorName":"bush"},{"x":116,"y":284,"decorName":"bush"},{"x":157,"y":701,"decorName":"bush"}]'))
    set_blocks(level54, json.loads('[{"type":"move_forwards","number":2},{"type":"turn_right","number":1},{"type":"turn_around","number":1},{"type":"controls_repeat","number":1}]'))

    level60 = Level(
        name="60", blocklyEnabled=True, character=van, default=True,
        destinations="[[3,3]]", direct_drive=False, fuel_gauge=True,
        max_fuel=9, origin='{"coordinate":[8,3],"direction":"W"}',
        path='[{"coordinate":[8,3],"connectedNodes":[1]},{"coordinate":[7,3],"connectedNodes":[2,0]},{"coordinate":[6,3],"connectedNodes":[3,1]},{"coordinate":[5,3],"connectedNodes":[4,2]},{"coordinate":[4,3],"connectedNodes":[5,3]},{"coordinate":[3,3],"connectedNodes":[6,4]},{"coordinate":[2,3],"connectedNodes":[7,5]},{"coordinate":[1,3],"connectedNodes":[9,6,10]},{"coordinate":[1,5],"connectedNodes":[9]},{"coordinate":[1,4],"connectedNodes":[8,7]},{"coordinate":[1,2],"connectedNodes":[7,11]},{"coordinate":[1,1],"connectedNodes":[10]}]',
        pythonEnabled=False, theme=city, model_solution='[5]',
        traffic_lights='[{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":1,"y":4},"direction":"N","startTime":0,"startingState":"RED"}]',
    )
    level60.save()
    set_decor(level60, json.loads('[{"url":"decor/city/hospital.svg","height":157,"width":140,"y":173,"x":426,"decorName":"pond"},{"url":"decor/city/shop.svg","height":70,"width":70,"y":408,"x":218,"decorName":"tree1"},{"url":"decor/city/shop.svg","height":70,"width":70,"y":206,"x":209,"decorName":"tree1"},{"url":"decor/city/school.svg","height":100,"width":100,"y":563,"x":87,"decorName":"tree2"},{"url":"decor/city/bush.svg","height":50,"width":50,"y":504,"x":190,"decorName":"bush"},{"url":"decor/city/bush.svg","height":50,"width":50,"y":560,"x":188,"decorName":"bush"},{"url":"decor/city/bush.svg","height":50,"width":50,"y":532,"x":243,"decorName":"bush"}]'))
    set_blocks(level60, json.loads('[{"type":"move_forwards","number":2},{"type":"turn_left","number":1},{"type":"turn_around","number":1},{"type":"controls_repeat_while","number":null},{"type":"road_exists","number":null},{"type":"dead_end","number":1}]'))

    level61 = Level(
        name="61", blocklyEnabled=True, character=van, default=True,
        destinations='[[7,6]]', direct_drive=False, fuel_gauge=True,
        max_fuel=16, origin='{"coordinate":[1,6],"direction":"S"}',
        path='[{"coordinate":[1,6],"connectedNodes":[1]},{"coordinate":[1,5],"connectedNodes":[0,2]},{"coordinate":[1,4],"connectedNodes":[1,22,3]},{"coordinate":[1,3],"connectedNodes":[2,4]},{"coordinate":[1,2],"connectedNodes":[3,5]},{"coordinate":[1,1],"connectedNodes":[4,6]},{"coordinate":[2,1],"connectedNodes":[5,7]},{"coordinate":[3,1],"connectedNodes":[6,25,8]},{"coordinate":[4,1],"connectedNodes":[7,9]},{"coordinate":[5,1],"connectedNodes":[8,10]},{"coordinate":[6,1],"connectedNodes":[9,21,11]},{"coordinate":[7,1],"connectedNodes":[10,12]},{"coordinate":[8,1],"connectedNodes":[11,13]},{"coordinate":[8,2],"connectedNodes":[14,12]},{"coordinate":[8,3],"connectedNodes":[15,13]},{"coordinate":[8,4],"connectedNodes":[18,16,14]},{"coordinate":[8,5],"connectedNodes":[17,15]},{"coordinate":[8,6],"connectedNodes":[28,16]},{"coordinate":[7,4],"connectedNodes":[19,15]},{"coordinate":[6,4],"connectedNodes":[27,18,20]},{"coordinate":[6,3],"connectedNodes":[19,21]},{"coordinate":[6,2],"connectedNodes":[20,10]},{"coordinate":[2,4],"connectedNodes":[2,23]},{"coordinate":[3,4],"connectedNodes":[22,26,24]},{"coordinate":[3,3],"connectedNodes":[23,25]},{"coordinate":[3,2],"connectedNodes":[24,7]},{"coordinate":[4,4],"connectedNodes":[23,27]},{"coordinate":[5,4],"connectedNodes":[26,19]},{"coordinate":[7,6],"connectedNodes":[17]}]',
        pythonEnabled=False, theme=grass, model_solution='[7]',
        traffic_lights='[{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":1,"y":5},"direction":"S","startTime":0,"startingState":"GREEN"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":3,"y":2},"direction":"S","startTime":0,"startingState":"RED"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":6,"y":3},"direction":"N","startTime":0,"startingState":"RED"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":6,"y":2},"direction":"S","startTime":0,"startingState":"GREEN"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":3,"y":3},"direction":"N","startTime":0,"startingState":"RED"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":4,"y":4},"direction":"W","startTime":0,"startingState":"GREEN"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":2,"y":4},"direction":"E","startTime":0,"startingState":"RED"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":8,"y":4},"direction":"N","startTime":0,"startingState":"RED"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":7,"y":4},"direction":"E","startTime":0,"startingState":"RED"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":4,"y":4},"direction":"E","startTime":0,"startingState":"RED"}]'
    )
    level61.save()
    set_decor(level61, json.loads('[{"url":"decor/grass/tree1.svg","height":100,"width":100,"y":497,"x":198,"decorName":"tree1"},{"url":"decor/grass/tree1.svg","height":100,"width":100,"y":499,"x":320,"decorName":"tree1"},{"url":"decor/grass/tree1.svg","height":100,"width":100,"y":505,"x":447,"decorName":"tree1"},{"url":"decor/grass/tree1.svg","height":100,"width":100,"y":494,"x":570,"decorName":"tree1"},{"url":"decor/grass/tree1.svg","height":100,"width":100,"y":495,"x":697,"decorName":"tree1"},{"url":"decor/grass/pond.svg","height":100,"width":150,"y":254,"x":430,"decorName":"pond"}]'))
    set_blocks(level61, json.loads('[{"type":"move_forwards","number":2},{"type":"turn_left","number":1},{"type":"turn_right","number":null},{"type":"turn_around","number":2},{"type":"wait","number":1},{"type":"controls_repeat_while","number":null},{"type":"road_exists","number":null},{"type":"dead_end","number":1}]'))

    level62 = Level(
        name="62", blocklyEnabled=True, character=van, default=True,
        destinations="[[7,3]]", direct_drive=False, fuel_gauge=True,
        max_fuel=14, origin='{"coordinate":[1,3],"direction":"E"}',
        path='[{"coordinate":[1,3],"connectedNodes":[22]},{"coordinate":[3,3],"connectedNodes":[22,23,2,24]},{"coordinate":[4,3],"connectedNodes":[1,8,3,9]},{"coordinate":[5,3],"connectedNodes":[2,25,4,26]},{"coordinate":[6,3],"connectedNodes":[3,10,5,11]},{"coordinate":[7,3],"connectedNodes":[4]},{"coordinate":[2,4],"connectedNodes":[18,23,22]},{"coordinate":[2,2],"connectedNodes":[22,24,20]},{"coordinate":[4,4],"connectedNodes":[14,2]},{"coordinate":[4,2],"connectedNodes":[2,17]},{"coordinate":[6,4],"connectedNodes":[25,12,4]},{"coordinate":[6,2],"connectedNodes":[26,4,15]},{"coordinate":[6,5],"connectedNodes":[13,28,10]},{"coordinate":[5,5],"connectedNodes":[14,12]},{"coordinate":[4,5],"connectedNodes":[19,13,8]},{"coordinate":[6,1],"connectedNodes":[16,11,29]},{"coordinate":[5,1],"connectedNodes":[17,15]},{"coordinate":[4,1],"connectedNodes":[21,9,16]},{"coordinate":[2,5],"connectedNodes":[27,19,6]},{"coordinate":[3,5],"connectedNodes":[18,14]},{"coordinate":[2,1],"connectedNodes":[30,7,21]},{"coordinate":[3,1],"connectedNodes":[20,17]},{"coordinate":[2,3],"connectedNodes":[0,6,1,7]},{"coordinate":[3,4],"connectedNodes":[6,1]},{"coordinate":[3,2],"connectedNodes":[7,1]},{"coordinate":[5,4],"connectedNodes":[10,3]},{"coordinate":[5,2],"connectedNodes":[3,11]},{"coordinate":[2,6],"connectedNodes":[18]},{"coordinate":[7,5],"connectedNodes":[12]},{"coordinate":[6,0],"connectedNodes":[15]},{"coordinate":[1,1],"connectedNodes":[20]}]',
        pythonEnabled=False, theme=snow, model_solution='[5]',
        traffic_lights='[{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":4,"y":4},"direction":"N","startTime":0,"startingState":"GREEN"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":4,"y":2},"direction":"S","startTime":0,"startingState":"GREEN"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":4,"y":3},"direction":"E","startTime":0,"startingState":"RED"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":2,"y":3},"direction":"E","startTime":0,"startingState":"RED"}]'
    )
    level62.save()
    set_decor(level62, json.loads('[{"url":"decor/snow/tree2.svg","height":100,"width":100,"y":418,"x":112,"decorName":"tree2"},{"url":"decor/snow/pond.svg","height":100,"width":150,"y":588,"x":302,"decorName":"pond"},{"url":"decor/snow/tree1.svg","height":100,"width":100,"y":418,"x":697,"decorName":"tree1"},{"url":"decor/snow/bush.svg","height":50,"width":50,"y":59,"x":560,"decorName":"bush"},{"url":"decor/snow/bush.svg","height":50,"width":50,"y":180,"x":297,"decorName":"bush"},{"url":"decor/snow/bush.svg","height":50,"width":50,"y":250,"x":371,"decorName":"bush"},{"url":"decor/snow/bush.svg","height":50,"width":50,"y":188,"x":358,"decorName":"bush"},{"url":"decor/snow/bush.svg","height":50,"width":50,"y":195,"x":493,"decorName":"bush"},{"url":"decor/snow/bush.svg","height":50,"width":50,"y":64,"x":116,"decorName":"bush"},{"url":"decor/snow/bush.svg","height":50,"width":50,"y":61,"x":176,"decorName":"bush"},{"url":"decor/snow/bush.svg","height":50,"width":50,"y":58,"x":243,"decorName":"bush"},{"url":"decor/snow/bush.svg","height":50,"width":50,"y":60,"x":307,"decorName":"bush"},{"url":"decor/snow/bush.svg","height":50,"width":50,"y":63,"x":370,"decorName":"bush"},{"url":"decor/snow/bush.svg","height":50,"width":50,"y":62,"x":434,"decorName":"bush"},{"url":"decor/snow/bush.svg","height":50,"width":50,"y":60,"x":494,"decorName":"bush"}]'))
    set_blocks(level62, json.loads('[{"type":"turn_left","number":2},{"type":"turn_right","number":1},{"type":"turn_around","number":1},{"type":"controls_repeat_while","number":null},{"type":"controls_repeat_until","number":1},{"type":"at_destination","number":1}]'))

    level63 = Level(
        name='63',
        default=True,
        path='[{"coordinate":[4,2],"connectedNodes":[4]},{"coordinate":[6,4],"connectedNodes":[2,6]},{"coordinate":[5,4],"connectedNodes":[1,3]},{"coordinate":[5,3],"connectedNodes":[2,4]},{"coordinate":[5,2],"connectedNodes":[0,3,5]},{"coordinate":[5,1],"connectedNodes":[4]},{"coordinate":[7,4],"connectedNodes":[1,7]},{"coordinate":[7,3],"connectedNodes":[6,8]},{"coordinate":[7,2],"connectedNodes":[9,7]},{"coordinate":[6,2],"connectedNodes":[8]}]',
        traffic_lights='[]',
        destinations='[[6,2]]',
        origin='{"coordinate":[4,2],"direction":"E"}',
        max_fuel=50,
        theme=Theme.objects.get(id=2),
        character=Character.objects.get(name='Van'),
        blocklyEnabled=True,
        pythonEnabled=False,
        model_solution='[7]',
    )
    level63.save()
    set_decor(level63, json.loads('[{"x":658,"y":505,"decorName":"tree2"},{"x":619,"y":611,"decorName":"tree2"},{"x":687,"y":700,"decorName":"tree2"},{"x":636,"y":356,"decorName":"bush"},{"x":473,"y":54,"decorName":"bush"},{"x":337,"y":227,"decorName":"bush"},{"x":265,"y":159,"decorName":"bush"},{"x":411,"y":0,"decorName":"bush"},{"x":412,"y":127,"decorName":"bush"},{"x":354,"y":80,"decorName":"bush"},{"x":207,"y":85,"decorName":"bush"},{"x":297,"y":15,"decorName":"bush"}]'))
    set_blocks(level63, json.loads('[{"type":"move_forwards","number":1},{"type":"turn_left","number":1},{"type":"turn_right","number":1},{"type":"turn_around","number":1},{"type":"controls_repeat_until"},{"type":"controls_if"},{"type":"at_destination"},{"type":"road_exists","number":2}]'))
    

    level60.next_level_id = level61.id
    level61.next_level_id = level62.id
    level62.next_level_id = level63.id
    level60.save()
    level61.save()
    level62.save()

    level52 = Level.objects.get(name="52")
    level52.next_level_id = level53.id
    level53.next_level_id = level54.id
    level52.save()
    level53.save()

    episode9 = Episode(name="Hard puzzles!", first_level=level60, r_branchiness=0.5,
                       r_loopiness=0.1, r_num_tiles=35, r_curviness=0.2, r_pythonEnabled=0,
                       r_blocklyEnabled=1, r_trafficLights=1, in_development=True)
    episode9.save()

class Migration(migrations.Migration):

    dependencies = [
        ('game', '0015_remove_level_decor'),
    ]

    operations = [
        migrations.RunPython(add_levels),
    ]
