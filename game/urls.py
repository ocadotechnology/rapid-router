from django.conf.urls import patterns, url

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
)
