from django.db import migrations


def mark_all_attempts_as_best(apps, schema_editor):
    Attempt = apps.get_model("game", "Attempt")
    Attempt.objects.all().update(is_best_attempt=True)


class Migration(migrations.Migration):

    dependencies = [("game", "0055_support_multiple_attempts")]

    operations = [migrations.RunPython(mark_all_attempts_as_best)]
