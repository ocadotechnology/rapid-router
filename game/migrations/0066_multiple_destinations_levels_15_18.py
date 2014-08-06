# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def add_destinations(apps, schema_editor):

    Level = apps.get_model('game', 'Level')
    Block = apps.get_model('game', 'Block')

    blocks = Block.objects.filter(type__in=['turn_left', 'turn_right', 'move_forwards', 'deliver'])

    level15 = Level.objects.get(pk=15)
    level15.destinations = [[5, 5], [7, 2]]
    level15.model_solution = [13]
    level15.blocks = blocks
    level15.save()

    level16 = Level.objects.get(pk=16)
    level16.destinations = [[7, 0], [5, 1], [1, 4]]
    level16.model_solution = [16]
    level16.blocks = blocks
    level16.save()

    level17 = Level.objects.get(pk=17)
    level17.destinations = [[4, 1], [5, 2], [5, 5], [3, 6]]
    level17.model_solution = [16]
    level17.blocks = blocks
    level17.save()

    level18 = Level.objects.get(pk=18)
    level18.destinations = [[2, 7], [7, 7], [8, 5], [8, 1]]
    level18.model_solution = [19]
    level18.blocks = blocks
    level18.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0065_change_pond_size'),
    ]

    operations = [
        migrations.RunPython(add_destinations)
    ]
