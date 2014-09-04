# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_leveldecor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attempt',
            name='level',
            field=models.ForeignKey(related_name=b'attempts', to='game.Level'),
        ),
        migrations.AlterField(
            model_name='attempt',
            name='student',
            field=models.ForeignKey(related_name=b'attempts', blank=True, to='portal.Student', null=True),
        ),
        migrations.AlterField(
            model_name='decor',
            name='theme',
            field=models.ForeignKey(related_name=b'decor', to='game.Theme'),
        ),
        migrations.AlterField(
            model_name='episode',
            name='r_blocks',
            field=models.ManyToManyField(related_name=b'episodes', to=b'game.Block'),
        ),
        migrations.AlterField(
            model_name='level',
            name='blocks',
            field=models.ManyToManyField(related_name=b'levels', to=b'game.Block'),
        ),
        migrations.AlterField(
            model_name='level',
            name='owner',
            field=models.ForeignKey(related_name=b'levels', blank=True, to='portal.UserProfile', null=True),
        ),
        migrations.AlterField(
            model_name='level',
            name='shared_with',
            field=models.ManyToManyField(related_name=b'shared', null=True, to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AlterField(
            model_name='workspace',
            name='owner',
            field=models.ForeignKey(related_name=b'workspaces', blank=True, to='portal.UserProfile', null=True),
        ),
    ]
