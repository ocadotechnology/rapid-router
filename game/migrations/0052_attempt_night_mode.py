# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [("game", "0051_level_score_49")]

    operations = [
        migrations.AddField(
            model_name="attempt",
            name="night_mode",
            field=models.BooleanField(default=False),
        )
    ]
