from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [("game", "0054_disable_route_score_for_levels_69_and_74")]

    operations = [
        migrations.AddField(
            model_name="attempt",
            name="is_best_attempt",
            field=models.BooleanField(default=False, db_index=True),
        ),
        migrations.AlterField(
            model_name="attempt",
            name="finish_time",
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
