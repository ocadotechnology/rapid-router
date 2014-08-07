# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def populate_characters(apps, schema_editor):

    Character = apps.get_model('game', 'Character')

    dee = Character(name='Dee', en_face='/static/game/image/characters/Dee.svg',
                    top_down='/static/game/image/characters/Dee_topDown.svg')

    kristy = Character(name='Kristy', en_face='/static/game/image/characters/Kristy.svg',
                       top_down='/static/game/image/characters/Kristy_topDown.svg')

    nigel = Character(name='Nigel', en_face='/static/game/image/characters/Nigel.svg',
                      top_down='/static/game/image/characters/Nigel_topDown.svg')

    van = Character(name='Van', en_face='/static/game/image/characters/van_small.svg',
                    top_down='/static/game/image/characters/van_small.svg')

    dee.save()
    kristy.save()
    nigel.save()
    van.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0071_character'),
    ]

    operations = [
        migrations.RunPython(populate_characters)
    ]
