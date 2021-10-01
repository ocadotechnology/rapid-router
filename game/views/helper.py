from __future__ import division

from django.shortcuts import render


def renderError(request, title, message):
    """Renders an error page with passed title and message.

    **Context**

    ``RequestContext``
    ``title``
        Title that is to be used as a title and header of the page. String.
    ``message``
        Message that will be shown on the error page. String.

    **Template:**

    :template:`game/error.html`
    """
    return render(
        request, "game/error.html", context={"title": title, "message": message}
    )
