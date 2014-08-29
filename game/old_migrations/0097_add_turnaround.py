# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def levels_turn_around(apps, schema_editor):

    Level = apps.get_model('game', 'Level')
    Block = apps.get_model('game', 'Block')

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

    for i in range(51, 55):
        Level.objects.get(pk=i).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0096_change_farm_field_size'),
    ]

    operations = [
        migrations.RunPython(levels_turn_around)
    ]
