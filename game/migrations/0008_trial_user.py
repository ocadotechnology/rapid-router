# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.contrib.auth.hashers import make_password

def insert_trial_user(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    admin = User.objects.create()
    admin.username = 'trial'
    admin.email = 'coding-for-life-xd@ocado.com', 
    admin.is_superuser = False
    admin.is_staff = False
    admin.password = make_password('cabbage')
    admin.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_admin_user'),
    ]

    operations = [
            migrations.RunPython(insert_trial_user),
    ]
