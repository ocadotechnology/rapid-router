# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0080_auto_20140808_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='r_trafficLights',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
