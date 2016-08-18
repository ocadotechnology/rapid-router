# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0065_rename_old_character_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='owner',
            field=models.ForeignKey(related_name='levels', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='workspace',
            name='owner',
            field=models.ForeignKey(related_name='workspaces', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
