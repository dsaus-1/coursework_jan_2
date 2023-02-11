from django import template

register = template.Library()

@register.simple_tag
def mailing_number():
    return 1