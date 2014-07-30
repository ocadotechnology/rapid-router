# -*- coding: utf-8 -*-
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [('game', '0049_episode_random_level_params')]

    operations = [
        migrations.RenameField('Level', 'destination', 'destinations')
    ]
