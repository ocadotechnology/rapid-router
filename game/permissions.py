#########################
# Workspace permissions #
#########################


def can_create_workspace(user):
    return not user.is_anonymous()


def can_load_workspace(user, workspace):
    return not user.is_anonymous() and workspace.owner == user.userprofile


def can_save_workspace(user, workspace):
    return not user.is_anonymous() and workspace.owner == user.userprofile


def can_delete_workspace(user, workspace):
    return not user.is_anonymous() and workspace.owner == user.userprofile

#####################
# Level permissions #
#####################


def can_create_level(user):
    return not user.is_anonymous()


def can_play_level(user, level):
    if level.default and not level.episode.in_development:
        return True
    elif level.anonymous:
        return False
    elif (level.default and level.episode.in_development and not user.is_anonymous() and
            user.userprofile.developer):
        return True
    elif user.is_anonymous():
        return level.default and not level.episode.in_development
    elif user.userprofile == level.owner:
        return True
    elif level.shared_with.filter(id=user.id).exists():
        return can_share_level_with(user, level.owner.user)
    else:
        return (hasattr(user.userprofile, 'teacher') and
                user.userprofile.teacher.teaches(level.owner))


def can_load_level(user, level):
    if user.is_anonymous():
        return False
    elif user.userprofile == level.owner:
        return True
    elif level.shared_with.filter(id=user.id).exists():
        return can_share_level_with(user, level.owner.user)
    else:
        return (hasattr(user.userprofile, 'teacher') and
                user.userprofile.teacher.teaches(level.owner))


def can_save_level(user, level):
    if level.anonymous:
        return True
    elif user.is_anonymous():
        return False
    else:
        return user.userprofile == level.owner


def can_delete_level(user, level):
    if user.is_anonymous():
        return False
    elif level.owner == user.userprofile:
        return True
    else:
        return (hasattr(user.userprofile, 'teacher') and
                user.userprofile.teacher.teaches(level.owner))


def can_share_level(user, level):
    if user.is_anonymous():
        return False
    elif hasattr(user.userprofile, 'student') and user.userprofile.student.is_independent():
        return False
    else:
        return level.owner == user.userprofile


def can_share_level_with(recipient, sharer):
    if recipient.is_anonymous() or sharer.is_anonymous():
        return False

    recipient_profile = recipient.userprofile
    sharer_profile = sharer.userprofile

    if (hasattr(sharer_profile, 'student') and not(sharer_profile.student.is_independent()) and
            hasattr(recipient_profile, 'student') and
            not(recipient_profile.student.is_independent())):
        # Are they in the same class?
        return sharer_profile.student.class_field == recipient_profile.student.class_field
    elif hasattr(sharer_profile, 'teacher') and sharer_profile.teacher.teaches(recipient_profile):
        # Is the recipient taught by the sharer?
        return True
    elif (hasattr(recipient_profile, 'teacher') and
            recipient_profile.teacher.teaches(sharer_profile)):
        # Is the sharer taught by the recipient?
        return True
    elif hasattr(sharer_profile, 'teacher') and hasattr(recipient_profile, 'teacher'):
        # Are they in the same organisation?
        return recipient_profile.teacher.school == sharer_profile.teacher.school
    else:
        return False


#####################
# Other permissions #
#####################

def can_see_class(user, class_):
    if user.is_anonymous():
        return False
    elif hasattr(user.userprofile, 'teacher'):
        return class_.teacher == user.userprofile.teacher


def can_see_level_moderation(user):
    if user.is_anonymous():
        return False
    else:
        return hasattr(user.userprofile, 'teacher')


def can_see_scoreboard(user):
    return not user.is_anonymous()
