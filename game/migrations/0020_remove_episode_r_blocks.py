# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0019_episode_pop_r_stats'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='episode',
            name='r_blocks',
        ),
    ]
