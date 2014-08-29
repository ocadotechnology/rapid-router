# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.contrib.auth.hashers import make_password

def insert_sharon(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    jason = User.objects.create()
    jason.username = 'sharon'
    jason.email = '',
    jason.is_superuser = False
    jason.is_staff = False
    jason.password = make_password('c3n6Zd741kb086a')
    jason.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0037_jason_user'),
    ]

    operations = [
            migrations.RunPython(insert_sharon),
    ]
