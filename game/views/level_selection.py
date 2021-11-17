from __future__ import division
from __future__ import absolute_import

from builtins import str
from django.core.cache import cache
from django.db.models import Max
from django.shortcuts import render
from django.utils.safestring import mark_safe

import game.level_management as level_management
import game.messages as messages
from game import app_settings
from game import random_road
from game.cache import cached_episode
from game.models import Attempt, Episode
from .level_editor import play_anonymous_level


def max_score(level):
    score = 0
    if not level.disable_route_score:
        score = score + 10
    if level.model_solution != "[]":
        score = score + 10
    return score


def fetch_episode_data_from_database(early_access, start, end):
    episode_data = []
    episode = Episode.objects.get(pk=start)
    current = start
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

            levels.append(
                {
                    "id": level.id,
                    "name": level_name,
                    "maxScore": max_score(level),
                    "title": get_level_title(level_name),
                }
            )

        e = {
            "id": episode.id,
            "levels": levels,
            "first_level": minName,
            "last_level": maxName,
            "random_levels_enabled": episode.r_random_levels_enabled,
        }

        episode_data.append(e)
        episode = episode.next_episode

        current += 1
        if current > end:
            break

    return episode_data


def fetch_episode_data(early_access, start=1, end=12):
    key = f"episode_data_{start}_{end}"
    if early_access:
        key = f"episode_data_early_access_{start}_{end}"

    data = cache.get(key)
    if data is None:
        data = fetch_episode_data_from_database(early_access, start, end)
        cache.set(key, data)
    return [
        dict(
            episode,
            name=messages.get_episode_title(episode["id"]),
            levels=[
                dict(level, title=get_level_title(level["name"]))
                for level in episode["levels"]
            ],
        )
        for episode in data
    ]


def get_level_title(i):
    title = "title_level" + str(i)
    try:
        titleCall = getattr(messages, title)
        return mark_safe(titleCall())
    except AttributeError:
        return ""


def attach_attempts_to_level(attempts, level):
    level["score"] = attempts.get(level["id"])


def is_student(user):
    return hasattr(user.userprofile, "student")


def levels(request):
    """Loads a page with all levels listed.

    **Context**

    ``RequestContext``
    ``episodes``

    **Template:**

    :template:`game/level_selection.html`
    """
    user = request.user
    if user.is_authenticated and is_student(user):
        best_attempts = (
            Attempt.objects.filter(student=user.userprofile.student)
            .values("level_id")
            .annotate(best_score=Max("score"))
            .all()
        )

        attempts = {a["level_id"]: a["best_score"] for a in best_attempts}
    else:
        attempts = {}

    blockly_episodes = fetch_episode_data(
        app_settings.EARLY_ACCESS_FUNCTION(request), 1, 9
    )
    for episode in blockly_episodes:
        for level in episode["levels"]:
            attach_attempts_to_level(attempts, level)

    python_episodes = fetch_episode_data(
        app_settings.EARLY_ACCESS_FUNCTION(request), 10, 11
    )
    for episode in python_episodes:
        for level in episode["levels"]:
            attach_attempts_to_level(attempts, level)

    owned_level_data = []
    shared_level_data = []
    if not request.user.is_anonymous:
        owned_levels, shared_levels = level_management.get_loadable_levels(request.user)

        for level in owned_levels:
            owned_level_data.append(
                {
                    "id": level.id,
                    "title": level.name,
                    "score": attempts.get(level.id),
                    "maxScore": 10,
                }
            )

        for level in shared_levels:
            shared_level_data.append(
                {
                    "id": level.id,
                    "title": level.name,
                    "owner": level.owner.user,
                    "score": attempts.get(level.id),
                    "maxScore": 10,
                }
            )

    return render(
        request,
        "game/level_selection.html",
        context={
            "blocklyEpisodes": blockly_episodes,
            "pythonEpisodes": python_episodes,
            "owned_levels": owned_level_data,
            "shared_levels": shared_level_data,
            "scores": attempts,
        },
    )


def random_level_for_episode(request, episodeID):
    """Generates a new random level based on the episodeID

    Redirects to :view:`game.views.play_level` with the id of the newly created :model:`game.Level`.
    """
    episode = cached_episode(episodeID)
    level = random_road.create(episode)
    return play_anonymous_level(request, level.id, False, random_level=True)
