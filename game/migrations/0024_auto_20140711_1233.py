# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0023_episode_r_curviness'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='r_curviness',
            field=models.FloatField(default=0),
        ),
    ]
