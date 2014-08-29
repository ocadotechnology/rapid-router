# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def repopulate_themes(apps, schema_editor):

    Level = apps.get_model('game', 'Level')
    Theme = apps.get_model('game', 'Theme')

    grass = Theme.objects.get(pk=1)
    winter = Theme.objects.get(pk=2)

    levels = Level.objects.all()

    for level in levels:
        if level.id > 25 and level.id < 29:
            level.theme = winter
        else:
            level.theme = grass
        level.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0061_level26_27_28'),
    ]

    operations = [
        migrations.RunPython(repopulate_themes)
    ]
