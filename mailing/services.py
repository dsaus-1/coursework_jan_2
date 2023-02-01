from mailing.models import *
from datetime import datetime, timedelta

from mailing.supportive_services import send_message


def automatic_mailing():

    for active_settings in Settings.objects.all():

        if active_settings.status == Settings.STATUS_LAUNCHED:
            obj = Send_message.objects.filter(settings_pk=active_settings.id).last()

            if obj is None:
                mailing_time = active_settings.mailing_time.replace(second=0, microsecond=0)
                time_now = datetime.now().time().replace(second=0, microsecond=0)

                if mailing_time == time_now:
                    send_message(active_settings)

            else:
                frequency = active_settings.frequency
                obj_time = obj.sending_time

                if frequency == Settings.FREQUENCY_DAY:
                    obj_time += timedelta(days=1)
                elif frequency == Settings.FREQUENCY_WEEK:
                    obj_time += timedelta(days=7)
                elif frequency == Settings.FREQUENCY_MONTH:
                    obj_time += timedelta(days=30)

                obj_time = obj_time.replace(second=0, microsecond=0)
                time_now = datetime.now().replace(second=0, microsecond=0)

                if obj_time == time_now:
                    send_message(active_settings)



