from django import template

from mailing.models import Settings

register = template.Library()

@register.simple_tag
def mailing_count():
    count = Settings.objects.all().count()
    if count % 10 == 1 and count != 11:
        return f'{count} рассылка'
    elif 1 < count % 10 < 5 and count not in (12, 13, 14):
        return f'{count} рассылки'
    else:
        return f'{count} рассылок'

@register.simple_tag
def active_mailing_count():
    count = Settings.objects.filter(status=Settings.STATUS_LAUNCHED).count()
    if count % 10 == 1 and count != 11:
        return f'а: {count} рассылка'
    elif 1 < count % 10 < 5 and count not in (12, 13, 14):
        return f'ы: {count} рассылки'
    else:
        return f'о: {count} рассылок'

