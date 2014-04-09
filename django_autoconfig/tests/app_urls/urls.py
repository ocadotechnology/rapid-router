from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^index/$', 'django_autoconfig.tests.app_urls.views.index'),
)