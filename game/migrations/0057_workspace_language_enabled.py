# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [("game", "0056_mark_all_attempts_as_best")]

    operations = [
        migrations.AddField(
            model_name="workspace",
            name="blockly_enabled",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="workspace",
            name="python_enabled",
            field=models.BooleanField(default=False),
        ),
    ]
