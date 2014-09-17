from __future__ import division

import os

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.template import RequestContext
from game.forms import AvatarUploadForm, AvatarPreUploadedForm
from game.models import Decor


def renderError(request, title, message):
    """ Renders an error page with passed title and message.

    **Context**

    ``RequestContext``
    ``title``
        Title that is to be used as a title and header of the page. String.
    ``message``
        Message that will be shown on the error page. String.

    **Template:**

    :template:`game/error.html`
    """
    context = RequestContext(request, {
        'title': title,
        'message': message
    })
    return render(request, 'game/error.html', context_instance=context)


def getDecorElement(name, theme):
    """ Helper method to get a decor element corresponding to the theme or a default one."""
    try:
        return Decor.objects.get(name=name, theme=theme)
    except ObjectDoesNotExist:
        return Decor.objects.filter(name=name)[0]


def renderAvatarChoice(request):
    """ Helper method for settings view. Generates and processes the avatar changing forms.
    """
    x = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(x, 'portal/static/portal/img/avatars')
    img_list = os.listdir(path)
    userProfile = request.user.userprofile
    avatar = userProfile.avatar
    avatarUploadForm = AvatarUploadForm(request.POST or None, request.FILES)
    avatarPreUploadedForm = AvatarPreUploadedForm(request.POST or None, my_choices=img_list)
    if request.method == 'POST':
        if "pre-uploaded" in request.POST and avatarPreUploadedForm.is_valid:
            avatar = avatarPreUploadedForm.data.get('pre-uploaded', False)
        elif "user-uploaded" in request.POST and avatarUploadForm.is_valid():
            avatar = request.FILES.get('avatar', False)
        userProfile.avatar = avatar
        userProfile.save()
    return avatarUploadForm, avatarPreUploadedForm
