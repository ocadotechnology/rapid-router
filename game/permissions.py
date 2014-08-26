#########################
# Workspace permissions #
#########################

def can_create_workspace(user):
    return not user.is_anonymous()

def can_load_workspace(user, workspace):
    return not user.is_anonymous() and workspace.owner == user.userprofile

def can_save_workspace(user):
    return not user.is_anonymous()

def can_delete_workspace(user, workspace):
    return not user.is_anonymous() and workspace.owner == user.userprofile

#####################
# Level permissions #
#####################

def can_create_level(user):
    return not user.is_anonymous()

def can_play_level(user, level):
    if level.default:
        return True
    elif user.is_anonymous():
        return level.default
    elif user.userprofile == level.owner:
        return True
    elif level.shared_with.filter(id=user.id).exists():
        return True
    elif hasattr(user.userprofile, 'teacher') and hasattr(level.owner, 'student'):
        teacher = user.userprofile.teacher
        students_teacher = level.owner.student.class_field.teacher
        return teacher == students_teacher
    return False

def can_load_level(user, level):
    if user.is_anonymous():
        return False
    elif user.userprofile == level.owner:
        return True
    elif level.shared_with.filter(id=user.id).exists():
        return True
    elif hasattr(user.userprofile, 'teacher') and hasattr(level.owner, 'student'):
        teacher = user.userprofile.teacher
        students_teacher = level.owner.student.class_field.teacher
        return teacher == students_teacher
    return False

def can_save_level(user, level):
    if user.is_anonymous():
        return False
    else:
        return user.userprofile == level.owner

def can_delete_level(user, level):
    if user.is_anonymous():
        return False
    elif level.owner == user.userprofile:
        return True
    elif hasattr(user.userprofile, 'teacher') and hasattr(level.owner, 'student'):
        teacher = user.userprofile.teacher
        student = level.owner.student

        if student.class_field.teacher == teacher:
            return True
    return False

def can_share_level(user, level):
    if user.is_anonymous():
        return False
    else:
        return level.owner == user.userprofile

def can_share_level_with(recipient, sharer):
    if recipient.is_anonymous() or sharer.is_anonymous():
        return False

    recipient_profile = recipient.userprofile
    sharer_profile = sharer.userprofile

    if hasattr(sharer_profile, 'student') and hasattr(recipient_profile, 'student'):
        # Are they in the same class?
        return sharer_profile.student.class_field == recipient_profile.student.class_field
    elif hasattr(sharer_profile, 'teacher') and hasattr(recipient_profile, 'student'):
        # Is the recipient taught by the sharer?
        return recipient_profile.student.class_field.teacher == sharer_profile.teacher
    elif hasattr(sharer_profile, 'student') and hasattr(recipient_profile, 'teacher'):
        # Is the sharer taught by the recipient?
        return sharer_profile.student.class_field.teacher == recipient_profile.teacher
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