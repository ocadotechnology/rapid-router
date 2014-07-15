# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0024_auto_20140711_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='threads',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
