# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def disable_python(apps, schema_editor):

    Level = apps.get_model('game', 'Level')

    for level in Level.objects.all():
        level.pythonEnabled = False;
        level.save()
        

class Migration(migrations.Migration):

    dependencies = [
        ('game', '0103_auto_20140827_1042'),
    ]

    operations = [
        migrations.RunPython(disable_python)
    ]
