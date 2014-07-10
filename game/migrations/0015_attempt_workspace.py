# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0014_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='attempt',
            name='workspace',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
    ]
