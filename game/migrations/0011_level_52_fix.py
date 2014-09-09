# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def fix_level(apps, schema_editor):
    Level = apps.get_model('game', 'Level')
    LevelBlock = apps.get_model('game', 'LevelBlock')
    Block = apps.get_model('game', 'Block')

    level52 = Level.objects.get(name="Block scarcity", default=True)

    rightType = Block.objects.get(type="turn_right")

    right = LevelBlock.objects.get(level=level52, type=rightType)
    right.number = 3;
    right.save()

    level52.name = "52"
    level52.save()

class Migration(migrations.Migration):

    dependencies = [
        ('game', '0010_episode_in_development'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='in_development',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),

        migrations.RunPython(fix_level),
    ]
