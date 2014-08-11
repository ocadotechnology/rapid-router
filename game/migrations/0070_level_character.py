# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0069_farm_theme'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='character',
            field=models.CharField(default=b'/static/game/image/characters/van_small.svg', max_length=500),
            preserve_default=True,
        ),
    ]
