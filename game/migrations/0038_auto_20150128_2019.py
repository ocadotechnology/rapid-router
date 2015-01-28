# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0037_level_score_79'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='episode',
            field=models.ForeignKey(default=-1, to='game.Episode'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='episode',
            name='first_level',
            field=models.ForeignKey(related_name=b'episodeForFirstLevel', to='game.Level'),
        ),
    ]
