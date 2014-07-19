# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_levels'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='traffic_lights',
            field=models.TextField(default=b'[]', max_length=10000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='command',
            name='command',
            field=models.CharField(default=b'Forward', max_length=15, choices=[(b'Right', b'right'), (b'Left', b'left'), (b'Forward', b'forward'), (b'TurnAround', b'turn around'), (b'Wait', b'wait'), (b'While', b'while'), (b'If', b'if')]),
        ),
    ]
