# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0032_episode_r_blocks'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='r_blocklyEnabled',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='episode',
            name='r_pythonEnabled',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
