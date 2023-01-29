from django.core.mail import send_mail
from django.core.management import BaseCommand
from config import settings
from mailing.models import *

class Command(BaseCommand):

    def handle(self, *args, **options):

        # message_qs = Message.objects.all()
        # for num, message in enumerate(message_qs, start=1):
        #     print(f'{num}. "{message.title}"')
        #
        # try:
        #     number_message = int(input('Введите номер сообщения, которое хотите отправить: '))
        #     message = message_qs[number_message-1]
        # except:
        #     raise Exception('Введен не соответствующий номер')
        #
        # mail_list = message.addressee.all()
        #
        # for num in range(len(mail_list)):
        #     print(send_mail(
        #         subject=message.title,
        #         message=message.text,
        #         from_email=settings.EMAIL_HOST_USER,
        #         recipient_list=[mail_list[num].email]
        #     ))




