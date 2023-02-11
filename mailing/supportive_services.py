import pytz
from mailing.models import Send_message, Settings
from django.core.mail import send_mail
import django.conf
import datetime

from users.models import User


def send_message(active_settings):
    status_list = []
    mail_list = active_settings.addressee.all()

    for item in mail_list:
        try:

            send_mail(
                subject=active_settings.message.title,
                message=active_settings.message.text,
                from_email=django.conf.settings.EMAIL_HOST_USER,
                recipient_list=[item.email],
                fail_silently=False
            )

        except:
            server_response = {'sending_time': datetime.datetime.now().astimezone(pytz.timezone(django.conf.settings.TIME_ZONE)),
                               'status': Send_message.STATUS_NOT_DELIVERED,
                               'server_response': item.email,
                               'settings_pk': Settings.objects.get(pk=active_settings.id),
                               'owner': User.objects.get(pk=active_settings.owner.id)}
            status_list.append(Send_message(**server_response))

        else:
            server_response = {'sending_time': datetime.datetime.now().astimezone(pytz.timezone(django.conf.settings.TIME_ZONE)),
                               'status': Send_message.STATUS_DELIVERED,
                               'server_response': item.email,
                               'settings_pk': Settings.objects.get(pk=active_settings.id),
                               'owner': User.objects.get(pk=active_settings.owner.id)}
            status_list.append(Send_message(**server_response))

    Send_message.objects.bulk_create(status_list)