"""CSP config"""

from common.app_settings import domain

CSP_CONFIG = {
    "CSP_DEFAULT_SRC": ("'self'",),
    "CSP_IMG_SRC": (
        f"{domain()}/static/game/image/",
        f"{domain()}/static/game/raphael_image/",
        f"{domain()}/static/game/js/blockly/media/",
        f"{domain()}/static/icons/",
        "https://cdn.crowdin.com/",
        "https://crowdin-static.downloads.crowdin.com/"
    ),
    "CSP_STYLE_SRC": ("https://code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css", "https://cdn.crowdin.com/"),
    "CSP_SCRIPT_SRC": ("'unsafe-eval'", "https://cdn.crowdin.com/"),
    "CSP_FRAME_SRC": (
        f"{domain()}/static/game/image/",
        "https://crowdin.com/"
    ),
    "CSP_OBJECT_SRC": (f"{domain()}/static/game/image/",),
    "CSP_CONNECT_SRC": ("https://crowdin.com/",)
}
