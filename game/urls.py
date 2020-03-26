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
from django.conf.urls import url, include
from django.views.decorators.cache import cache_page
from django.views.i18n import javascript_catalog

from django_js_reverse.views import urls_js

from game.views.api import (
    level_list,
    level_detail,
    api_root,
    episode_list,
    episode_detail,
    levelblock_detail,
    block_detail,
    theme_detail,
    block_list,
    theme_list,
    character_list,
    character_detail,
    level_for_episode,
    levelblock_for_level,
    decor_list,
    decor_detail,
    map_for_level,
    leveldecor_detail,
    leveldecor_for_level,
    mode_for_level,
    map_list,
)
from game.views.level_editor import (
    level_editor,
    delete_level_for_editor,
    load_level_for_editor,
    save_level_for_editor,
    generate_random_map_for_editor,
    get_sharing_information_for_editor,
    share_level_for_editor,
    play_anonymous_level,
    owned_levels,
    shared_levels,
)
from game.views.level_moderation import (
    level_moderation,
    get_students_for_level_moderation,
)
from game.views.level_selection import levels, random_level_for_episode
from game.views.level import (
    submit_attempt,
    play_default_level,
    start_episode,
    load_workspace,
    load_list_of_workspaces,
    save_workspace,
    delete_workspace,
    delete_level,
    play_custom_level,
    play_custom_level_from_editor,
    load_workspace_solution,
)
from game.views.scoreboard import scoreboard

urlpatterns = [
    url(r"^$", levels, name="levels"),
    url(r"^submit/$", submit_attempt, name="submit_attempt"),
    url(r"^(?P<levelName>[A-Z0-9]+)/$", play_default_level, name="play_default_level"),
    url(r"^custom/(?P<levelId>[0-9]+)/$", play_custom_level, name="play_custom_level"),
    url(r"^episode/(?P<episodeId>[0-9]+)/$", start_episode, name="start_episode"),
    url(
        r"^levels/random/([0-9]+)/$",
        random_level_for_episode,
        name="random_level_for_episode",
    ),
    url(r"^scoreboard/$", scoreboard, name="scoreboard"),
    url(
        r"^workspace/",
        include(
            [
                url(
                    r"^load/(?P<workspaceID>[0-9]+)/$",
                    load_workspace,
                    name="load_workspace",
                ),
                url(
                    r"^load_list/$",
                    load_list_of_workspaces,
                    name="load_list_of_workspaces",
                ),
                url(r"^save/$", save_workspace, name="save_workspace"),
                url(
                    r"^save/(?P<workspaceID>[0-9]+)/$",
                    save_workspace,
                    name="save_workspace",
                ),
                url(
                    r"^delete/(?P<workspaceID>[0-9]+)/$",
                    delete_workspace,
                    name="delete_workspace",
                ),
                url(
                    r"^solution/(?P<levelName>[0-9]+)/$",
                    load_workspace_solution,
                    name="load_workspace_solution",
                ),
            ]
        ),
    ),
    url(
        r"^level_moderation/",
        include(
            [
                url(r"^$", level_moderation, name="level_moderation"),
                url(
                    r"^class/(?P<class_id>[0-9]+)/$",
                    get_students_for_level_moderation,
                    name="students_for_level_moderation",
                ),
                url(
                    r"^delete/(?P<levelID>[0-9]+)/$", delete_level, name="delete_level"
                ),
            ]
        ),
    ),
    url(
        r"^level_editor/",
        include(
            [
                url(r"^$", level_editor, name="level_editor"),
                url(
                    r"^play_anonymous/(?P<levelId>[0-9]+)/$",
                    play_anonymous_level,
                    name="play_anonymous_level",
                ),
                url(
                    r"^play_custom/(?P<levelId>[0-9]+)/$",
                    play_custom_level_from_editor,
                    name="play_custom_level_from_editor",
                ),
                url(
                    r"^get/(?P<levelID>[0-9]+)/$",
                    load_level_for_editor,
                    name="load_level_for_editor",
                ),
                url(
                    r"^delete/(?P<levelId>[0-9]+)/$",
                    delete_level_for_editor,
                    name="delete_level_for_editor",
                ),
                url(r"^save/$", save_level_for_editor, name="save_level_for_editor"),
                url(
                    r"^save/(?P<levelId>[0-9]+)/$",
                    save_level_for_editor,
                    name="save_level_for_editor",
                ),
                url(
                    r"^random/$",
                    generate_random_map_for_editor,
                    name="generate_random_map_for_editor",
                ),
                url(
                    r"^get_sharing_information/(?P<levelID>[0-9]+)/$",
                    get_sharing_information_for_editor,
                    name="get_sharing_information_for_editor",
                ),
                url(
                    r"^share/(?P<levelID>[0-9]+)/$",
                    share_level_for_editor,
                    name="share_level_for_editor",
                ),
                url(r"^levels/owned/$", owned_levels, name="owned_levels"),
                url(r"^levels/shared/$", shared_levels, name="shared_levels"),
            ]
        ),
    ),
    url(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    url(
        r"^api/",
        include(
            [
                url(r"^$", api_root),
                url(r"^blocks/$", block_list, name="block-list"),
                url(r"^blocks/(?P<pk>[0-9]+)/$", block_detail, name="block-detail"),
                url(r"^characters/$", character_list, name="character-list"),
                url(
                    r"^characters/(?P<pk>[0-9]+)/$",
                    character_detail,
                    name="character-detail",
                ),
                url(r"^decors/$", decor_list, name="decor-list"),
                url(r"^decors/(?P<pk>[0-9]+)/$", decor_detail, name="decor-detail"),
                url(r"^episodes/$", episode_list, name="episode-list"),
                url(
                    r"^episodes/(?P<pk>[0-9]+)/$", episode_detail, name="episode-detail"
                ),
                url(
                    r"^episodes/(?P<pk>[0-9]+)/levels/$",
                    level_for_episode,
                    name="level-for-episode",
                ),
                url(r"^levels/$", level_list, name="level-list"),
                url(r"^levels/(?P<pk>[0-9]+)/$", level_detail, name="level-detail"),
                url(
                    r"^levels/(?P<pk>[0-9]+)/blocks/$",
                    levelblock_for_level,
                    name="levelblock-for-level",
                ),
                url(
                    r"^levels/(?P<pk>[0-9]+)/decors/$",
                    leveldecor_for_level,
                    name="leveldecor-for-level",
                ),
                url(
                    r"^levels/(?P<pk>[0-9]+)/map/$", map_for_level, name="map-for-level"
                ),
                url(
                    r"^levels/(?P<pk>[0-9]+)/mode/$",
                    mode_for_level,
                    name="mode-for-level",
                ),
                url(
                    r"^levelblocks/(?P<pk>[0-9]+)/$",
                    levelblock_detail,
                    name="levelblock-detail",
                ),
                url(
                    r"^leveldecors/(?P<pk>[0-9]+)/$",
                    leveldecor_detail,
                    name="leveldecor-detail",
                ),
                url(r"^maps/$", map_list, name="map-list"),
                url(r"^themes/$", theme_list, name="theme-list"),
                url(r"^themes/(?P<pk>[0-9]+)/$", theme_detail, name="theme-detail"),
            ]
        ),
    ),
    url(r"^js-reverse/$", cache_page(60 * 60 * 24)(urls_js), name="js-reverse"),
    url(
        r"^js-i18n/$",
        cache_page(60 * 60 * 24)(javascript_catalog),
        {"packages": ("game",)},
        name="rapid-router/javascript-catalog",
    ),
]
