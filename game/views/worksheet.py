from __future__ import absolute_import, division

from django.shortcuts import render

from game.models import Worksheet


def worksheet(request, worksheetId):
    """Loads a level for rendering in the game.

    **Context**

    ``RequestContext``
    ``level``
        Level that is about to be played. An instance of :model:`game.Level`.
    ``blocks``
        Blocks that are available during the game. List of :model:`game.Block`.
    ``lesson``
        Instruction shown at the load of the level. String from `game.messages`.
    ``hint``
        Hint shown after a number of failed attempts. String from `game.messages`.

    **Template:**

    :template:`game/game.html`
    """

    worksheet = Worksheet.objects.get(pk=worksheetId)

    return render(
        request, "game/python_den_worksheet.html", context={"worksheet": worksheet}
    )
