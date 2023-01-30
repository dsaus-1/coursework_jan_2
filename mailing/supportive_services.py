from mailing.models import *
from django.core.mail import send_mail
from config import settings
import datetime

def send_message(mail_list, active_settings, status_list):
    for item in mail_list:
        try:

            send_mail(
                subject=active_settings.message.title,
                message=active_settings.message.text,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[item.email],
                fail_silently=False
            )

        except:
            server_response = {'sending_time': datetime.datetime.now(),
                               'status': 'not_delivered',
                               'server_response': item.email,
                               'settings_pk': Settings.objects.get(pk=active_settings.id)}
            status_list.append(Send_message(**server_response))

        else:
            server_response = {'sending_time': datetime.datetime.now(),
                               'status': 'delivered',
                               'server_response': item.email,
                               'settings_pk': Settings.objects.get(pk=active_settings.id)}
            status_list.append(Send_message(**server_response))

        finally:
            Send_message.objects.bulk_create(status_list)
