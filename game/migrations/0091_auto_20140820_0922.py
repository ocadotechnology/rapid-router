# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0090_change_decor_49_50'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='command',
            name='attempt',
        ),
        migrations.DeleteModel(
            name='Command',
        ),
    ]
