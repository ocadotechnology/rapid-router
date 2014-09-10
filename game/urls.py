from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^$', 'game.views.levels'),
    url(r'^submit$', 'game.views.submit_attempt'),
    url(r'^(?P<levelName>[A-Z0-9]+)$', 'game.views.play_default_level'),
    url(r'^custom/(?P<levelID>[0-9]+)$', 'game.views.play_custom_level'),
    url(r'^episode/(?P<episode>[0-9]+)$', 'game.views.start_episode'),
    url(r'^levels/random/([0-9]+)$', 'game.views.random_level_for_episode'),
    url(r'^logged_students$', 'game.views.logged_students'),
    url(r'^scoreboard$', 'game.views.scoreboard'),

    url(r'^workspace/load/(?P<workspaceID>[0-9]+)$', 'game.views.load_workspace'),
    url(r'^workspace/load_list$', 'game.views.load_list_of_workspaces'),
    url(r'^workspace/save$', 'game.views.save_workspace'),
    url(r'^workspace/save/(?P<workspaceID>[0-9]+)$', 'game.views.save_workspace'),
    url(r'^workspace/delete/(?P<workspaceID>[0-9]+)$', 'game.views.delete_workspace'),

    url(r'^level_moderation$', 'game.views.level_moderation'),
    url(r'^level_moderation/class/(?P<class_id>[0-9]+)$',
        'game.views.get_students_for_level_moderation'),
    url(r'^level_moderation/delete/(?P<levelID>[0-9]+)$', 'game.views.delete_level'),

    url(r'^level_editor$', 'game.views.level_editor'),
    url(r'^level_editor/level/play_anonymous/(?P<levelID>[0-9]+)$',
        'game.views.play_anonymous_level'),
    url(r'^level_editor/level/get_all$', 'game.views.get_loadable_levels_for_editor'),
    url(r'^level_editor/level/get/(?P<levelID>[0-9]+)$', 'game.views.load_level_for_editor'),
    url(r'^level_editor/level/delete/(?P<levelID>[0-9]+)$', 'game.views.delete_level_for_editor'),
    url(r'^level_editor/level/save$', 'game.views.save_level_for_editor'),
    url(r'^level_editor/level/save/(?P<levelID>[0-9]+)$', 'game.views.save_level_for_editor'),
    url(r'^level_editor/level/random/$', 'game.views.generate_random_map_for_editor'),
    url(r'^level_editor/level/get_sharing_information/(?P<levelID>[0-9]+)$',
        'game.views.get_sharing_information_for_editor'),
    url(r'^level_editor/level/share/(?P<levelID>[0-9]+)$', 'game.views.share_level_for_editor'),
)
