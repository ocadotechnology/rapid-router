# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def change_level_27(apps, schema_editor):

    Level = apps.get_model('game', 'Level')

    level27 = Level.objects.get(pk=27)
    level27.model_solution = [16, 14]
    level27.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_leveldecor'),
    ]

    operations = [
        migrations.RunPython(change_level_27)
    ]
