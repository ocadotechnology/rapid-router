# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def add_levels(apps, schema_editor):

    Level = apps.get_model('game', 'Level')
    Theme = apps.get_model('game', 'Theme')
    Character = apps.get_model('game', 'Character')

    grass = Theme.objects.get(name='grass')
    snow = Theme.objects.get(name='snow')
    farm = Theme.objects.get(name='farm')
    city = Theme.objects.get(name='city')

    van = Character.objects.get(name='Van')
    dee = Character.objects.get(name='Dee')

    level1 = Level(name='1', anonymous=False, blocklyEnabled=True, character=van, default=True,
                   decor='[{"coordinate":{"x":100,"y":100}, "url":"/static/game/image/tree1.svg"}]',
                   destinations='[[2, 3]]', direct_drive=True, fuel_gauge=False, max_fuel=50,
                   model_solution='[1]', origin='{"coordinate":[0, 3], "direction":"E"}',
                   path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[2,3],"connectedNodes":[1]}]',
                   pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level2 = Level(name='2', anonymous=False, blocklyEnabled=True, character=van, default=True,
                   decor='[{"coordinate":{"x":67,"y":570},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":663,"y":443},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":192,"y":58},"url":"/static/game/image/bush.svg"}]',
                   destinations='[[4, 3]]', direct_drive=True, fuel_gauge=False, max_fuel=50,
                   model_solution='[3]', origin='{"coordinate":[0, 3], "direction":"E"}',
                   path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[2,3],"connectedNodes":[1,3]},{"coordinate":[3,3],"connectedNodes":[2,4]},{"coordinate":[4,3],"connectedNodes":[3]}]',
                   pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level3 = Level(name='3', anonymous=False, blocklyEnabled=True, character=van, default=True,
                   decor='[{"coordinate":{"x":0,"y":398},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":100,"y":397},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":201,"y":397},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":300,"y":404},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":401,"y":409},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":499,"y":398},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":601,"y":403},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":704,"y":402},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":804,"y":398},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":903,"y":401},"url":"/static/game/image/tree2.svg"}]',
                   destinations='[[2, 2]]', direct_drive=True, fuel_gauge=False, max_fuel=50,
                   model_solution='[2]', origin='{"coordinate":[0, 3], "direction":"E"}',
                   path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[2,3],"connectedNodes":[1,3]},{"coordinate":[2,2],"connectedNodes":[2]}]',
                   pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level4 = Level(name='4', anonymous=False, blocklyEnabled=True, character=van, default=True,
                   decor='[{"coordinate":{"x":531,"y":624},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":442,"y":632},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":531,"y":498},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":495,"y":564},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":584,"y":565},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":615,"y":630},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":669,"y":565},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":621,"y":497},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":500,"y":694},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":300,"y":633},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":380,"y":704},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":365,"y":596},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":287,"y":713},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":596,"y":714},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":711,"y":704},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":813,"y":702},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":906,"y":700},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":897,"y":607},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":807,"y":608},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":719,"y":636},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":857,"y":659},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":766,"y":701},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":665,"y":694},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":851,"y":568},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":766,"y":555},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":155,"y":680},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":216,"y":541},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":530,"y":402},"url":"/static/game/image/tree1.svg"}]',
                   destinations='[[4, 5]]', direct_drive=True, fuel_gauge=False, max_fuel=50,
                   model_solution='[5]', origin='{"coordinate":[0, 3], "direction":"E"}',
                   path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[2,3],"connectedNodes":[1,3]},{"coordinate":[3,3],"connectedNodes":[2,4]},{"coordinate":[4,3],"connectedNodes":[3,5]},{"coordinate":[4,4],"connectedNodes":[6,4]},{"coordinate":[4,5],"connectedNodes":[5]}]',
                   pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level5 = Level(name='5', anonymous=False, blocklyEnabled=True, character=van, default=True,
                   decor='[{"coordinate":{"x":19,"y":459},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":135,"y":564},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":240,"y":666},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":52,"y":184},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":208,"y":291},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":338,"y":410},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":497,"y":519},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":467,"y":701},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":898,"y":26},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":755,"y":22},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":901,"y":168},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":900,"y":322},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":607,"y":22},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":893,"y":638},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":899,"y":479},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":445,"y":23},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":293,"y":23},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":126,"y":23},"url":"/static/game/image/bush.svg"}]',
                   destinations='[[4, 6]]', direct_drive=True, fuel_gauge=False, max_fuel=50,
                   model_solution='[6]', origin='{"coordinate":[0, 3], "direction":"E"}',
                   path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[1,4],"connectedNodes":[1,3]},{"coordinate":[2,4],"connectedNodes":[2,4]},{"coordinate":[2,5],"connectedNodes":[3,5]},{"coordinate":[3,5],"connectedNodes":[4,6]},{"coordinate":[3,6],"connectedNodes":[5,7]},{"coordinate":[4,6],"connectedNodes":[6]}]',
                   pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level6 = Level(name='6', anonymous=False, blocklyEnabled=True, character=van, default=True,
                   decor='[{"coordinate":{"x":224,"y":654},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":87,"y":656},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":63,"y":591},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":163,"y":562},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":100,"y":506},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":153,"y":624},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":608,"y":480},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":584,"y":366},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":591,"y":220},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":676,"y":254},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":689,"y":351},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":673,"y":509},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":557,"y":574},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":104,"y":200},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":301,"y":199},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":201,"y":201},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":102,"y":102},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":201,"y":102},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":301,"y":103},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":147,"y":197},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":240,"y":127},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":154,"y":121},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":262,"y":215},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":328,"y":155},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":147,"y":715},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":65,"y":144},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":78,"y":220},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":262,"y":70},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":371,"y":85},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":64,"y":63},"url":"/static/game/image/tree2.svg"}]',
                   destinations='[[6, 1]]', direct_drive=True, fuel_gauge=False, max_fuel=50,
                   model_solution='[10]', origin='{"coordinate":[0, 4], "direction":"E"}',
                   path='[{"coordinate":[0,4],"connectedNodes":[1]},{"coordinate":[1,4],"connectedNodes":[0,2]},{"coordinate":[2,4],"connectedNodes":[1,3]},{"coordinate":[3,4],"connectedNodes":[2,4]},{"coordinate":[3,5],"connectedNodes":[5,3]},{"coordinate":[4,5],"connectedNodes":[4,6]},{"coordinate":[5,5],"connectedNodes":[5,7]},{"coordinate":[5,4],"connectedNodes":[6,8]},{"coordinate":[5,3],"connectedNodes":[7,9]},{"coordinate":[5,2],"connectedNodes":[8,10]},{"coordinate":[5,1],"connectedNodes":[9,11]},{"coordinate":[6,1],"connectedNodes":[10]}]',
                   pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level7 = Level(name='7', anonymous=False, blocklyEnabled=True, character=van, default=True,
                   decor='[{"coordinate":{"x":6,"y":424},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":5,"y":559},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":5,"y":688},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":676,"y":644},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":588,"y":633},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":686,"y":578},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":766,"y":659},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":625,"y":669},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":801,"y":696},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":610,"y":576},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":583,"y":524},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":762,"y":584},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":682,"y":511},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":699,"y":716},"url":"/static/game/image/tree2.svg"}]',
                   destinations='[[5, 3]]', direct_drive=True, fuel_gauge=False, max_fuel=50,
                   model_solution='[12]', origin='{"coordinate":[0, 3], "direction":"E"}',
                   path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[1,4],"connectedNodes":[1,3]},{"coordinate":[1,5],"connectedNodes":[2,4]},{"coordinate":[1,6],"connectedNodes":[3,5]},{"coordinate":[2,6],"connectedNodes":[4,6]},{"coordinate":[2,5],"connectedNodes":[5,7]},{"coordinate":[3,5],"connectedNodes":[6,8]},{"coordinate":[3,4],"connectedNodes":[7,9]},{"coordinate":[3,3],"connectedNodes":[8,10]},{"coordinate":[3,2],"connectedNodes":[9,11]},{"coordinate":[4,2],"connectedNodes":[10,12]},{"coordinate":[4,3],"connectedNodes":[11,13]},{"coordinate":[5,3],"connectedNodes":[12]}]',
                   pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level8 = Level(name='8', anonymous=False, blocklyEnabled=True, character=van, default=True,
                   decor='[{"coordinate":{"x":484,"y":438},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":660,"y":410},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":111,"y":589},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":39,"y":491},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":569,"y":267},"url":"/static/game/image/pond.svg"},{"coordinate":{"x":385,"y":307},"url":"/static/game/image/tree1.svg"}]',
                   destinations='[[4, 1]]', direct_drive=True, fuel_gauge=False, max_fuel=50,
                   model_solution='[8]', origin='{"coordinate":[3, 6], "direction":"S"}',
                   path='[{"coordinate":[3,6],"connectedNodes":[1]},{"coordinate":[3,5],"connectedNodes":[0,2]},{"coordinate":[3,4],"connectedNodes":[3,1]},{"coordinate":[2,4],"connectedNodes":[4,2]},{"coordinate":[1,4],"connectedNodes":[3,5]},{"coordinate":[1,3],"connectedNodes":[4,6]},{"coordinate":[1,2],"connectedNodes":[5,7]},{"coordinate":[2,2],"connectedNodes":[6,8]},{"coordinate":[3,2],"connectedNodes":[7,9]},{"coordinate":[4,2],"connectedNodes":[8,10]},{"coordinate":[4,1],"connectedNodes":[9]}]',
                   pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level9 = Level(name='9', anonymous=False, blocklyEnabled=True, character=van, default=True,
                   decor='[{"coordinate":{"x":167,"y":207},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":263,"y":203},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":364,"y":202},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":571,"y":203},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":465,"y":199},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":29,"y":433},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":505,"y":652},"url":"/static/game/image/bush.svg"}]',
                   destinations='[[8, 1]]', direct_drive=True, fuel_gauge=False, max_fuel=50,
                   model_solution='[13]', origin='{"coordinate":[6, 3], "direction":"W"}',
                   path='[{"coordinate":[6,3],"connectedNodes":[1]},{"coordinate":[5,3],"connectedNodes":[2,0]},{"coordinate":[4,3],"connectedNodes":[3,1]},{"coordinate":[3,3],"connectedNodes":[4,2]},{"coordinate":[2,3],"connectedNodes":[5,3]},{"coordinate":[1,3],"connectedNodes":[4,6]},{"coordinate":[1,2],"connectedNodes":[5,7]},{"coordinate":[1,1],"connectedNodes":[6,8]},{"coordinate":[2,1],"connectedNodes":[7,9]},{"coordinate":[3,1],"connectedNodes":[8,10]},{"coordinate":[4,1],"connectedNodes":[9,11]},{"coordinate":[5,1],"connectedNodes":[10,12]},{"coordinate":[6,1],"connectedNodes":[11,13]},{"coordinate":[7,1],"connectedNodes":[12,14]},{"coordinate":[8,1],"connectedNodes":[13]}]',
                   pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level10 = Level(name='10', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    decor='[{"coordinate":{"x":99,"y":699},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":201,"y":700},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":54,"y":634},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":143,"y":632},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":-5,"y":703},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":298,"y":697},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":94,"y":555},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":504,"y":389},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":-13,"y":584},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":17,"y":503},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":484,"y":604},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":582,"y":600},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":599,"y":413},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":606,"y":501},"url":"/static/game/image/bush.svg"}]',
                    destinations='[[3, 3]]', direct_drive=True, fuel_gauge=False, max_fuel=50,
                    model_solution='[7]', origin='{"coordinate":[5, 5], "direction":"W"}',
                    path='[{"coordinate":[5,5],"connectedNodes":[1]},{"coordinate":[4,5],"connectedNodes":[2,0]},{"coordinate":[4,6],"connectedNodes":[3,1]},{"coordinate":[3,6],"connectedNodes":[4,2]},{"coordinate":[2,6],"connectedNodes":[3,5]},{"coordinate":[2,5],"connectedNodes":[4,6]},{"coordinate":[2,4],"connectedNodes":[5,7]},{"coordinate":[2,3],"connectedNodes":[6,8]},{"coordinate":[3,3],"connectedNodes":[7]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level11 = Level(name='11', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    decor='[{"coordinate":{"x":396,"y":304},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":600,"y":302},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":242,"y":301},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":601,"y":434},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":599,"y":701},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":598,"y":580},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":0,"y":700},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":116,"y":701},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":236,"y":698},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":359,"y":697},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":480,"y":698},"url":"/static/game/image/tree2.svg"}]',
                    destinations='[[1, 3]]', direct_drive=True, fuel_gauge=False, max_fuel=50,
                    model_solution='[12]', origin='{"coordinate":[3, 4], "direction":"W"}',
                    path='[{"coordinate":[3,4],"connectedNodes":[1]},{"coordinate":[2,4],"connectedNodes":[2,0]},{"coordinate":[2,5],"connectedNodes":[3,1]},{"coordinate":[3,5],"connectedNodes":[2,4]},{"coordinate":[4,5],"connectedNodes":[3,5]},{"coordinate":[5,5],"connectedNodes":[4,6]},{"coordinate":[5,4],"connectedNodes":[5,7]},{"coordinate":[5,3],"connectedNodes":[6,8]},{"coordinate":[5,2],"connectedNodes":[9,7]},{"coordinate":[4,2],"connectedNodes":[10,8]},{"coordinate":[3,2],"connectedNodes":[11,9]},{"coordinate":[2,2],"connectedNodes":[12,10]},{"coordinate":[1,2],"connectedNodes":[13,11]},{"coordinate":[1,3],"connectedNodes":[12]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level12 = Level(name='12', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    decor='[{"coordinate":{"x":331,"y":509},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":267,"y":489},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":284,"y":561},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":402,"y":479},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":452,"y":532},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":418,"y":583},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":376,"y":545},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":356,"y":606},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":164,"y":86},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":-15,"y":-11},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":279,"y":-20},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":202,"y":4},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":73,"y":109},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":-4,"y":84},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":63,"y":18},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":119,"y":2},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":381,"y":-14},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":323,"y":40},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":565,"y":81},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":493,"y":148},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":445,"y":-23},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":417,"y":72},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":549,"y":7},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":265,"y":120},"url":"/static/game/image/tree2.svg"}]',
                    destinations='[[1, 3]]', direct_drive=True, fuel_gauge=False, max_fuel=50,
                    model_solution='[17]', origin='{"coordinate":[5, 7], "direction":"W"}',
                    path='[{"coordinate":[5,7],"connectedNodes":[17]},{"coordinate":[2,6],"connectedNodes":[18,2]},{"coordinate":[2,5],"connectedNodes":[3,1]},{"coordinate":[1,5],"connectedNodes":[2,4]},{"coordinate":[1,4],"connectedNodes":[3,5]},{"coordinate":[2,4],"connectedNodes":[4,6]},{"coordinate":[3,4],"connectedNodes":[5,7]},{"coordinate":[4,4],"connectedNodes":[6,8]},{"coordinate":[4,3],"connectedNodes":[7,9]},{"coordinate":[4,2],"connectedNodes":[10,8]},{"coordinate":[3,2],"connectedNodes":[11,9]},{"coordinate":[2,2],"connectedNodes":[12,10]},{"coordinate":[1,2],"connectedNodes":[13,11]},{"coordinate":[1,3],"connectedNodes":[12]},{"coordinate":[1,7],"connectedNodes":[15,18]},{"coordinate":[2,7],"connectedNodes":[14,16]},{"coordinate":[3,7],"connectedNodes":[15,17]},{"coordinate":[4,7],"connectedNodes":[16,0]},{"coordinate":[1,6],"connectedNodes":[14,1]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level13 = Level(name='13', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    decor='[{"coordinate":{"x":48,"y":658},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":49,"y":553},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":48,"y":446},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":50,"y":340},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":52,"y":235},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":406,"y":512},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":496,"y":492},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":500,"y":302},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":501,"y":245},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":500,"y":193},"url":"/static/game/image/bush.svg"}]',
                    destinations='[[0, 1]]', direct_drive=True, fuel_gauge=False, max_fuel=50,
                    model_solution='[11]', origin='{"coordinate":[2, 7], "direction":"S"}',
                    path='[{"coordinate":[2,7],"connectedNodes":[1]},{"coordinate":[2,6],"connectedNodes":[0,2]},{"coordinate":[3,6],"connectedNodes":[1,3,10]},{"coordinate":[4,6],"connectedNodes":[2,4]},{"coordinate":[5,6],"connectedNodes":[3,5]},{"coordinate":[6,6],"connectedNodes":[4,6]},{"coordinate":[6,5],"connectedNodes":[5,7]},{"coordinate":[6,4],"connectedNodes":[13,6,8]},{"coordinate":[6,3],"connectedNodes":[7,9]},{"coordinate":[6,2],"connectedNodes":[8,14]},{"coordinate":[3,5],"connectedNodes":[2,11]},{"coordinate":[3,4],"connectedNodes":[10,12]},{"coordinate":[4,4],"connectedNodes":[11,13,18]},{"coordinate":[5,4],"connectedNodes":[12,7]},{"coordinate":[6,1],"connectedNodes":[15,9]},{"coordinate":[5,1],"connectedNodes":[16,14]},{"coordinate":[4,1],"connectedNodes":[19,17,15]},{"coordinate":[4,2],"connectedNodes":[18,16]},{"coordinate":[4,3],"connectedNodes":[12,17]},{"coordinate":[3,1],"connectedNodes":[20,16]},{"coordinate":[2,1],"connectedNodes":[21,19]},{"coordinate":[1,1],"connectedNodes":[22,20]},{"coordinate":[0,1],"connectedNodes":[21]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level14 = Level(name='14', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    decor='[{"coordinate":{"x":209,"y":392},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":307,"y":302},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":281,"y":187},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":498,"y":197},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":771,"y":662},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":866,"y":557},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":754,"y":491},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":890,"y":310},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":725,"y":353},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":780,"y":87},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":862,"y":177},"url":"/static/game/image/tree1.svg"}]',
                    destinations='[[2, 5]]', direct_drive=True, fuel_gauge=False, max_fuel=50,
                    model_solution='[7]', origin='{"coordinate":[7, 2], "direction":"W"}',
                    path='[{"coordinate":[7,2],"connectedNodes":[27]},{"coordinate":[4,2],"connectedNodes":[4,14]},{"coordinate":[3,1],"connectedNodes":[3,14]},{"coordinate":[2,1],"connectedNodes":[7,2]},{"coordinate":[4,3],"connectedNodes":[10,5,1]},{"coordinate":[5,3],"connectedNodes":[4,6]},{"coordinate":[6,3],"connectedNodes":[5,11,27]},{"coordinate":[1,1],"connectedNodes":[8,3]},{"coordinate":[1,2],"connectedNodes":[21,7]},{"coordinate":[3,4],"connectedNodes":[16,10]},{"coordinate":[4,4],"connectedNodes":[9,4]},{"coordinate":[6,4],"connectedNodes":[12,6]},{"coordinate":[6,5],"connectedNodes":[20,11]},{"coordinate":[5,1],"connectedNodes":[14,15]},{"coordinate":[4,1],"connectedNodes":[2,1,13]},{"coordinate":[6,1],"connectedNodes":[13,27]},{"coordinate":[3,5],"connectedNodes":[26,17,9]},{"coordinate":[3,6],"connectedNodes":[18,16]},{"coordinate":[4,6],"connectedNodes":[17,19]},{"coordinate":[5,6],"connectedNodes":[18,20]},{"coordinate":[6,6],"connectedNodes":[19,12]},{"coordinate":[2,2],"connectedNodes":[8,22]},{"coordinate":[2,3],"connectedNodes":[23,21]},{"coordinate":[1,3],"connectedNodes":[24,22]},{"coordinate":[1,4],"connectedNodes":[25,23]},{"coordinate":[1,5],"connectedNodes":[26,24]},{"coordinate":[2,5],"connectedNodes":[25,16]},{"coordinate":[6,2],"connectedNodes":[6,0,15]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level15 = Level(name='15', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    decor='[{"coordinate":{"x":406,"y":205},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":296,"y":296},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":98,"y":661},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":93,"y":592},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":15,"y":608},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":46,"y":697},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":579,"y":501},"url":"/static/game/image/bush.svg"}]',
                    destinations='[[5, 5], [7, 2]]', direct_drive=True, fuel_gauge=False,
                    max_fuel=50, model_solution='[13]',
                    origin='{"coordinate":[2, 7], "direction":"S"}',
                    path='[{"coordinate":[2,7],"connectedNodes":[1]},{"coordinate":[2,6],"connectedNodes":[0,4,2]},{"coordinate":[2,5],"connectedNodes":[3,1]},{"coordinate":[1,5],"connectedNodes":[9,2]},{"coordinate":[3,6],"connectedNodes":[1,5]},{"coordinate":[4,6],"connectedNodes":[4,6]},{"coordinate":[4,7],"connectedNodes":[7,5]},{"coordinate":[5,7],"connectedNodes":[6,8]},{"coordinate":[5,6],"connectedNodes":[7,13]},{"coordinate":[0,5],"connectedNodes":[3,10]},{"coordinate":[0,4],"connectedNodes":[9,11]},{"coordinate":[1,4],"connectedNodes":[10,12]},{"coordinate":[2,4],"connectedNodes":[11,15]},{"coordinate":[5,5],"connectedNodes":[8,14]},{"coordinate":[5,4],"connectedNodes":[16,13,17]},{"coordinate":[3,4],"connectedNodes":[12,16]},{"coordinate":[4,4],"connectedNodes":[15,14,21]},{"coordinate":[5,3],"connectedNodes":[21,14,18]},{"coordinate":[5,2],"connectedNodes":[17,19]},{"coordinate":[6,2],"connectedNodes":[18,20]},{"coordinate":[7,2],"connectedNodes":[19]},{"coordinate":[4,3],"connectedNodes":[16,17]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level16 = Level(name='16', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    decor='[{"coordinate":{"x":188,"y":399},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":587,"y":97},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":652,"y":704},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":751,"y":704},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":787,"y":627},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":687,"y":623},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":924,"y":699},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":922,"y":608},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":843,"y":690},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":956,"y":517},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":544,"y":675},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":791,"y":504},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":926,"y":425},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":859,"y":563},"url":"/static/game/image/tree2.svg"}] ',
                    destinations='[[7, 0], [5, 1], [1, 4]]', direct_drive=True, fuel_gauge=False,
                    max_fuel=50, model_solution='[16]',
                    origin='{"coordinate":[2, 7], "direction":"S"}',
                    path='[{"coordinate":[2,7],"connectedNodes":[1]},{"coordinate":[2,6],"connectedNodes":[2,0,11]},{"coordinate":[1,6],"connectedNodes":[1,3]},{"coordinate":[1,5],"connectedNodes":[2,4]},{"coordinate":[1,4],"connectedNodes":[3,5]},{"coordinate":[1,3],"connectedNodes":[4,6]},{"coordinate":[1,2],"connectedNodes":[5,7]},{"coordinate":[2,2],"connectedNodes":[6,8]},{"coordinate":[3,2],"connectedNodes":[7,29,9]},{"coordinate":[4,2],"connectedNodes":[8,10]},{"coordinate":[5,2],"connectedNodes":[9,27,17]},{"coordinate":[2,5],"connectedNodes":[1,12]},{"coordinate":[3,5],"connectedNodes":[11,13]},{"coordinate":[3,6],"connectedNodes":[14,12]},{"coordinate":[4,6],"connectedNodes":[13,15]},{"coordinate":[4,5],"connectedNodes":[14,21,16]},{"coordinate":[4,4],"connectedNodes":[28,15]},{"coordinate":[5,1],"connectedNodes":[10,18]},{"coordinate":[5,0],"connectedNodes":[17,19]},{"coordinate":[6,0],"connectedNodes":[18,20]},{"coordinate":[7,0],"connectedNodes":[19]},{"coordinate":[5,5],"connectedNodes":[15,22]},{"coordinate":[6,5],"connectedNodes":[21,23]},{"coordinate":[7,5],"connectedNodes":[22,24]},{"coordinate":[7,4],"connectedNodes":[23,25]},{"coordinate":[7,3],"connectedNodes":[24,26]},{"coordinate":[7,2],"connectedNodes":[27,25]},{"coordinate":[6,2],"connectedNodes":[10,26]},{"coordinate":[3,4],"connectedNodes":[16,29]},{"coordinate":[3,3],"connectedNodes":[28,8]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level17 = Level(name='17', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    decor='[{"coordinate":{"x":573,"y":200},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":200,"y":674},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":200,"y":673},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":380,"y":523},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":580,"y":479},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":196,"y":190},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":296,"y":402},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":-2,"y":532},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":-4,"y":387},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":-3,"y":224},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":-2,"y":68},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":1,"y":674},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":170,"y":403},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":308,"y":190},"url":"/static/game/image/tree1.svg"}]',
                    destinations='[[4, 1], [5, 2], [5, 5], [3, 6]]', direct_drive=True,
                    fuel_gauge=False, max_fuel=50, model_solution='[16]',
                    origin='{"coordinate":[2, 6], "direction":"S"}',
                    path='[{"coordinate":[2,6],"connectedNodes":[30]},{"coordinate":[3,6],"connectedNodes":[2,28]},{"coordinate":[4,6],"connectedNodes":[1,3]},{"coordinate":[5,6],"connectedNodes":[2,6,4]},{"coordinate":[5,5],"connectedNodes":[3,5]},{"coordinate":[5,4],"connectedNodes":[10,4]},{"coordinate":[6,6],"connectedNodes":[3,7]},{"coordinate":[7,6],"connectedNodes":[6,8]},{"coordinate":[7,5],"connectedNodes":[7,9]},{"coordinate":[7,4],"connectedNodes":[8,16]},{"coordinate":[4,4],"connectedNodes":[5,26]},{"coordinate":[1,2],"connectedNodes":[29,19]},{"coordinate":[2,3],"connectedNodes":[29,13]},{"coordinate":[3,3],"connectedNodes":[12,26]},{"coordinate":[5,3],"connectedNodes":[15,17]},{"coordinate":[6,3],"connectedNodes":[14,16]},{"coordinate":[7,3],"connectedNodes":[15,9,25]},{"coordinate":[5,2],"connectedNodes":[27,14,18]},{"coordinate":[5,1],"connectedNodes":[22,17,23]},{"coordinate":[1,1],"connectedNodes":[11,20]},{"coordinate":[2,1],"connectedNodes":[19,21]},{"coordinate":[3,1],"connectedNodes":[20,22]},{"coordinate":[4,1],"connectedNodes":[21,18]},{"coordinate":[6,1],"connectedNodes":[18,24]},{"coordinate":[7,1],"connectedNodes":[23,25]},{"coordinate":[7,2],"connectedNodes":[16,24]},{"coordinate":[4,3],"connectedNodes":[13,10,27]},{"coordinate":[4,2],"connectedNodes":[26,17]},{"coordinate":[3,5],"connectedNodes":[30,1]},{"coordinate":[1,3],"connectedNodes":[12,11]},{"coordinate":[2,5],"connectedNodes":[0,28]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level18 = Level(name='18', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    decor='[{"coordinate":{"x":875,"y":86},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":874,"y":448},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":775,"y":688},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":119,"y":512},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":93,"y":397},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":296,"y":289},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":487,"y":203},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":231,"y":189},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":73,"y":172},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":604,"y":300},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":672,"y":194},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":516,"y":286},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":587,"y":211},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":700,"y":283},"url":"/static/game/image/tree2.svg"}]',
                    destinations='[[2, 7], [7, 7], [8, 5], [8, 1]]', direct_drive=True,
                    fuel_gauge=False, max_fuel=50, model_solution='[19]',
                    origin='{"coordinate":[6, 1], "direction":"S"}', pythonEnabled=False,
                    path='[{"coordinate":[6,1],"connectedNodes":[4]},{"coordinate":[3,0],"connectedNodes":[49,2]},{"coordinate":[4,0],"connectedNodes":[1,3]},{"coordinate":[5,0],"connectedNodes":[2,4]},{"coordinate":[6,0],"connectedNodes":[3,0,5]},{"coordinate":[7,0],"connectedNodes":[4,6]},{"coordinate":[8,0],"connectedNodes":[5,11]},{"coordinate":[1,0],"connectedNodes":[8,49]},{"coordinate":[1,1],"connectedNodes":[9,7]},{"coordinate":[2,1],"connectedNodes":[8,10]},{"coordinate":[3,1],"connectedNodes":[9,38]},{"coordinate":[8,1],"connectedNodes":[12,6]},{"coordinate":[8,2],"connectedNodes":[13,11]},{"coordinate":[8,3],"connectedNodes":[14,12]},{"coordinate":[8,4],"connectedNodes":[15,13]},{"coordinate":[8,5],"connectedNodes":[16,14]},{"coordinate":[8,6],"connectedNodes":[17,15]},{"coordinate":[7,6],"connectedNodes":[43,18,16,42]},{"coordinate":[7,7],"connectedNodes":[19,17]},{"coordinate":[6,7],"connectedNodes":[20,18]},{"coordinate":[5,7],"connectedNodes":[21,19]},{"coordinate":[4,7],"connectedNodes":[22,20]},{"coordinate":[3,7],"connectedNodes":[30,21]},{"coordinate":[2,6],"connectedNodes":[24,30,48,29]},{"coordinate":[1,6],"connectedNodes":[25,23]},{"coordinate":[0,6],"connectedNodes":[24,26]},{"coordinate":[0,5],"connectedNodes":[25,27]},{"coordinate":[0,4],"connectedNodes":[26,31]},{"coordinate":[2,4],"connectedNodes":[29,34,33]},{"coordinate":[2,5],"connectedNodes":[23,28]},{"coordinate":[2,7],"connectedNodes":[22,23]},{"coordinate":[0,3],"connectedNodes":[27,32]},{"coordinate":[1,3],"connectedNodes":[31,33]},{"coordinate":[2,3],"connectedNodes":[32,28]},{"coordinate":[3,4],"connectedNodes":[28,35]},{"coordinate":[4,4],"connectedNodes":[34,39,36]},{"coordinate":[4,3],"connectedNodes":[35,37]},{"coordinate":[4,2],"connectedNodes":[36,38]},{"coordinate":[4,1],"connectedNodes":[10,37]},{"coordinate":[5,4],"connectedNodes":[35,40]},{"coordinate":[6,4],"connectedNodes":[39,41]},{"coordinate":[7,4],"connectedNodes":[40,42]},{"coordinate":[7,5],"connectedNodes":[17,41]},{"coordinate":[6,6],"connectedNodes":[44,17]},{"coordinate":[5,6],"connectedNodes":[43,45]},{"coordinate":[5,5],"connectedNodes":[46,44]},{"coordinate":[4,5],"connectedNodes":[47,45]},{"coordinate":[4,6],"connectedNodes":[48,46]},{"coordinate":[3,6],"connectedNodes":[23,47]},{"coordinate":[2,0],"connectedNodes":[7,1]}]',
                    theme=grass, threads=1, traffic_lights='[]')

    level19 = Level(name='19', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    decor='[{"coordinate":{"x":393,"y":539},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":271,"y":613},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":340,"y":648},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":77,"y":639},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":147,"y":624},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":227,"y":682},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":228,"y":532},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":80,"y":518},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":327,"y":437},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":770,"y":-12},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":432,"y":-1},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":468,"y":-9},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":632,"y":-8},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":542,"y":-18},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":622,"y":187},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":645,"y":45},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":542,"y":91},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":707,"y":284},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":711,"y":35},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":826,"y":26},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":782,"y":107},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":748,"y":135},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":848,"y":138},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":334,"y":94},"url":"/static/game/image/tree1.svg"}]',
                    destinations='[[4, 3]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    model_solution='[2]', origin='{"coordinate":[0, 3], "direction":"E"}',
                    path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[2,3],"connectedNodes":[1,3]},{"coordinate":[3,3],"connectedNodes":[2,4]},{"coordinate":[4,3],"connectedNodes":[3]}] ',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level20 = Level(name='20', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    decor='[{"coordinate":{"x":676,"y":311},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":700,"y":145},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":527,"y":190},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":829,"y":471},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":782,"y":188},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":650,"y":466},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":622,"y":235},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":758,"y":318},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":856,"y":269},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":831,"y":386},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":153,"y":669},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":4,"y":548},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":86,"y":565},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":64,"y":665},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":393,"y":109},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":424,"y":352},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":595,"y":86},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":755,"y":407},"url":"/static/game/image/tree2.svg"}]',
                    destinations='[[4, 6]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    model_solution='[3]', origin='{"coordinate":[0, 3], "direction":"E"}',
                    path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[1,4],"connectedNodes":[1,3]},{"coordinate":[2,4],"connectedNodes":[2,4]},{"coordinate":[2,5],"connectedNodes":[3,5]},{"coordinate":[3,5],"connectedNodes":[4,6]},{"coordinate":[3,6],"connectedNodes":[5,7]},{"coordinate":[4,6],"connectedNodes":[6]}] ',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level21 = Level(name='21', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    decor='[{"coordinate":{"x":300,"y":610},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":294,"y":412},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":200,"y":525},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":389,"y":515},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":162,"y":688},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":209,"y":610},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":296,"y":513},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":26,"y":19},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":148,"y":5},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":216,"y":80},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":600,"y":-29},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":707,"y":2},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":638,"y":91},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":697,"y":186},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":439,"y":113},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":401,"y":-30},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":302,"y":18},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":89,"y":113},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":516,"y":47},"url":"/static/game/image/tree2.svg"}]',
                    destinations='[[3, 7]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    model_solution='[5]', origin='{"coordinate":[1, 6], "direction":"S"}',
                    path='[{"coordinate":[1,6],"connectedNodes":[2]},{"coordinate":[1,4],"connectedNodes":[2,3]},{"coordinate":[1,5],"connectedNodes":[0,1]},{"coordinate":[2,4],"connectedNodes":[1,4]},{"coordinate":[2,3],"connectedNodes":[3,5]},{"coordinate":[3,3],"connectedNodes":[4,6]},{"coordinate":[4,3],"connectedNodes":[5,7]},{"coordinate":[4,4],"connectedNodes":[8,6]},{"coordinate":[5,4],"connectedNodes":[7,9]},{"coordinate":[5,5],"connectedNodes":[10,8]},{"coordinate":[5,6],"connectedNodes":[11,9]},{"coordinate":[4,6],"connectedNodes":[12,10]},{"coordinate":[4,7],"connectedNodes":[13,11]},{"coordinate":[3,7],"connectedNodes":[12]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level22 = Level(name='22', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    decor='[{"coordinate":{"x":859,"y":698},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":727,"y":698},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":574,"y":696},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":414,"y":694},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":256,"y":695},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":83,"y":693},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":840,"y":1},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":651,"y":0},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":457,"y":-1},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":257,"y":-2},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":58,"y":-3},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":378,"y":478},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":209,"y":426},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":409,"y":292},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":233,"y":226},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":629,"y":201},"url":"/static/game/image/tree1.svg"}]',
                    destinations='[[7, 5]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    model_solution='[19]', origin='{"coordinate":[8, 3], "direction":"W"}',
                    path='[{"coordinate":[8,3],"connectedNodes":[1]},{"coordinate":[7,3],"connectedNodes":[2,0]},{"coordinate":[6,3],"connectedNodes":[3,1]},{"coordinate":[5,3],"connectedNodes":[4,2]},{"coordinate":[5,4],"connectedNodes":[5,3]},{"coordinate":[5,5],"connectedNodes":[6,4]},{"coordinate":[5,6],"connectedNodes":[7,5]},{"coordinate":[4,6],"connectedNodes":[8,6]},{"coordinate":[3,6],"connectedNodes":[9,7]},{"coordinate":[2,6],"connectedNodes":[10,8]},{"coordinate":[1,6],"connectedNodes":[9,11]},{"coordinate":[1,5],"connectedNodes":[10,12]},{"coordinate":[1,4],"connectedNodes":[11,13]},{"coordinate":[1,3],"connectedNodes":[12,14]},{"coordinate":[1,2],"connectedNodes":[13,15]},{"coordinate":[1,1],"connectedNodes":[14,16]},{"coordinate":[2,1],"connectedNodes":[15,17]},{"coordinate":[3,1],"connectedNodes":[16,18]},{"coordinate":[4,1],"connectedNodes":[17,19]},{"coordinate":[5,1],"connectedNodes":[18,20]},{"coordinate":[6,1],"connectedNodes":[19,21]},{"coordinate":[7,1],"connectedNodes":[20,22]},{"coordinate":[8,1],"connectedNodes":[21,23]},{"coordinate":[9,1],"connectedNodes":[22,24]},{"coordinate":[9,2],"connectedNodes":[25,23]},{"coordinate":[9,3],"connectedNodes":[26,24]},{"coordinate":[9,4],"connectedNodes":[27,25]},{"coordinate":[9,5],"connectedNodes":[28,26]},{"coordinate":[8,5],"connectedNodes":[29,27]},{"coordinate":[7,5],"connectedNodes":[28]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level23 = Level(name='23', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    decor='[{"coordinate":{"x":1,"y":4},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":3,"y":400},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":-1,"y":199},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":101,"y":697},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":2,"y":600},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":200,"y":2},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":399,"y":3},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":603,"y":2},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":299,"y":697},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":501,"y":699},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":702,"y":699},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":895,"y":698},"url":"/static/game/image/bush.svg"}]',
                    destinations='[[7, 2]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    model_solution='[9]', origin='{"coordinate":[8, 6], "direction":"W"}',
                    path='[{"coordinate":[8,6],"connectedNodes":[1]},{"coordinate":[7,6],"connectedNodes":[2,0]},{"coordinate":[6,6],"connectedNodes":[3,1]},{"coordinate":[5,6],"connectedNodes":[4,2]},{"coordinate":[4,6],"connectedNodes":[5,3]},{"coordinate":[3,6],"connectedNodes":[6,4]},{"coordinate":[2,6],"connectedNodes":[5,7]},{"coordinate":[2,5],"connectedNodes":[6,8]},{"coordinate":[3,5],"connectedNodes":[7,9]},{"coordinate":[4,5],"connectedNodes":[8,10]},{"coordinate":[5,5],"connectedNodes":[9,11]},{"coordinate":[6,5],"connectedNodes":[10,12]},{"coordinate":[7,5],"connectedNodes":[11,13]},{"coordinate":[8,5],"connectedNodes":[12,14]},{"coordinate":[8,4],"connectedNodes":[15,13]},{"coordinate":[7,4],"connectedNodes":[16,14]},{"coordinate":[6,4],"connectedNodes":[17,15]},{"coordinate":[5,4],"connectedNodes":[18,16]},{"coordinate":[4,4],"connectedNodes":[19,17]},{"coordinate":[3,4],"connectedNodes":[20,18]},{"coordinate":[2,4],"connectedNodes":[19,21]},{"coordinate":[2,3],"connectedNodes":[20,22]},{"coordinate":[3,3],"connectedNodes":[21,23]},{"coordinate":[4,3],"connectedNodes":[22,24]},{"coordinate":[5,3],"connectedNodes":[23,25]},{"coordinate":[6,3],"connectedNodes":[24,26]},{"coordinate":[7,3],"connectedNodes":[25,27]},{"coordinate":[8,3],"connectedNodes":[26,28]},{"coordinate":[8,2],"connectedNodes":[29,27]},{"coordinate":[7,2],"connectedNodes":[28]}] ',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level24 = Level(name='24', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    decor='[{"coordinate":{"x":476,"y":109},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":699,"y":64},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":572,"y":20},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":633,"y":95},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":75,"y":560},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":217,"y":704},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":101,"y":696},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":48,"y":624},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":700,"y":400},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":552,"y":402},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":401,"y":400},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":246,"y":401},"url":"/static/game/image/bush.svg"}]',
                    destinations='[[2, 2]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    model_solution='[12]', origin='{"coordinate":[2, 6], "direction":"S"}',
                    path='[{"coordinate":[2,6],"connectedNodes":[27]},{"coordinate":[2,3],"connectedNodes":[2,28]},{"coordinate":[3,3],"connectedNodes":[1,3]},{"coordinate":[3,2],"connectedNodes":[2,4]},{"coordinate":[4,2],"connectedNodes":[3,5]},{"coordinate":[4,3],"connectedNodes":[6,4]},{"coordinate":[5,3],"connectedNodes":[5,7]},{"coordinate":[5,2],"connectedNodes":[6,8]},{"coordinate":[6,2],"connectedNodes":[7,9]},{"coordinate":[6,3],"connectedNodes":[10,8]},{"coordinate":[7,3],"connectedNodes":[9,11]},{"coordinate":[7,2],"connectedNodes":[10,12]},{"coordinate":[8,2],"connectedNodes":[11,13]},{"coordinate":[8,3],"connectedNodes":[14,12]},{"coordinate":[8,4],"connectedNodes":[15,13]},{"coordinate":[8,5],"connectedNodes":[16,14]},{"coordinate":[8,6],"connectedNodes":[17,15]},{"coordinate":[7,6],"connectedNodes":[16,18]},{"coordinate":[7,5],"connectedNodes":[19,17]},{"coordinate":[6,5],"connectedNodes":[20,18]},{"coordinate":[6,6],"connectedNodes":[21,19]},{"coordinate":[5,6],"connectedNodes":[20,22]},{"coordinate":[5,5],"connectedNodes":[23,21]},{"coordinate":[4,5],"connectedNodes":[24,22]},{"coordinate":[4,6],"connectedNodes":[25,23]},{"coordinate":[3,6],"connectedNodes":[24,26]},{"coordinate":[3,5],"connectedNodes":[27,25]},{"coordinate":[2,5],"connectedNodes":[0,26]},{"coordinate":[2,2],"connectedNodes":[1]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level25 = Level(name='25', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    decor='[{"coordinate":{"x":295,"y":589},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":403,"y":489},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":207,"y":399},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":108,"y":506},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":596,"y":391},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":401,"y":301},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":497,"y":205},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":700,"y":294},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":6,"y":110},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":109,"y":-2},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":4,"y":6},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":222,"y":-6},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":0,"y":230},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":885,"y":687},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":651,"y":689},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":767,"y":693},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":885,"y":575},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":887,"y":463},"url":"/static/game/image/tree1.svg"}]',
                    destinations='[[8, 2]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    model_solution='[6]', origin='{"coordinate":[0, 6], "direction":"E"}',
                    path='[{"coordinate":[0,6],"connectedNodes":[1]},{"coordinate":[1,6],"connectedNodes":[0,2]},{"coordinate":[2,6],"connectedNodes":[1,3]},{"coordinate":[2,5],"connectedNodes":[2,4]},{"coordinate":[3,5],"connectedNodes":[3,5]},{"coordinate":[3,4],"connectedNodes":[4,6]},{"coordinate":[4,4],"connectedNodes":[5,7]},{"coordinate":[5,4],"connectedNodes":[6,8]},{"coordinate":[5,3],"connectedNodes":[7,9]},{"coordinate":[6,3],"connectedNodes":[8,10]},{"coordinate":[6,2],"connectedNodes":[9,11]},{"coordinate":[7,2],"connectedNodes":[10,12]},{"coordinate":[8,2],"connectedNodes":[11]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level26 = Level(name='26', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    decor='[{"coordinate":{"x":176,"y":520},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":176,"y":400},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":179,"y":286},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":500,"y":627},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":499,"y":508},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":500,"y":388},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":690,"y":203},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":780,"y":81},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":865,"y":419},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":875,"y":180},"url":"/static/game/image/tree2.svg"}]',
                    destinations='[[8, 3]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    model_solution='[5]', origin='{"coordinate":[4, 6], "direction":"S"}',
                    path='[{"coordinate":[4,6],"connectedNodes":[1]},{"coordinate":[4,5],"connectedNodes":[0,2]},{"coordinate":[4,4],"connectedNodes":[1,3]},{"coordinate":[4,3],"connectedNodes":[2,4]},{"coordinate":[5,3],"connectedNodes":[3,5]},{"coordinate":[6,3],"connectedNodes":[4,6]},{"coordinate":[7,3],"connectedNodes":[5,7]},{"coordinate":[8,3],"connectedNodes":[6]}]',
                    pythonEnabled=False, theme=snow, threads=1, traffic_lights='[]')

    level27 = Level(name='27', anonymous=False, blocklyEnabled=True, character=dee, default=True,
                    decor='[{"coordinate":{"x":647,"y":351},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":220,"y":353},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":346,"y":316},"url":"/static/game/image/pond.svg"},{"coordinate":{"x":574,"y":183},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":610,"y":609},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":478,"y":608},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":354,"y":608},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":214,"y":606},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":510,"y":396},"url":"/static/game/image/tree1.svg"}]',
                    destinations='[[8, 3]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    model_solution='[16]', origin='{"coordinate":[4, 5], "direction":"E"}',
                    path='[{"coordinate":[4,5],"connectedNodes":[1]},{"coordinate":[5,5],"connectedNodes":[0,2]},{"coordinate":[6,5],"connectedNodes":[1,3]},{"coordinate":[7,5],"connectedNodes":[2,4]},{"coordinate":[7,6],"connectedNodes":[5,3]},{"coordinate":[7,7],"connectedNodes":[6,4]},{"coordinate":[6,7],"connectedNodes":[7,5]},{"coordinate":[5,7],"connectedNodes":[8,6]},{"coordinate":[4,7],"connectedNodes":[9,7]},{"coordinate":[3,7],"connectedNodes":[10,8]},{"coordinate":[2,7],"connectedNodes":[11,9]},{"coordinate":[1,7],"connectedNodes":[10,12]},{"coordinate":[1,6],"connectedNodes":[11,13]},{"coordinate":[1,5],"connectedNodes":[12,14]},{"coordinate":[1,4],"connectedNodes":[13,15]},{"coordinate":[1,3],"connectedNodes":[14,16]},{"coordinate":[1,2],"connectedNodes":[15,17]},{"coordinate":[2,2],"connectedNodes":[16,18]},{"coordinate":[2,1],"connectedNodes":[17,19]},{"coordinate":[3,1],"connectedNodes":[18,20]},{"coordinate":[4,1],"connectedNodes":[19,21]},{"coordinate":[5,1],"connectedNodes":[20,22]},{"coordinate":[6,1],"connectedNodes":[21,23]},{"coordinate":[7,1],"connectedNodes":[22,24]},{"coordinate":[7,2],"connectedNodes":[25,23]},{"coordinate":[8,2],"connectedNodes":[24,26]},{"coordinate":[8,3],"connectedNodes":[25]}]',
                    pythonEnabled=False, theme=farm, threads=1, traffic_lights='[]')

    level28 = Level(name='28', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    decor='[{"coordinate":{"x":415,"y":488},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":520,"y":434},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":513,"y":291},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":405,"y":368},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":182,"y":589},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":115,"y":468},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":194,"y":380},"url":"/static/game/image/tree1.svg"}]',
                    destinations='[[9, 4]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    model_solution='[19]', origin='{"coordinate":[1, 3], "direction":"E"}',
                    path='[{"coordinate":[1,3],"connectedNodes":[1]},{"coordinate":[2,3],"connectedNodes":[0,2]},{"coordinate":[3,3],"connectedNodes":[1,3]},{"coordinate":[3,4],"connectedNodes":[4,2]},{"coordinate":[3,5],"connectedNodes":[5,3]},{"coordinate":[3,6],"connectedNodes":[6,4]},{"coordinate":[4,6],"connectedNodes":[5,7]},{"coordinate":[5,6],"connectedNodes":[6,8]},{"coordinate":[6,6],"connectedNodes":[7,9]},{"coordinate":[6,5],"connectedNodes":[8,10]},{"coordinate":[6,4],"connectedNodes":[9,11]},{"coordinate":[6,3],"connectedNodes":[10,12]},{"coordinate":[6,2],"connectedNodes":[13,11]},{"coordinate":[5,2],"connectedNodes":[14,12]},{"coordinate":[4,2],"connectedNodes":[15,13]},{"coordinate":[3,2],"connectedNodes":[14,16]},{"coordinate":[3,1],"connectedNodes":[15,17]},{"coordinate":[4,1],"connectedNodes":[16,18]},{"coordinate":[5,1],"connectedNodes":[17,19]},{"coordinate":[6,1],"connectedNodes":[18,20]},{"coordinate":[7,1],"connectedNodes":[19,21]},{"coordinate":[8,1],"connectedNodes":[20,22]},{"coordinate":[8,2],"connectedNodes":[23,21]},{"coordinate":[9,2],"connectedNodes":[22,24]},{"coordinate":[9,3],"connectedNodes":[25,23]},{"coordinate":[9,4],"connectedNodes":[24]}]',
                    pythonEnabled=False, theme=city, threads=1, traffic_lights='[]')

    level29 = Level(name='29', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    decor='[{"coordinate":{"x":96,"y":599},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":200,"y":599},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":300,"y":600},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":257,"y":514},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":149,"y":512},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":209,"y":431},"url":"/static/game/image/tree1.svg"}]',
                    destinations='[[4, 3]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    model_solution='[3]', origin='{"coordinate":[0, 3], "direction":"E"}',
                    path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[2,3],"connectedNodes":[1,3]},{"coordinate":[3,3],"connectedNodes":[2,4]},{"coordinate":[4,3],"connectedNodes":[3]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level30 = Level(name='30', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    decor='[{"coordinate":{"x":117,"y":700},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":244,"y":697},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":-6,"y":697},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":55,"y":594},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":184,"y":599},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":117,"y":490},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":480,"y":500},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":412,"y":397},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":544,"y":399},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":487,"y":295},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":618,"y":298},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":414,"y":188},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":564,"y":189},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":704,"y":189},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":265,"y":192},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":342,"y":295},"url":"/static/game/image/tree2.svg"}]',
                    destinations='[[4, 6]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    model_solution='[4]', origin='{"coordinate":[0, 3], "direction":"E"}',
                    path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[1,4],"connectedNodes":[1,3]},{"coordinate":[2,4],"connectedNodes":[2,4]},{"coordinate":[2,5],"connectedNodes":[3,5]},{"coordinate":[3,5],"connectedNodes":[4,6]},{"coordinate":[3,6],"connectedNodes":[5,7]},{"coordinate":[4,6],"connectedNodes":[6]}] ',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level31 = Level(name='31', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    decor='[{"coordinate":{"x":476,"y":585},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":424,"y":476},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":260,"y":272},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":197,"y":388},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":264,"y":347},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":313,"y":94},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":389,"y":21},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":547,"y":233},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":600,"y":93},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":537,"y":163},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":639,"y":183},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":311,"y":13},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":400,"y":558},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":494,"y":512},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":196,"y":701},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":404,"y":698},"url":"/static/game/image/bush.svg"}]',
                    destinations='[[3, 7]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    model_solution='[6]', origin='{"coordinate":[5, 0], "direction":"N"}',
                    path='[{"coordinate":[5,0],"connectedNodes":[1]},{"coordinate":[5,1],"connectedNodes":[2,0]},{"coordinate":[4,1],"connectedNodes":[3,1]},{"coordinate":[4,2],"connectedNodes":[4,2]},{"coordinate":[4,3],"connectedNodes":[5,3]},{"coordinate":[4,4],"connectedNodes":[6,4]},{"coordinate":[3,4],"connectedNodes":[7,5]},{"coordinate":[3,5],"connectedNodes":[8,6]},{"coordinate":[3,6],"connectedNodes":[9,7]},{"coordinate":[3,7],"connectedNodes":[8]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level32 = Level(name='32', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    decor='[{"coordinate":{"x":153,"y":476},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":33,"y":363},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":189,"y":297},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":808,"y":660},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":888,"y":593},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":719,"y":705},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":694,"y":570},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":589,"y":694},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":919,"y":490},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":903,"y":685},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":817,"y":748},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":809,"y":506},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":886,"y":360},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":136,"y":365},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":82,"y":427},"url":"/static/game/image/tree1.svg"}]',
                    destinations='[[5, 0]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    model_solution='[5]', origin='{"coordinate":[2, 7], "direction":"S"}',
                    path='[{"coordinate":[2,7],"connectedNodes":[1]},{"coordinate":[2,6],"connectedNodes":[0,2]},{"coordinate":[3,6],"connectedNodes":[1,3]},{"coordinate":[3,5],"connectedNodes":[2,4]},{"coordinate":[3,4],"connectedNodes":[3,5]},{"coordinate":[4,4],"connectedNodes":[4,6]},{"coordinate":[4,3],"connectedNodes":[5,7]},{"coordinate":[4,2],"connectedNodes":[6,8]},{"coordinate":[5,2],"connectedNodes":[7,9]},{"coordinate":[5,1],"connectedNodes":[8,10]},{"coordinate":[5,0],"connectedNodes":[9]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level33 = Level(name='33', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    decor='[{"coordinate":{"x":2,"y":101},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":101,"y":100},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":203,"y":98},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":306,"y":101},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":403,"y":97},"url":"/static/game/image/tree1.svg"}]',
                    destinations='[[4, 3]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    model_solution='[5]', origin='{"coordinate":[0, 3], "direction":"E"}',
                    path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[2,3],"connectedNodes":[1,3]},{"coordinate":[3,3],"connectedNodes":[2,4]},{"coordinate":[4,3],"connectedNodes":[3]}] ',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level34 = Level(name='34', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    decor='[{"coordinate":{"x":700,"y":303},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":397,"y":298},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":-42,"y":699},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":244,"y":296},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":702,"y":459},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":698,"y":602},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":246,"y":97},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":404,"y":101},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":560,"y":99},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":707,"y":100},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":894,"y":102},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":898,"y":299},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":901,"y":461},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":896,"y":603},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":7,"y":692},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":16,"y":596},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":0,"y":512},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":88,"y":657},"url":"/static/game/image/tree2.svg"}]',
                    destinations='[[6, 6]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    model_solution='[8, 7]', origin='{"coordinate":[1, 2], "direction":"E"}',
                    path='[{"coordinate":[1,2],"connectedNodes":[1]},{"coordinate":[2,2],"connectedNodes":[0,2]},{"coordinate":[3,2],"connectedNodes":[1,3]},{"coordinate":[4,2],"connectedNodes":[2,4]},{"coordinate":[5,2],"connectedNodes":[3,5]},{"coordinate":[6,2],"connectedNodes":[4,6]},{"coordinate":[7,2],"connectedNodes":[5,7]},{"coordinate":[8,2],"connectedNodes":[6,8]},{"coordinate":[8,3],"connectedNodes":[9,7]},{"coordinate":[8,4],"connectedNodes":[10,8]},{"coordinate":[8,5],"connectedNodes":[11,9]},{"coordinate":[8,6],"connectedNodes":[12,10]},{"coordinate":[8,7],"connectedNodes":[13,11]},{"coordinate":[7,7],"connectedNodes":[14,12]},{"coordinate":[6,7],"connectedNodes":[15,13]},{"coordinate":[5,7],"connectedNodes":[16,14]},{"coordinate":[4,7],"connectedNodes":[17,15]},{"coordinate":[3,7],"connectedNodes":[16,18]},{"coordinate":[3,6],"connectedNodes":[17,19]},{"coordinate":[3,5],"connectedNodes":[18,20]},{"coordinate":[3,4],"connectedNodes":[19,21]},{"coordinate":[4,4],"connectedNodes":[20,22]},{"coordinate":[5,4],"connectedNodes":[21,23]},{"coordinate":[6,4],"connectedNodes":[22,24]},{"coordinate":[6,5],"connectedNodes":[25,23]},{"coordinate":[6,6],"connectedNodes":[24]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level35 = Level(name='35', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    decor='[{"coordinate":{"x":684,"y":299},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":484,"y":297},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":617,"y":288},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":540,"y":309},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":577,"y":501},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":665,"y":501},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":508,"y":517},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":620,"y":507},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":742,"y":512},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":368,"y":342},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":306,"y":241},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":420,"y":711},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":548,"y":687},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":698,"y":713},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":479,"y":681},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":632,"y":688},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":760,"y":697},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":820,"y":732},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":899,"y":692},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":892,"y":304},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":898,"y":580},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":899,"y":521},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":881,"y":444},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":888,"y":371},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":829,"y":483},"url":"/static/game/image/tree2.svg"}]',
                    destinations='[[1, 1]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    model_solution='[11, 9]', origin='{"coordinate":[8, 6], "direction":"W"}',
                    path='[{"coordinate":[8,6],"connectedNodes":[1]},{"coordinate":[7,6],"connectedNodes":[2,0]},{"coordinate":[6,6],"connectedNodes":[3,1]},{"coordinate":[5,6],"connectedNodes":[4,2]},{"coordinate":[4,6],"connectedNodes":[3,5]},{"coordinate":[4,5],"connectedNodes":[4,6]},{"coordinate":[4,4],"connectedNodes":[5,7]},{"coordinate":[5,4],"connectedNodes":[6,8]},{"coordinate":[6,4],"connectedNodes":[7,9]},{"coordinate":[7,4],"connectedNodes":[8,10]},{"coordinate":[8,4],"connectedNodes":[9,11]},{"coordinate":[8,3],"connectedNodes":[10,12]},{"coordinate":[8,2],"connectedNodes":[13,11]},{"coordinate":[7,2],"connectedNodes":[14,12]},{"coordinate":[6,2],"connectedNodes":[15,13]},{"coordinate":[5,2],"connectedNodes":[16,14]},{"coordinate":[4,2],"connectedNodes":[15,17]},{"coordinate":[4,1],"connectedNodes":[18,16]},{"coordinate":[3,1],"connectedNodes":[19,17]},{"coordinate":[2,1],"connectedNodes":[20,18]},{"coordinate":[1,1],"connectedNodes":[19]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level36 = Level(name='36', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    decor='[{"coordinate":{"x":350,"y":337},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":348,"y":439},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":344,"y":540},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":342,"y":645},"url":"/static/game/image/tree2.svg"}]',
                    destinations='[[5, 3]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    model_solution='[11, 9]', origin='{"coordinate":[0, 3], "direction":"E"}',
                    path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[1,4],"connectedNodes":[1,3]},{"coordinate":[1,5],"connectedNodes":[2,4]},{"coordinate":[1,6],"connectedNodes":[3,5]},{"coordinate":[2,6],"connectedNodes":[4,6]},{"coordinate":[2,5],"connectedNodes":[5,7]},{"coordinate":[3,5],"connectedNodes":[6,8]},{"coordinate":[3,4],"connectedNodes":[7,9]},{"coordinate":[3,3],"connectedNodes":[8,10]},{"coordinate":[3,2],"connectedNodes":[9,11]},{"coordinate":[4,2],"connectedNodes":[10,12]},{"coordinate":[4,3],"connectedNodes":[11,13]},{"coordinate":[5,3],"connectedNodes":[12]}] ',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level37 = Level(name='37', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    decor='[{"coordinate":{"x":424,"y":640},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":441,"y":561},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":503,"y":545},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":503,"y":639},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":298,"y":401},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":19,"y":594},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":85,"y":551},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":7,"y":507},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":38,"y":58},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":6,"y":89},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":101,"y":16},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":177,"y":6},"url":"/static/game/image/tree2.svg"}]',
                    destinations='[[3, 2]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    model_solution='[11, 9]', origin='{"coordinate":[6, 1], "direction":"E"}',
                    path='[{"coordinate":[6,1],"connectedNodes":[19]},{"coordinate":[5,3],"connectedNodes":[2,22]},{"coordinate":[4,3],"connectedNodes":[3,1]},{"coordinate":[3,3],"connectedNodes":[4,2]},{"coordinate":[2,3],"connectedNodes":[5,3]},{"coordinate":[2,4],"connectedNodes":[6,4]},{"coordinate":[2,5],"connectedNodes":[7,5]},{"coordinate":[3,5],"connectedNodes":[6,8]},{"coordinate":[4,5],"connectedNodes":[7,9]},{"coordinate":[4,4],"connectedNodes":[8,10]},{"coordinate":[5,4],"connectedNodes":[9,11]},{"coordinate":[6,4],"connectedNodes":[10,12]},{"coordinate":[6,5],"connectedNodes":[13,11]},{"coordinate":[6,6],"connectedNodes":[14,12]},{"coordinate":[7,6],"connectedNodes":[13,15]},{"coordinate":[7,5],"connectedNodes":[14,16]},{"coordinate":[7,4],"connectedNodes":[15,17]},{"coordinate":[7,3],"connectedNodes":[16,18]},{"coordinate":[7,2],"connectedNodes":[17,19]},{"coordinate":[7,1],"connectedNodes":[0,18]},{"coordinate":[3,2],"connectedNodes":[21]},{"coordinate":[4,2],"connectedNodes":[20,22]},{"coordinate":[5,2],"connectedNodes":[21,1]}] ',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level38 = Level(name='38', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    decor='[{"coordinate":{"x":865,"y":655},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":867,"y":457},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":867,"y":275},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":864,"y":91},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":668,"y":307},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":542,"y":301},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":194,"y":695},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":340,"y":704},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":87,"y":671},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":187,"y":50},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":62,"y":86},"url":"/static/game/image/tree2.svg"}]',
                    destinations='[[6, 0]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    model_solution='[11, 9]', origin='{"coordinate":[7, 6], "direction":"W"}',
                    path='[{"coordinate":[7,6],"connectedNodes":[1]},{"coordinate":[6,6],"connectedNodes":[2,0]},{"coordinate":[5,6],"connectedNodes":[3,1]},{"coordinate":[4,6],"connectedNodes":[4,2]},{"coordinate":[3,6],"connectedNodes":[5,3]},{"coordinate":[2,6],"connectedNodes":[4,6]},{"coordinate":[2,5],"connectedNodes":[7,5]},{"coordinate":[1,5],"connectedNodes":[8,6]},{"coordinate":[1,6],"connectedNodes":[9,7]},{"coordinate":[0,6],"connectedNodes":[8,10]},{"coordinate":[0,5],"connectedNodes":[9,11]},{"coordinate":[0,4],"connectedNodes":[10,12]},{"coordinate":[1,4],"connectedNodes":[11,13]},{"coordinate":[2,4],"connectedNodes":[12,14]},{"coordinate":[3,4],"connectedNodes":[13,15]},{"coordinate":[3,5],"connectedNodes":[16,14]},{"coordinate":[4,5],"connectedNodes":[15,17]},{"coordinate":[5,5],"connectedNodes":[16,18]},{"coordinate":[6,5],"connectedNodes":[17,19]},{"coordinate":[7,5],"connectedNodes":[18,20]},{"coordinate":[7,4],"connectedNodes":[21,19]},{"coordinate":[6,4],"connectedNodes":[22,20]},{"coordinate":[5,4],"connectedNodes":[23,21]},{"coordinate":[4,4],"connectedNodes":[22,24]},{"coordinate":[4,3],"connectedNodes":[25,23]},{"coordinate":[3,3],"connectedNodes":[26,24]},{"coordinate":[2,3],"connectedNodes":[27,25]},{"coordinate":[1,3],"connectedNodes":[26,28]},{"coordinate":[1,2],"connectedNodes":[27,29]},{"coordinate":[2,2],"connectedNodes":[28,30]},{"coordinate":[3,2],"connectedNodes":[29,31]},{"coordinate":[3,1],"connectedNodes":[30,32]},{"coordinate":[3,0],"connectedNodes":[31,33]},{"coordinate":[4,0],"connectedNodes":[32,34]},{"coordinate":[4,1],"connectedNodes":[35,33]},{"coordinate":[4,2],"connectedNodes":[36,34]},{"coordinate":[5,2],"connectedNodes":[35,37]},{"coordinate":[6,2],"connectedNodes":[36,38]},{"coordinate":[6,1],"connectedNodes":[37,39]},{"coordinate":[6,0],"connectedNodes":[38]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level39 = Level(name='39', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    decor='[{"coordinate":{"x":639,"y":285},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":502,"y":388},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":655,"y":443},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":263,"y":92},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":551,"y":90},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":695,"y":89},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":411,"y":89},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":833,"y":91},"url":"/static/game/image/bush.svg"}]',
                    destinations='[[8, 7]]', direct_drive=False, fuel_gauge=True, max_fuel=50,
                    model_solution='[5, 6]', origin='{"coordinate":[1, 2], "direction":"E"}',
                    path='[{"coordinate":[1,2],"connectedNodes":[1]},{"coordinate":[2,2],"connectedNodes":[0,2]},{"coordinate":[3,2],"connectedNodes":[1,3]},{"coordinate":[4,2],"connectedNodes":[2,9,4]},{"coordinate":[5,2],"connectedNodes":[3,5]},{"coordinate":[6,2],"connectedNodes":[4,6]},{"coordinate":[7,2],"connectedNodes":[5,7]},{"coordinate":[8,2],"connectedNodes":[6,11,8]},{"coordinate":[9,2],"connectedNodes":[7]},{"coordinate":[4,3],"connectedNodes":[10,3]},{"coordinate":[4,4],"connectedNodes":[9]},{"coordinate":[8,3],"connectedNodes":[12,7]},{"coordinate":[8,4],"connectedNodes":[13,11]},{"coordinate":[8,5],"connectedNodes":[14,12]},{"coordinate":[8,6],"connectedNodes":[15,13]},{"coordinate":[8,7],"connectedNodes":[14]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level40 = Level(name='40', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    decor='[{"coordinate":{"x":377,"y":509},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":787,"y":424},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":609,"y":364},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":686,"y":210},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":752,"y":307},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":709,"y":380},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":389,"y":420},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":95,"y":578},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":11,"y":558},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":117,"y":513},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":76,"y":626},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":48,"y":481},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":6,"y":405},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":191,"y":435},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":254,"y":488},"url":"/static/game/image/tree2.svg"}]',
                    destinations='[[3, 4]]', direct_drive=False, fuel_gauge=True, max_fuel=50,
                    model_solution='[8, 9]', origin='{"coordinate":[3, 6], "direction":"E"}',
                    path='[{"coordinate":[3,6],"connectedNodes":[1]},{"coordinate":[4,6],"connectedNodes":[0,2]},{"coordinate":[5,6],"connectedNodes":[1,3]},{"coordinate":[5,5],"connectedNodes":[2,5,4]},{"coordinate":[5,4],"connectedNodes":[3,9]},{"coordinate":[6,5],"connectedNodes":[3,6]},{"coordinate":[7,5],"connectedNodes":[5,7]},{"coordinate":[7,6],"connectedNodes":[8,6]},{"coordinate":[8,6],"connectedNodes":[7]},{"coordinate":[5,3],"connectedNodes":[10,4,13]},{"coordinate":[4,3],"connectedNodes":[11,9]},{"coordinate":[3,3],"connectedNodes":[12,10]},{"coordinate":[3,4],"connectedNodes":[11]},{"coordinate":[5,2],"connectedNodes":[9,14]},{"coordinate":[5,1],"connectedNodes":[13,15]},{"coordinate":[6,1],"connectedNodes":[14,16]},{"coordinate":[7,1],"connectedNodes":[15,17]},{"coordinate":[8,1],"connectedNodes":[16,18]},{"coordinate":[8,2],"connectedNodes":[17]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level41 = Level(name='41', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    decor='[{"coordinate":{"x":99,"y":597},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":100,"y":495},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":117,"y":408},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":101,"y":197},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":92,"y":107},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":106,"y":1},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":607,"y":593},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":590,"y":493},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":513,"y":412},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":597,"y":3},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":697,"y":1},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":799,"y":0},"url":"/static/game/image/tree2.svg"}]',
                    destinations='[[5, 3]]', direct_drive=False, fuel_gauge=True, max_fuel=50,
                    model_solution='[8, 9]', origin='{"coordinate":[0, 3], "direction":"E"}',
                    path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[2,3],"connectedNodes":[1,3,9]},{"coordinate":[2,4],"connectedNodes":[2,4]},{"coordinate":[3,4],"connectedNodes":[3,5]},{"coordinate":[4,4],"connectedNodes":[4,6]},{"coordinate":[4,3],"connectedNodes":[5,10,7]},{"coordinate":[4,2],"connectedNodes":[6,8]},{"coordinate":[3,2],"connectedNodes":[7,9]},{"coordinate":[2,2],"connectedNodes":[2,8]},{"coordinate":[5,3],"connectedNodes":[6]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level42 = Level(name='42', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    decor='[{"coordinate":{"x":0,"y":595},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":2,"y":502},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":6,"y":398},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":0,"y":700},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":5,"y":201},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":8,"y":104},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":0,"y":5},"url":"/static/game/image/tree1.svg"}]',
                    destinations='[[4, 2]]', direct_drive=False, fuel_gauge=True, max_fuel=50,
                    model_solution='[4]', origin='{"coordinate":[0, 3], "direction":"E"}',
                    path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[2,27,26,0]},{"coordinate":[1,4],"connectedNodes":[1,3]},{"coordinate":[1,5],"connectedNodes":[2,4]},{"coordinate":[1,6],"connectedNodes":[3,5]},{"coordinate":[1,7],"connectedNodes":[4,6]},{"coordinate":[2,7],"connectedNodes":[5,7]},{"coordinate":[3,7],"connectedNodes":[6,8]},{"coordinate":[4,7],"connectedNodes":[7,9]},{"coordinate":[5,7],"connectedNodes":[8,10]},{"coordinate":[6,7],"connectedNodes":[9,11]},{"coordinate":[7,7],"connectedNodes":[10,12]},{"coordinate":[7,6],"connectedNodes":[11,13]},{"coordinate":[7,5],"connectedNodes":[12,14]},{"coordinate":[7,4],"connectedNodes":[13,15]},{"coordinate":[7,3],"connectedNodes":[14,16]},{"coordinate":[7,2],"connectedNodes":[15,17]},{"coordinate":[7,1],"connectedNodes":[16,18]},{"coordinate":[7,0],"connectedNodes":[17,19]},{"coordinate":[6,0],"connectedNodes":[18,20]},{"coordinate":[5,0],"connectedNodes":[19,21]},{"coordinate":[4,0],"connectedNodes":[20,22]},{"coordinate":[3,0],"connectedNodes":[21,23]},{"coordinate":[2,0],"connectedNodes":[22,24]},{"coordinate":[1,0],"connectedNodes":[23,25]},{"coordinate":[1,1],"connectedNodes":[24,26]},{"coordinate":[1,2],"connectedNodes":[25,1]},{"coordinate":[2,3],"connectedNodes":[28,45,44,1]},{"coordinate":[2,4],"connectedNodes":[27,29]},{"coordinate":[2,5],"connectedNodes":[28,30]},{"coordinate":[2,6],"connectedNodes":[29,31]},{"coordinate":[3,6],"connectedNodes":[30,32]},{"coordinate":[4,6],"connectedNodes":[31,33]},{"coordinate":[5,6],"connectedNodes":[32,34]},{"coordinate":[6,6],"connectedNodes":[33,35]},{"coordinate":[6,5],"connectedNodes":[34,36]},{"coordinate":[6,4],"connectedNodes":[35,37]},{"coordinate":[6,3],"connectedNodes":[36,38]},{"coordinate":[6,2],"connectedNodes":[37,39]},{"coordinate":[6,1],"connectedNodes":[38,40]},{"coordinate":[5,1],"connectedNodes":[39,41]},{"coordinate":[4,1],"connectedNodes":[40,42]},{"coordinate":[3,1],"connectedNodes":[41,43]},{"coordinate":[2,1],"connectedNodes":[42,44]},{"coordinate":[2,2],"connectedNodes":[43,27]},{"coordinate":[3,3],"connectedNodes":[46,54,53,27]},{"coordinate":[3,4],"connectedNodes":[45,47]},{"coordinate":[3,5],"connectedNodes":[46,48]},{"coordinate":[4,5],"connectedNodes":[47,49]},{"coordinate":[5,5],"connectedNodes":[48,50]},{"coordinate":[5,4],"connectedNodes":[49,51]},{"coordinate":[5,3],"connectedNodes":[50,52]},{"coordinate":[5,2],"connectedNodes":[51,56]},{"coordinate":[3,2],"connectedNodes":[45,56]},{"coordinate":[4,3],"connectedNodes":[45,55]},{"coordinate":[4,4],"connectedNodes":[54]},{"coordinate":[4,2],"connectedNodes":[52,53]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level43 = Level(name='43', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    decor='[{"coordinate":{"x":399,"y":398},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":605,"y":397},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":576,"y":604},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":434,"y":601},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":600,"y":199},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":852,"y":649},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":853,"y":499},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":854,"y":348},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":855,"y":198},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":854,"y":42},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":176,"y":598},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":404,"y":199},"url":"/static/game/image/bush.svg"}]',
                    destinations='[[5, 7]]', direct_drive=False, fuel_gauge=True, max_fuel=50,
                    model_solution='[21]', origin='{"coordinate":[0, 5], "direction":"E"}',
                    path='[{"coordinate":[0,5],"connectedNodes":[1]},{"coordinate":[1,5],"connectedNodes":[0,2]},{"coordinate":[1,4],"connectedNodes":[1,3]},{"coordinate":[2,4],"connectedNodes":[2,4]},{"coordinate":[2,3],"connectedNodes":[5,3]},{"coordinate":[1,3],"connectedNodes":[4,6]},{"coordinate":[1,2],"connectedNodes":[5,7,8]},{"coordinate":[2,2],"connectedNodes":[6,9]},{"coordinate":[1,1],"connectedNodes":[6,9]},{"coordinate":[2,1],"connectedNodes":[8,7,10]},{"coordinate":[2,0],"connectedNodes":[9,11]},{"coordinate":[3,0],"connectedNodes":[10,12]},{"coordinate":[4,0],"connectedNodes":[11,13]},{"coordinate":[4,1],"connectedNodes":[14,12]},{"coordinate":[3,1],"connectedNodes":[15,13]},{"coordinate":[3,2],"connectedNodes":[16,14]},{"coordinate":[3,3],"connectedNodes":[17,15]},{"coordinate":[4,3],"connectedNodes":[16,18]},{"coordinate":[5,3],"connectedNodes":[17,19,28,20]},{"coordinate":[5,4],"connectedNodes":[29,18]},{"coordinate":[5,2],"connectedNodes":[18,21]},{"coordinate":[5,1],"connectedNodes":[20,22]},{"coordinate":[5,0],"connectedNodes":[21,23]},{"coordinate":[6,0],"connectedNodes":[22,24]},{"coordinate":[7,0],"connectedNodes":[23,25]},{"coordinate":[7,1],"connectedNodes":[26,24]},{"coordinate":[7,2],"connectedNodes":[27,25]},{"coordinate":[7,3],"connectedNodes":[28,26]},{"coordinate":[6,3],"connectedNodes":[18,27]},{"coordinate":[5,5],"connectedNodes":[30,40,19]},{"coordinate":[4,5],"connectedNodes":[31,29]},{"coordinate":[3,5],"connectedNodes":[32,30]},{"coordinate":[3,6],"connectedNodes":[33,31]},{"coordinate":[3,7],"connectedNodes":[41,34,32]},{"coordinate":[4,7],"connectedNodes":[33,35]},{"coordinate":[5,7],"connectedNodes":[34,36]},{"coordinate":[6,7],"connectedNodes":[35,37]},{"coordinate":[7,7],"connectedNodes":[36,38]},{"coordinate":[7,6],"connectedNodes":[37,39]},{"coordinate":[7,5],"connectedNodes":[40,38]},{"coordinate":[6,5],"connectedNodes":[29,39]},{"coordinate":[2,7],"connectedNodes":[42,33]},{"coordinate":[1,7],"connectedNodes":[41]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

    level44 = Level(name='44', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    decor='[{"coordinate":{"x":472,"y":686},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":532,"y":623},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":459,"y":606},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":612,"y":693},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":139,"y":697},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":209,"y":612},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":45,"y":608},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":67,"y":504},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":154,"y":529},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":265,"y":20},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":173,"y":16},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":-21,"y":-14},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":64,"y":54},"url":"/static/game/image/bush.svg"}]',
                    destinations='[[6, 3]]', direct_drive=False, fuel_gauge=True, max_fuel=50,
                    model_solution='[5, 6]', origin='{"coordinate":[0, 3], "direction":"E"}',
                    path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[2,3],"connectedNodes":[1,3]},{"coordinate":[3,3],"connectedNodes":[2,4]},{"coordinate":[4,3],"connectedNodes":[3,5]},{"coordinate":[5,3],"connectedNodes":[4,6]},{"coordinate":[6,3],"connectedNodes":[5]}]',
                    pythonEnabled=False, theme=grass, threads=1,
                    traffic_lights='[{"direction":"E", "startTime":0, "sourceCoordinate":{"y":3, "x":3}, "greenDuration":2, "startingState":"RED", "redDuration":4}]')

    level45 = Level(name='45', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    decor='[{"coordinate":{"x":198,"y":702},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":400,"y":702},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":600,"y":700},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":802,"y":699},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":100,"y":601},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":299,"y":601},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":503,"y":600},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":701,"y":600},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":899,"y":601},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":4,"y":1},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":199,"y":-2},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":401,"y":0},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":600,"y":0},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":801,"y":0},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":101,"y":99},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":299,"y":97},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":502,"y":97},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":700,"y":106},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":899,"y":100},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":0,"y":699},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":4,"y":493},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":200,"y":495},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":398,"y":500},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":604,"y":498},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":804,"y":503},"url":"/static/game/image/tree2.svg"}]',
                    destinations='[[0, 3]]', direct_drive=False, fuel_gauge=True, max_fuel=50,
                    model_solution='[6, 7]', origin='{"coordinate":[7, 3], "direction":"W"}',
                    path='[{"coordinate":[7,3],"connectedNodes":[6]},{"coordinate":[1,3],"connectedNodes":[7,2]},{"coordinate":[2,3],"connectedNodes":[1,3]},{"coordinate":[3,3],"connectedNodes":[2,4]},{"coordinate":[4,3],"connectedNodes":[3,5]},{"coordinate":[5,3],"connectedNodes":[4,6]},{"coordinate":[6,3],"connectedNodes":[5,0]},{"coordinate":[0,3],"connectedNodes":[1]}] ',
                    pythonEnabled=False, theme=grass, threads=1,
                    traffic_lights='[{"direction":"W", "startTime":0, "sourceCoordinate":{"y":3, "x":4}, "greenDuration":1, "startingState":"GREEN", "redDuration":4},{"direction":"W", "startTime":0, "sourceCoordinate":{"y":3, "x":5}, "greenDuration":1, "startingState":"RED", "redDuration":3}]')

    level46 = Level(name='46', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    decor='[{"coordinate":{"x":772,"y":670},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":900,"y":569},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":772,"y":501},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":654,"y":632},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":811,"y":576},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":861,"y":694},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":707,"y":741},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":-1,"y":198},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":22,"y":70},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":100,"y":150},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":121,"y":-13},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":58,"y":-15},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":151,"y":45},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":719,"y":223},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":654,"y":103},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":755,"y":128},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":3,"y":623},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":59,"y":697},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":27,"y":563},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":111,"y":680},"url":"/static/game/image/tree1.svg"}]',
                    destinations='[[2, 6]]', direct_drive=False, fuel_gauge=True, max_fuel=50,
                    model_solution='[8, 9]', origin='{"coordinate":[6, 5], "direction":"S"}',
                    path='[{"coordinate":[6,5],"connectedNodes":[1]},{"coordinate":[6,4],"connectedNodes":[0,2]},{"coordinate":[6,3],"connectedNodes":[3,1]},{"coordinate":[5,3],"connectedNodes":[4,2]},{"coordinate":[4,3],"connectedNodes":[5,3]},{"coordinate":[3,3],"connectedNodes":[6,4]},{"coordinate":[2,3],"connectedNodes":[7,5]},{"coordinate":[2,4],"connectedNodes":[8,6]},{"coordinate":[2,5],"connectedNodes":[9,7]},{"coordinate":[2,6],"connectedNodes":[8]}]',
                    pythonEnabled=False, theme=grass, threads=1,
                    traffic_lights='[{"direction":"W", "startTime":0, "sourceCoordinate":{"y":3, "x":5}, "greenDuration":2, "startingState":"RED", "redDuration":4}]')

    level47 = Level(name='47', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    decor='[{"coordinate":{"x":46,"y":683},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":8,"y":589},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":149,"y":716},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":106,"y":568},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":806,"y":262},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":760,"y":165},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":852,"y":86},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":761,"y":51},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":865,"y":175},"url":"/static/game/image/tree2.svg"}]',
                    destinations='[[4, 3]]', direct_drive=False, fuel_gauge=True, max_fuel=50,
                    model_solution='[8, 9]', origin='{"coordinate":[6, 1], "direction":"N"}',
                    path='[{"coordinate":[6,1],"connectedNodes":[1]},{"coordinate":[6,2],"connectedNodes":[2,0]},{"coordinate":[6,3],"connectedNodes":[3,1]},{"coordinate":[6,4],"connectedNodes":[4,2]},{"coordinate":[6,5],"connectedNodes":[5,3]},{"coordinate":[6,6],"connectedNodes":[6,4]},{"coordinate":[5,6],"connectedNodes":[7,5]},{"coordinate":[4,6],"connectedNodes":[8,6]},{"coordinate":[3,6],"connectedNodes":[9,7]},{"coordinate":[2,6],"connectedNodes":[8,10]},{"coordinate":[2,5],"connectedNodes":[9,11]},{"coordinate":[2,4],"connectedNodes":[10,12]},{"coordinate":[2,3],"connectedNodes":[11,13]},{"coordinate":[2,2],"connectedNodes":[12,14]},{"coordinate":[3,2],"connectedNodes":[13,15]},{"coordinate":[4,2],"connectedNodes":[14,16]},{"coordinate":[4,3],"connectedNodes":[15]}]',
                    pythonEnabled=False, theme=grass, threads=1,
                    traffic_lights='[{"direction":"N", "startTime":0, "sourceCoordinate":{"y":3, "x":6}, "greenDuration":3, "startingState":"RED", "redDuration":3}, {"direction":"W", "startTime":0, "sourceCoordinate":{"y":6, "x":5}, "greenDuration":3, "startingState":"RED", "redDuration":3}, {"direction":"S", "startTime":, "sourceCoordinate":{"y":5, "x":2}, "greenDuration":3, "startingState":"RED", "redDuration":3}, {"direction":"E", "startTime":0, "sourceCoordinate":{"y":2, "x":3}, "greenDuration":3, "startingState":"GREEN", "redDuration":3}]')

    level48 = Level(name='48', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    decor='[{"coordinate":{"x":144,"y":399},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":240,"y":372},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":169,"y":294},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":81,"y":333},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":520,"y":605},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":639,"y":598},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":740,"y":560},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":731,"y":695},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":12,"y":6},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":203,"y":6},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":403,"y":9},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":603,"y":11},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":804,"y":10},"url":"/static/game/image/bush.svg"}]',
                    destinations='[[1, 2]]', direct_drive=False, fuel_gauge=True, max_fuel=50,
                    model_solution='[12, 13]', origin='{"coordinate":[1, 5], "direction":"E"}',
                    path='[{"coordinate":[1,5],"connectedNodes":[1]},{"coordinate":[2,5],"connectedNodes":[0,2]},{"coordinate":[3,5],"connectedNodes":[1,3]},{"coordinate":[4,5],"connectedNodes":[2,4,6,5]},{"coordinate":[4,6],"connectedNodes":[7,3]},{"coordinate":[4,4],"connectedNodes":[3,10]},{"coordinate":[5,5],"connectedNodes":[3,17]},{"coordinate":[4,7],"connectedNodes":[8,4]},{"coordinate":[5,7],"connectedNodes":[7,9]},{"coordinate":[6,7],"connectedNodes":[8]},{"coordinate":[4,3],"connectedNodes":[5,11]},{"coordinate":[4,2],"connectedNodes":[14,10,12]},{"coordinate":[5,2],"connectedNodes":[11,13]},{"coordinate":[6,2],"connectedNodes":[12]},{"coordinate":[3,2],"connectedNodes":[15,11]},{"coordinate":[2,2],"connectedNodes":[16,14]},{"coordinate":[1,2],"connectedNodes":[15]},{"coordinate":[6,5],"connectedNodes":[6,18]},{"coordinate":[7,5],"connectedNodes":[17,19]},{"coordinate":[7,4],"connectedNodes":[18]}]',
                    pythonEnabled=False, theme=grass, threads=1,
                    traffic_lights='[{"direction":"E", "startTime":0, "sourceCoordinate":{"y":5, "x":3}, "greenDuration":2, "startingState":"RED", "redDuration":4}, {"direction":"S", "startTime":0, "sourceCoordinate":{"y":6, "x":4}, "greenDuration":4, "startingState":"GREEN", "redDuration":2}, {"direction":"N", "startTime":, "sourceCoordinate":{"y":4, "x":4}, "greenDuration":4, "startingState":"GREEN", "redDuration":2}, {"direction":"W", "startTime":0, "sourceCoordinate":{"y":5, "x":5}, "greenDuration":2, "startingState":"RED", "redDuration":4}]')

    level49 = Level(name='49', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    decor='[{"coordinate":{"x":501,"y":487},"name":"tree2"},{"coordinate":{"x":475,"y":262},"name":"pond"},{"coordinate":{"x":181,"y":323},"name":"tree1"},{"coordinate":{"x":65,"y":489},"name":"bush"},{"coordinate":{"x":63,"y":426},"name":"bush"},{"coordinate":{"x":60,"y":356},"name":"bush"},{"coordinate":{"x":57,"y":291},"name":"bush"},{"coordinate":{"x":130,"y":489},"name":"bush"},{"coordinate":{"x":194,"y":491},"name":"bush"},{"coordinate":{"x":262,"y":492},"name":"bush"},{"coordinate":{"x":479,"y":196},"name":"bush"},{"coordinate":{"x":400,"y":290},"name":"bush"},{"coordinate":{"x":637,"y":287},"name":"bush"},{"coordinate":{"x":639,"y":350},"name":"bush"},{"coordinate":{"x":404,"y":353},"name":"bush"},{"coordinate":{"x":556,"y":196},"name":"bush"},{"coordinate":{"x":777,"y":530},"name":"tree1"},{"coordinate":{"x":787,"y":453},"name":"bush"},{"coordinate":{"x":789,"y":380},"name":"bush"},{"coordinate":{"x":787,"y":308},"name":"bush"}]',
                    destinations='[[9, 6]]', direct_drive=False, fuel_gauge=True, max_fuel=50,
                    model_solution='[12, 13]', origin='{"coordinate":[3, 6], "direction":"S"}',
                    path='[{"coordinate":[3,6],"connectedNodes":[1]},{"coordinate":[3,5],"connectedNodes":[0,2]},{"coordinate":[3,4],"connectedNodes":[3,1,4,5]},{"coordinate":[2,4],"connectedNodes":[19,2]},{"coordinate":[4,4],"connectedNodes":[2,6]},{"coordinate":[3,3],"connectedNodes":[2,16]},{"coordinate":[5,4],"connectedNodes":[4,7]},{"coordinate":[6,4],"connectedNodes":[6,8]},{"coordinate":[7,4],"connectedNodes":[7,9,13]},{"coordinate":[7,5],"connectedNodes":[10,8]},{"coordinate":[7,6],"connectedNodes":[11,9]},{"coordinate":[8,6],"connectedNodes":[10,12]},{"coordinate":[9,6],"connectedNodes":[11]},{"coordinate":[7,3],"connectedNodes":[8,14]},{"coordinate":[7,2],"connectedNodes":[13,15]},{"coordinate":[8,2],"connectedNodes":[14]},{"coordinate":[3,2],"connectedNodes":[17,5]},{"coordinate":[2,2],"connectedNodes":[18,16]},{"coordinate":[1,2],"connectedNodes":[21,20,17]},{"coordinate":[1,4],"connectedNodes":[3,20]},{"coordinate":[1,3],"connectedNodes":[19,18]},{"coordinate":[0,2],"connectedNodes":[18,22]},{"coordinate":[0,1],"connectedNodes":[21]}]',
                    pythonEnabled=False, theme=city, threads=1,
                    traffic_lights='[{"direction":"S", "startTime":0, "sourceCoordinate":{"y":5, "x":3}, "greenDuration":2, "startingState":"RED", "redDuration":4}, {"direction":"E", "startTime":0, "sourceCoordinate":{"y":4, "x":2}, "greenDuration":2, "startingState":"GREEN", "redDuration":4}, {"direction":"W", "startTime":, "sourceCoordinate":{"y":4, "x":4}, "greenDuration":2, "startingState":"GREEN", "redDuration":4}, {"direction":"N", "startTime":0, "sourceCoordinate":{"y":3, "x":3}, "greenDuration":2, "startingState":"RED", "redDuration":4}, {"direction":"S", "startTime":0, "sourceCoordinate":{"y":5, "x":7},"greenDuration":4, "startingState":"GREEN", "redDuration":2}, {"direction":"N", "startTime":0, "sourceCoordinate":{"y":3, "x":7}, "greenDuration":4, "startingState":"GREEN", "redDuration":2}, {"direction":"E", "startTime":, "sourceCoordinate":{"y":4, "x":6}, "greenDuration":2, "startingState":"RED", "redDuration":4}]')

    level50 = Level(name='50', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    decor='[{"coordinate":{"x":482,"y":75},"name":"pond"},{"coordinate":{"x":797,"y":491},"name":"tree2"},{"coordinate":{"x":494,"y":492},"name":"bush"},{"coordinate":{"x":494,"y":558},"name":"bush"},{"coordinate":{"x":494,"y":426},"name":"bush"},{"coordinate":{"x":495,"y":356},"name":"bush"},{"coordinate":{"x":495,"y":291},"name":"bush"},{"coordinate":{"x":284,"y":584},"name":"tree1"},{"coordinate":{"x":686,"y":39},"name":"bush"},{"coordinate":{"x":686,"y":98},"name":"bush"},{"coordinate":{"x":684,"y":160},"name":"bush"}]',
                    destinations='[[6, 4]]', direct_drive=False, fuel_gauge=True, max_fuel=50,
                    model_solution='[16]', origin='{"coordinate":[0, 3], "direction":"E"}',
                    path='[{"coordinate":[0,3],"connectedNodes":[1]}, {"coordinate":[1,3],"connectedNodes":[0,27,2]},{"coordinate":[1,2],"connectedNodes":[1,3]}, {"coordinate":[1,1],"connectedNodes":[2,4]},{"coordinate":[2,1],"connectedNodes":[3,6,5]}, {"coordinate":[2,0],"connectedNodes":[4]},{"coordinate":[3,1],"connectedNodes":[4,7]}, {"coordinate":[4,1],"connectedNodes":[6,8]},{"coordinate":[4,2],"connectedNodes":[9,11,7]}, {"coordinate":[4,3],"connectedNodes":[10,36,8]},{"coordinate":[3,3],"connectedNodes":[9]}, {"coordinate":[5,2],"connectedNodes":[8,12]},{"coordinate":[6,2],"connectedNodes":[11,15,13]}, {"coordinate":[6,1],"connectedNodes":[12,14]},{"coordinate":[6,0],"connectedNodes":[13]}, {"coordinate":[7,2],"connectedNodes":[12,16]},{"coordinate":[8,2],"connectedNodes":[15,25,17]}, {"coordinate":[8,1],"connectedNodes":[16,18]},{"coordinate":[8,0],"connectedNodes":[17,19]}, {"coordinate":[9,0],"connectedNodes":[18,20]},{"coordinate":[9,1],"connectedNodes":[21,19]}, {"coordinate":[9,2],"connectedNodes":[22,20]},{"coordinate":[9,3],"connectedNodes":[23,21]}, {"coordinate":[9,4],"connectedNodes":[24,22]},{"coordinate":[8,4],"connectedNodes":[26,23,25]}, {"coordinate":[8,3],"connectedNodes":[24,16]},{"coordinate":[7,4],"connectedNodes":[42,28,24]}, {"coordinate":[1,4],"connectedNodes":[41,1]},{"coordinate":[7,5],"connectedNodes":[29,26]}, {"coordinate":[7,6],"connectedNodes":[32,30,28]},{"coordinate":[8,6],"connectedNodes":[29,31]}, {"coordinate":[9,6],"connectedNodes":[30]},{"coordinate":[6,6],"connectedNodes":[33,29]}, {"coordinate":[5,6],"connectedNodes":[34,32]},{"coordinate":[4,6],"connectedNodes":[33,35]}, {"coordinate":[4,5],"connectedNodes":[37,34,36]},{"coordinate":[4,4],"connectedNodes":[35,9]}, {"coordinate":[3,5],"connectedNodes":[38,35]},{"coordinate":[2,5],"connectedNodes":[39,37]}, {"coordinate":[2,6],"connectedNodes":[40,38]},{"coordinate":[1,6],"connectedNodes":[39,41]}, {"coordinate":[1,5],"connectedNodes":[40,27]},{"coordinate":[6,4],"connectedNodes":[26]} ]',
                    pythonEnabled=False, theme=city, threads=1,
                    traffic_lights='[{"direction":"E", "startTime":0, "sourceCoordinate":{"y":1, "x":1}, "greenDuration":2, "startingState":"RED", "redDuration":4}, {"direction":"N", "startTime":2, "sourceCoordinate":{"y":0, "x":2}, "greenDuration":2, "startingState":"RED", "redDuration":4}, {"direction":"W", "startTime":, "sourceCoordinate":{"y":1, "x":3}, "greenDuration":2, "startingState":"GREEN", "redDuration":4}, {"direction":"N", "startTime":0, "sourceCoordinate":{"y":1, "x":4}, "greenDuration":2, "startingState":"RED", "redDuration":4}, {"direction":"S", "startTime":2, "sourceCoordinate":{"y":3, "x":4},"greenDuration":2, "startingState":"RED", "redDuration":4}, {"direction":"W", "startTime":0, "sourceCoordinate":{"y":2, "x":5}, "greenDuration":2, "startingState":"GREEN", "redDuration":4}, {"direction":"E", "startTime":, "sourceCoordinate":{"y":5, "x":3}, "greenDuration":2, "startingState":"RED", "redDuration":4}, {"direction":"S", "startTime":2, "sourceCoordinate":{"y":6, "x":4}, "greenDuration":2, "startingState":"RED", "redDuration":4}, {"direction":"N", "startTime":0, "sourceCoordinate":{"y":4, "x":4},"greenDuration":2, "startingState":"GREEN", "redDuration":4}, {"direction":"W", "startTime":0, "sourceCoordinate":{"y":6, "x":2}, "greenDuration":4, "startingState":"RED", "redDuration":2}, {"direction":"W", "startTime":, "sourceCoordinate":{"y":4, "x":9}, "greenDuration":2, "startingState":"RED", "redDuration":4}, {"direction":"N", "startTime":2, "sourceCoordinate":{"y":3, "x":8}, "greenDuration":2, "startingState":"RED", "redDuration":4}, {"direction":"E", "startTime":0, "sourceCoordinate":{"y":4, "x":7},"greenDuration":2, "startingState":"GREEN", "redDuration":4}]')

    level1.save()
    level2.save()
    level3.save()
    level4.save()
    level5.save()
    level6.save()
    level7.save()
    level8.save()
    level9.save()
    level10.save()
    level11.save()
    level12.save()
    level13.save()
    level14.save()
    level15.save()
    level16.save()
    level17.save()
    level18.save()
    level19.save()
    level20.save()
    level21.save()
    level22.save()
    level23.save()
    level24.save()
    level25.save()
    level26.save()
    level27.save()
    level28.save()
    level29.save()
    level30.save()
    level31.save()
    level32.save()
    level33.save()
    level34.save()
    level35.save()
    level36.save()
    level37.save()
    level38.save()
    level39.save()
    level40.save()
    level41.save()
    level42.save()
    level43.save()
    level44.save()
    level45.save()
    level46.save()
    level47.save()
    level48.save()
    level49.save()
    level50.save()

    level1.next_level = level2
    level2.next_level = level3
    level3.next_level = level4
    level4.next_level = level5
    level5.next_level = level6
    level6.next_level = level7
    level7.next_level = level8
    level8.next_level = level9
    level9.next_level = level10
    level10.next_level = level11
    level11.next_level = level12

    level13.next_level = level14
    level14.next_level = level15
    level15.next_level = level16
    level16.next_level = level17
    level17.next_level = level18

    level19.next_level = level20
    level20.next_level = level21
    level21.next_level = level22
    level22.next_level = level23
    level23.next_level = level24
    level24.next_level = level25
    level25.next_level = level26
    level26.next_level = level27
    level27.next_level = level28

    level29.next_level = level30
    level30.next_level = level31
    level31.next_level = level32

    level33.next_level = level34
    level34.next_level = level35
    level35.next_level = level36
    level36.next_level = level37
    level37.next_level = level38
    level38.next_level = level39
    level39.next_level = level40
    level40.next_level = level41
    level41.next_level = level42
    level42.next_level = level43

    level44.next_level = level45
    level45.next_level = level46
    level46.next_level = level47
    level47.next_level = level48
    level48.next_level = level49
    level49.next_level = level50

    level1.save()
    level2.save()
    level3.save()
    level4.save()
    level5.save()
    level6.save()
    level7.save()
    level8.save()
    level9.save()
    level10.save()
    level11.save()
    level12.save()
    level13.save()
    level14.save()
    level15.save()
    level16.save()
    level17.save()
    level18.save()
    level19.save()
    level20.save()
    level21.save()
    level22.save()
    level23.save()
    level24.save()
    level25.save()
    level26.save()
    level27.save()
    level28.save()
    level29.save()
    level30.save()
    level31.save()
    level32.save()
    level33.save()
    level34.save()
    level35.save()
    level36.save()
    level37.save()
    level38.save()
    level39.save()
    level40.save()
    level41.save()
    level42.save()
    level43.save()
    level44.save()
    level45.save()
    level46.save()
    level47.save()
    level48.save()
    level49.save()
    level50.save()


def setup_blocks(apps, schema_editor):

    Level = apps.get_model('game', 'Level')
    Block = apps.get_model('game', 'Block')

    blocks = Block.objects.filter(type="move_forwards")

    for i in range(1, 3):
        level = Level.objects.get(pk=i)
        level.blocks = blocks
        level.save()

    level3 = Level.objects.get(pk=3)
    level3.blocks = Block.objects.filter(type__in=["turn_right", "move_forwards"])
    level3.save()

    level4 = Level.objects.get(pk=4)
    level4.blocks = Block.objects.filter(type__in=["turn_left", "move_forwards"])
    level4.save()

    blocks = Block.objects.filter(type__in=["turn_right", "turn_left", "move_forwards"])

    for i in range(5, 15):
        level = Level.objects.get(pk=i)
        level.blocks = blocks
        level.save()

    blocks = Block.objects.filter(type__in=["turn_right", "turn_left", "move_forwards", "deliver"])

    for i in range(15, 19):
        level = Level.objects.get(pk=i)
        level.blocks = blocks
        level.save()

    blocks = Block.objects.filter(type__in=["turn_right", "turn_left", "move_forwards",
                                            "controls_repeat"])

    for i in range(19, 29):
        level = Level.objects.get(pk=i)
        level.blocks = blocks
        level.save()

    blocks = Block.objects.filter(type__in=["turn_right", "turn_left", "move_forwards",
                                            "controls_repeat_until", "at_destination",
                                            "road_exists", "controls_if"])

    for i in range(29, 33):
        level = Level.objects.get(pk=i)
        level.blocks = blocks
        level.save()

    blocks = Block.objects.filter(type__in=["turn_right", "turn_left", "move_forwards",
                                            "controls_repeat_until", "at_destination"])

    for i in range(29, 39):
        level = Level.objects.get(pk=i)
        level.blocks = blocks
        level.save()

    blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards",
                                            "turn_around", "controls_repeat_until",
                                            "at_destination", "controls_if", "road_exists",
                                            "at_destination", "controls_repeat", "dead_end"])

    for i in range(39, 44):
        level = Level.objects.get(pk=i)
        level.blocks = blocks
        level.save()

    blocks = Block.objects.filter(type__in=["move_forwards", "controls_repeat_until",
                                            "at_destination", "controls_if", "road_exists",
                                            "controls_repeat", "controls_repeat_while",
                                            "wait", "traffic_light"])

    level44 = Level.objects.get(pk=44)
    level44.blocks = blocks
    level44.save()

    level45 = Level.objects.get(pk=45)
    level45.blocks = blocks
    level45.save()

    blocks = Block.objects.filter(type__in=["move_forwards", "turn_right", "controls_repeat_until",
                                            "at_destination", "controls_if", "road_exists",
                                            "controls_repeat", "controls_repeat_while",
                                            "wait", "traffic_light"])

    level46 = Level.objects.get(pk=46)
    level46.blocks = blocks
    level46.save()

    blocks = Block.objects.filter(type__in=["move_forwards", "turn_right", "turn_left",
                                            "controls_repeat_until", "at_destination",
                                            "controls_if", "road_exists", "controls_repeat",
                                            "controls_repeat_while", "wait", "traffic_light"])

    level47 = Level.objects.get(pk=47)
    level47.blocks = blocks
    level47.save()

    blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards",
                                            "controls_repeat_until", "at_destination",
                                            "controls_if", "road_exists", "at_destination",
                                            "controls_repeat", "dead_end", "controls_repeat_while",
                                            "wait", "traffic_light", "turn_around"])

    for i in range(48, 51):
        level = Level.objects.get(pk=i)
        level.blocks = blocks
        level.save()


