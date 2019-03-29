# -*- coding: utf-8 -*-
# Code for Life
#
# Copyright (C) 2019, Ocado Innovation Limited
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ADDITIONAL TERMS – Section 7 GNU General Public Licence
#
# This licence does not grant any right, title or interest in any “Ocado” logos,
# trade names or the trademark “Ocado” or any other trademarks or domain names
# owned by Ocado Innovation Limited or the Ocado group of companies or any other
# distinctive brand features of “Ocado” as may be secured from time to time. You
# must not distribute any modification of this program using the trademark
# “Ocado” or claim any affiliation or association with Ocado or its employees.
#
# You are not authorised to use the name Ocado (or any of its trade names) or
# the names of any author or contributor in advertising or for publicity purposes
# pertaining to the distribution of this program, without the prior written
# authorisation of Ocado.
#
# Any propagation, distribution or conveyance of this program must include this
# copyright notice and these terms. You must not misrepresent the origins of this
# program; modified versions of the program must be marked as such and not
# identified as the original program.
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


def can_play_level(user, level, early_access):
    if level.default and not level.episode.in_development:
        return True
    elif level.anonymous:
        return False
    elif level.default and level.episode.in_development and early_access:
        return True
    elif user.is_anonymous():
        return level.default and not level.episode.in_development
    elif user.userprofile == level.owner:
        return True
    elif level.shared_with.filter(id=user.id):
        return can_share_level_with(user, level.owner.user)
    else:
        return hasattr(
            user.userprofile, "teacher"
        ) and user.userprofile.teacher.teaches(level.owner)


def can_load_level(user, level):
    if user.is_anonymous():
        return False
    elif user.userprofile == level.owner:
        return True
    elif level.shared_with.filter(id=user.id):
        return can_share_level_with(user, level.owner.user)
    else:
        return hasattr(
            user.userprofile, "teacher"
        ) and user.userprofile.teacher.teaches(level.owner)


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
        return hasattr(
            user.userprofile, "teacher"
        ) and user.userprofile.teacher.teaches(level.owner)


def can_share_level(user, level):
    if user.is_anonymous():
        return False
    elif (
        hasattr(user.userprofile, "student")
        and user.userprofile.student.is_independent()
    ):
        return False
    else:
        return level.owner == user.userprofile


def can_share_level_with(recipient, sharer):
    if recipient.is_anonymous() or sharer.is_anonymous():
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
            sharer_profile.student.class_field == recipient_profile.student.class_field
        )
    elif hasattr(sharer_profile, "teacher") and sharer_profile.teacher.teaches(
        recipient_profile
    ):
        # Is the recipient taught by the sharer?
        return True
    elif hasattr(recipient_profile, "teacher") and recipient_profile.teacher.teaches(
        sharer_profile
    ):
        # Is the sharer taught by the recipient?
        return True
    elif hasattr(sharer_profile, "teacher") and hasattr(recipient_profile, "teacher"):
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
    elif hasattr(user.userprofile, "teacher"):
        return class_.teacher == user.userprofile.teacher


def can_see_level_moderation(user):
    if user.is_anonymous():
        return False
    else:
        return hasattr(user.userprofile, "teacher")


def can_see_scoreboard(user):
    return not user.is_anonymous()
