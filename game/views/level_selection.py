from __future__ import absolute_import, division

from builtins import str

import game.level_management as level_management
import game.messages as messages
from django.core.cache import cache
from django.db.models import Max
from django.shortcuts import render
from django.utils.safestring import mark_safe
from game import app_settings, random_road
from game.cache import cached_episode
from game.models import Attempt, Episode, Level, Worksheet

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
            "difficulty": episode.difficulty,
        }

        episode_data.append(e)

        if episode.id == end:
            break

        episode = episode.next_episode

    return episode_data


def fetch_episode_data(early_access, start=1, end=12):
    key = f"episode_data_{start}_{end}"
    if early_access:
        key = f"episode_data_early_access_{start}_{end}"

    data = cache.get(key)
    if data is None:
        data = fetch_episode_data_from_database(early_access, start, end)
        cache.set(key, data)

    def worksheet_to_dict(index, worksheet):
        return {
            "id": worksheet.id,
            "index": index,
            "before_level": worksheet.before_level_id,
            "lesson_plan_link": worksheet.lesson_plan_link,
            "slides_link": worksheet.slides_link,
            "student_worksheet_link": worksheet.student_worksheet_link,
            "indy_worksheet_link": worksheet.indy_worksheet_link,
            "video_link": worksheet.video_link,
        }

    episodes = []
    for episode in data:
        worksheets = [
            worksheet_to_dict(index, worksheet)
            for index, worksheet in enumerate(
                Worksheet.objects.filter(
                    episode=episode["id"],
                    before_level__isnull=False,
                ).order_by("before_level"),
                start=1,
            )
        ]
        
        worksheets += [
            worksheet_to_dict(index, worksheet)
            for index, worksheet in enumerate(
                Worksheet.objects.filter(
                    episode=episode["id"],
                    before_level__isnull=True,
                ),
                start=1 + len(worksheets),
            )
        ]
        
        episodes.append(
            dict(
                episode,
                name=messages.get_episode_title(episode["id"]),
                levels=[
                    dict(level, title=get_level_title(level["name"]))
                    for level in episode["levels"]
                ],
                worksheets=worksheets,
            )
        )
    
    return episodes


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


def is_teacher(user):
    return hasattr(user.userprofile, "teacher")


def is_admin_teacher(user):
    return (
        hasattr(user.userprofile, "teacher")
        and user.userprofile.teacher.is_admin
    )


def get_blockly_episodes(request):
    return fetch_episode_data(app_settings.EARLY_ACCESS_FUNCTION(request), 1, 9)


def get_python_episodes(request):
    return fetch_episode_data(
        app_settings.EARLY_ACCESS_FUNCTION(request), 16, 24
    )


def levels(request, language):
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

    owned_level_data = []
    directly_shared_levels = []
    indirectly_shared_levels = {}
    if not request.user.is_anonymous:
        owned_levels, shared_levels = level_management.get_loadable_levels(
            request.user
        )

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
            # if user is an admin teacher, sort levels by their own classes first (directly shared levels) and then by
            # other classes in the school (indirectly shared levels). For each of those, get the levels owned by a
            # teacher as well as those owned by a student.
            if is_admin_teacher(user):
                # get levels shared by fellow teachers
                if is_teacher(level.owner.user):
                    teacher = level.owner.teacher.new_user

                    if teacher not in indirectly_shared_levels:
                        indirectly_shared_levels[teacher] = []

                    indirectly_shared_levels[teacher].append(
                        get_shared_level(level, attempts)
                    )
                else:
                    student_class = level.owner.student.class_field
                    class_teacher = student_class.teacher.new_user

                    # get levels shared by students in the current user's classes
                    if class_teacher == user:
                        directly_shared_levels.append(
                            get_shared_level(level, attempts, student_class)
                        )
                    # get levels shared by students in the other teachers' classes
                    else:
                        if class_teacher not in indirectly_shared_levels:
                            indirectly_shared_levels[class_teacher] = []

                        indirectly_shared_levels[class_teacher].append(
                            get_shared_level(level, attempts, student_class)
                        )
            # if user is a student or a standard teacher, just get levels shared with them directly.
            else:
                directly_shared_levels.append(get_shared_level(level, attempts))

    context = {
        "owned_levels": owned_level_data,
        "directly_shared_levels": directly_shared_levels,
        "indirectly_shared_levels": indirectly_shared_levels,
        "scores": attempts,
    }

    if language == "blockly":
        blockly_episodes = get_blockly_episodes(request)

        for episode in blockly_episodes:
            for level in episode["levels"]:
                attach_attempts_to_level(attempts, level)
                level["locked_for_class"] = Level.objects.get(
                    id=level["id"]
                ).locked_for_class

        context["blocklyEpisodes"] = blockly_episodes

    elif language == "python":
        python_episodes = get_python_episodes(request)

        for episode in python_episodes:
            for level in episode["levels"]:
                attach_attempts_to_level(attempts, level)
                level["locked_for_class"] = Level.objects.get(
                    id=level["id"]
                ).locked_for_class

            for worksheet in episode["worksheets"]:
                worksheet["locked_classes"] = Worksheet.objects.get(
                    id=worksheet["id"]
                ).locked_classes

        context["pythonEpisodes"] = python_episodes

    return context


def blockly_levels(request):
    return render(
        request, "game/level_selection.html", context=levels(request, "blockly")
    )


def python_levels(request):
    return render(
        request,
        "game/python_den_level_selection.html",
        context=levels(request, "python"),
    )


def get_shared_level(level, attempts, student_class=None):
    return {
        "id": level.id,
        "title": level.name,
        "owner": level.owner.user,
        "class": student_class,
        "score": attempts.get(level.id),
        "maxScore": 10,
    }


def random_level_for_episode(request, episodeID):
    """Generates a new random level based on the episodeID

    Redirects to :view:`game.views.play_level` with the id of the newly created :model:`game.Level`.
    """
    episode = cached_episode(episodeID)
    level = random_road.create(episode)
    return play_anonymous_level(request, level.id, False, random_level=True)
