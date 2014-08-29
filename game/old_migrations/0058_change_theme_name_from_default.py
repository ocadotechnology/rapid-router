# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def rename_default(apps, schema_editor):

    Theme = apps.get_model('game', 'Theme')

    grass = Theme.objects.get(pk=1)
    grass.name = 'grass'
    grass.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0057_add_background_decor'),
    ]

    operations = [
        migrations.RunPython(rename_default)
    ]
