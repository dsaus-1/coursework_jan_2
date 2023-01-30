from django.core.mail import send_mail
from django.http import Http404
from config import settings
from mailing.models import *
import datetime

from mailing.supportive_services import send_message


def automatic_mailing():

    status_list = []

    for active_settings in Settings.objects.all():

        if active_settings.status == 'launched':
            mail_list = active_settings.addressee.all()
            send_message(mail_list, active_settings, status_list)


            # obj = Send_message.objects.filter(settings_pk=active_settings.id).last()
            #
            # if obj == None and active_settings.mailing_time > datetime.datetime.now():
            #     send_message(mail_list, active_settings, status_list)

            # elif obj.:



            # if get_object_or_404(Send_message, settings_pk=active_settings.id).sending_time <



