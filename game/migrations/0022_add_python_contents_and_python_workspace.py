# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0021_fix_level_63'),
    ]

    operations = [
        migrations.AddField(
            model_name='attempt',
            name='python_workspace',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='workspace',
            name='python_contents',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
    ]
