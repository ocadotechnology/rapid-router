# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def change_decor_urls(apps, schema_editor):

    Decor = apps.get_model('game', 'Decor')
    Theme = apps.get_model('game', 'Theme')

    for decor in Decor.objects.all():
        theme =  Theme.objects.get(id=decor.theme_id)
        decor.url = '/static/game/image/decor/' + theme.name + '/' + decor.name + '.svg'
        decor.save();

class Migration(migrations.Migration):

    dependencies = [
        ('game', '0078_change_farm_tree1_size'),
    ]

    operations = [
    	migrations.RunPython(change_decor_urls)
    ]
