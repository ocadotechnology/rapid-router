# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0046_set_img_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='r_cows',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='level',
            name='cows',
            field=models.TextField(default=b'[]', max_length=10000),
            preserve_default=True,
        ),
    ]
