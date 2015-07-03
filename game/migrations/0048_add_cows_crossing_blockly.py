# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

import json


def add_cows_block(apps, schema_editor):

    Block = apps.get_model('game', 'Block')

    cow_crossing = Block.objects.create(type='cow_crossing')
    cow_crossing.save()
    declare_event = Block.objects.create(type='declare_event')
    declare_event.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0047_add_cows'),
    ]

    operations = [
        migrations.RunPython(add_cows_block)
    ]
