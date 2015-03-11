# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0042_level_score_73'),
    ]

    operations = [
        migrations.AddField(
            model_name='decor',
            name='z_index',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
