# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def character_urls(apps, schema_editor):

    Character = apps.get_model('game', 'Character')

    van = Character.objects.get(name='Van')
    van.en_face = 'characters/front_view/Van.svg'
    van.top_down = 'characters/top_view/Van.svg'
    van.save()

    dee = Character.objects.get(name='Dee')
    dee.en_face = 'characters/front_view/Dee.svg'
    dee.top_down = 'characters/top_view/Dee.svg'
    dee.save()

    nigel = Character.objects.get(name='Nigel')
    nigel.en_face = 'characters/front_view/Nigel.svg'
    nigel.top_down = 'characters/top_view/Nigel.svg'
    nigel.save()

    kirsty = Character.objects.get(name='Kirsty')
    kirsty.en_face = 'characters/front_view/Kirsty.svg'
    kirsty.top_down = 'characters/top_view/Kirsty.svg'
    kirsty.save()

    wes = Character.objects.get(name='Wes')
    wes.en_face = 'characters/front_view/Wes.svg'
    wes.top_down = 'characters/top_view/Wes.svg'
    wes.save()

    phil = Character.objects.get(name='Phil')
    phil.en_face = 'characters/front_view/Phil.svg'
    phil.top_down = 'characters/top_view/Phil.svg'
    phil.save()

class Migration(migrations.Migration):

    dependencies = [
        ('game', '0107_add_blocks_back_to_episodes'),
    ]

    operations = [
        migrations.RunPython(character_urls)
    ]
