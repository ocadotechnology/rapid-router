# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def add_levels(apps, schema_editor):

    Level = apps.get_model('game', 'Level')
    Episode = apps.get_model('game', 'Episode')
    Theme = apps.get_model('game', 'Theme')
    Character = apps.get_model('game', 'Character')
    LevelDecor = apps.get_model('game', 'LevelDecor')
    LevelBlock = apps.get_model('game', 'LevelBlock')

    grass = Theme.objects.get(name='grass')
    snow = Theme.objects.get(name='snow')
    farm = Theme.objects.get(name='farm')
    city = Theme.objects.get(name='city')

    van = Character.objects.get(name='Van')

    # keep track of where we're copying the vague basis of the python levels
    levelPairs = []

    # from level6
    levelPairs.append(["6","80"])
    level80 = Level(name='80', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[6, 1]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    origin='{"coordinate":[0, 4], "direction":"E"}',
                    path='[{"coordinate":[0,4],"connectedNodes":[1]},{"coordinate":[1,4],"connectedNodes":[0,2]},{"coordinate":[2,4],"connectedNodes":[1,3]},{"coordinate":[3,4],"connectedNodes":[2,4]},{"coordinate":[3,5],"connectedNodes":[5,3]},{"coordinate":[4,5],"connectedNodes":[4,6]},{"coordinate":[5,5],"connectedNodes":[5,7]},{"coordinate":[5,4],"connectedNodes":[6,8]},{"coordinate":[5,3],"connectedNodes":[7,9]},{"coordinate":[5,2],"connectedNodes":[8,10]},{"coordinate":[5,1],"connectedNodes":[9,11]},{"coordinate":[6,1],"connectedNodes":[10]}]',
                    pythonEnabled=True, theme=grass, threads=1, traffic_lights='[]')

    # from level13
    levelPairs.append(["13","81"])
    level81 = Level(name='81', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[0, 1]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    origin='{"coordinate":[2, 7], "direction":"S"}',
                    path='[{"coordinate":[2,7],"connectedNodes":[1]},{"coordinate":[2,6],"connectedNodes":[0,2]},{"coordinate":[3,6],"connectedNodes":[1,3,10]},{"coordinate":[4,6],"connectedNodes":[2,4]},{"coordinate":[5,6],"connectedNodes":[3,5]},{"coordinate":[6,6],"connectedNodes":[4,6]},{"coordinate":[6,5],"connectedNodes":[5,7]},{"coordinate":[6,4],"connectedNodes":[13,6,8]},{"coordinate":[6,3],"connectedNodes":[7,9]},{"coordinate":[6,2],"connectedNodes":[8,14]},{"coordinate":[3,5],"connectedNodes":[2,11]},{"coordinate":[3,4],"connectedNodes":[10,12]},{"coordinate":[4,4],"connectedNodes":[11,13,18]},{"coordinate":[5,4],"connectedNodes":[12,7]},{"coordinate":[6,1],"connectedNodes":[15,9]},{"coordinate":[5,1],"connectedNodes":[16,14]},{"coordinate":[4,1],"connectedNodes":[19,17,15]},{"coordinate":[4,2],"connectedNodes":[18,16]},{"coordinate":[4,3],"connectedNodes":[12,17]},{"coordinate":[3,1],"connectedNodes":[20,16]},{"coordinate":[2,1],"connectedNodes":[21,19]},{"coordinate":[1,1],"connectedNodes":[22,20]},{"coordinate":[0,1],"connectedNodes":[21]}]',
                    pythonEnabled=True, theme=grass, threads=1, traffic_lights='[]')

    # from level21
    levelPairs.append(["21","82"])
    level82 = Level(name='82', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[3, 7]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    origin='{"coordinate":[1, 6], "direction":"S"}',
                    path='[{"coordinate":[1,6],"connectedNodes":[2]},{"coordinate":[1,4],"connectedNodes":[2,3]},{"coordinate":[1,5],"connectedNodes":[0,1]},{"coordinate":[2,4],"connectedNodes":[1,4]},{"coordinate":[2,3],"connectedNodes":[3,5]},{"coordinate":[3,3],"connectedNodes":[4,6]},{"coordinate":[4,3],"connectedNodes":[5,7]},{"coordinate":[4,4],"connectedNodes":[8,6]},{"coordinate":[5,4],"connectedNodes":[7,9]},{"coordinate":[5,5],"connectedNodes":[10,8]},{"coordinate":[5,6],"connectedNodes":[11,9]},{"coordinate":[4,6],"connectedNodes":[12,10]},{"coordinate":[4,7],"connectedNodes":[13,11]},{"coordinate":[3,7],"connectedNodes":[12]}]',
                    pythonEnabled=True, theme=grass, threads=1, traffic_lights='[]')

    # from level29
    levelPairs.append(["29","83"])
    level83 = Level(name='83', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[4, 3]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    origin='{"coordinate":[0, 3], "direction":"E"}',
                    path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[2,3],"connectedNodes":[1,3]},{"coordinate":[3,3],"connectedNodes":[2,4]},{"coordinate":[4,3],"connectedNodes":[3]}]',
                    pythonEnabled=True, theme=grass, threads=1, traffic_lights='[]')

    # from level35
    levelPairs.append(["35","84"])
    level84 = Level(name='84', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[1, 1]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    origin='{"coordinate":[8, 6], "direction":"W"}',
                    path='[{"coordinate":[8,6],"connectedNodes":[1]},{"coordinate":[7,6],"connectedNodes":[2,0]},{"coordinate":[6,6],"connectedNodes":[3,1]},{"coordinate":[5,6],"connectedNodes":[4,2]},{"coordinate":[4,6],"connectedNodes":[3,5]},{"coordinate":[4,5],"connectedNodes":[4,6]},{"coordinate":[4,4],"connectedNodes":[5,7]},{"coordinate":[5,4],"connectedNodes":[6,8]},{"coordinate":[6,4],"connectedNodes":[7,9]},{"coordinate":[7,4],"connectedNodes":[8,10]},{"coordinate":[8,4],"connectedNodes":[9,11]},{"coordinate":[8,3],"connectedNodes":[10,12]},{"coordinate":[8,2],"connectedNodes":[13,11]},{"coordinate":[7,2],"connectedNodes":[14,12]},{"coordinate":[6,2],"connectedNodes":[15,13]},{"coordinate":[5,2],"connectedNodes":[16,14]},{"coordinate":[4,2],"connectedNodes":[15,17]},{"coordinate":[4,1],"connectedNodes":[18,16]},{"coordinate":[3,1],"connectedNodes":[19,17]},{"coordinate":[2,1],"connectedNodes":[20,18]},{"coordinate":[1,1],"connectedNodes":[19]}]',
                    pythonEnabled=True, theme=grass, threads=1, traffic_lights='[]')

    # from level 36
    levelPairs.append(["36","85"])
    level85 = Level(name='85', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[5, 3]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                    origin='{"coordinate":[0, 3], "direction":"E"}',
                    path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[1,4],"connectedNodes":[1,3]},{"coordinate":[1,5],"connectedNodes":[2,4]},{"coordinate":[1,6],"connectedNodes":[3,5]},{"coordinate":[2,6],"connectedNodes":[4,6]},{"coordinate":[2,5],"connectedNodes":[5,7]},{"coordinate":[3,5],"connectedNodes":[6,8]},{"coordinate":[3,4],"connectedNodes":[7,9]},{"coordinate":[3,3],"connectedNodes":[8,10]},{"coordinate":[3,2],"connectedNodes":[9,11]},{"coordinate":[4,2],"connectedNodes":[10,12]},{"coordinate":[4,3],"connectedNodes":[11,13]},{"coordinate":[5,3],"connectedNodes":[12]}] ',
                    pythonEnabled=True, theme=grass, threads=1, traffic_lights='[]')

    # from level47
    levelPairs.append(["47","86"])
    level86 = Level(name='86', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    destinations='[[4, 3]]', direct_drive=False, fuel_gauge=True, max_fuel=50,
                    origin='{"coordinate":[6, 1], "direction":"N"}',
                    path='[{"coordinate":[6,1],"connectedNodes":[1]},{"coordinate":[6,2],"connectedNodes":[2,0]},{"coordinate":[6,3],"connectedNodes":[3,1]},{"coordinate":[6,4],"connectedNodes":[4,2]},{"coordinate":[6,5],"connectedNodes":[5,3]},{"coordinate":[6,6],"connectedNodes":[6,4]},{"coordinate":[5,6],"connectedNodes":[7,5]},{"coordinate":[4,6],"connectedNodes":[8,6]},{"coordinate":[3,6],"connectedNodes":[9,7]},{"coordinate":[2,6],"connectedNodes":[8,10]},{"coordinate":[2,5],"connectedNodes":[9,11]},{"coordinate":[2,4],"connectedNodes":[10,12]},{"coordinate":[2,3],"connectedNodes":[11,13]},{"coordinate":[2,2],"connectedNodes":[12,14]},{"coordinate":[3,2],"connectedNodes":[13,15]},{"coordinate":[4,2],"connectedNodes":[14,16]},{"coordinate":[4,3],"connectedNodes":[15]}]',
                    pythonEnabled=True, theme=grass, threads=1,
                    traffic_lights='[{"direction": "N", "startTime": 0, "sourceCoordinate": {"y":3, "x": 6}, "greenDuration": 3, "startingState": "RED", "redDuration": 3}, {"direction":"W", "startTime": 0, "sourceCoordinate": {"y": 6, "x": 5}, "greenDuration":3, "startingState": "RED", "redDuration": 3}, {"direction": "S", "startTime":0, "sourceCoordinate": {"y": 5, "x": 2}, "greenDuration": 3, "startingState":"RED", "redDuration": 3}, {"direction": "E", "startTime": 0, "sourceCoordinate":{"y": 2, "x": 3}, "greenDuration": 3, "startingState": "GREEN", "redDuration":3}]')

    
    level80.save()
    level81.save()
    level82.save()
    level83.save()
    level84.save()
    level85.save()
    level86.save()
    level80.next_level_id = level81.id
    level81.next_level_id = level82.id
    level82.next_level_id = level83.id
    level83.next_level_id = level84.id
    level84.next_level_id = level85.id
    level85.next_level_id = level86.id
    level80.save()
    level81.save()
    level82.save()
    level83.save()
    level84.save()
    level85.save()
    level86.save()

    # from level7
    levelPairs.append(["7","100"])
    level100 = Level(name='100', anonymous=False, blocklyEnabled=False, character=van, default=True,
                     destinations='[[5, 3]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                     origin='{"coordinate":[0, 3], "direction":"E"}',
                     path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[1,4],"connectedNodes":[1,3]},{"coordinate":[1,5],"connectedNodes":[2,4]},{"coordinate":[1,6],"connectedNodes":[3,5]},{"coordinate":[2,6],"connectedNodes":[4,6]},{"coordinate":[2,5],"connectedNodes":[5,7]},{"coordinate":[3,5],"connectedNodes":[6,8]},{"coordinate":[3,4],"connectedNodes":[7,9]},{"coordinate":[3,3],"connectedNodes":[8,10]},{"coordinate":[3,2],"connectedNodes":[9,11]},{"coordinate":[4,2],"connectedNodes":[10,12]},{"coordinate":[4,3],"connectedNodes":[11,13]},{"coordinate":[5,3],"connectedNodes":[12]}]',
                     pythonEnabled=True, theme=grass, threads=1, traffic_lights='[]')

    # from level14
    levelPairs.append(["14","101"])
    level101 = Level(name='101', anonymous=False, blocklyEnabled=False, character=van, default=True,
                     destinations='[[2, 5]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                     origin='{"coordinate":[7, 2], "direction":"W"}',
                     path='[{"coordinate":[7,2],"connectedNodes":[27]},{"coordinate":[4,2],"connectedNodes":[4,14]},{"coordinate":[3,1],"connectedNodes":[3,14]},{"coordinate":[2,1],"connectedNodes":[7,2]},{"coordinate":[4,3],"connectedNodes":[10,5,1]},{"coordinate":[5,3],"connectedNodes":[4,6]},{"coordinate":[6,3],"connectedNodes":[5,11,27]},{"coordinate":[1,1],"connectedNodes":[8,3]},{"coordinate":[1,2],"connectedNodes":[21,7]},{"coordinate":[3,4],"connectedNodes":[16,10]},{"coordinate":[4,4],"connectedNodes":[9,4]},{"coordinate":[6,4],"connectedNodes":[12,6]},{"coordinate":[6,5],"connectedNodes":[20,11]},{"coordinate":[5,1],"connectedNodes":[14,15]},{"coordinate":[4,1],"connectedNodes":[2,1,13]},{"coordinate":[6,1],"connectedNodes":[13,27]},{"coordinate":[3,5],"connectedNodes":[26,17,9]},{"coordinate":[3,6],"connectedNodes":[18,16]},{"coordinate":[4,6],"connectedNodes":[17,19]},{"coordinate":[5,6],"connectedNodes":[18,20]},{"coordinate":[6,6],"connectedNodes":[19,12]},{"coordinate":[2,2],"connectedNodes":[8,22]},{"coordinate":[2,3],"connectedNodes":[23,21]},{"coordinate":[1,3],"connectedNodes":[24,22]},{"coordinate":[1,4],"connectedNodes":[25,23]},{"coordinate":[1,5],"connectedNodes":[26,24]},{"coordinate":[2,5],"connectedNodes":[25,16]},{"coordinate":[6,2],"connectedNodes":[6,0,15]}]',
                     pythonEnabled=True, theme=grass, threads=1, traffic_lights='[]')


    # from level26
    levelPairs.append(["26","102"])
    level102 = Level(name='102', anonymous=False, blocklyEnabled=False, character=van, default=True,
                     destinations='[[8, 3]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                     origin='{"coordinate":[4, 6], "direction":"S"}',
                     path='[{"coordinate":[4,6],"connectedNodes":[1]},{"coordinate":[4,5],"connectedNodes":[0,2]},{"coordinate":[4,4],"connectedNodes":[1,3]},{"coordinate":[4,3],"connectedNodes":[2,4]},{"coordinate":[5,3],"connectedNodes":[3,5]},{"coordinate":[6,3],"connectedNodes":[4,6]},{"coordinate":[7,3],"connectedNodes":[5,7]},{"coordinate":[8,3],"connectedNodes":[6]}]',
                     pythonEnabled=True, theme=snow, threads=1, traffic_lights='[]')

    # from level32
    levelPairs.append(["32","103"])
    level103 = Level(name='103', anonymous=False, blocklyEnabled=False, character=van, default=True,
                     destinations='[[5, 0]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                     origin='{"coordinate":[2, 7], "direction":"S"}',
                     path='[{"coordinate":[2,7],"connectedNodes":[1]},{"coordinate":[2,6],"connectedNodes":[0,2]},{"coordinate":[3,6],"connectedNodes":[1,3]},{"coordinate":[3,5],"connectedNodes":[2,4]},{"coordinate":[3,4],"connectedNodes":[3,5]},{"coordinate":[4,4],"connectedNodes":[4,6]},{"coordinate":[4,3],"connectedNodes":[5,7]},{"coordinate":[4,2],"connectedNodes":[6,8]},{"coordinate":[5,2],"connectedNodes":[7,9]},{"coordinate":[5,1],"connectedNodes":[8,10]},{"coordinate":[5,0],"connectedNodes":[9]}]',
                     pythonEnabled=True, theme=grass, threads=1, traffic_lights='[]')

    # from level 34
    levelPairs.append(["34","104"])
    level104 = Level(name='104', anonymous=False, blocklyEnabled=False, character=van, default=True,
                     destinations='[[6, 6]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                     origin='{"coordinate":[1, 2], "direction":"E"}',
                     path='[{"coordinate":[1,2],"connectedNodes":[1]},{"coordinate":[2,2],"connectedNodes":[0,2]},{"coordinate":[3,2],"connectedNodes":[1,3]},{"coordinate":[4,2],"connectedNodes":[2,4]},{"coordinate":[5,2],"connectedNodes":[3,5]},{"coordinate":[6,2],"connectedNodes":[4,6]},{"coordinate":[7,2],"connectedNodes":[5,7]},{"coordinate":[8,2],"connectedNodes":[6,8]},{"coordinate":[8,3],"connectedNodes":[9,7]},{"coordinate":[8,4],"connectedNodes":[10,8]},{"coordinate":[8,5],"connectedNodes":[11,9]},{"coordinate":[8,6],"connectedNodes":[12,10]},{"coordinate":[8,7],"connectedNodes":[13,11]},{"coordinate":[7,7],"connectedNodes":[14,12]},{"coordinate":[6,7],"connectedNodes":[15,13]},{"coordinate":[5,7],"connectedNodes":[16,14]},{"coordinate":[4,7],"connectedNodes":[17,15]},{"coordinate":[3,7],"connectedNodes":[16,18]},{"coordinate":[3,6],"connectedNodes":[17,19]},{"coordinate":[3,5],"connectedNodes":[18,20]},{"coordinate":[3,4],"connectedNodes":[19,21]},{"coordinate":[4,4],"connectedNodes":[20,22]},{"coordinate":[5,4],"connectedNodes":[21,23]},{"coordinate":[6,4],"connectedNodes":[22,24]},{"coordinate":[6,5],"connectedNodes":[25,23]},{"coordinate":[6,6],"connectedNodes":[24]}]',
                     pythonEnabled=True, theme=grass, threads=1, traffic_lights='[]')

    # from level38
    levelPairs.append(["38","105"])
    level105 = Level(name='105', anonymous=False, blocklyEnabled=False, character=van, default=True,
                     destinations='[[6, 0]]', direct_drive=False, fuel_gauge=False, max_fuel=50,
                     origin='{"coordinate":[7, 6], "direction":"W"}',
                     path='[{"coordinate":[7,6],"connectedNodes":[1]},{"coordinate":[6,6],"connectedNodes":[2,0]},{"coordinate":[5,6],"connectedNodes":[3,1]},{"coordinate":[4,6],"connectedNodes":[4,2]},{"coordinate":[3,6],"connectedNodes":[5,3]},{"coordinate":[2,6],"connectedNodes":[4,6]},{"coordinate":[2,5],"connectedNodes":[7,5]},{"coordinate":[1,5],"connectedNodes":[8,6]},{"coordinate":[1,6],"connectedNodes":[9,7]},{"coordinate":[0,6],"connectedNodes":[8,10]},{"coordinate":[0,5],"connectedNodes":[9,11]},{"coordinate":[0,4],"connectedNodes":[10,12]},{"coordinate":[1,4],"connectedNodes":[11,13]},{"coordinate":[2,4],"connectedNodes":[12,14]},{"coordinate":[3,4],"connectedNodes":[13,15]},{"coordinate":[3,5],"connectedNodes":[16,14]},{"coordinate":[4,5],"connectedNodes":[15,17]},{"coordinate":[5,5],"connectedNodes":[16,18]},{"coordinate":[6,5],"connectedNodes":[17,19]},{"coordinate":[7,5],"connectedNodes":[18,20]},{"coordinate":[7,4],"connectedNodes":[21,19]},{"coordinate":[6,4],"connectedNodes":[22,20]},{"coordinate":[5,4],"connectedNodes":[23,21]},{"coordinate":[4,4],"connectedNodes":[22,24]},{"coordinate":[4,3],"connectedNodes":[25,23]},{"coordinate":[3,3],"connectedNodes":[26,24]},{"coordinate":[2,3],"connectedNodes":[27,25]},{"coordinate":[1,3],"connectedNodes":[26,28]},{"coordinate":[1,2],"connectedNodes":[27,29]},{"coordinate":[2,2],"connectedNodes":[28,30]},{"coordinate":[3,2],"connectedNodes":[29,31]},{"coordinate":[3,1],"connectedNodes":[30,32]},{"coordinate":[3,0],"connectedNodes":[31,33]},{"coordinate":[4,0],"connectedNodes":[32,34]},{"coordinate":[4,1],"connectedNodes":[35,33]},{"coordinate":[4,2],"connectedNodes":[36,34]},{"coordinate":[5,2],"connectedNodes":[35,37]},{"coordinate":[6,2],"connectedNodes":[36,38]},{"coordinate":[6,1],"connectedNodes":[37,39]},{"coordinate":[6,0],"connectedNodes":[38]}]',
                     pythonEnabled=True, theme=grass, threads=1, traffic_lights='[]')

    # from level43
    levelPairs.append(["43","106"])
    level106 = Level(name='106', anonymous=False, blocklyEnabled=False, character=van, default=True,
                     destinations='[[5, 7]]', direct_drive=False, fuel_gauge=True, max_fuel=50,
                     origin='{"coordinate":[0, 5], "direction":"E"}',
                     path='[{"coordinate":[0,5],"connectedNodes":[1]},{"coordinate":[1,5],"connectedNodes":[0,2]},{"coordinate":[1,4],"connectedNodes":[1,3]},{"coordinate":[2,4],"connectedNodes":[2,4]},{"coordinate":[2,3],"connectedNodes":[5,3]},{"coordinate":[1,3],"connectedNodes":[4,6]},{"coordinate":[1,2],"connectedNodes":[5,7,8]},{"coordinate":[2,2],"connectedNodes":[6,9]},{"coordinate":[1,1],"connectedNodes":[6,9]},{"coordinate":[2,1],"connectedNodes":[8,7,10]},{"coordinate":[2,0],"connectedNodes":[9,11]},{"coordinate":[3,0],"connectedNodes":[10,12]},{"coordinate":[4,0],"connectedNodes":[11,13]},{"coordinate":[4,1],"connectedNodes":[14,12]},{"coordinate":[3,1],"connectedNodes":[15,13]},{"coordinate":[3,2],"connectedNodes":[16,14]},{"coordinate":[3,3],"connectedNodes":[17,15]},{"coordinate":[4,3],"connectedNodes":[16,18]},{"coordinate":[5,3],"connectedNodes":[17,19,28,20]},{"coordinate":[5,4],"connectedNodes":[29,18]},{"coordinate":[5,2],"connectedNodes":[18,21]},{"coordinate":[5,1],"connectedNodes":[20,22]},{"coordinate":[5,0],"connectedNodes":[21,23]},{"coordinate":[6,0],"connectedNodes":[22,24]},{"coordinate":[7,0],"connectedNodes":[23,25]},{"coordinate":[7,1],"connectedNodes":[26,24]},{"coordinate":[7,2],"connectedNodes":[27,25]},{"coordinate":[7,3],"connectedNodes":[28,26]},{"coordinate":[6,3],"connectedNodes":[18,27]},{"coordinate":[5,5],"connectedNodes":[30,40,19]},{"coordinate":[4,5],"connectedNodes":[31,29]},{"coordinate":[3,5],"connectedNodes":[32,30]},{"coordinate":[3,6],"connectedNodes":[33,31]},{"coordinate":[3,7],"connectedNodes":[41,34,32]},{"coordinate":[4,7],"connectedNodes":[33,35]},{"coordinate":[5,7],"connectedNodes":[34,36]},{"coordinate":[6,7],"connectedNodes":[35,37]},{"coordinate":[7,7],"connectedNodes":[36,38]},{"coordinate":[7,6],"connectedNodes":[37,39]},{"coordinate":[7,5],"connectedNodes":[40,38]},{"coordinate":[6,5],"connectedNodes":[29,39]},{"coordinate":[2,7],"connectedNodes":[42,33]},{"coordinate":[1,7],"connectedNodes":[41]}]',
                     pythonEnabled=True, theme=grass, threads=1, traffic_lights='[]')

    # from level50
    levelPairs.append(["50","107"])
    level107 = Level(name='107', anonymous=False, blocklyEnabled=False, character=van, default=True,
                     destinations='[[6, 4]]', direct_drive=False, fuel_gauge=True, max_fuel=50,
                     origin='{"coordinate":[0, 3], "direction":"E"}',
                     path='[{"coordinate":[0,3],"connectedNodes":[1]}, {"coordinate":[1,3],"connectedNodes":[0,27,2]},{"coordinate":[1,2],"connectedNodes":[1,3]}, {"coordinate":[1,1],"connectedNodes":[2,4]},{"coordinate":[2,1],"connectedNodes":[3,6,5]}, {"coordinate":[2,0],"connectedNodes":[4]},{"coordinate":[3,1],"connectedNodes":[4,7]}, {"coordinate":[4,1],"connectedNodes":[6,8]},{"coordinate":[4,2],"connectedNodes":[9,11,7]}, {"coordinate":[4,3],"connectedNodes":[10,36,8]},{"coordinate":[3,3],"connectedNodes":[9]}, {"coordinate":[5,2],"connectedNodes":[8,12]},{"coordinate":[6,2],"connectedNodes":[11,15,13]}, {"coordinate":[6,1],"connectedNodes":[12,14]},{"coordinate":[6,0],"connectedNodes":[13]}, {"coordinate":[7,2],"connectedNodes":[12,16]},{"coordinate":[8,2],"connectedNodes":[15,25,17]}, {"coordinate":[8,1],"connectedNodes":[16,18]},{"coordinate":[8,0],"connectedNodes":[17,19]}, {"coordinate":[9,0],"connectedNodes":[18,20]},{"coordinate":[9,1],"connectedNodes":[21,19]}, {"coordinate":[9,2],"connectedNodes":[22,20]},{"coordinate":[9,3],"connectedNodes":[23,21]}, {"coordinate":[9,4],"connectedNodes":[24,22]},{"coordinate":[8,4],"connectedNodes":[26,23,25]}, {"coordinate":[8,3],"connectedNodes":[24,16]},{"coordinate":[7,4],"connectedNodes":[42,28,24]}, {"coordinate":[1,4],"connectedNodes":[41,1]},{"coordinate":[7,5],"connectedNodes":[29,26]}, {"coordinate":[7,6],"connectedNodes":[32,30,28]},{"coordinate":[8,6],"connectedNodes":[29,31]}, {"coordinate":[9,6],"connectedNodes":[30]},{"coordinate":[6,6],"connectedNodes":[33,29]}, {"coordinate":[5,6],"connectedNodes":[34,32]},{"coordinate":[4,6],"connectedNodes":[33,35]}, {"coordinate":[4,5],"connectedNodes":[37,34,36]},{"coordinate":[4,4],"connectedNodes":[35,9]}, {"coordinate":[3,5],"connectedNodes":[38,35]},{"coordinate":[2,5],"connectedNodes":[39,37]}, {"coordinate":[2,6],"connectedNodes":[40,38]},{"coordinate":[1,6],"connectedNodes":[39,41]}, {"coordinate":[1,5],"connectedNodes":[40,27]},{"coordinate":[6,4],"connectedNodes":[26]} ]',
                     pythonEnabled=True, theme=city, threads=1,
                     traffic_lights='[{"direction": "E", "startTime": 0, "sourceCoordinate": {"y":1, "x": 1}, "greenDuration": 2, "startingState": "RED", "redDuration": 4}, {"direction":"N", "startTime": 2, "sourceCoordinate": {"y": 0, "x": 2}, "greenDuration":2, "startingState": "RED", "redDuration": 4}, {"direction": "W", "startTime":0, "sourceCoordinate": {"y": 1, "x": 3}, "greenDuration": 2, "startingState":"GREEN", "redDuration": 4}, {"direction": "N", "startTime": 0, "sourceCoordinate":{"y": 1, "x": 4}, "greenDuration": 2, "startingState": "RED", "redDuration":4}, {"direction": "S", "startTime": 2, "sourceCoordinate": {"y": 3, "x": 4},"greenDuration": 2, "startingState": "RED", "redDuration": 4}, {"direction":"W", "startTime": 0, "sourceCoordinate": {"y": 2, "x": 5}, "greenDuration":2, "startingState": "GREEN", "redDuration": 4}, {"direction": "E", "startTime":0, "sourceCoordinate": {"y": 5, "x": 3}, "greenDuration": 2, "startingState":"RED", "redDuration": 4}, {"direction": "S", "startTime": 2, "sourceCoordinate":{"y": 6, "x": 4}, "greenDuration": 2, "startingState": "RED", "redDuration":4}, {"direction": "N", "startTime": 0, "sourceCoordinate": {"y": 4, "x": 4},"greenDuration": 2, "startingState": "GREEN", "redDuration": 4}, {"direction":"W", "startTime": 0, "sourceCoordinate": {"y": 6, "x": 2}, "greenDuration":4, "startingState": "RED", "redDuration": 2}, {"direction": "W", "startTime":0, "sourceCoordinate": {"y": 4, "x": 9}, "greenDuration": 2, "startingState":"RED", "redDuration": 4}, {"direction": "N", "startTime": 2, "sourceCoordinate":{"y": 3, "x": 8}, "greenDuration": 2, "startingState": "RED", "redDuration":4}, {"direction": "E", "startTime": 0, "sourceCoordinate": {"y": 4, "x": 7},"greenDuration": 2, "startingState": "GREEN", "redDuration": 4}]')

    level100.save()
    level101.save()
    level102.save()
    level103.save()
    level104.save()
    level105.save()
    level106.save()
    level107.save()
    level100.next_level_id = level101.id
    level101.next_level_id = level102.id
    level102.next_level_id = level103.id
    level103.next_level_id = level104.id
    level104.next_level_id = level105.id
    level105.next_level_id = level106.id
    level106.next_level_id = level107.id
    level100.save()
    level101.save()
    level102.save()
    level103.save()
    level104.save()
    level105.save()
    level106.save()
    level107.save()

    # Add level decor
    for levelPair in levelPairs:
        oldName = levelPair[0]
        newName = levelPair[1]
        oldLevel = Level.objects.get(name=oldName, default=True)
        newLevel = Level.objects.get(name=newName, default=True)
        levelDecors = LevelDecor.objects.filter(level=oldLevel)
        for levelDecor in levelDecors:
            newDecor = LevelDecor(decorName=levelDecor.decorName, level=newLevel, x=levelDecor.x, y=levelDecor.y)
            newDecor.save()

    # Add level blocks for blockly and python levels
    count = 0
    while count < 7:
        levelPair = levelPairs[count]
        oldName = levelPair[0]
        newName = levelPair[1]
        oldLevel = Level.objects.get(name=oldName, default=True)
        newLevel = Level.objects.get(name=newName, default=True)
        levelBlocks = LevelBlock.objects.filter(level=oldLevel)
        for levelBlock in levelBlocks:
            newBlock = LevelBlock(type=levelBlock.type, number=levelBlock.number, level=newLevel)
            newBlock.save()
        count += 1

    blocklyAndPythonEpisode = Episode(name="Introduction to Python", first_level=level80, r_branchiness=0.5,
                                      r_loopiness=0.1, r_num_tiles=35, r_curviness=0.2, r_pythonEnabled=0,
                                      r_blocklyEnabled=1, r_trafficLights=1, in_development=True)
    blocklyAndPythonEpisode.save()

    pythonOnlyEpisode = Episode(name="Python!", first_level=level100, r_branchiness=0.5,
                                r_loopiness=0.1, r_num_tiles=35, r_curviness=0.2, r_pythonEnabled=0,
                                r_blocklyEnabled=1, r_trafficLights=1, in_development=True)
    pythonOnlyEpisode.save()  


def correct_model_score(apps, schema_editor):
    Level = apps.get_model('game', 'Level')

    level53 = Level.objects.get(name='53', default=True)
    level53.model_solution = '[18, 19]'
    level53.save()

class Migration(migrations.Migration):

    dependencies = [
        ('game', '0018_method_levels'),
    ]

    operations = [
        migrations.RunPython(add_levels),
        migrations.RunPython(correct_model_score),
    ]
