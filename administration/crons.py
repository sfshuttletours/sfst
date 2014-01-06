from l10n.utils import moneyfmt
import datetime
import logging

import django

from django.conf import settings as django_settings
from django.core.urlresolvers import reverse

from common.helper import send_mail
from common.cron import Schedule, CronJobBase
from common.cron.models import CronJobLog
from product.modules.configurable.models import ConfigurableProduct

from localsite.models import TourProduct, DayOfWeek
from administration.models import OrderItemCheckin, TourProductCheckinFinalization, OrderCheckin
from satchmo_store.shop.models import OrderPayment


class DailyAuthorizedPaymentsCronJob(CronJobBase):
    """
    Send out daily sales amount -- taken from 3:45 - 3:44 the next day
    """
    RUN_AT_TIMES = ['15:45']

    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'administration.authorized_daily_payments'

    def do(self):
        """
        Send out daily authorize.net payments to John
        """
        start_of_day_time = datetime.time(0, 0)
        start_of_today = datetime.datetime.combine(datetime.date.today(), start_of_day_time)
        today_cutoff_time = start_of_today + datetime.timedelta(hours=15, minutes=45)
        yesterday_cutoff_time = today_cutoff_time - datetime.timedelta(hours=23, minutes=59, seconds=59)
        payments = OrderPayment.objects.filter(time_stamp__gte=yesterday_cutoff_time, time_stamp__lt=today_cutoff_time)
        checkins = OrderCheckin.objects.filter(timestamp__gte=yesterday_cutoff_time, timestamp__lt=today_cutoff_time)
        todays_total_payments = 0
        for payment in payments:
            todays_total_payments += payment.amount
        for checkin in checkins:
            todays_total_payments += checkin.gross_amount()

        if todays_total_payments > 0:
            todays_total_payments = moneyfmt(todays_total_payments)
            send_mail('Sales total for today: %s' % todays_total_payments,
                'http://%s%s' % (django_settings.SITE_DOMAIN, reverse('checkin_reports')),
                django_settings.DEFAULT_FROM_EMAIL, ['john@sanfranshuttletours.com', ] if django_settings.IS_PROD else ['sfst@tivix.com'],
                connection=django.core.mail.get_connection(backend='django.core.mail.backends.smtp.EmailBackend')
            )


class DailySettlementCronJob(CronJobBase):
    """
    Send out daily settlement to John after 6pm
    """
    RUN_EVERY_MINS = 60  # check every hour

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'administration.daily_settlement'

    def do(self):
        """
        Send out daily settlement to John.
        """
        # check to see if its after 6pm, if not don't run
        if datetime.datetime.now().hour < 18:
            return

        # check if its already run
        logs = CronJobLog.objects.filter(code=self.code).order_by('-end_time')[:1]
        if logs:
            end_time = logs[0].end_time
            if end_time.hour >= 18:  # one already ran at or > 6pm!
                return

        logging.info('Sending daily settlement email to John!')
        product_ids = []
        for tour_product in TourProduct.objects.filter(day=datetime.date.today()):
            try:
                product_ids += tour_product.product.configurableproduct.productvariation_set.all().values_list(
                        'product__id', flat=True)
            except ConfigurableProduct.DoesNotExist:
                product_ids += [tour_product.product.id]

        order_item_checkins = OrderItemCheckin.objects.filter(order_item__product__id__in=product_ids)
        total = 0
        counted_order_checkins = []
        for order_item_checkin in order_item_checkins:
            order_checkin = order_item_checkin.order_checkin    # so as not to double count
            if order_checkin not in counted_order_checkins:
                total += order_checkin.amount_taken_sales if order_checkin.amount_taken_sales else 0
                total += order_checkin.amount_taken_change_order_fees if order_checkin.amount_taken_change_order_fees else 0
                counted_order_checkins.append(order_checkin)

        send_mail('Daily Settlement $%s' % total,
            'http://%s%s' % (django_settings.SITE_DOMAIN, reverse('checkin_reports')),
            django_settings.DEFAULT_FROM_EMAIL, ['john@sanfranshuttletours.com'],
            connection=django.core.mail.get_connection(backend='django.core.mail.backends.smtp.EmailBackend')
        )


class UnfinalizedTourAlertCronJob(CronJobBase):
    """
    Alert email to point out any unfinalized tours.
    """
    RUN_EVERY_MINS = 60  # check every hour

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'administration.unfinalized_tour_alert'

    def do(self):
        # check to see if its after 4pm, if not don't run
        if datetime.now().hour < 16:
            return

        # check if its already run
        logs = CronJobLog.objects.filter(code=self.code).order_by('-end_time')[:1]
        if logs:
            end_time = logs[0].end_time
            if end_time.hour >= 16:  # one already ran at or > 6pm!
                return

        day = date.today()
        dow = DayOfWeek.objects.get(isoweekday=day.isoweekday())
        schedules = dow.tourschedule_set.filter(tour_type__is_combo=False).select_related('tour_type')

        tour_products_not_finalized = []
        for sched in schedules:
            if sched.active:
                tour_product = sched.tour_type.get_product(day, schedule=sched, create=False)
                # tour_product.product.total_sold > 0 in the conditions since there was some dummy products apparently
                if tour_product \
                        and tour_product.tour_type.active \
                        and tour_product.tour_type.featured \
                        and tour_product.product.total_sold > 0 \
                        and tour_product not in tour_products_not_finalized:
                    tour_products_not_finalized.append(tour_product)

        logging.info(tour_products_not_finalized)
        for tour_product in tour_products_not_finalized:
            if TourProductCheckinFinalization.objects.filter(tour_product=tour_product):
                tour_products_not_finalized.remove(tour_product)

        if len(tour_products_not_finalized) > 0:
            logging.info(tour_products_not_finalized)
            logging.info('Sending unfinalized tour alert')
            message = 'Following tours haven\'t been finalized:\n\n'
            for tour_product in tour_products_not_finalized:
                message += tour_product.product.name
                message += '%s\n\n'
            logging.info(message)
            send_mail('ALERT: Some tours not finalized for %s' % day, message, django_settings.DEFAULT_FROM_EMAIL,
                [django_settings.DEFAULT_TO_EMAIL])
            

from administration.bing import getBingReport 
from administration.adwords import get_adwords_report

class PullAdsReportCronJob(CronJobBase):
    """
    Alert email to point out any unfinalized tours.
    """
    RUN_EVERY_MINS = 60  # check every hour

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'administration.pull_ads_report'

    def do(self):
        logging.info('Pulling ads reports')
        adwords_report = get_adwords_report(True)
        report = getBingReport(1600)



