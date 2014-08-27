# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def fix_Kirsty(apps, schema_editor):

    Character = apps.get_model('game', 'Character')

    Kirsty = Character.objects.get(pk=4)
    Kirsty.name = 'Kirsty'
    Kirsty.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0102_merge'),
    ]

    operations = [
        migrations.RunPython(fix_Kirsty)
    ]
