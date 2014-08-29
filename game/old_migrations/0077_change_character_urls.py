# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def change_character_urls(apps, schema_editor):

    Character = apps.get_model('game', 'Character')

    for character in Character.objects.all():
        character.en_face = '/static/game/image/characters/front_view/' + character.name + '.svg'
        character.top_down = '/static/game/image/characters/top_view/' + character.name + '.svg'
        character.save();


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0076_traffic_light_fixes'),
    ]

    operations = [
    	migrations.RunPython(change_character_urls)
    ]
