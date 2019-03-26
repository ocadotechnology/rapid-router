# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    Level = apps.get_model("game", "Level")
    Character = apps.get_model("game", "Character")
    db_alias = schema_editor.connection.alias
    for character in Character.objects.using(db_alias):
        Level.objects.filter(character=character).update(character_name=character.name)


def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [("game", "0063_level_character_name")]

    operations = [migrations.RunPython(forwards_func, reverse_func)]
