from django.core.management.base import BaseCommand
from django.conf import settings as django_settings

from common.cron import CronJobManager

from localsite.crons import DailySurveyEmailsCronJob, PriorToTourEmailCronJob
from administration.crons import DailySettlementCronJob, DailyAuthorizedPaymentsCronJob


crons_to_run = [DailySurveyEmailsCronJob,
                DailyAuthorizedPaymentsCronJob,
                PriorToTourEmailCronJob]  # add to list if more in the future

if not django_settings.IS_QA:   # don't want daily settlment emails on QA
    crons_to_run.append(DailySettlementCronJob)


class Command(BaseCommand):
    def handle(self, *args, **options):
        for cron_class in crons_to_run:
            instance = cron_class()
            CronJobManager.run(instance)
