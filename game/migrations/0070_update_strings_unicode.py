# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-07-16 13:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("game", "0069_remove_user_levels_from_episodes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="level",
            name="character_name",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Van", "Van"),
                    ("Dee", "Dee"),
                    ("Nigel", "Nigel"),
                    ("Kirsty", "Kirsty"),
                    ("Wes", "Wes"),
                    ("Phil", "Phil"),
                ],
                default=None,
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="level",
            name="theme_name",
            field=models.CharField(
                blank=True,
                choices=[
                    ("grass", "grass"),
                    ("snow", "snow"),
                    ("farm", "farm"),
                    ("city", "city"),
                ],
                default=None,
                max_length=10,
                null=True,
            ),
        ),
    ]
