from django.urls import include, path, re_path
from django.views.i18n import JavaScriptCatalog
from django_reverse_js.views import urls_js

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
from game.views.level_editor import (
    level_editor,
    delete_level_for_editor,
    load_level_for_editor,
    save_level_for_editor,
    generate_random_map_for_editor,
    SharingInformationForEditor,
    ShareLevelView,
    play_anonymous_level,
    owned_levels,
    shared_levels,
)
from game.views.level_moderation import level_moderation, approve_level
from game.views.level_selection import blockly_levels, random_level_for_episode
from game.views.scoreboard import blockly_scoreboard

urlpatterns = [
    re_path(r"^$", blockly_levels, name="levels"),
    re_path(r"^submit/$", submit_attempt, name="submit_attempt"),
    re_path(
        r"^(?P<level_name>[A-Z0-9]+)/$",
        play_default_level,
        name="play_default_level",
    ),
    re_path(
        r"^custom/(?P<levelId>[0-9]+)/$",
        play_custom_level,
        name="play_custom_level",
    ),
    re_path(
        r"^episode/(?P<episodeId>[0-9]+)/$", start_episode, name="start_episode"
    ),
    re_path(
        r"^levels/random/([0-9]+)/$",
        random_level_for_episode,
        name="random_level_for_episode",
    ),
    re_path(r"^scoreboard/$", blockly_scoreboard, name="scoreboard"),
    re_path(
        r"^workspace/",
        include(
            [
                re_path(
                    r"^load/(?P<workspaceID>[0-9]+)/$",
                    load_workspace,
                    name="load_workspace",
                ),
                re_path(
                    r"^load_list/$",
                    load_list_of_workspaces,
                    name="load_list_of_workspaces",
                ),
                re_path(r"^save/$", save_workspace, name="save_workspace"),
                re_path(
                    r"^save/(?P<workspaceID>[0-9]+)/$",
                    save_workspace,
                    name="save_workspace",
                ),
                re_path(
                    r"^delete/(?P<workspaceID>[0-9]+)/$",
                    delete_workspace,
                    name="delete_workspace",
                ),
                re_path(
                    r"^solution/(?P<level_name>[0-9]+)/$",
                    load_workspace_solution,
                    name="load_workspace_solution",
                ),
            ]
        ),
    ),
    re_path(
        r"^level_moderation/",
        include(
            [
                re_path(r"^$", level_moderation, name="level_moderation"),
                re_path(
                    r"^delete/(?P<levelID>[0-9]+)/$",
                    delete_level,
                    name="delete_level",
                ),
                re_path(
                    r"^approve/(?P<levelID>[0-9]+)/$",
                    approve_level,
                    name="approve_level",
                ),
            ]
        ),
    ),
    re_path(
        r"^level_editor/",
        include(
            [
                re_path(r"^$", level_editor, name="level_editor"),
                re_path(
                    r"^(?P<levelId>[0-9]+)/$",
                    level_editor,
                    name="level_editor_chosen_level",
                ),
                re_path(
                    r"^play_anonymous/(?P<levelId>[0-9]+)/$",
                    play_anonymous_level,
                    name="play_anonymous_level",
                ),
                re_path(
                    r"^play_custom/(?P<levelId>[0-9]+)/$",
                    play_custom_level_from_editor,
                    name="play_custom_level_from_editor",
                ),
                re_path(
                    r"^get/(?P<levelID>[0-9]+)/$",
                    load_level_for_editor,
                    name="load_level_for_editor",
                ),
                re_path(
                    r"^delete/(?P<levelId>[0-9]+)/$",
                    delete_level_for_editor,
                    name="delete_level_for_editor",
                ),
                re_path(
                    r"^save/$",
                    save_level_for_editor,
                    name="save_level_for_editor",
                ),
                re_path(
                    r"^save/(?P<levelId>[0-9]+)/$",
                    save_level_for_editor,
                    name="save_level_for_editor",
                ),
                re_path(
                    r"^random/$",
                    generate_random_map_for_editor,
                    name="generate_random_map_for_editor",
                ),
                re_path(
                    r"^get_sharing_information/(?P<levelID>[0-9]+)/$",
                    SharingInformationForEditor.as_view(),
                    name="get_sharing_information_for_editor",
                ),
                re_path(
                    r"^share/(?P<levelID>[0-9]+)/$",
                    ShareLevelView.as_view(),
                    name="share_level_for_editor",
                ),
                re_path(r"^levels/owned/$", owned_levels, name="owned_levels"),
                re_path(
                    r"^levels/shared/$", shared_levels, name="shared_levels"
                ),
            ]
        ),
    ),
    re_path(
        r"^api-auth/",
        include("rest_framework.urls", namespace="rest_framework"),
    ),
    re_path(
        r"^api/",
        include(
            [
                re_path(r"^$", api_root),
                re_path(r"^blocks/$", block_list, name="block-list"),
                re_path(
                    r"^blocks/(?P<pk>[0-9]+)/$",
                    block_detail,
                    name="block-detail",
                ),
                re_path(
                    r"^characters/$", character_list, name="character-list"
                ),
                re_path(
                    r"^characters/(?P<pk>[0-9]+)/$",
                    character_detail,
                    name="character-detail",
                ),
                re_path(r"^decors/$", decor_list, name="decor-list"),
                re_path(
                    r"^decors/(?P<pk>[0-9]+)/$",
                    decor_detail,
                    name="decor-detail",
                ),
                re_path(r"^episodes/$", episode_list, name="episode-list"),
                re_path(
                    r"^episodes/(?P<pk>[0-9]+)/$",
                    episode_detail,
                    name="episode-detail",
                ),
                re_path(
                    r"^episodes/(?P<pk>[0-9]+)/levels/$",
                    level_for_episode,
                    name="level-for-episode",
                ),
                re_path(r"^levels/$", level_list, name="level-list"),
                re_path(
                    r"^levels/(?P<pk>[0-9]+)/$",
                    level_detail,
                    name="level-detail",
                ),
                re_path(
                    r"^levels/(?P<pk>[0-9]+)/blocks/$",
                    levelblock_for_level,
                    name="levelblock-for-level",
                ),
                re_path(
                    r"^levels/(?P<pk>[0-9]+)/decors/$",
                    leveldecor_for_level,
                    name="leveldecor-for-level",
                ),
                re_path(
                    r"^levels/(?P<pk>[0-9]+)/map/$",
                    map_for_level,
                    name="map-for-level",
                ),
                re_path(
                    r"^levels/(?P<pk>[0-9]+)/mode/$",
                    mode_for_level,
                    name="mode-for-level",
                ),
                re_path(
                    r"^levelblocks/(?P<pk>[0-9]+)/$",
                    levelblock_detail,
                    name="levelblock-detail",
                ),
                re_path(
                    r"^leveldecors/(?P<pk>[0-9]+)/$",
                    leveldecor_detail,
                    name="leveldecor-detail",
                ),
                re_path(r"^maps/$", map_list, name="map-list"),
                re_path(r"^themes/$", theme_list, name="theme-list"),
                re_path(
                    r"^themes/(?P<pk>[0-9]+)/$",
                    theme_detail,
                    name="theme-detail",
                ),
            ]
        ),
    ),
    path("reverse.js", urls_js, name="js-reverse"),
    re_path(
        r"^js-i18n/$",
        JavaScriptCatalog.as_view(packages=["game"]),
        name="rapid-router/javascript-catalog",
    ),
]
