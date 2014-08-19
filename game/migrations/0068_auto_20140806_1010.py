# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0019_auto_20140804_1713'),
        ('game', '0067_theme_add_colours'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='school',
        ),
        migrations.RemoveField(
            model_name='class',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='guardian',
            name='children',
        ),
        migrations.RemoveField(
            model_name='guardian',
            name='user',
        ),
        migrations.RemoveField(
            model_name='student',
            name='class_field',
        ),
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='attempt',
            name='student',
        ),
        migrations.RemoveField(
            model_name='level',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='workspace',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Guardian',
        ),
        migrations.DeleteModel(
            name='School',
        ),
        migrations.DeleteModel(
            name='Class',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
