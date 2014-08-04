# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def change_pond_size(apps, schema_editor):

    Decor = apps.get_model('game', 'Decor')

    ponds = Decor.objects.filter(name='pond')

    for pond in ponds:
        pond.width = 150
        pond.height = 100
        pond.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0064_themes_add_backgrounds'),
    ]

    operations = [
        migrations.RunPython(change_pond_size)
    ]
