# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-07-16 16:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('game', '0070_update_strings_unicode'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.AlterField(
                    model_name='attempt',
                    name='student',
                    field=models.ForeignKey(blank=True, null=True,
                                            on_delete=django.db.models.deletion.CASCADE,
                                            related_name='attempts',
                                            to='common.Student'),
                ),
            ],
            # You're reusing an existing table, so do nothing
            database_operations=[],
        ),
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.AlterField(
                    model_name='level',
                    name='owner',
                    field=models.ForeignKey(blank=True, null=True,
                                            on_delete=django.db.models.deletion.CASCADE,
                                            related_name='levels',
                                            to='common.UserProfile'),
                ),
            ],
            # You're reusing an existing table, so do nothing
            database_operations=[],
        ),
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.AlterField(
                    model_name='workspace',
                    name='owner',
                    field=models.ForeignKey(blank=True, null=True,
                                            on_delete=django.db.models.deletion.CASCADE,
                                            related_name='workspaces',
                                            to='common.UserProfile'),
                ),
            ],
            # You're reusing an existing table, so do nothing
            database_operations=[],
        ),
    ]
