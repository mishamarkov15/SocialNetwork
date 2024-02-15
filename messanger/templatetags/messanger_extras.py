from django import template

register = template.Library()


@register.filter
def cat_room_name(arg1, arg2):
    """concatenate arg1 & arg2"""
    if int(arg1) < int(arg2):
        return f"{arg1}t{arg2}"
    else:
        return f"{arg2}t{arg1}"
