# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0034_auto_20140721_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='blocklyEnabled',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='level',
            name='pythonEnabled',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
