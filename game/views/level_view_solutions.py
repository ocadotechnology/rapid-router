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
from __future__ import division
import game.messages as messages
from django.template import RequestContext
from django.utils.safestring import mark_safe

from game.models import Episode
from django.core.cache import cache
from game import app_settings
from portal.permissions import logged_in_as_teacher
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render


@login_required(login_url=reverse_lazy('login_view'))
@user_passes_test(logged_in_as_teacher, login_url=reverse_lazy('login_view'))
def default_solution(request, levelName):
    if 80 <= int(levelName) <= 91:
        return render(request, 'game/teacher_solutionPY.html', {'levelName': levelName})
    else:
        return render(request, 'game/teacher_solution.html', {'levelName': levelName})


def fetch_episode_data_from_database(early_access):
    episode_data = []
    episode = Episode.objects.get(pk=1)
    while episode is not None:
        if episode.in_development and not early_access:
            break

        levels, minName, maxName = min_max_levels(episode.levels)

        e = {"id": episode.id,
             "name": episode.name,
             "levels": levels,
             "first_level": minName,
             "last_level": maxName,
             "random_levels_enabled": episode.r_random_levels_enabled}

        episode_data.append(e)
        episode = episode.next_episode
    return episode_data


def min_max_levels(episode_levels):
    levels = []
    minName = 1000
    maxName = 0

    for level in episode_levels:
        level_name = int(level.name)
        if level_name > maxName:
            maxName = level_name
        if level_name < minName:
            minName = level_name

        levels.append({
            "id": level.id,
            "name": level_name,
            "title": get_level_title(level_name)})

    return levels, minName, maxName


def fetch_episode_data(early_access):
    key = "episode_data"
    if early_access:
        key = "episode_data_early_access"
    data = cache.get(key)
    if data is None:
        data = fetch_episode_data_from_database(early_access)
        cache.set(key, data)
    return data


def get_level_title(i):
    title = 'title_level' + str(i)
    try:
        titleCall = getattr(messages, title)
        return mark_safe(titleCall())
    except AttributeError:
        return ""


@login_required(login_url=reverse_lazy('teach'))
@user_passes_test(logged_in_as_teacher, login_url=reverse_lazy('teach'))
def levels_solutions(request):
    """ Loads a page with all levels listed.

    **Context**

    ``RequestContext``
    ``episodes``

    **Template:**

    :template:`game/level_selection.html`
    """

    episode_data = fetch_episode_data(app_settings.EARLY_ACCESS_FUNCTION(request))

    context = RequestContext(request, {
        'episodeData': episode_data,
    })
    return render(request, 'game/teacher_level_solutions.html', context_instance=context)
