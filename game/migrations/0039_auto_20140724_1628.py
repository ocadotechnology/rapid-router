# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0038_sharon_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='destination',
            field=models.CharField(max_length=50),
        ),
    ]
