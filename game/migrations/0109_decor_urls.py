# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def decor_urls(apps, schema_editor):

    Decor = apps.get_model('game', 'Decor')

    for decor in Decor.objects.all():
        if decor.url.startswith('/static/game/image/'):
            decor.url = decor.url[19:]
            decor.save()

class Migration(migrations.Migration):

    dependencies = [
        ('game', '0108_character_urls'),
    ]

    operations = [
        migrations.RunPython(decor_urls)
    ]
