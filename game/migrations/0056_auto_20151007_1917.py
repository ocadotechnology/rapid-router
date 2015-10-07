# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0055_bestattempt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attempt',
            name='finish_time',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
