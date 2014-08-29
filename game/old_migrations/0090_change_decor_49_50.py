# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

import re


def change_decor(apps, schema_editor):

    Block = apps.get_model('game', 'Block')
    Episode = apps.get_model('game', 'Episode')
    Level = apps.get_model('game', 'Level')
    LevelDecor = apps.get_model('game', 'LevelDecor')

    traffic_lights = Episode.objects.get(name='Traffic Lights')
    traffic_lights.next_episode = None
    traffic_lights.save()

    decor49 = '[{"coordinate":{"x":501,"y":487},"name":"tree2"},{"coordinate":{"x":475,"y":262},"name":"pond"},{"coordinate":{"x":181,"y":323},"name":"tree1"},{"coordinate":{"x":65,"y":489},"name":"bush"},{"coordinate":{"x":63,"y":426},"name":"bush"},{"coordinate":{"x":60,"y":356},"name":"bush"},{"coordinate":{"x":57,"y":291},"name":"bush"},{"coordinate":{"x":130,"y":489},"name":"bush"},{"coordinate":{"x":194,"y":491},"name":"bush"},{"coordinate":{"x":262,"y":492},"name":"bush"},{"coordinate":{"x":479,"y":196},"name":"bush"},{"coordinate":{"x":400,"y":290},"name":"bush"},{"coordinate":{"x":637,"y":287},"name":"bush"},{"coordinate":{"x":639,"y":350},"name":"bush"},{"coordinate":{"x":404,"y":353},"name":"bush"},{"coordinate":{"x":556,"y":196},"name":"bush"},{"coordinate":{"x":777,"y":530},"name":"tree1"},{"coordinate":{"x":787,"y":453},"name":"bush"},{"coordinate":{"x":789,"y":380},"name":"bush"},{"coordinate":{"x":787,"y":308},"name":"bush"}]'
    decor50 = '[{"coordinate":{"x":482,"y":75},"name":"pond"},{"coordinate":{"x":797,"y":491},"name":"tree2"},{"coordinate":{"x":494,"y":492},"name":"bush"},{"coordinate":{"x":494,"y":558},"name":"bush"},{"coordinate":{"x":494,"y":426},"name":"bush"},{"coordinate":{"x":495,"y":356},"name":"bush"},{"coordinate":{"x":495,"y":291},"name":"bush"},{"coordinate":{"x":284,"y":584},"name":"tree1"},{"coordinate":{"x":686,"y":39},"name":"bush"},{"coordinate":{"x":686,"y":98},"name":"bush"},{"coordinate":{"x":684,"y":160},"name":"bush"}]'

    level49 = Level.objects.get(pk=49)
    level50 = Level.objects.get(pk=50)

    LevelDecor.objects.filter(level=level49).delete()
    LevelDecor.objects.filter(level=level50).delete()

    level49.decor = decor49
    level50.decor = decor50
    level49.model_solution = [12, 13]
    level50.model_solution = [16]
    level49.save()
    level50.save()

    regex = re.compile('(({"coordinate" *:{"x": *)([0-9]+)(,"y": *)([0-9]+)(}, *"name": *")([a-zA-Z0-9]+)("}))')

    items = regex.findall(decor49)

    for item in items:
        name = item[6]
        levelDecor = LevelDecor(level=level49, x=item[2], y=item[4], decorName=name)
        levelDecor.save()

    items = regex.findall(decor50)

    for item in items:
        name = item[6]
        levelDecor = LevelDecor(level=level50, x=item[2], y=item[4], decorName=name)
        levelDecor.save()

    blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards",
                                            "controls_repeat_until", "at_destination",
                                            "controls_if", "road_exists", "at_destination",
                                            "controls_repeat", "dead_end", "controls_repeat_while",
                                            "wait", "traffic_light", "turn_around"])

    for i in range(44, 51):
        level = Level.objects.get(pk=i)
        level.blocks = blocks
        level.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0089_until_episode_levels49_50_city_split_while_until'),
    ]

    operations = [
        migrations.RunPython(change_decor)
    ]
