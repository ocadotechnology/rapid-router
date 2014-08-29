# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0048_fix_level_blocks'),
    ]

    operations = [
        migrations.AddField(
            model_name='leveldecor',
            name='decorName',
            field=models.CharField(default=b'tree1', max_length=100),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='leveldecor',
            name='decor',
        ),
        migrations.AlterField(
            model_name='level',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
