from datetime import datetime, timedelta
import pytz
from django.conf import settings

from users.models import User


def delete_not_confirmed_user():
    not_confirmed_user = User.objects.filter(is_active=False)
    check_time = datetime.now().astimezone(pytz.timezone(settings.TIME_ZONE))
    for user in not_confirmed_user:
        deadline = user.token_time.astimezone(pytz.timezone(settings.TIME_ZONE)) + timedelta(days=3)
        if check_time > deadline:
            user.delete()
