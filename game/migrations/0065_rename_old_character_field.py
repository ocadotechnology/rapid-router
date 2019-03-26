# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [("game", "0064_character_name_data")]

    operations = [
        migrations.RenameField(
            model_name="level", old_name="character", new_name="character_old"
        )
    ]
