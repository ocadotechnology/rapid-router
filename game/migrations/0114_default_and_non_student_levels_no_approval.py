from django.apps.registry import Apps
from django.db import migrations
from django.db.models import Q


def mark_default_and_non_student_levels_as_not_needing_approval(apps: Apps, *args):
    Level = apps.get_model("game", "Level")

    Level.objects.filter(Q(default=True) | Q(owner__user__email__isnull=False)).update(
        needs_approval=False
    )


def unmark_default_and_non_student_levels_as_not_needing_approval(apps: Apps, *args):
    Level = apps.get_model("game", "Level")

    Level.objects.filter(Q(default=True) | Q(owner__user__email__isnull=False)).update(
        needs_approval=True
    )


class Migration(migrations.Migration):

    dependencies = [("game", "0113_level_needs_approval")]

    operations = [
        migrations.RunPython(
            code=mark_default_and_non_student_levels_as_not_needing_approval,
            reverse_code=unmark_default_and_non_student_levels_as_not_needing_approval,
        )
    ]
