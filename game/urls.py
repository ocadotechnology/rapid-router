from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'game.views.levels'),
    url(r'^submit$', 'game.views.submit'),
    url(r'^(?P<level>[0-9]+)$', 'game.views.level'),
    url(r'^episode/(?P<episode>[0-9]+)$', 'game.views.start_episode'),
    url(r'^level_editor$', 'game.views.level_editor'),
    url(r'^levels/random$', 'game.views.level_random'),
    url(r'^levels/new$', 'game.views.level_new'),
    url(r'^settings$', 'game.views.settings'),
    url(r'^logged_students$', 'game.views.logged_students'),
    url(r'^students_in_class$', 'game.views.students_in_class'),
)
