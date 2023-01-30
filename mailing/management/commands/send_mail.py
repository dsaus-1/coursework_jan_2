from django.core.management import BaseCommand
from mailing.services import automatic_mailing


class Command(BaseCommand):

    def handle(self, *args, **options):
        automatic_mailing()
