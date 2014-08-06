# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0068_auto_20140806_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='attempt',
            name='student',
            field=models.ForeignKey(default=0, to='portal.Student'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='level',
            name='owner',
            field=models.ForeignKey(blank=True, to='portal.UserProfile', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='workspace',
            name='owner',
            field=models.ForeignKey(default=0, to='portal.Student'),
            preserve_default=False,
        ),
    ]
