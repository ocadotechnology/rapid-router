# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0062_repopulating_themes'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='background',
            field=models.CharField(default=b'#EFF8FF', max_length=7),
            preserve_default=True,
        ),
    ]
