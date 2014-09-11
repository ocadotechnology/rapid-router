# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0014_correct_old_episode_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='level',
            name='decor',
        ),
    ]
