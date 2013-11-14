from django.core.management.base import BaseCommand

from satchmo_store.shop.models import Order


class Command(BaseCommand):
    requires_model_validation = False
    
    def handle(self, *args, **options):
        for order in Order.objects.filter(id__gt=35000).iterator():
            if order.status == 'Pending' or order.status == '' or not order.status:
                if not order.is_affiliate_order():
                    if sum(map(lambda x: x.amount, order.payments_completed())) <= 0:
                        print order.id
                        print sum(map(lambda x: x.amount, order.payments_completed()))
