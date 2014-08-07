# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0072_populate_characters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='character',
            field=models.ForeignKey(default=4, to='game.Character'),
        ),
    ]
