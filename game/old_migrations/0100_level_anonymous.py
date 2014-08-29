# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0099_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='anonymous',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
