# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0009_auto_20140905_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='in_development',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
