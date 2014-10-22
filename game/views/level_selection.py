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

def levels(request):
    """ Loads a page with all levels listed.

    **Context**

    ``RequestContext``
    ``episodes``

    **Template:**

    :template:`game/level_selection.html`
    """
    user = request.user
    if not user.is_anonymous() and hasattr(user.userprofile, 'student'):
        attempts = {a["level_id"]: a["best_score"] for a in \
                Attempt.objects.filter(student=user.userprofile.student).values("level_id").annotate(best_score=Max("score")).all()}
    else:
        attempts = {}

    def with_scores(level):
        attach_attempts_to_level(attempts, level)

    beta_mode = (not request.user.is_anonymous()) and request.get_host().startswith("beta")
    developer = (not request.user.is_anonymous()) and request.user.userprofile.developer
    early_access = developer or beta_mode
    episode_data = fetch_episode_data(early_access)
    for e in episode_data:
        for l in e["levels"]:
            with_scores(l)

    owned_level_data = []
    shared_level_data = []
    if not request.user.is_anonymous():
        owned_levels, shared_levels = level_management.get_list_of_loadable_levels(request.user)

        for level in owned_levels:
            owned_level_data.append({
                "id": level.id,
                "title": level.name,
                "score": attempts.get(level.id)
            })

        for level in shared_levels:
            shared_level_data.append({
                "id": level.id,
                "title": level.name,
                "owner": level.owner.user,
                "score": attempts.get(level.id)
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
    return play_anonymous_level(request, level.id, False)
