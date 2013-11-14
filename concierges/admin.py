from django.contrib import admin

from concierges.models import Concierge, ConciergeCommission

class ConciergeCommissionAdmin(admin.TabularInline):
    model = ConciergeCommission
    
class ConciergeAdmin(admin.ModelAdmin):
    raw_id_fields = ('contact', 'orders')
    search_fields = ('contact__first_name', 'contact__last_name', 'contact__addressbook__street2')
    list_display = ('handle', 'hotel_name')
    inlines = [ConciergeCommissionAdmin, ]

admin.site.register(Concierge, ConciergeAdmin)