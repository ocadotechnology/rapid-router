# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

import json

def change_traffic_light_representation(apps, schema_editor):

    Level = apps.get_model('game', 'Level')

    level44 = Level.objects.get(id=44)
    level44.traffic_lights = json.dumps([{"sourceCoordinate": {'x':3,'y':3}, "startTime": 0, "direction": 'E', "greenDuration": 2, "startingState": "RED", "redDuration": 4}])
    level44.save();

    level45 = Level.objects.get(id=45)
    level45.traffic_lights = json.dumps([{"sourceCoordinate": {'x':4,'y':3}, "startTime": 0, "direction": 'W', "greenDuration": 1, "startingState": "GREEN", "redDuration": 4},
                                        {"sourceCoordinate": {'x':5,'y':3}, "startTime": 0, "direction": 'W', "greenDuration": 1, "startingState": "RED", "redDuration": 3}])
    level45.save();

    level46 = Level.objects.get(id=46)
    level46.traffic_lights = json.dumps([{"sourceCoordinate": {'x':5,'y':3}, "startTime": 0, "direction": 'W', "greenDuration": 2, "startingState": "RED", "redDuration": 4}])
    level46.save();

    level47 = Level.objects.get(id=47)
    level47.traffic_lights = json.dumps([{"sourceCoordinate": {'x':6,'y':3}, "startTime": 0, "direction": 'N', "greenDuration": 3, "startingState": "RED", "redDuration": 3}, 
                                         {"sourceCoordinate": {'x':5,'y':6}, "startTime": 0, "direction": 'W', "greenDuration": 3, "startingState": "RED", "redDuration": 3}, 
                                         {"sourceCoordinate": {'x':2,'y':5}, "startTime": 0, "direction": 'S', "greenDuration": 3, "startingState": "RED", "redDuration": 3}, 
                                         {"sourceCoordinate": {'x':3,'y':2}, "startTime": 0, "direction": 'E', "greenDuration": 3, "startingState": "GREEN", "redDuration": 3}])
    level47.save();

    level48 = Level.objects.get(id=48)
    level48.traffic_lights = json.dumps([{"sourceCoordinate": {'x':3,'y':5}, "startTime": 0, "direction": 'E', "greenDuration": 2, "startingState": "RED", "redDuration": 4}, 
                                        {"sourceCoordinate": {'x':4,'y':6}, "startTime": 0, "direction": 'S', "greenDuration": 4, "startingState": "GREEN", "redDuration": 2}, 
                                        {"sourceCoordinate": {'x':4,'y':4}, "startTime": 0, "direction": 'N', "greenDuration": 4, "startingState": "GREEN", "redDuration": 2}, 
                                        {"sourceCoordinate": {'x':5,'y':5}, "startTime": 0, "direction": 'W', "greenDuration": 2, "startingState": "RED", "redDuration": 4}])
    level48.save();

    level49 = Level.objects.get(id=49)
    level49.traffic_lights = json.dumps([{"sourceCoordinate": {'x':3,'y':5}, "startTime": 0, "direction": 'S', "greenDuration": 2, "startingState": "RED", "redDuration": 4}, 
                                        {"sourceCoordinate": {'x':2,'y':4}, "startTime": 0, "direction": 'E', "greenDuration": 2, "startingState": "GREEN", "redDuration": 4}, 
                                        {"sourceCoordinate": {'x':4,'y':4}, "startTime": 0, "direction": 'W', "greenDuration": 2, "startingState": "GREEN", "redDuration": 4}, 
                                        {"sourceCoordinate": {'x':3,'y':3}, "startTime": 0, "direction": 'N', "greenDuration": 2, "startingState": "RED", "redDuration": 4}, 
                                        {"sourceCoordinate": {'x':7,'y':5}, "startTime": 0, "direction": 'S', "greenDuration": 4, "startingState": "GREEN", "redDuration": 2}, 
                                        {"sourceCoordinate": {'x':7,'y':3}, "startTime": 0, "direction": 'N', "greenDuration": 4, "startingState": "GREEN", "redDuration": 2}, 
                                        {"sourceCoordinate": {'x':6,'y':4}, "startTime": 0, "direction": 'E', "greenDuration": 2, "startingState": "RED", "redDuration": 4}])
    level49.save();

    level50 = Level.objects.get(id=50)
    level50.traffic_lights = json.dumps([{"sourceCoordinate": {'x':1,'y':1}, "startTime": 0, "direction": 'E', "greenDuration": 2, "startingState": "RED", "redDuration": 4}, 
                                        {"sourceCoordinate": {'x':2,'y':0}, "startTime": 2, "direction": 'N', "greenDuration": 2, "startingState": "RED", "redDuration": 4}, 
                                        {"sourceCoordinate": {'x':3,'y':1}, "startTime": 0, "direction": 'W', "greenDuration": 2, "startingState": "GREEN", "redDuration": 4}, 
                                        {"sourceCoordinate": {'x':4,'y':1}, "startTime": 0, "direction": 'N', "greenDuration": 2, "startingState": "RED", "redDuration": 4}, 
                                        {"sourceCoordinate": {'x':4,'y':3}, "startTime": 2, "direction": 'S', "greenDuration": 2, "startingState": "RED", "redDuration": 4}, 
                                        {"sourceCoordinate": {'x':5,'y':2}, "startTime": 0, "direction": 'W', "greenDuration": 2, "startingState": "GREEN", "redDuration": 4}, 
                                        {"sourceCoordinate": {'x':3,'y':5}, "startTime": 0, "direction": 'E', "greenDuration": 2, "startingState": "RED", "redDuration": 4}, 
                                        {"sourceCoordinate": {'x':4,'y':6}, "startTime": 2, "direction": 'S', "greenDuration": 2, "startingState": "RED", "redDuration": 4}, 
                                        {"sourceCoordinate": {'x':4,'y':4}, "startTime": 0, "direction": 'N', "greenDuration": 2, "startingState": "GREEN", "redDuration": 4}, 
                                        {"sourceCoordinate": {'x':2,'y':6}, "startTime": 0, "direction": 'W', "greenDuration": 4, "startingState": "RED", "redDuration": 2}, 
                                        {"sourceCoordinate": {'x':9,'y':4}, "startTime": 0, "direction": 'W', "greenDuration": 2, "startingState": "RED", "redDuration": 4}, 
                                        {"sourceCoordinate": {'x':8,'y':3}, "startTime": 2, "direction": 'N', "greenDuration": 2, "startingState": "RED", "redDuration": 4}, 
                                        {"sourceCoordinate": {'x':7,'y':4}, "startTime": 0, "direction": 'E', "greenDuration": 2, "startingState": "GREEN", "redDuration": 4}])
    level50.save();

    
class Migration(migrations.Migration):

    dependencies = [
        ('game', '0092_add_character_size'),
    ]

    operations = [
        migrations.RunPython(change_traffic_light_representation)
    ]
