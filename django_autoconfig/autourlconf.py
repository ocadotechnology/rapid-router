'''This module can be set as a ROOT_URLCONF (or included into one).'''

from django.conf import settings
from django.conf.urls import include, patterns, url

urlpatterns = patterns('')

for app_name in settings.INSTALLED_APPS:
    try:
        urlpatterns += patterns(
            '',
            url(
                r'^%s/' % app_name.replace("_","-"),
                include("%s.urls" % app_name),
            ),
        )
    except ImportError:
        pass
