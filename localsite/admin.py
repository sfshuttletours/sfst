from datetime import date
from django.contrib import admin
from django.contrib.admin.filterspecs import *
from django import forms
from django.utils.translation import ugettext as _

from product.models import OptionGroup
from product.admin import OptionGroupOptions

from localsite.models import DayOfWeek, TourCategory, TourType, TourSchedule, TourProduct, TourCapacity, TeamMember,\
    OrderConfirmationSection, OrderConfirmationSubSection, OrderConfirmationBannerText, OrderConfirmationCoupon,\
    SiteSkin, OrderCompletedSiteSkin, ComboSchedule, TourGuest, CartGuest, OverbookingAttempt, PriorToEmailSent


# class TourCapacityForm(forms.ModelForm):
#     model = TourCapacity
#     override = forms.BooleanField(label='Override Overbooking Error', required=False, initial=False)
#
#     def get_affected_tour_products(self):
#         return TourProduct.objects.filter(day__gte=date.today()).filter(
#                                           day__gte=self.cleaned_data['from_date'],
#                                           day__lte=self.cleaned_data['to_date'])
#
#     def clean(self):
#         overbookings = self.get_affected_tour_products().filter(product__total_sold__gt=self.cleaned_data['seats_available'])
#         if not self.cleaned_data['override'] and overbookings:
#             dates = ['%s at %s' % (t.day.strftime('%B, %d %Y'), t.pretty_time) for t in overbookings]
#             raise forms.ValidationError, 'Change would result in overbookings for the following dates: %s' % ', '.join(dates)
#         return self.cleaned_data
#
#     def save(self, *args, **kwargs):
#         super(TourCapacityForm, self).save(*args, **kwargs)
#         tour_products = self.get_affected_tour_products()
#         for tp in tour_products:
#             product = tp.product
#             product.items_in_stock = self.cleaned_data['seats_available']
#             product.save()
#             print 'saved', product.id
#
# class TourCapacityAdmin(admin.TabularInline):
#     model = TourCapacity
#     form = TourCapacityForm
#     extra = 1


class ComboScheduleAdminForm(forms.ModelForm):
    class Meta:
        model = ComboSchedule

class ComboScheduleAdmin(admin.TabularInline):
    form = ComboScheduleAdminForm
    model = ComboSchedule
    extra = 1

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "tourschedule":
            kwargs["queryset"] = TourSchedule.objects.filter(tour_type__active=True).\
                exclude(tour_type__is_combo=True).order_by('tour_type__name')
        return super(ComboScheduleAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

class TourScheduleAdmin(admin.TabularInline):
    model = TourSchedule
    extra = 1

class TourAdmin(admin.ModelAdmin):
    inlines = [ComboScheduleAdmin, TourScheduleAdmin]
    list_filter = ('active', 'default_site_skin', 'featured', 'is_combo',
        'sell_in_even_quantities_only', 'requires_names')
    search_fields = ['name', 'description', 'slug', 'default_site_skin__code',
        'default_site_skin__name']

    def url(obj):
        try:
            if obj.active:
                return "<a href='%s' target='_blank'>View on site</a>" % (obj.get_absolute_url(),)
            else:
                return "(Inactive)"
        except:
            return "Bad tour slug (please fix)"

    def option_group_url(obj):
        if obj.option_group:
            return '<a href="/admin/product/optiongroup/%s">%s</a>' %\
                (obj.option_group.id, obj.option_group)
        else:
            return ''

    url.short_description = 'Url'
    url.allow_tags = True
    option_group_url.short_description = 'Option group (age)'
    option_group_url.allow_tags = True

    list_display = ('name', url, 'allow_refunds', option_group_url)

admin.site.register(TourType, TourAdmin)

class OrderCompletedSiteSkinAdmin(admin.ModelAdmin):
    exclude = ('order', )

admin.site.register(OrderCompletedSiteSkin, OrderCompletedSiteSkinAdmin)

class SiteSkinAdmin(admin.ModelAdmin):
    exclude = ('hash', )

admin.site.register(SiteSkin, SiteSkinAdmin)

class TourProductAdmin(admin.ModelAdmin):
    # inlines = [ComboScheduleAdmin, TourScheduleAdmin]
    list_filter = ('day', 'tour_type')
    search_fields = ('product__name',)
    raw_id_fields = ('product', )

admin.site.register(TourProduct, TourProductAdmin)


admin.site.register(TourCategory)
admin.site.register(DayOfWeek)
admin.site.register(TeamMember)
admin.site.register(TourSchedule)

class TourGuestAdmin(admin.ModelAdmin):
    search_fields = ['name', 'order_item__product__name']

admin.site.register(TourGuest, TourGuestAdmin)

class CartGuestAdmin(admin.ModelAdmin):
    search_fields = ['name', 'cart_item__product__name']

admin.site.register(CartGuest, CartGuestAdmin)


# order confirmation pretty email / html stuff

class OrderConfirmationSubSectionAdmin(admin.TabularInline):
    """
    subsections inline in each section in admin.
    """
    model = OrderConfirmationSubSection
    extra = 2

class OrderConfirmationSectionAdmin(admin.ModelAdmin):
    inlines = [OrderConfirmationSubSectionAdmin]



admin.site.register(OrderConfirmationSection, OrderConfirmationSectionAdmin)
admin.site.register(OrderConfirmationBannerText)
admin.site.register(OrderConfirmationCoupon)


class OverbookingAttemptAdmin(admin.ModelAdmin):
    pass

class PriorToEmailSentAdmin(admin.ModelAdmin):
    search_fields = ('order', )

admin.site.register(OverbookingAttempt, OverbookingAttemptAdmin)
admin.site.register(PriorToEmailSent, PriorToEmailSentAdmin)


from django.contrib.admin.filterspecs import FilterSpec, BooleanFieldFilterSpec
# custom filter for filtering OptionGroup by active field in TourType


class IsOptionGroupActive(admin.filterspecs.BooleanFieldFilterSpec):

    def __init__(self, f, request, params, model, model_admin):
        super(BooleanFieldFilterSpec, self).__init__(f, request, params, model, model_admin)
        self.lookup_kwarg = 'tour_types__active__exact'
        self.lookup_kwarg2 = 'tour_types__active__exact'
        self.lookup_val = request.GET.get(self.lookup_kwarg, None)
        self.lookup_val2 = request.GET.get(self.lookup_kwarg2, None)

    def choices(self, cl):
        for k, v in ((_('All'), None), (_('Yes'), '1'), (_('No'), '0')):
            print k, v, self.lookup_val, self.lookup_val2
            yield {'selected': self.lookup_val == v,
                   'query_string': cl.get_query_string({self.lookup_kwarg: v},
                    [self.lookup_kwarg2]),
                   'display': k}

    def title(self):
        return 'active'

# adding filter to wrong field is intended
FilterSpec.filter_specs.insert(0, (lambda f: getattr(f, 'sort_order_filter',
    False), IsOptionGroupActive))
f = OptionGroup._meta.get_field_by_name('sort_order')[0]
setattr(f, 'sort_order_filter', True)

admin.site.unregister(OptionGroup)

class OptionGroupAdmin(OptionGroupOptions):
    list_filter = ('sort_order',)


admin.site.register(OptionGroup, OptionGroupAdmin)
