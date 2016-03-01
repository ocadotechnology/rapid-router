# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    Level = apps.get_model("game", "Level")
    Theme = apps.get_model("game", "Theme")
    db_alias = schema_editor.connection.alias
    for theme in Theme.objects.using(db_alias):
        Level.objects.filter(theme=theme).update(theme_name=theme.name)


def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0058_level_theme_name'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
