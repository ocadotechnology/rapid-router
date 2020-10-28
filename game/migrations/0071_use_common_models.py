# -*- coding: utf-8 -*-
"""
This migration updates the models to reference the Common package's models instead of
Portal's models. This is to get rid of the circular dependency between Rapid Router and
Portal's models.

The important thing to note here is the use of migrations.SeparateDatabaseAndState.
This operation makes it possible to makes different changes to the state and to the
database. Essentially this is used to update the models' references to point to
Common's models, without having to change the table that the DB points to.
This migration has been made following the tutorial on how to move Django models:
https://realpython.com/move-django-model/ (following the Django way example).
"""
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("game", "0070_update_strings_unicode"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.AlterField(
                    model_name="attempt",
                    name="student",
                    field=models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="attempts",
                        to="common.Student",
                    ),
                ),
            ],
            # You're reusing an existing table, so do nothing
            database_operations=[],
        ),
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.AlterField(
                    model_name="level",
                    name="owner",
                    field=models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="levels",
                        to="common.UserProfile",
                    ),
                ),
            ],
            # You're reusing an existing table, so do nothing
            database_operations=[],
        ),
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.AlterField(
                    model_name="workspace",
                    name="owner",
                    field=models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="workspaces",
                        to="common.UserProfile",
                    ),
                ),
            ],
            # You're reusing an existing table, so do nothing
            database_operations=[],
        ),
    ]
