from django.db import models

from satchmo_store.shop.models import OrderItem

class Adjustment(models.Model):
    DELETED = 1
    REFUNDED = 2
    VOIDED = 3
    MOVED = 4
    VOUCHER_STANDBY_CREATED = 5
    VOUCHER_OK_TO_BOOK = 6
    VOUCHER_STANDBY_USED = 7
    REFUND_REQUESTED = 8
    REFUND_REQUEST_REJECTED = 9

    STATUS_CHOICES = (
        (DELETED, 'Deleted'),
        (REFUNDED, 'Refunded'),
        (VOIDED, 'Voided'),
        (REFUND_REQUESTED, 'Refund/Void Requested'),
        (REFUND_REQUEST_REJECTED, 'Refund/Void Requested Rejected'),
        (MOVED, 'Moved'),
        (VOUCHER_STANDBY_CREATED, '"Credit Voucher-Standby" Created'),
        (VOUCHER_OK_TO_BOOK, '"Credit Voucher-OK to Book" Created'),
        (VOUCHER_STANDBY_USED, '"Credit Voucher-Standby" Used'),
    )

    status = models.IntegerField(choices=STATUS_CHOICES)
    # order = models.OneToOne('shop.Order')
    item = models.OneToOneField('shop.OrderItem')

    def latest(self):
        return self.history.order_by('-timestamp')[0]

    @property
    def voucher_created(self):
        """Was a voucher ever created for this item?"""
        voucher_ids = [self.VOUCHER_STANDBY_CREATED, self.VOUCHER_OK_TO_BOOK]
        return self.history.filter(to_status__in=voucher_ids).count()

    @property
    def moved(self):
        """Was this order ever moved"""
        return self.history.filter(to_status=self.MOVED).count()


class AdjustmentHistory(models.Model):

    adjustment = models.ForeignKey(Adjustment, related_name='history')
    user = models.ForeignKey('auth.User', null=True)
    from_status = models.IntegerField(choices=Adjustment.STATUS_CHOICES, blank=True, null=True)
    to_status = models.IntegerField(choices=Adjustment.STATUS_CHOICES)
    notes = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
