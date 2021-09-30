from __future__ import unicode_literals

from django.db import migrations


def change_level_order(apps, schema_editor):

    Level = apps.get_model("game", "Level")

    level93 = Level.objects.get(name="93", default=1)
    level96 = Level.objects.get(name="94", default=1)
    level94 = Level.objects.get(name="95", default=1)
    level95 = Level.objects.get(name="96", default=1)
    level97 = Level.objects.get(name="97", default=1)
    level98 = Level.objects.get(name="98", default=1)

    level93.name = "93"
    level94.name = "94"
    level95.name = "95"
    level96.name = "96"
    level97.name = "97"

    level93.next_level = level94
    level94.next_level = level95
    level95.next_level = level96
    level96.next_level = level97
    level97.next_level = level98

    level93.save()
    level94.save()
    level95.save()
    level96.save()
    level97.save()


class Migration(migrations.Migration):

    dependencies = [("game", "0026_levels_pt2")]

    operations = [migrations.RunPython(change_level_order)]
