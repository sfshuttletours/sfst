from django.contrib import admin

from administration.models import InventoryDayNote, OrderCheckin

class OrderCheckinAdmin(admin.ModelAdmin):
    pass

admin.site.register(OrderCheckin, OrderCheckinAdmin)


admin.site.register(InventoryDayNote)
