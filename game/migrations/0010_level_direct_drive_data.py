# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def direct_drive(apps, schema_editor):
    Level = apps.get_model("game", "Level")
    for level in Level.objects.all():
        if level.id <= 12:
            level.direct_drive = True
            level.save()

class Migration(migrations.Migration):

    dependencies = [
        ('game', '0009_level_direct_drive'),
    ]

    operations = [
        migrations.RunPython(direct_drive),
    ]
