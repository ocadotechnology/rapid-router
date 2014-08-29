# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

import json


def fix_lights(apps, schema_editor):

    Level = apps.get_model('game', 'Level')

    levels = Level.objects.all()

    for level in levels:
        traffic_lights = json.loads(level.traffic_lights)
        
        for tl in traffic_lights:
            if 'id' in tl:
                del tl['id']
            if 'index' in tl:
                del tl['index']
            if 'node' in tl:
                tl['controlledNode'] = tl['node']
                del tl['node']

        level.traffic_lights = json.dumps(traffic_lights)

        level.save()
        

class Migration(migrations.Migration):

    dependencies = [
        ('game', '0075_insert_characters'),
    ]

    operations = [
        migrations.RunPython(fix_lights),
    ]
