from django.apps.registry import Apps
from django.db import migrations


def delete_invalid_attempts(apps: Apps, *args):
    Attempt = apps.get_model("game", "Attempt")

    Attempt.objects.filter(start_time__isnull=True).delete()


class Migration(migrations.Migration):
    dependencies = [("game", "0104_remove_level_direct_drive")]
    operations = [
        migrations.RunPython(
            delete_invalid_attempts,
            reverse_code=migrations.RunPython.noop,
        )
    ]
