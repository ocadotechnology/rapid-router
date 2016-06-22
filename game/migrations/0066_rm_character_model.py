# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0065_rename_old_character_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='level',
            name='character_old',
        ),
        migrations.DeleteModel(
            name='Character',
        ),
    ]
