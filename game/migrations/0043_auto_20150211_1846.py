# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0042_remove_episode_first_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='episode',
            field=models.ForeignKey(default=None, blank=True, to='game.Episode', null=True),
        ),
    ]
