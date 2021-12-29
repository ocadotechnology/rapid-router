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
