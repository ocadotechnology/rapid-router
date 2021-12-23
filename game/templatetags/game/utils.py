from django import template
from django.template.defaultfilters import stringfilter
from common.utils import using_two_factor

register = template.Library()


@register.filter
@stringfilter
def trim(text):
    return text.strip()


@register.filter
def booltojs(var):
    if var:
        return "true"
    else:
        return "false"


@register.filter
def get_item(value, arg):
    return value.get(arg)


@register.filter(name="has_2FA")
def has_2FA(u):
    return using_two_factor(u)


@register.filter(name="is_logged_in")
def is_logged_in(u):
    return (
        u
        and u.is_authenticated
        and (not using_two_factor(u) or (hasattr(u, "is_verified") and u.is_verified()))
    )


@register.filter(name="is_logged_in_as_teacher")
def is_logged_in_as_teacher(u):
    return is_logged_in(u) and u.userprofile and hasattr(u.userprofile, "teacher")


@register.filter(name="is_independent_student")
def is_independent_student(u):
    return (
        u.userprofile
        and u.userprofile.student
        and u.userprofile.student.is_independent()
    )
