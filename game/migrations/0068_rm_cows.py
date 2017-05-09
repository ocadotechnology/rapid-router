# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0067_level_score_27'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='episode',
            name='r_cows',
        ),
        migrations.RemoveField(
            model_name='level',
            name='cows',
        ),
    ]
