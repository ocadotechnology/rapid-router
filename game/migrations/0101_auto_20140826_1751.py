# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0100_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workspace',
            name='workspace',
        ),
        migrations.AddField(
            model_name='workspace',
            name='contents',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='level',
            name='origin',
            field=models.CharField(default=b'[]', max_length=10),
        ),
        migrations.AlterField(
            model_name='workspace',
            name='owner',
            field=models.ForeignKey(blank=True, to='portal.UserProfile', null=True),
        ),
    ]
