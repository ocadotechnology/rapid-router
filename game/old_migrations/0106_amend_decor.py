# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def amend_decor(apps, schema_editor):

    Level = apps.get_model('game', 'Level')
    LevelDecor = apps.get_model('game', 'LevelDecor')

    level17 = Level.objects.get(pk=17)
    levelDecor = LevelDecor.objects.filter(level=level17, x=200)
    for dec in levelDecor:
        dec.delete()
    levelDecor = LevelDecor.objects.filter(level=level17, x=573)
    for dec in levelDecor:
        dec.delete()

    level21 = Level.objects.get(pk=21)
    levelDecor = LevelDecor.objects.filter(level=level21, x=300)
    for dec in levelDecor:
        dec.delete()


def fix_Phil(apps, schema_editor):

    Character = apps.get_model('game', 'Character')

    phil = Character.objects.get(name='Phil')
    phil.top_down = '/static/game/image/characters/top_view/Phil.svg'
    phil.en_face = '/static/game/image/characters/front_view/Phil.svg'
    phil.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0105_re-add_origins'),
    ]

    operations = [
        migrations.RunPython(amend_decor),
        migrations.RunPython(fix_Phil)
    ]
