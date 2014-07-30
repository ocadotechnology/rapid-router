# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0021_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='r_blocks',
            field=models.ManyToManyField(to=b'game.Block'),
            preserve_default=True,
        ),
    ]
