# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def add_solutions(apps, schema_editor):

    Level = apps.get_model('game', 'Level')

    level43 = Level.objects.get(name='43', default=True)
    level43.model_solutions = '[10, 11, 21]'
    level43.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0022_add_python_contents_and_python_workspace'),
    ]

    operations = [
        migrations.RunPython(add_solutions)
    ]
