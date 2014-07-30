# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

import re


def populate_solutions(apps, schema_editor):

    Level = apps.get_model('game', 'Level')
    LevelDecor = apps.get_model('game', 'LevelDecor')

    levels = Level.objects.all()

    for level in levels:
        solution = level.model_solution
        level.model_solution = [int(solution)]
        level.save()

    level8 = Level.objects.get(pk=8)
    level8.path = '[{"coordinate":[3,6],"connectedNodes":[1]},{"coordinate":[3,5],"connectedNodes":[0,2]},{"coordinate":[3,4],"connectedNodes":[3,1]},{"coordinate":[2,4],"connectedNodes":[4,2]},{"coordinate":[1,4],"connectedNodes":[3,5]},{"coordinate":[1,3],"connectedNodes":[4,6]},{"coordinate":[1,2],"connectedNodes":[5,7]},{"coordinate":[2,2],"connectedNodes":[6,8]},{"coordinate":[3,2],"connectedNodes":[7,9]},{"coordinate":[4,2],"connectedNodes":[8,10]},{"coordinate":[4,1],"connectedNodes":[9]}]'
    level8.model_solution = '[8]'
    level8.decor = '[{"coordinate":{"x":484,"y":438},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":660,"y":410},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":111,"y":589},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":39,"y":491},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":569,"y":267},"url":"/static/game/image/pond.svg"},{"coordinate":{"x":385,"y":307},"url":"/static/game/image/tree1.svg"}]'
    level8.destinations = [[4, 1]]
    level8.save()

    LevelDecor.objects.filter(level=level8).delete()

    regex = re.compile('(({"coordinate" *:{"x": *)([0-9]+)(,"y": *)([0-9]+)(}, *"url": *")(((/[a-zA-Z0-9]+)+.svg)+)("}))')
    items = regex.findall(level8.decor)

    for item in items:
        name = item[8][1:]
        levelDecor = LevelDecor(level=level8, x=item[2], y=item[4], decorName=name)
        levelDecor.save()

    level34 = Level.objects.get(pk=34)
    level34.model_solution = '[8, 7]'
    level34.save()

    level35 = Level.objects.get(pk=35)
    level35.model_solution = '[11, 9]'
    level35.save()

    level36 = Level.objects.get(pk=36)
    level36.model_solution = '[11, 9]'
    level36.save()

    level37 = Level.objects.get(pk=37)
    level37.model_solution = '[11, 9]'
    level37.save()

    level38 = Level.objects.get(pk=38)
    level38.model_solution = '[11, 9]'
    level38.save()

    level39 = Level.objects.get(pk=39)
    level39.path = '[{"coordinate":[1,2],"connectedNodes":[1]},{"coordinate":[2,2],"connectedNodes":[0,2]},{"coordinate":[3,2],"connectedNodes":[1,3]},{"coordinate":[4,2],"connectedNodes":[2,9,4]},{"coordinate":[5,2],"connectedNodes":[3,5]},{"coordinate":[6,2],"connectedNodes":[4,6]},{"coordinate":[7,2],"connectedNodes":[5,7]},{"coordinate":[8,2],"connectedNodes":[6,11,8]},{"coordinate":[9,2],"connectedNodes":[7]},{"coordinate":[4,3],"connectedNodes":[10,3]},{"coordinate":[4,4],"connectedNodes":[9]},{"coordinate":[8,3],"connectedNodes":[12,7]},{"coordinate":[8,4],"connectedNodes":[13,11]},{"coordinate":[8,5],"connectedNodes":[14,12]},{"coordinate":[8,6],"connectedNodes":[15,13]},{"coordinate":[8,7],"connectedNodes":[14]}]'
    level39.destinations = [[8, 7]]
    level39.decor = '[{"coordinate":{"x":639,"y":285},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":502,"y":388},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":655,"y":443},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":263,"y":92},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":551,"y":90},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":695,"y":89},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":411,"y":89},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":833,"y":91},"url":"/static/game/image/bush.svg"}]'
    level39.model_solution = '[5, 6]'
    level39.save()
    
    LevelDecor.objects.filter(level=level39).delete()

    items = regex.findall(level8.decor)

    for item in items:
        name = item[8][1:]
        levelDecor = LevelDecor(level=level8, x=item[2], y=item[4], decorName=name)
        levelDecor.save()

    level40 = Level.objects.get(pk=40)
    level40.destinations = [[3, 4]]
    level40.model_solution = '[8, 9]'
    level40.save()

    level41 = Level.objects.get(pk=41)
    level41.model_solution = '[8, 9]'
    level41.save()

    level43 = Level.objects.get(pk=43)
    level43.model_solution = '[21]'
    level43.save()

    level44 = Level.objects.get(pk=44)
    level44.model_solution = '[5, 6]'
    level44.save()

    level45 = Level.objects.get(pk=45)
    level45.model_solution = '[6, 7]'
    level45.save()

    level46 = Level.objects.get(pk=46)
    level46.model_solution = '[8, 9]'
    level46.save()

    level47 = Level.objects.get(pk=47)
    level47.model_solution = '[8, 9]'
    level47.save()

    level48 = Level.objects.get(pk=48)
    level48.model_solution = '[12, 13]'
    level48.save()




class Migration(migrations.Migration):

    dependencies = [
        ('game', '0059_multiple_solutions'),
    ]

    operations = [
        migrations.RunPython(populate_solutions)
    ]
