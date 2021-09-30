from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [("game", "0042_level_score_73")]

    operations = [
        migrations.RemoveField(model_name="episode", name="first_level"),
        migrations.AlterField(
            model_name="level",
            name="episode",
            field=models.ForeignKey(
                default=None,
                blank=True,
                to="game.Episode",
                null=True,
                on_delete=models.PROTECT,
            ),
        ),
    ]
