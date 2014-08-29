# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def make_levels_default(apps, schema_editor):
    Level = apps.get_model('game', 'Level')

    level26 = Level.objects.get(pk=26)
    level27 = Level.objects.get(pk=27)
    level28 = Level.objects.get(pk=28)

    level26.default = 1
    level27.default = 1
    level28.default = 1

    level26.save()
    level27.save()
    level28.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0094_level_origin'),
    ]

    operations = [
        migrations.RunPython(make_levels_default)
    ]
