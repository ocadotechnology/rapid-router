# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

import json


def add_wait_to_level_4(apps, schema_editor):

    Level = apps.get_model('game', 'Level')
    Block = apps.get_model('game', 'Block')


    blocks = Block.objects.filter(type__in=["move_forwards", "controls_repeat_until",
                                            "at_destination", "controls_if", "road_exists",
                                            "controls_repeat", "controls_repeat_while",
                                            "wait", "traffic_light"])

    for i in range(4, 4):
        level = Level.objects.get(pk=i)
        level.blocks = blocks
        level.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0050_add_cow_levels_and_episodes'),
    ]

    operations = [
        migrations.RunPython(add_wait_to_level_4)
    ]
