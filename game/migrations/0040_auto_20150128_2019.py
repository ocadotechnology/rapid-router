# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0039_second_episodes_release'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='episode',
            field=models.ForeignKey(default=-1, to='game.Episode'),
            preserve_default=False,
        ),
    ]
