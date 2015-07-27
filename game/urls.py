from django.conf.urls import patterns, url, include
from game.views.api import level_list, level_detail, api_root, episode_list, episode_detail, levelblock_detail, \
    block_detail, theme_detail, block_list, theme_list, character_list, character_detail, level_for_episode, \
    levelblock_for_level, decor_list, decor_detail, map_for_level, leveldecor_detail, leveldecor_for_level, \
    mode_for_level, map_list

from game.views.level_editor import level_editor, get_loadable_levels_for_editor, \
    delete_level_for_editor, load_level_for_editor, save_level_for_editor, play_anonymous_level, \
    generate_random_map_for_editor, get_sharing_information_for_editor, share_level_for_editor

from game.views.level_moderation import level_moderation, get_students_for_level_moderation

from game.views.level_selection import levels, random_level_for_episode

from game.views.level import submit_attempt, play_default_level, play_custom_level, \
    start_episode, load_workspace, load_list_of_workspaces, save_workspace, delete_workspace, \
    delete_level


from game.views.scoreboard import scoreboard

urlpatterns = patterns(
    '',
    url(r'^$', levels, name='levels'),
    url(r'^submit/$', submit_attempt, name='submit_attempt'),
    url(r'^(?P<levelName>[A-Z0-9]+)/$', play_default_level, name='play_default_level'),
    url(r'^custom/(?P<levelID>[0-9]+)/$', play_custom_level, name='play_custom_level'),
    url(r'^episode/(?P<episode>[0-9]+)/$', start_episode, name='start_episode'),
    url(r'^levels/random/([0-9]+)/$', random_level_for_episode, name='random_level_for_episode'),
    url(r'^scoreboard/$', scoreboard, name='scoreboard'),

    url(r'^workspace/load/(?P<workspaceID>[0-9]+)/$', load_workspace, name='load_workspace'),
    url(r'^workspace/load_list/$', load_list_of_workspaces, name='load_list_of_workspaces'),
    url(r'^workspace/save/$', save_workspace, name='save_workspace'),
    url(r'^workspace/save/(?P<workspaceID>[0-9]+)/$', save_workspace, name='save_workspace'),
    url(r'^workspace/delete/(?P<workspaceID>[0-9]+)/$', delete_workspace, name='delete_workspace'),

    url(r'^level_moderation/$', level_moderation, name='level_moderation'),
    url(r'^level_moderation/class/(?P<class_id>[0-9]+)/$',
        get_students_for_level_moderation, name='get_students_for_level_moderation'),
    url(r'^level_moderation/delete/(?P<levelID>[0-9]+)/$', delete_level, name='delete_level'),

    url(r'^level_editor/$', level_editor, name='level_editor'),
    url(r'^level_editor/level/play_anonymous/(?P<levelID>[0-9]+)/$',
        play_anonymous_level, name='play_anonymous_level'),
    url(r'^level_editor/level/get_all/$',
        get_loadable_levels_for_editor, name='get_loadable_levels_for_editor'),
    url(r'^level_editor/level/get/(?P<levelID>[0-9]+)/$',
        load_level_for_editor, name='load_level_for_editor'),
    url(r'^level_editor/level/delete/(?P<levelID>[0-9]+)/$',
        delete_level_for_editor, name='delete_level_for_editor'),
    url(r'^level_editor/level/save/$', 'game.views.level_editor.save_level_for_editor'),
    url(r'^level_editor/level/save/(?P<levelID>[0-9]+)/$',
        save_level_for_editor, name='save_level_for_editor'),
    url(r'^level_editor/level/random/$',
        generate_random_map_for_editor, name='generate_random_map_for_editor'),
    url(r'^level_editor/level/get_sharing_information/(?P<levelID>[0-9]+)/$',
        get_sharing_information_for_editor, name='get_sharing_information_for_editor'),
    url(r'^level_editor/level/share/(?P<levelID>[0-9]+)/$',
        share_level_for_editor, name='share_level_for_editor'),

    # Routing for api related urls
    url(r'^api/$', api_root),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/blocks/$', block_list, name='block-list'),
    url(r'^api/blocks/(?P<pk>[0-9]+)/$', block_detail, name='block-detail'),
    url(r'^api/characters/$', character_list, name='character-list'),
    url(r'^api/characters/(?P<pk>[0-9]+)/$', character_detail, name='character-detail'),
    url(r'^api/decors/$', decor_list, name='decor-list'),
    url(r'^api/decors/(?P<pk>[0-9]+)/$', decor_detail, name='decor-detail'),
    url(r'^api/episodes/$', episode_list, name='episode-list'),
    url(r'^api/episodes/(?P<pk>[0-9]+)/$', episode_detail, name='episode-detail'),
    url(r'^api/episodes/(?P<pk>[0-9]+)/levels/$', level_for_episode, name='level-for-episode'),
    url(r'^api/levels/$', level_list, name='level-list'),
    url(r'^api/levels/(?P<pk>[0-9]+)/$', level_detail, name='level-detail'),
    url(r'^api/levels/(?P<pk>[0-9]+)/blocks/$', levelblock_for_level, name='levelblock-for-level'),
    url(r'^api/levels/(?P<pk>[0-9]+)/decors/$', leveldecor_for_level, name='leveldecor-for-level'),
    url(r'^api/levels/(?P<pk>[0-9]+)/map/$', map_for_level, name='map-for-level'),
    url(r'^api/levels/(?P<pk>[0-9]+)/mode/$', mode_for_level, name='mode-for-level'),
    url(r'^api/levelblocks/(?P<pk>[0-9]+)/$', levelblock_detail, name='levelblock-detail'),
    url(r'^api/leveldecors/(?P<pk>[0-9]+)/$', leveldecor_detail, name='leveldecor-detail'),
    url(r'^api/maps/$', map_list, name='map-list'),
    url(r'^api/themes/$', theme_list, name='theme-list'),
    url(r'^api/themes/(?P<pk>[0-9]+)/$', theme_detail, name='theme-detail'),

)
