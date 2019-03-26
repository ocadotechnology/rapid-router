# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [("game", "0057_workspace_language_enabled")]

    operations = [
        migrations.AddField(
            model_name="level",
            name="theme_name",
            field=models.CharField(
                default=None,
                max_length=10,
                null=True,
                blank=True,
                choices=[
                    ("farm", "farm"),
                    ("city", "city"),
                    ("grass", "grass"),
                    ("snow", "snow"),
                ],
            ),
        )
    ]
