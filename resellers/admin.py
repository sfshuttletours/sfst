from django.contrib import admin

from resellers.models import Reseller, ResellerRequest, ResellerCategory

class ResellerAdmin(admin.ModelAdmin):
    exclude = ('contact', 'orders', 'code')
    list_display = ('company_name', 'commission', 'discount', 'category', 'reseller_type')
    list_editable = ('commission', 'discount', 'category', 'reseller_type')

admin.site.register(Reseller, ResellerAdmin)
admin.site.register(ResellerRequest)
admin.site.register(ResellerCategory)