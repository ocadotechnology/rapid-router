# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def change_farm_tree1_size(apps, schema_editor):

    Decor = apps.get_model('game', 'Decor')

    tree = Decor.objects.get(name='tree1', theme_id=3)
    tree.height = 100
    tree.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0077_change_character_urls'),
    ]

    operations = [
        migrations.RunPython(change_farm_tree1_size)
    ]
