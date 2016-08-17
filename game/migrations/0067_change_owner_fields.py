# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


def copy_owners(apps, schema_editor):
    for model_name in ('Level', 'Workspace'):
        model = apps.get_model('game', model_name)
        for r in model.objects.all():
            if r.owner is None:
                continue
            r.new_owner = r.owner.user
            r.save()


def restore_owners(apps, schema_editor):
    for model_name in ('Level', 'Workspace'):
        model = apps.get_model('game', model_name)
        for r in model.objects.all():
            if r.new_owner is None:
                continue
            r.owner = r.new_owner.userprofile
            r.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0066_rm_character_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='new_owner',
            field=models.ForeignKey(related_name='levels', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='workspace',
            name='new_owner',
            field=models.ForeignKey(related_name='workspaces', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.RunPython(copy_owners, reverse_code=restore_owners),
        migrations.RemoveField(
            model_name='level',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='workspace',
            name='owner',
        ),
        migrations.RenameField(
            model_name='level',
            old_name='new_owner',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='workspace',
            old_name='new_owner',
            new_name='owner',
        ),
    ]