def add_episodes(apps, schema_editor):

    Level = apps.get_model('game', 'Level')
    Episode = apps.get_model('game', 'Episode')
    Block = apps.get_model('game', 'Block')

    level1 = Level.objects.get(pk=1)

    episode1 = Episode(pk=1, name="Getting Started", first_level=level1, r_branchiness=0,
                       r_loopiness=0, r_num_tiles=10, r_curviness=0.5, r_pythonEnabled=0,
                       r_blocklyEnabled=1, r_trafficLights=0)
    episode1.save()

    level13 = Level.objects.get(pk=13)

    episode2 = Episode(pk=2, name="Shortest Route", first_level=level13, r_branchiness=0.3,
                       r_loopiness=0.05, r_num_tiles=20, r_curviness=0.15, r_pythonEnabled=0,
                       r_blocklyEnabled=1, r_trafficLights=0)
    episode2.save()

    level19 = Level.objects.get(pk=19)

    episode3 = Episode(pk=3, name="Loops and Repetitions", first_level=level19, r_branchiness=0,
                       r_loopiness=0, r_num_tiles=15, r_curviness=0.2, r_pythonEnabled=0,
                       r_blocklyEnabled=1, r_trafficLights=0)
    episode3.save()

    level29 = Level.objects.get(pk=29)

    episode4 = Episode(pk=4, name="Loops with Conditions", first_level=level29, r_branchiness=0,
                       r_loopiness=0, r_num_tiles=15, r_curviness=0.2, r_pythonEnabled=0,
                       r_blocklyEnabled=1, r_trafficLights=0)
    episode4.save()

    level33 = Level.objects.get(pk=33)

    episode5 = Episode(pk=5, name="If... Only", first_level=level33, r_branchiness=0.4,
                       r_loopiness=0.4, r_num_tiles=13, r_curviness=0.3, r_pythonEnabled=0,
                       r_blocklyEnabled=1, r_trafficLights=0)
    episode5.save()

    level44 = Level.objects.get(pk=44)

    episode6 = Episode(pk=6, name="Traffic Lights", first_level=level44, r_branchiness=0.5,
                       r_loopiness=0.1, r_num_tiles=35, r_curviness=0.2, r_pythonEnabled=0,
                       r_blocklyEnabled=1, r_trafficLights=1)
    episode6.save()

    episode1.next_episode = episode2
    episode2.next_episode = episode3
    episode3.next_episode = episode4
    episode4.next_episode = episode5
    episode5.next_episode = episode6

    episode1.r_blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards"])

    episode2.r_blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards",
                                                       "deliver"])

    episode3.r_blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards",
                                                       "controls_repeat"])

    episode4.r_blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards",
                                                       "controls_repeat_until", "at_destination",
                                                       "controls_repeat"])

    episode5.r_blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards",
                                                       "controls_repeat_until", "at_destination",
                                                       "controls_if", "road_exists", "dead_end",
                                                       "controls_repeat", "turn_around"])

    episode6.r_blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards",
                                                       "controls_repeat_until", "controls_if",
                                                       "road_exists", "at_destination", "wait",
                                                       "controls_repeat", "dead_end", "turn_around",
                                                       "controls_repeat_while", "traffic_light"])

    episode1.save()
    episode2.save()
    episode3.save()
    episode4.save()
    episode5.save()
    episode6.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_characters_theme_decor_block'),
    ]

    operations = [
        migrations.RunPython(add_levels),
        migrations.RunPython(setup_blocks),
        migrations.RunPython(add_episodes)
    ]
