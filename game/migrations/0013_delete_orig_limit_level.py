# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations



def delete_old_limit_level(apps, schema_editor):
    Level = apps.get_model('game', 'Level')

    if Level.objects.filter(name="Limited blocks test", default=True).exists():
        old_limit_level = Level.objects.get(name="Limited blocks test", default=True)
        old_limit_level.delete()



class Migration(migrations.Migration):

    dependencies = [
        ('game', '0012_remove_level_blocks'),
    ]

    operations = [
        migrations.RunPython(delete_old_limit_level),
    ]
