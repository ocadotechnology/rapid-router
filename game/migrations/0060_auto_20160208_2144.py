# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [("game", "0059_theme_name_data")]

    operations = [
        migrations.AlterField(
            model_name="level",
            name="theme",
            field=models.ForeignKey(
                db_column=b"theme_id",
                default=None,
                blank=True,
                to="game.Theme",
                null=True,
            ),
        )
    ]
