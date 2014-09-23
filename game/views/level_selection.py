from __future__ import division
import game.messages as messages
import game.level_management as level_management

from django.shortcuts import render
from django.template import RequestContext
from django.utils.safestring import mark_safe
from game import random_road
from game.cache import cached_episode
from game.models import Attempt, Episode
from level_editor import play_anonymous_level


def levels(request):
    """ Loads a page with all levels listed.

    **Context**

    ``RequestContext``
    ``episodes``

    **Template:**

    :template:`game/level_selection.html`
    """
    def get_level_title(i):
        title = 'title_level' + str(i)
        try:
            titleCall = getattr(messages, title)
            return mark_safe(titleCall())
        except AttributeError:
            return ""

    def get_attempt_score(level):
        user = request.user
        if not user.is_anonymous() and hasattr(user.userprofile, 'student'):
            student = user.userprofile.student
            attempt = Attempt.objects.filter(level=level, student=student).first()

            if attempt:
                return attempt.score

    developer = (not request.user.is_anonymous()) and request.user.userprofile.developer
    episode_data = []
    episode = Episode.objects.get(pk=1)
    while episode is not None:
        if episode.in_development and not developer:
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
                "title": get_level_title(level_name),
                "score": get_attempt_score(level)})

        e = {"id": episode.id,
             "name": episode.name,
             "levels": levels,
             "first_level": minName,
             "last_level": maxName,
             "random_levels_enabled": episode.r_random_levels_enabled}

        episode_data.append(e)
        episode = episode.next_episode

    owned_level_data = []
    shared_level_data = []
    if not request.user.is_anonymous():
        owned_levels, shared_levels = level_management.get_list_of_loadable_levels(request.user)

        for level in owned_levels:
            owned_level_data.append({
                "id": level.id,
                "title": level.name,
                "score": get_attempt_score(level)
            })

        for level in shared_levels:
            shared_level_data.append({
                "id": level.id,
                "title": level.name,
                "owner": level.owner.user,
                "score": get_attempt_score(level)
            })

    context = RequestContext(request, {
        'episodeData': episode_data,
        'owned_levels': owned_level_data,
        'shared_levels': shared_level_data,
    })
    return render(request, 'game/level_selection.html', context_instance=context)


def random_level_for_episode(request, episodeID):
    """ Generates a new random level based on the episodeID

    Redirects to :view:`game.views.play_level` with the id of the newly created :model:`game.Level`.
    """
    episode = cached_episode(episodeID)
    level = random_road.create(episode)
    return play_anonymous_level(request, level.id, False)
