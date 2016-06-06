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
import game.level_management as level_management

from django.shortcuts import render
from django.template import RequestContext
from django.utils.safestring import mark_safe
from django.db.models import Max
from game import random_road
from game.cache import cached_episode
from game.models import Attempt, Episode
from level_editor import play_anonymous_level
from django.core.cache import cache
from game import app_settings


def max_score(level):
    score = 0
    if not level.disable_route_score:
        score = score + 10
    if level.model_solution != "[]":
        score = score + 10
    return score


def fetch_episode_data_from_database(early_access):
    episode_data = []
    episode = Episode.objects.get(pk=1)
    while episode is not None:
        if episode.in_development and not early_access:
            break

        levels = []
        minName = None
        maxName = None
        for level in episode.levels:
            level_name = int(level.name)
            if not maxName or level_name > maxName:
                maxName = level_name
            if not minName or level_name < minName:
                minName = level_name

            levels.append({
                "id": level.id,
                "name": level_name,
                "maxScore": max_score(level),
                "title": get_level_title(level_name)})

        e = {"id": episode.id,
             "name": episode.name,
             "levels": levels,
             "first_level": minName,
             "last_level": maxName,
             "random_levels_enabled": episode.r_random_levels_enabled}

        episode_data.append(e)
        episode = episode.next_episode
    return episode_data


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


def attach_attempts_to_level(attempts, level):
    level["score"] = attempts.get(level["id"])


def is_student(user):
    return hasattr(user.userprofile, 'student')


def levels(request):
    """ Loads a page with all levels listed.

    **Context**

    ``RequestContext``
    ``episodes``

    **Template:**

    :template:`game/level_selection.html`
    """
    user = request.user
    if user.is_authenticated() and is_student(user):
        best_attempts = Attempt.objects \
            .filter(student=user.userprofile.student) \
            .values("level_id") \
            .annotate(best_score=Max("score")) \
            .all()

        attempts = {a["level_id"]: a["best_score"] for a in best_attempts}
    else:
        attempts = {}

    def with_scores(level):
        attach_attempts_to_level(attempts, level)

    episode_data = fetch_episode_data(app_settings.EARLY_ACCESS_FUNCTION(request))
    for episode in episode_data:
        for level in episode["levels"]:
            with_scores(level)

    owned_level_data = []
    shared_level_data = []
    if not request.user.is_anonymous():
        owned_levels, shared_levels = level_management.get_loadable_levels(request.user)

        for level in owned_levels:
            owned_level_data.append({
                "id": level.id,
                "title": level.name,
                "score": attempts.get(level.id),
                "maxScore": 10
            })

        for level in shared_levels:
            shared_level_data.append({
                "id": level.id,
                "title": level.name,
                "owner": level.owner.user,
                "score": attempts.get(level.id),
                "maxScore": 10
            })

    context = RequestContext(request, {
        'episodeData': episode_data,
        'owned_levels': owned_level_data,
        'shared_levels': shared_level_data,
        'scores': attempts
    })
    return render(request, 'game/level_selection.html', context_instance=context)


def random_level_for_episode(request, episodeID):
    """ Generates a new random level based on the episodeID

    Redirects to :view:`game.views.play_level` with the id of the newly created :model:`game.Level`.
    """
    episode = cached_episode(episodeID)
    level = random_road.create(episode)
    return play_anonymous_level(request, level.id, False, random_level=True)
