# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0011_level_52_fix'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='level',
            name='blocks',
        ),
    ]
