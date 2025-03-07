import logging

from rest_framework import permissions

LOGGER = logging.getLogger(__name__)


def _get_userprofile_school(userprofile):
    if hasattr(userprofile, "teacher"):
        return userprofile.teacher.school
    elif hasattr(userprofile, "student"):
        return userprofile.student.class_field.teacher.school
    else:
        LOGGER.error(
            f"Userprofile ID {userprofile.id} has no teacher or student attribute"
        )
        return None


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


def can_play_or_delete_level(user, level):
    # If the teacher is an admin, they can play any student's level in the school, otherwise only student levels
    # from their own classes
    if user.userprofile.teacher.is_admin and hasattr(level.owner, "student"):
        return (
            user.userprofile.teacher.school
            == level.owner.student.class_field.teacher.school
        )
    else:
        return user.userprofile.teacher.teaches(level.owner)


def can_approve_level(user, level):
    return (
        hasattr(user.userprofile, "teacher")
        and level.shared_with.filter(id=user.id).exists()
    )


def can_play_level(user, level, early_access):
    if (
        not user.is_anonymous
        and hasattr(user.userprofile, "student")
        and user.userprofile.student.class_field
    ):
        # If the user is a student, check that the level isn't locked for their class
        return user.userprofile.id == level.owner_id or (
            user.userprofile.student.class_field not in level.locked_for_class.all()
            and not level.needs_approval
        )
    elif level.default and not level.episode.in_development:
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
        user_school = _get_userprofile_school(user.userprofile)
        owner_school = _get_userprofile_school(level.owner)
        return user_school is not None and user_school == owner_school
    else:
        return can_play_or_delete_level(user, level)


def can_load_level(user, level):
    if user.is_anonymous:
        return False
    elif user.userprofile == level.owner:
        return True
    elif level.shared_with.filter(id=user.id):
        user_school = _get_userprofile_school(user.userprofile)
        owner_school = _get_userprofile_school(level.owner)
        return user_school is not None and user_school == owner_school
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
    elif hasattr(user.userprofile, "teacher"):
        return can_play_or_delete_level(user, level)

    return False


class CanShareLevel(permissions.BasePermission):
    """
    Used to verify that an incoming request is made by a user who is authorised to share
    the level - that is, that they are the owner of the level as a student and the level has been approved by a teacher,
    or if they're a teacher that the level was shared with them.
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
        # if the user is a teacher and the level is shared with them
        elif (
            hasattr(request.user.userprofile, "teacher")
            and obj.shared_with.filter(id=request.user.id).exists()
        ):
            return True
        else:
            return obj.owner == request.user.userprofile and not obj.needs_approval


class CanShareLevelWith(permissions.BasePermission):
    """
    Used to verify that the user who is requesting to share their level is authorised to share the level with a specific
    recipient.
    The user is authorised if:
    - neither they nor the recipient are anonymous,
    - neither they nor the recipient are independent students,
    - they are a student and the recipient is a student in the same class, or their teacher
    - they are a teacher and the recipient is a teacher in the same school, or their student
    - they are an admin teacher and the recipient is a student in the same school
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
        elif hasattr(sharer_profile, "teacher") and sharer_profile.teacher.is_admin:
            return (
                recipient_profile.student.class_field.teacher.school
                == sharer_profile.teacher.school
            )
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
