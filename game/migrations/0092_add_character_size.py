# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def add_character_sizes(apps, schema_editor):

    Character = apps.get_model('game', 'Character')

    van_width = 40
    van_height = 20

    wes = Character.objects.get(name='Wes')
    dee = Character.objects.get(name='Dee')
    nigel = Character.objects.get(name='Nigel')
    kristy = Character.objects.get(name='Kristy')
    phil = Character.objects.get(name='Phil')

    wes.width = van_width
    wes.height = van_width
    wes.save()

    dee.width = int(1.3 * van_width)
    dee.height = int(1.4 * van_height)
    dee.save()

    nigel.width = int(1.4 * van_width)
    nigel.height = int(1.6 * van_height)
    nigel.save()

    kristy.width = int(1.5 * van_width)
    kristy.height = int(1.6 * van_height)
    kristy.save()

    phil.width = van_width
    phil.height = int(1.6 * van_height)
    phil.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0091_auto_20140820_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='height',
            field=models.IntegerField(default=20),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='width',
            field=models.IntegerField(default=40),
            preserve_default=True,
        ),
        migrations.RunPython(add_character_sizes)
    ]
