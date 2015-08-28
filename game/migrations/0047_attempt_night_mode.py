# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0046_set_img_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='attempt',
            name='night_mode',
            field=models.BooleanField(default=False),
        ),
    ]
