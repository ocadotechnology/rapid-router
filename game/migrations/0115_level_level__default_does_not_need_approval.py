# Generated by Django 4.2.18 on 2025-02-14 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("game", "0114_default_and_non_student_levels_no_approval"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="level",
            constraint=models.CheckConstraint(
                check=models.Q(
                    ("default", True), ("needs_approval", True), _negated=True
                ),
                name="level__default_does_not_need_approval",
            ),
        ),
    ]
