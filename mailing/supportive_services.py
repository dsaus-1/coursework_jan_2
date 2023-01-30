from mailing.models import *
from django.core.mail import send_mail
from config import settings
import datetime

def send_message(mail_list, active_settings, status_list):
    for num in range(len(mail_list)):

        answer = send_mail(
            subject=active_settings.message.title,
            message=active_settings.message.text,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[mail_list[num].email],
            fail_silently=False
        )
        if answer:
            server_response = {'sending_time': datetime.datetime.now(),
                               'status': 'delivered',
                               'server_response': mail_list[num].email,
                               'settings_pk': Settings.objects.get(pk=active_settings.id)}
            status_list.append(Send_message(**server_response))

        else:
            server_response = {'sending_time': datetime.datetime.now(),
                               'status': 'not_delivered',
                               'server_response': mail_list[num].email,
                               'settings_pk': Settings.objects.get(pk=active_settings.id)}
            status_list.append(Send_message(**server_response))

        # except:
        #     server_response = {'sending_time': datetime.datetime.now(),
        #                        'status': 'not_delivered',
        #                        'server_response': mail_list[num].email,
        #                        'settings_pk': Settings.objects.get(pk=active_settings.id)}
        #     status_list.append(Send_message(**server_response))
        #
        # else:
        #     server_response = {'sending_time': datetime.datetime.now(),
        #                        'status': 'delivered',
        #                        'server_response': mail_list[num].email,
        #                        'settings_pk': Settings.objects.get(pk=active_settings.id)}
        #     status_list.append(Send_message(**server_response))

    Send_message.objects.bulk_create(status_list)
