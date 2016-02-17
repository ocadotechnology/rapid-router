# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


def set_user(apps, schema_editor):
    model = apps.get_model('game', 'Attempt')
    for r in model.objects.all():
        if r.student is None:
            continue
        r.user = r.student.user.user
        r.save()


def restore_student(apps, schema_editor):
    model = apps.get_model('game', 'Attempt')
    for r in model.objects.all():
        if r.user is None:
            continue
        r.student = r.user.userprofile.student
        r.save()


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game', '0058_change_owner_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='attempt',
            name='user',
            field=models.ForeignKey(related_name='attempts', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.RemoveField(
            model_name='attempt',
            name='student',
        ),
    ]
