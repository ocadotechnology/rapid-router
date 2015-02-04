# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0041_level_episode_refs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='episode',
            name='first_level',
        ),
    ]
