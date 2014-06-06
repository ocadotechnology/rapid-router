from django.core.exceptions import MiddlewareNotUsed
import os
import sys

# Some stuff taken from djangoappengine

class AppEngineMiddleware:
    def __init__(self):
        # inject everything app engine specific into the python path
        appengine_path = os.path.dirname(__file__)
        if appengine_path not in sys.path:
            sys.path.append(appengine_path)
        raise MiddlewareNotUsed
