# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0060_auto_20160208_2144'),
    ]

    operations = [
        migrations.RenameField(
            model_name='level',
            old_name='theme',
            new_name='theme_old',
        ),
    ]
