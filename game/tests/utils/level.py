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
from game.models import Level
import game.level_management as level_management


def create_save_level(teacher):
    data = {
        u"origin": u'{"coordinate":[3,5],"direction":"S"}',
        u"pythonEnabled": False,
        u"decor": [],
        u"blocklyEnabled": True,
        u"blocks": [
            {u"type": u"move_forwards"},
            {u"type": u"turn_left"},
            {u"type": u"turn_right"},
        ],
        u"max_fuel": u"50",
        u"pythonViewEnabled": False,
        u"character": u"3",
        u"name": u"abc",
        u"theme": 1,
        u"anonymous": False,
        u"cows": u"[]",
        u"path": u'[{"coordinate":[3,5],"connectedNodes":[1]},{"coordinate":[3,4],"connectedNodes":[0]}]',
        u"traffic_lights": u"[]",
        u"destinations": u"[[3,4]]",
    }
    level = Level(default=False, anonymous=data["anonymous"])
    level.owner = teacher.user.user.userprofile
    level_management.save_level(level, data)
    level.save()

    return level.id
