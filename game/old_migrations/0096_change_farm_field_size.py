# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def change_farm_field_size(apps, schema_editor):
    Decor = apps.get_model('game', 'Decor')

    field = Decor.objects.get(name="pond",  theme_id=3)

    field.width = 150
    field.height = 100

    field.save();


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0095_show_level_26_27_28'),
    ]

    operations = [
        migrations.RunPython(change_farm_field_size)
    ]
