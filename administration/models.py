from django.db import models
from django.contrib.auth.models import User

from satchmo_store.shop.models import Order, OrderItem

from localsite.models import TourProduct
from concierges.models import Concierge


class ConciergeMessage(models.Model):
    is_global = models.BooleanField(default=False, db_index=True)
    message = models.TextField(max_length=500)
    concierge = models.ForeignKey(Concierge, null=True)
    last_updated = models.DateTimeField(auto_now=True, auto_now_add=True)


class InventoryDayNote(models.Model):
    """
    Also used for checkin reports etc.
    """
    TYPE_INVENTORY = 1
    TYPE_CHECKIN = 2
    TYPE_CHOICES = (
        (TYPE_INVENTORY, 'Inventory'),
        (TYPE_CHECKIN, 'Checkin')
    )

    note = models.TextField(max_length=500)
    type = models.IntegerField(choices=TYPE_CHOICES, default=TYPE_INVENTORY)    # default to inventory note type
    for_date = models.DateField()
    user = models.ForeignKey(User)
    date_added = models.DateTimeField(auto_now=True, auto_now_add=True)

    class Meta:
        unique_together = ('for_date', 'type')

    def __unicode__(self):
        return self.note


class OrderCheckin(models.Model):
    TYPE_CASH = 1
    TYPE_CREDIT = 2

    AMOUNT_CHOICES = (
        (TYPE_CREDIT, 'Credit Card'),
        (TYPE_CASH, 'Cash'),
    )

    order = models.OneToOneField(Order, related_name='checkin')
    amount_taken_sales = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name="$'s owed")
    amount_taken_change_order_fees = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True,
        verbose_name='Change order fees')
    amount_type = models.IntegerField(choices=AMOUNT_CHOICES, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def total_amount_in(self):
        amount = 0
        if self.amount_taken_sales:
            amount += self.amount_taken_sales
        if self.amount_taken_change_order_fees:
            amount += self.amount_taken_change_order_fees

        return amount

    def gross_amount(self):
        return self.total_amount_in()

    def __unicode__(self):
        return str(self.order.id)


class OrderItemCheckin(models.Model):
    order_checkin = models.ForeignKey(OrderCheckin, related_name='order_item_checkins')
    order_item = models.OneToOneField(OrderItem, related_name='checkin')
    num_checkedin = models.IntegerField(verbose_name='Number checked in')
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=True)

    def __unicode__(self):
        return self.order_item.product.name


class TourProductCheckinFinalizationManager(models.Manager):
    def is_finalized(self, tour_product):
        return True if self.filter(tour_product=tour_product) else False


class TourProductCheckinFinalization(models.Model):
    tour_product = models.OneToOneField(TourProduct)
    done_by = models.ForeignKey(User)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=True)

    objects = TourProductCheckinFinalizationManager()
