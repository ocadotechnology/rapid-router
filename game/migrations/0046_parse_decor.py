# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

import re


def parse_levels(apps, schema_editor):
    
    Level = apps.get_model('game', 'Level')
    Decor = apps.get_model('game', 'Decor')
    LevelDecor = apps.get_model('game', 'LevelDecor')

    levels = Level.objects.all()

    regex = re.compile('(({"coordinate":{"x":)([0-9]+)(,"y":)([0-9]+)(},"url":")(((/[a-zA-Z0-9]+)+.svg)+)("}))')

    for level in levels:
        if len(level.decor) > 0:
            items = regex.findall(level.decor)

            for item in items:
                decor = Decor.objects.get(url=item[6])
                levelDecor = LevelDecor(level=level, decor=decor, x=item[2], y=item[4])
                levelDecor.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0045_level_theme'),
    ]

    operations = [
        migrations.RunPython(parse_levels)
    ]
