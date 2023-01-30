from mailing.models import *
from datetime import datetime, timedelta, time

from mailing.supportive_services import send_message


def automatic_mailing():

    status_list = []

    for active_settings in Settings.objects.all():

        if active_settings.status == 'launched':
            obj = Send_message.objects.filter(settings_pk=active_settings.id).last()
            mail_list = active_settings.addressee.all()

            if obj == None:

                if active_settings.mailing_time.replace(second=0, microsecond=0) == datetime.now().time().replace(second=0, microsecond=0):
                    send_message(mail_list, active_settings, status_list)

            else:
                frequency = active_settings.frequency
                time = obj.sending_time

                if frequency == 'day':
                    time += timedelta(days=1)
                elif frequency == 'week':
                    time += timedelta(days=7)
                elif frequency == 'month':
                    time += timedelta(days=30)

                if time.replace(second=0, microsecond=0) == datetime.now().replace(second=0, microsecond=0):
                    send_message(mail_list, active_settings, status_list)



