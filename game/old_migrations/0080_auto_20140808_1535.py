# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0079_change_decor_urls'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theme',
            name='background',
        ),
        migrations.RemoveField(
            model_name='theme',
            name='border',
        ),
        migrations.RemoveField(
            model_name='theme',
            name='selected',
        ),
    ]
