import django.core.handlers.wsgi
import django

django.setup()

application = django.core.handlers.wsgi.WSGIHandler()
