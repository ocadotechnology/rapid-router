# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def remove_text_block(apps, schema_editor):
    Block = apps.get_model('game', 'Block')
    text_block=Block.objects.get(type="text");
    text_block.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0071_character'),
    ]

    operations = [
    	migrations.RunPython(remove_text_block),
    ]
