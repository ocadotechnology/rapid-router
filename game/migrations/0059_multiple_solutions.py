# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0058_change_theme_name_from_default'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='model_solution',
            field=models.CharField(default=b'[]', max_length=10, blank=True),
        ),
    ]
