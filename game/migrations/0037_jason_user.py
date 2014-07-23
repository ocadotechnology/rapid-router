# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.contrib.auth.hashers import make_password

def insert_jason(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    jason = User.objects.create()
    jason.username = 'jason'
    jason.email = '',
    jason.is_superuser = False
    jason.is_staff = False
    jason.password = make_password('pU23tZC15YE6bhh')
    jason.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0036_merge'),
    ]

    operations = [
            migrations.RunPython(insert_jason),
    ]
