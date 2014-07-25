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
            field=models.ForeignKey(default=1, to='game.Theme'),
            preserve_default=True,
        ),
    ]
