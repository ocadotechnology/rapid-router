# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def fix_dee(apps, schema_editor):

    Character = apps.get_model('game', 'Character')

    dee = Character.objects.get(name='Dee')
    dee.en_face = 'characters/front_view/Dee.svg'
    dee.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_added_block__limits'),
    ]

    operations = [
        migrations.RunPython(fix_dee)
    ]
