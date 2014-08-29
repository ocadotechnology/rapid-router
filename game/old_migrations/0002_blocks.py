# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def initial_blocks(apps, schema_editor):
    Block = apps.get_model('game', 'Block')
    types = ["move_forwards",
            "turn_left",
            "turn_right",
            "turn_around",
            "controls_repeat",
            "controls_whileUntil",
            "controls_if",
            "logic_negate",
            "road_exists",
            "dead_end",
            "at_destination"]
    for t in types:
        b = Block(type=t)
        b.save()


class Migration(migrations.Migration):

    dependencies = [
            ('game', '0001_initial'),
    ]

    operations = [
            migrations.RunPython(initial_blocks),
    ]
