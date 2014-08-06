# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def change_theme_data(apps, schema_editor):

    Theme = apps.get_model('game', 'Theme')

    winter = Theme.objects.get(pk=2)
    winter.border = '#b3deff'
    winter.selected = '#83c9fe'
    winter.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0067_theme_add_colours'),
    ]

    operations = [
        migrations.RunPython(change_theme_data)
    ]
