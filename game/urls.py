from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'game.views.levels'),
    url(r'^(?P<level>[0-9]+)$', 'game.views.level'),
    url(r'^level_editor$', 'game.views.level_editor'),
    url(r'^settings$', 'game.views.settings'),
    url(r'^logged_students$', 'game.views.logged_students'),
	url(r'^students_in_class$', 'game.views.students_in_class'),
)

