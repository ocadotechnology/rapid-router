from rest_framework import permissions

#########################
# Workspace permissions #
#########################


def can_create_workspace(user):
    return not user.is_anonymous


def can_load_workspace(user, workspace):
    return not user.is_anonymous and workspace.owner == user.userprofile


def can_save_workspace(user, workspace):
    return not user.is_anonymous and workspace.owner == user.userprofile


def can_delete_workspace(user, workspace):
    return not user.is_anonymous and workspace.owner == user.userprofile


#####################
# Level permissions #
#####################


def can_create_level(user):
    return not user.is_anonymous


def can_play_level(user, level, early_access):
    if level.default and not level.episode.in_development:
        return True
    elif level.anonymous:
        return False
    elif level.default and level.episode.in_development and early_access:
        return True
    elif user.is_anonymous:
        return level.default and not level.episode.in_development
    elif user.userprofile == level.owner:
        return True
    elif level.shared_with.filter(id=user.id):
        return CanShareLevelWith().can_share_level_with(user, level.owner.user)
    else:
        return hasattr(
            user.userprofile, "teacher"
        ) and user.userprofile.teacher.teaches(level.owner)


def can_load_level(user, level):
    if user.is_anonymous:
        return False
    elif user.userprofile == level.owner:
        return True
    elif level.shared_with.filter(id=user.id):
        return CanShareLevelWith().can_share_level_with(user, level.owner.user)
    else:
        return hasattr(
            user.userprofile, "teacher"
        ) and user.userprofile.teacher.teaches(level.owner)


def can_save_level(user, level):
    if level.anonymous:
        return True
    elif user.is_anonymous:
        return False
    else:
        return user.userprofile == level.owner


def can_delete_level(user, level):
    if user.is_anonymous:
        return False
    elif level.owner == user.userprofile:
        return True
    else:
        return hasattr(
            user.userprofile, "teacher"
        ) and user.userprofile.teacher.teaches(level.owner)


class CanShareLevel(permissions.BasePermission):
    """
    Used to verify that an incoming request is made by a user who is authorised to share
    the level - that is, that they are the owner of the level.
    """

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_anonymous:
            return False
        elif (
            hasattr(request.user.userprofile, "student")
            and request.user.userprofile.student.is_independent()
        ):
            return False
        else:
            return obj.owner == request.user.userprofile


class CanShareLevelWith(permissions.BasePermission):
    """
    Used to verify that an the user who is requesting to share their level is
    authorised to share the level with a specific recipient.
    The user is authorised if:
    - neither they nor the recipient are anonymous,
    - neither they nor the recipient are independent students,
    - they are a student and the recipient is a student in the same class, or their
    teacher
    - they are a teacher and the recipient is a teacher in the same school, or their
    student
    """

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        sharer = request.user
        return self.can_share_level_with(obj, sharer)

    def can_share_level_with(self, recipient, sharer):
        if recipient.is_anonymous or sharer.is_anonymous:
            return False

        recipient_profile = recipient.userprofile
        sharer_profile = sharer.userprofile

        if (
            hasattr(sharer_profile, "student")
            and not (sharer_profile.student.is_independent())
            and hasattr(recipient_profile, "student")
            and not (recipient_profile.student.is_independent())
        ):
            # Are they in the same class?
            return (
                sharer_profile.student.class_field
                == recipient_profile.student.class_field
            )
        elif hasattr(sharer_profile, "teacher") and sharer_profile.teacher.teaches(
            recipient_profile
        ):
            # Is the recipient taught by the sharer?
            return True
        elif hasattr(
            recipient_profile, "teacher"
        ) and recipient_profile.teacher.teaches(sharer_profile):
            # Is the sharer taught by the recipient?
            return True
        elif hasattr(sharer_profile, "teacher") and hasattr(
            recipient_profile, "teacher"
        ):
            # Are they in the same organisation?
            return recipient_profile.teacher.school == sharer_profile.teacher.school
        else:
            return False


#####################
# Other permissions #
#####################


def can_see_class(user, class_):
    if user.is_anonymous:
        return False
    elif hasattr(user.userprofile, "teacher"):
        return class_.teacher == user.userprofile.teacher


def can_see_level_moderation(user):
    if user.is_anonymous:
        return False
    else:
        return hasattr(user.userprofile, "teacher")


def can_see_scoreboard(user):
    return not user.is_anonymous
