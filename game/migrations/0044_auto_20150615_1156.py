from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [("game", "0043_auto_20150615_1155")]

    operations = [
        migrations.AlterField(
            model_name="episode",
            name="r_blocks",
            field=models.ManyToManyField(related_name="episodes", to="game.Block"),
        ),
        migrations.AlterField(
            model_name="level",
            name="shared_with",
            field=models.ManyToManyField(
                related_name="shared", to=settings.AUTH_USER_MODEL, blank=True
            ),
        ),
    ]
