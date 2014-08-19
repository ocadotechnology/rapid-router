# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0073_populate_characters'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='level',
            name='character',
        ),
    ]
