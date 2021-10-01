from django.conf import settings
from django.utils.module_loading import import_string

NIGHT_MODE_FEATURE_ENABLED = getattr(settings, "NIGHT_MODE_FEATURE_ENABLED", False)

COW_FEATURE_ENABLED = getattr(settings, "COW_FEATURE_ENABLED", False)

#: Name of a function that determines if a request qualifies for early access
EARLY_ACCESS_FUNCTION_NAME = getattr(
    settings, "RAPID_ROUTER_EARLY_ACCESS_FUNCTION_NAME", ""
)


def default_early_access_function(request):
    """Determine if this request qualifies for early access."""
    if EARLY_ACCESS_FUNCTION_NAME:
        func = import_string(EARLY_ACCESS_FUNCTION_NAME)
        return func(request)
    else:
        return True


#: Function that determines if a request qualifies for early access
EARLY_ACCESS_FUNCTION = getattr(
    settings, "RAPID_ROUTER_EARLY_ACCESS_FUNCTION", default_early_access_function
)
