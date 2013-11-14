from django.contrib import admin

from adjustments.models import Adjustment, AdjustmentHistory

class AdjustmentHistoryAdmin(admin.StackedInline):
    model = AdjustmentHistory

class AdjustmentAdmin(admin.ModelAdmin):
    inlines = [AdjustmentHistoryAdmin, ]
    raw_id_fields = ('item', )
    
admin.site.register(Adjustment, AdjustmentAdmin)