# -*- coding: utf-8 -*-
# Code for Life
#
# Copyright (C) 2019, Ocado Innovation Limited
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
from django.db import migrations


def update(apps, schema_editor):
    mappings = [
        (13, 0),
        (14, 0),
        (22, 0),
        (23, 0),
        (15, 0),
        (5, 1),
        (11, 1),
        (17, 1),
        (4, 1),
        (10, 1),
        (16, 1),
        (24, 1),
        (6, 2),
        (12, 2),
        (21, 2),
        (28, 2),
        (3, 3),
        (9, 3),
        (18, 3),
        (25, 3),
        (1, 4),
        (7, 4),
        (19, 4),
        (26, 4),
        (2, 4),
        (8, 4),
        (20, 4),
        (27, 4),
    ]
    for mapping in mappings:
        decor = apps.get_model("game", "Decor").objects.get(id=mapping[0])
        decor.z_index = mapping[1]
        decor.save()


class Migration(migrations.Migration):
    dependencies = [("game", "0045_decor_z_index")]

    operations = [migrations.RunPython(update)]
