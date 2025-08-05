from __future__ import absolute_import, division

from django.shortcuts import render

from game.models import Worksheet


def worksheet(request, worksheetId):
    worksheet = Worksheet.objects.get(pk=worksheetId)

    return render(
        request, "game/python_den_worksheet.html", context={"worksheet": worksheet}
    )
