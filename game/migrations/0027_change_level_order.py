# -*- coding: utf-8 -*-
# Code for Life
#
# Copyright (C) 2016, Ocado Innovation Limited
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ADDITIONAL TERMS – Section 7 GNU General Public Licence
#
# This licence does not grant any right, title or interest in any “Ocado” logos,
# trade names or the trademark “Ocado” or any other trademarks or domain names
# owned by Ocado Innovation Limited or the Ocado group of companies or any other
# distinctive brand features of “Ocado” as may be secured from time to time. You
# must not distribute any modification of this program using the trademark
# “Ocado” or claim any affiliation or association with Ocado or its employees.
#
# You are not authorised to use the name Ocado (or any of its trade names) or
# the names of any author or contributor in advertising or for publicity purposes
# pertaining to the distribution of this program, without the prior written
# authorisation of Ocado.
#
# Any propagation, distribution or conveyance of this program must include this
# copyright notice and these terms. You must not misrepresent the origins of this
# program; modified versions of the program must be marked as such and not
# identified as the original program.
from __future__ import unicode_literals

from django.db import migrations


def change_level_order(apps, schema_editor):

    Level = apps.get_model('game', 'Level')

    level93 = Level.objects.get(name='93', default=1)
    level96 = Level.objects.get(name='94', default=1)
    level94 = Level.objects.get(name='95', default=1)
    level95 = Level.objects.get(name='96', default=1)
    level97 = Level.objects.get(name='97', default=1)
    level98 = Level.objects.get(name='98', default=1)

    level93.name = '93'
    level94.name = '94'
    level95.name = '95'
    level96.name = '96'
    level97.name = '97'

    level93.next_level = level94
    level94.next_level = level95
    level95.next_level = level96
    level96.next_level = level97
    level97.next_level = level98

    level93.save()
    level94.save()
    level95.save()
    level96.save()
    level97.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0026_levels_pt2'),
    ]

    operations = [
        migrations.RunPython(change_level_order)
    ]
