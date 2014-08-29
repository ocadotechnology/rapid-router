# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

import json

def add_origin_to_level(apps, schema_editor):
    Level = apps.get_model('game', 'Level')

    for level in Level.objects.all():
        path = json.loads(level.path)
        coord = path[0]['coordinate']
        
        nextCoord = path[path[0]['connectedNodes'][0]]['coordinate']

        if nextCoord[1] > coord[1]:
            direction = "N"
        elif nextCoord[0] > coord[0]:
            direction = "E"
        elif nextCoord[1] < coord[1]:
            direction = "S"
        elif nextCoord[0] < coord[0]:
            direction = "W"

        level.origin = json.dumps({'coordinate': coord, 'direction': direction})
        level.save()

class Migration(migrations.Migration):

    dependencies = [
        ('game', '0093_change_traffic_light_representation'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='origin',
            field=models.CharField(default=b'[]', max_length=50),
            preserve_default=True,
        ),
        migrations.RunPython(add_origin_to_level)
    ]