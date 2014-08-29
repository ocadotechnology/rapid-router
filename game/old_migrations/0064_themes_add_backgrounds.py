# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def add_backgrounds(apps, schema_editor):

    Theme = apps.get_model('game', 'Theme')

    grass = Theme.objects.get(pk=1)
    winter = Theme.objects.get(pk=2)

    grass.background = '#a0c53a'
    winter.background = '#eff8ff'

    grass.save()
    winter.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0063_theme_background'),
    ]

    operations = [
        migrations.RunPython(add_backgrounds)
    ]
