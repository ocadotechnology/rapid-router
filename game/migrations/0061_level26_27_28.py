# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

import re


def set_level26_27_28(apps, schema_editor):

    Level = apps.get_model('game', 'Level')
    Theme = apps.get_model('game', 'Theme')
    LevelDecor = apps.get_model('game', 'LevelDecor')

    level26 = Level.objects.get(pk=26)
    level27 = Level.objects.get(pk=27)
    level28 = Level.objects.get(pk=28)
    winter = Theme.objects.get(pk=2)

    level26.model_solution = '[5]'
    level26.next_level = level27
    level26.save()

    level27.path = '[{"coordinate":[4,5],"connectedNodes":[1]},{"coordinate":[5,5],"connectedNodes":[0,2]},{"coordinate":[6,5],"connectedNodes":[1,3]},{"coordinate":[7,5],"connectedNodes":[2,4]},{"coordinate":[7,6],"connectedNodes":[5,3]},{"coordinate":[7,7],"connectedNodes":[6,4]},{"coordinate":[6,7],"connectedNodes":[7,5]},{"coordinate":[5,7],"connectedNodes":[8,6]},{"coordinate":[4,7],"connectedNodes":[9,7]},{"coordinate":[3,7],"connectedNodes":[10,8]},{"coordinate":[2,7],"connectedNodes":[11,9]},{"coordinate":[1,7],"connectedNodes":[10,12]},{"coordinate":[1,6],"connectedNodes":[11,13]},{"coordinate":[1,5],"connectedNodes":[12,14]},{"coordinate":[1,4],"connectedNodes":[13,15]},{"coordinate":[1,3],"connectedNodes":[14,16]},{"coordinate":[1,2],"connectedNodes":[15,17]},{"coordinate":[2,2],"connectedNodes":[16,18]},{"coordinate":[2,1],"connectedNodes":[17,19]},{"coordinate":[3,1],"connectedNodes":[18,20]},{"coordinate":[4,1],"connectedNodes":[19,21]},{"coordinate":[5,1],"connectedNodes":[20,22]},{"coordinate":[6,1],"connectedNodes":[21,23]},{"coordinate":[7,1],"connectedNodes":[22,24]},{"coordinate":[7,2],"connectedNodes":[25,23]},{"coordinate":[8,2],"connectedNodes":[24,26]},{"coordinate":[8,3],"connectedNodes":[25]}]'
    level27.decor = '[{"coordinate":{"x":647,"y":351},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":220,"y":353},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":346,"y":316},"url":"/static/game/image/pond.svg"},{"coordinate":{"x":574,"y":183},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":610,"y":609},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":478,"y":608},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":354,"y":608},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":214,"y":606},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":510,"y":396},"url":"/static/game/image/tree1.svg"}]'
    level27.destinations = [[8, 3]]
    level27.next_level = level28
    level27.model_solution = '[16]'
    level27.theme = winter
    level27.save()

    level28.path = '[{"coordinate":[1,3],"connectedNodes":[1]},{"coordinate":[2,3],"connectedNodes":[0,2]},{"coordinate":[3,3],"connectedNodes":[1,3]},{"coordinate":[3,4],"connectedNodes":[4,2]},{"coordinate":[3,5],"connectedNodes":[5,3]},{"coordinate":[3,6],"connectedNodes":[6,4]},{"coordinate":[4,6],"connectedNodes":[5,7]},{"coordinate":[5,6],"connectedNodes":[6,8]},{"coordinate":[6,6],"connectedNodes":[7,9]},{"coordinate":[6,5],"connectedNodes":[8,10]},{"coordinate":[6,4],"connectedNodes":[9,11]},{"coordinate":[6,3],"connectedNodes":[10,12]},{"coordinate":[6,2],"connectedNodes":[13,11]},{"coordinate":[5,2],"connectedNodes":[14,12]},{"coordinate":[4,2],"connectedNodes":[15,13]},{"coordinate":[3,2],"connectedNodes":[14,16]},{"coordinate":[3,1],"connectedNodes":[15,17]},{"coordinate":[4,1],"connectedNodes":[16,18]},{"coordinate":[5,1],"connectedNodes":[17,19]},{"coordinate":[6,1],"connectedNodes":[18,20]},{"coordinate":[7,1],"connectedNodes":[19,21]},{"coordinate":[8,1],"connectedNodes":[20,22]},{"coordinate":[8,2],"connectedNodes":[23,21]},{"coordinate":[9,2],"connectedNodes":[22,24]},{"coordinate":[9,3],"connectedNodes":[25,23]},{"coordinate":[9,4],"connectedNodes":[24]}]'
    level28.decor = '[{"coordinate":{"x":415,"y":488},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":520,"y":434},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":513,"y":291},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":405,"y":368},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":182,"y":589},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":115,"y":468},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":194,"y":380},"url":"/static/game/image/tree1.svg"}]'
    level28.destinations = [[9, 4]]
    level28.model_solution = '[19]'
    level28.theme = winter
    level28.save()

    regex = re.compile('(({"coordinate" *:{"x": *)([0-9]+)(,"y": *)([0-9]+)(}, *"url": *")(((/[a-zA-Z0-9]+)+.svg)+)("}))')
    items = regex.findall(level27.decor)

    for item in items:
        name = item[8][1:]
        levelDecor = LevelDecor(level=level27, x=item[2], y=item[4], decorName=name)
        levelDecor.save()

    items = regex.findall(level28.decor)

    for item in items:
        name = item[8][1:]
        levelDecor = LevelDecor(level=level28, x=item[2], y=item[4], decorName=name)
        levelDecor.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0060_multiple_solutions_data'),
    ]

    operations = [
        migrations.RunPython(set_level26_27_28)
    ]
