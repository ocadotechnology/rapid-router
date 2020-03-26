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
        (u"1", 1),
        (u"2", 1),
        (u"3", 1),
        (u"4", 1),
        (u"5", 1),
        (u"6", 1),
        (u"7", 1),
        (u"8", 1),
        (u"9", 1),
        (u"10", 1),
        (u"11", 1),
        (u"12", 1),
        (u"13", 2),
        (u"14", 2),
        (u"15", 2),
        (u"16", 2),
        (u"17", 2),
        (u"18", 2),
        (u"19", 3),
        (u"20", 3),
        (u"21", 3),
        (u"22", 3),
        (u"23", 3),
        (u"24", 3),
        (u"25", 3),
        (u"26", 3),
        (u"27", 3),
        (u"28", 3),
        (u"29", 4),
        (u"30", 4),
        (u"31", 4),
        (u"32", 4),
        (u"33", 5),
        (u"34", 5),
        (u"35", 5),
        (u"36", 5),
        (u"37", 5),
        (u"38", 5),
        (u"39", 5),
        (u"40", 5),
        (u"41", 5),
        (u"42", 5),
        (u"43", 5),
        (u"44", 6),
        (u"45", 6),
        (u"46", 6),
        (u"47", 6),
        (u"48", 6),
        (u"49", 6),
        (u"50", 6),
        (u"62", 7),
        (u"51", 8),
        (u"59", 8),
        (u"60", 8),
        (u"68", 9),
        (u"69", 9),
        (u"70", 9),
        (u"71", 9),
        (u"63", 7),
        (u"67", 7),
        (u"65", 7),
        (u"81", 10),
        (u"82", 10),
        (u"83", 10),
        (u"85", 10),
        (u"86", 10),
        (u"87", 10),
        (u"89", 10),
        (u"93", 11),
        (u"94", 11),
        (u"96", 11),
        (u"95", 11),
        (u"98", 11),
        (u"99", 11),
        (u"52", 8),
        (u"53", 8),
        (u"54", 8),
        (u"55", 8),
        (u"56", 8),
        (u"57", 8),
        (u"58", 8),
        (u"61", 7),
        (u"64", 7),
        (u"66", 7),
        (u"72", 9),
        (u"75", 9),
        (u"74", 9),
        (u"73", 9),
        (u"79", 9),
        (u"80", 10),
        (u"84", 10),
        (u"88", 10),
        (u"90", 10),
        (u"91", 10),
        (u"92", 11),
        (u"97", 11),
        (u"100", 11),
        (u"101", 11),
        (u"102", 11),
        (u"103", 11),
        (u"104", 11),
        (u"105", 11),
        (u"106", 11),
        (u"107", 11),
        (u"108", 11),
        (u"109", 11),
        (u"76", 9),
        (u"77", 9),
        (u"78", 9),
    ]
    for mapping in mappings:
        level = apps.get_model("game", "Level").objects.get(
            name=mapping[0], default=True
        )
        level.episode = apps.get_model("game", "Episode").objects.get(pk=mapping[1])
        level.save()


class Migration(migrations.Migration):
    dependencies = [("game", "0040_auto_20150128_2019")]

    operations = [migrations.RunPython(update)]
