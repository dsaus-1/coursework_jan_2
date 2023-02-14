from django.core.management import BaseCommand

from users.services import delete_not_confirmed_user


class Command(BaseCommand):

    def handle(self, *args, **options):
        delete_not_confirmed_user()
