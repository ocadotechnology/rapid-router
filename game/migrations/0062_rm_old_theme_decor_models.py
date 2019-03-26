# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [("game", "0061_auto_20160208_2144")]

    operations = [
        migrations.RemoveField(model_name="decor", name="theme"),
        migrations.RemoveField(model_name="level", name="theme_old"),
        migrations.DeleteModel(name="Decor"),
        migrations.DeleteModel(name="Theme"),
    ]
