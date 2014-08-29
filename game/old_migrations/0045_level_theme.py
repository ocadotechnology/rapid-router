# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0044_remove_level_theme'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='theme',
            field=models.ForeignKey(to='game.Theme', blank=True, null=True, default=None),
            preserve_default=True,
        ),
    ]
