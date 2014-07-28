# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

import re


def populate_level_decor(apps, schema_editor):

    Level = apps.get_model('game', 'Level')
    LevelDecor = apps.get_model('game', 'LevelDecor')
    LevelDecor.objects.all().delete()

    levels = Level.objects.all()

    regex = re.compile('(({"coordinate" *:{"x": *)([0-9]+)(,"y": *)([0-9]+)(}, *"url": *")(((/[a-zA-Z0-9]+)+.svg)+)("}))')

    for level in levels:
        items = regex.findall(level.decor)

        for item in items:
            name = item[8][1:]
            levelDecor = LevelDecor(level=level, x=item[2], y=item[4], decorName=name)
            levelDecor.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0049_change_leveldecor'),
    ]

    operations = [
        migrations.RunPython(populate_level_decor)
    ]
