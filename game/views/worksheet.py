from __future__ import absolute_import, division

from django.shortcuts import render

from game import messages
from game.models import Worksheet
from .helper import renderError


def worksheet(request, worksheetId):
    if request.user.is_anonymous:
        return renderError(
            request,
            messages.no_permission_python_den_worksheet_title(),
            messages.no_permission_python_den_worksheet_page(),
        )

    worksheet = Worksheet.objects.get(pk=worksheetId)
    starter_code = messages.worksheet_starter_code()

    return render(
        request,
        "game/python_den_worksheet.html",
        context={"worksheet": worksheet, "starter_code": starter_code},
    )
