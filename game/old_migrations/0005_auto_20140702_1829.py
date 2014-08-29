# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_auto_20140702_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='decor',
            field=models.TextField(default=b'[]', max_length=10000),
        ),
        migrations.AlterField(
            model_name='level',
            name='path',
            field=models.TextField(max_length=10000),
        ),
    ]
