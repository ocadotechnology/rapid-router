# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def upload_backgrounds(apps, schema_editor):

    Decor = apps.get_model('game', 'Decor')
    Theme = apps.get_model('game', 'Theme')

    grass = Theme.objects.get(pk=1)
    winter = Theme.objects.get(pk=2)

    grass_tile = Decor(name='tile1', url='/static/game/image/grassTile1.svg', width=100,
                       height=100, theme=grass)

    snow_tile1 = Decor(name='tile1', url='/static/game/image/snowTile2.svg', width=100,
                       height=100, theme=winter)

    snow_tile2 = Decor(name='tile2', url='/static/game/image/snowTile1.svg', width=100,
                       height=100, theme=winter)

    grass_tile.save()
    snow_tile1.save()
    snow_tile2.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0056_winter_wonderland'),
    ]

    operations = [
        migrations.RunPython(upload_backgrounds)
    ]
