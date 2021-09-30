from __future__ import unicode_literals

from django.db import models, migrations


def disable_route_scores(apps, schema_editor):

    Level = apps.get_model("game", "Level")
    level52 = Level.objects.get(name="52")
    level54 = Level.objects.get(name="54")
    level59 = Level.objects.get(name="59")
    level60 = Level.objects.get(name="60")
    level68 = Level.objects.get(name="68")

    level52.disable_route_score = True
    level52.save()
    level54.disable_route_score = True
    level54.save()
    level59.disable_route_score = True
    level59.save()
    level60.disable_route_score = True
    level60.save()
    level68.disable_route_score = True
    level68.save()


class Migration(migrations.Migration):

    dependencies = [("game", "0028_level_disable_route_score")]

    operations = [migrations.RunPython(disable_route_scores)]
