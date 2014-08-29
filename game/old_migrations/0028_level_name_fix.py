# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def levelFix(apps, schema_editor):
    Level = apps.get_model("game", "Level")

    # Episode 9

    levels = Level.objects.filter(name="21")

    for level in levels:
        if level.threads == 2:
            level.name = "29"
            level.save()

class Migration(migrations.Migration):

    dependencies = [
        ('game', '0027_merge')
    ]

    operations = [
        migrations.RunPython(levelFix),
    ]