from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [("game", "0044_auto_20150615_1156")]

    operations = [
        migrations.AddField(
            model_name="decor",
            name="z_index",
            field=models.IntegerField(default=0),
            preserve_default=False,
        )
    ]
