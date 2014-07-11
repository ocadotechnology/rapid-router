# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0017_student_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='r_blocks',
            field=models.ManyToManyField(to=b'game.Block'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='episode',
            name='r_branchiness',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='episode',
            name='r_loopiness',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='episode',
            name='r_num_tiles',
            field=models.IntegerField(default=5),
            preserve_default=True,
        ),
    ]
