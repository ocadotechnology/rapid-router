# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

import json


def add_cows_to_levels(apps, schema_editor):

    Level = apps.get_model('game', 'Level')

    level4 = Level.objects.get(name='4', default=True)
    level4.cows = '[{"potentialCoordinates":[{"x":1,"y":3},{"x":2,"y":3},{"x":3,"y":3},{"x":4,"y":3},{"x":4,"y":4},{"x":4,"y":5}],"minCows":1,"maxCows":1}]'
    level4.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0048_add_cows_crossing_blockly'),
    ]

    operations = [
        migrations.RunPython(add_cows_to_levels)
    ]
