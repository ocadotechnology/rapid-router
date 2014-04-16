from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'game.views.game'),
    url(r'^logged_students$', 'game.views.logged_students'),
	url(r'^students_in_class$', 'game.views.students_in_class'),
    url(r'^submit_commands$', 'game.views.submit_commands'),
    url(r'^submit_reply$', 'game.views.submit_reply',),
)

