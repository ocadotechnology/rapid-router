from django.conf.urls import patterns, url
from views import WorkspaceViewList, WorkspaceViewDetail, LevelViewList, LevelViewDetail

urlpatterns = patterns('',
    url(r'^$', 'game.views.levels'),
    url(r'^submit$', 'game.views.submit'),
    url(r'^(?P<level>[0-9]+)$', 'game.views.level'),
    url(r'^episode/(?P<episode>[0-9]+)$', 'game.views.start_episode'),
    url(r'^level_editor$', 'game.views.level_editor'),
    url(r'^level_editor/random', 'game.views.level_editor_random'),
    url(r'^level_editor/level$', LevelViewList.as_view()),
    url(r'^level_editor/level/(?P<pk>[0-9]+)$', LevelViewDetail.as_view()),
    url(r'^levels/random/([0-9]+)$', 'game.views.random_level_for_episode'),
    url(r'^levels/new$', 'game.views.level_new'),
    url(r'^settings$', 'game.views.settings'),
    url(r'^logged_students$', 'game.views.logged_students'),
    url(r'^scoreboard$', 'game.views.scoreboard'),
    url(r'^workspace$', WorkspaceViewList.as_view()),
    url(r'^workspace/(?P<pk>[0-9]+)$', WorkspaceViewDetail.as_view()),
)