"""CSP config"""

from common.app_settings import domain

CSP_CONFIG = {
    "CSP_DEFAULT_SRC": ("'self'",),
    "CSP_IMG_SRC": (
        f"{domain()}/static/game/image/",
        f"{domain()}/static/game/raphael_image/",
        f"{domain()}/static/game/js/blockly/media/",
        f"{domain()}/static/icons/",
    ),
    "CSP_SCRIPT_SRC": ("'unsafe-eval'",),
    "CSP_FRAME_SRC": (
        f"{domain()}/static/game/image/",
    ),
    "CSP_OBJECT_SRC": (f"{domain()}/static/game/image/",),
}
