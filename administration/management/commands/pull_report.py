from django.core.management.base import BaseCommand, CommandError

from administration.bing import *
from administration.adwords import *

class Command(BaseCommand):

    def handle(self, *args, **options):
        adwords_report = get_adwords_report()
        report = getBingReport(1600)
