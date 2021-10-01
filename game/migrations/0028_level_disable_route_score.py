from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [("game", "0027_change_level_order")]

    operations = [
        migrations.AddField(
            model_name="level",
            name="disable_route_score",
            field=models.BooleanField(default=False),
            preserve_default=True,
        )
    ]
