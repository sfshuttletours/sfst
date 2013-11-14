from datetime import date, datetime, timedelta

import django
from django.conf import settings as django_settings
from django.core.mail import send_mass_mail

from common.helper import start_thread
from common.cron import Schedule, CronJobBase
from localsite.models import DayOfWeek, TourType, TourSchedule, SurveyEmailSent
from localsite.models import TourProduct, PriorToEmailSent


class DailySurveyEmailsCronJob(CronJobBase):
    """
    Sends out survey emails in the evenings around 6 or 7pm
    """
    RUN_EVERY_MINS = 60  # check every hour

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'localsite.survey_emails'

    def do(self):
        """
        Get all unique contacts that were on a tour today, and send them emails. Also make sure only 1 email per order
        goes out, even though an order may have tours over multiple days etc.
        """
        # check to see if its after 6pm, if not don't run
        if datetime.now().hour < 18:
            return

        today = date.today()    # people who were on the tour today
        dow = DayOfWeek.objects.get(isoweekday=today.isoweekday())
        for tour_type in TourType.objects.filter(active=True):
            schedules = TourSchedule.objects.filter(active=True, tour_type=tour_type, day_of_week=dow)
            for schedule in schedules:
                # get orders to email for "today", and exclude ones that have already been emailed
                orders_to_email = \
                    list(set(map(lambda x: x.order, tour_type.get_product(day=today, schedule=schedule, create=False).items)))
                orders_already_emailed = map(lambda x: x.order, SurveyEmailSent.objects.filter(order__in=orders_to_email))

                for order in orders_already_emailed:
                    if orders_to_email.count(order) > 0:
                        orders_to_email.remove(order)

                # we're going to mass mail these email_addresses now!
                message_list = []
                for order in orders_to_email:
                    if order.contact.email:
                        # construct the message, with proper salutation
                        message_body = 'Dear %s,' % order.contact.first_name if order.contact.first_name else 'Hi,'
                        message_body += '\n\nWe hope you enjoyed your recent tour with San Francisco Shuttle Tours / Wine Country Tour Shuttle! Would you take a few moments to give us your feedback? Please click on the link below to a brief, 6-question survey. We really appreciate your input!\n\n'
                        message_body += 'http://www.surveymonkey.com/s/K33XCKT'
                        message_body += '\n\nSincerely,\nCustomer Service San Francisco Shuttle Tours / Wine Country Tour Shuttle'
                        message_list += [('Follow-up from SF Shuttle Tours', message_body,
                            django_settings.DEFAULT_FROM_EMAIL, (order.contact.email,))]

                    SurveyEmailSent.objects.get_or_create(order=order)

                if len(message_list) > 0:
                    email_connection = None
                    if django_settings.IS_PROD:
                        email_connection=django.core.mail.get_connection(
                            backend='django.core.mail.backends.smtp.EmailBackend')
                    start_thread(send_mass_mail, tuple(message_list), connection=email_connection)


class PriorToTourEmailCronJob(CronJobBase):
    """
    Sends out an email to all tours that require a prior email.
    """
    RUN_EVERY_MINS = 60  # check every 1 hour

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'localsite.prior_to_tour_emails'

    def do(self):
        now = datetime.now()
        for tour_type in TourType.objects.filter(active=True).filter(
                prior_to_tour_email_required=True,
                prior_to_tour_email_hours__isnull=False):
            day_to_check = now + timedelta(hours=tour_type.prior_to_tour_email_hours)
            dow = DayOfWeek.objects.get(isoweekday=day_to_check.isoweekday())
            schedules = TourSchedule.objects.filter(active=True,
                tour_type=tour_type, day_of_week=dow)

            # if tour_type.prior_to_tour_email_hours <= 0:
            #     schedules = schedules.filter(tour_time__lte=day_to_check.time())

            schedules = schedules.select_related('tour_type')

            for schedule in schedules:
                this_tour_orders = tour_type.get_product(day=day_to_check,
                    schedule=schedule, create=False)
                orders_to_email = []
                if this_tour_orders:
                    # for x in this_tour_orders.items:
                    #     print x  #this will show you the exact tour
                    #only get the order and no dups
                    orders_to_email = list(set(map(lambda x: x.order,
                        this_tour_orders.items)))
                    orders_already_emailed = map(lambda x: x.order,
                        PriorToEmailSent.objects.filter(order__in=orders_to_email))

                    for order in orders_already_emailed:
                        if orders_to_email.count(order) > 0:
                            orders_to_email.remove(order)

                # we're going to mass mail these email_addresses now!
                message_list = []
                for order in orders_to_email:
                    if order.contact.email:
                        # construct the message
                        message_list += [(
                                tour_type.prior_to_tour_email_subject,
                                tour_type.prior_to_tour_email_body,
                                tour_type.followup_email_from,
                                (order.contact.email,)
                            )]
                    PriorToEmailSent.objects.get_or_create(order=order)

                if len(message_list) > 0:
                    email_connection = None
                    if django_settings.IS_PROD:
                        email_connection=django.core.mail.get_connection(
                            backend='django.core.mail.backends.smtp.EmailBackend')
                    send_mass_mail(tuple(message_list), connection=email_connection)
