# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

import re


def create_level(apps, schema_editor):

    Level = apps.get_model('game', 'Level')
    Block = apps.get_model('game', 'Block')
    Theme = apps.get_model('game', 'Theme')
    LevelDecor = apps.get_model('game', 'LevelDecor')

    winter = Theme.objects.get(pk=2)

    level25 = Level.objects.get(pk=25)

    level26 = Level.objects.get(pk=26)
    level26.path = '[{"coordinate":[4,6],"connectedNodes":[1]},{"coordinate":[4,5],"connectedNodes":[0,2]},{"coordinate":[4,4],"connectedNodes":[1,3]},{"coordinate":[4,3],"connectedNodes":[2,4]},{"coordinate":[5,3],"connectedNodes":[3,5]},{"coordinate":[6,3],"connectedNodes":[4,6]},{"coordinate":[7,3],"connectedNodes":[5,7]},{"coordinate":[8,3],"connectedNodes":[6]}]'
    level26.decor = '[{"coordinate":{"x":176,"y":520},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":176,"y":400},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":179,"y":286},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":500,"y":627},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":499,"y":508},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":500,"y":388},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":690,"y":203},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":780,"y":81},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":865,"y":419},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":875,"y":180},"url":"/static/game/image/tree2.svg"}]'
    level26.theme = winter
    level26.destinations = '[[8,3]]'

    level25.next_level = level26

    blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards",
                                            "controls_repeat"])
    level26.blocks = blocks

    level25.save()
    level26.save()

    regex = re.compile('(({"coordinate" *:{"x": *)([0-9]+)(,"y": *)([0-9]+)(}, *"url": *")(((/[a-zA-Z0-9]+)+.svg)+)("}))')

    items = regex.findall(level26.decor)

    for item in items:
        name = item[8][1:]
        levelDecor = LevelDecor(level=level26, x=item[2], y=item[4], decorName=name)
        levelDecor.save()


class Migration(migrations.Migration):



    dependencies = [
        ('game', '0052_merge'),
    ]

    operations = [
        migrations.RunPython(create_level)
    ]
