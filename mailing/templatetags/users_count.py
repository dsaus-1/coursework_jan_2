from django import template

from mailing.models import Client
from users.models import User

register = template.Library()

@register.simple_tag
def client_count():
    count = Client.objects.distinct("email").count()
    if count % 10 == 1 and count != 11:
        return f'{count} абонента'
    elif 1 < count % 10 < 5 and count not in (12, 13, 14):
        return f'{count} абонентов'
    else:
        return f'{count} абонентов'


@register.simple_tag
def user_count():
    count = User.objects.all().count()
    if count % 10 == 1 and count != 11:
        return f'{count} клиент'
    elif 1 < count % 10 < 5 and count not in (12, 13, 14):
        return f'{count} клиента'
    else:
        return f'{count} клиентов'