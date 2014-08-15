# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0084_city_theme_populate_colours_add_Phil'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='fuel_gauge',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
