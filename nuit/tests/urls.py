'''Test URLs'''
from django.conf.urls import patterns

urlpatterns = patterns('',
    (r'^error400/$', 'nuit.handlers.handler400'),
    (r'^error403/$', 'nuit.handlers.handler403'),
    (r'^error404/$', 'nuit.handlers.handler404'),
    (r'^error500/$', 'nuit.handlers.handler500'),
)
