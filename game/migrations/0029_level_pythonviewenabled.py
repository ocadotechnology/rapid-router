from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [("game", "0028_level_disable_route_score")]

    operations = [
        migrations.AddField(
            model_name="level",
            name="pythonViewEnabled",
            field=models.BooleanField(default=False),
            preserve_default=True,
        )
    ]
