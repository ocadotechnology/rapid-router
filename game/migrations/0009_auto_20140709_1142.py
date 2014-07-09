# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def levels(apps, schema_editor):
    Level = apps.get_model("game", "Level")
    Block = apps.get_model("game", "Block")

    blocks = Block.objects.filter(type__in=["move_forwards", "turn_left", "turn_right",
                                            "controls_whileUntil", "at_destination"])

    for i in range(13, 17):
        level = Level.objects.get(id=i)
        level.blocks = blocks
        level.save()

    blocks = Block.objects.filter(type__in=["move_forwards", "turn_left", "turn_right",
                                            "controls_whileUntil", "controls_if", "logic_negate",
                                            "road_exists", "at_destination", "turn_around",
                                            "controls_repeat", "road_exists", "dead_end",
                                            "turn_around"])

    for i in range(24, 26):
        level = Level.objects.get(id=i)
        level.blocks = blocks
        level.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0008_trial_user'),
    ]

    operations = [
        migrations.RunPython(levels),
    ]
