from django.contrib import admin
from .models import Sale, PaymentType, FreightCompany


admin.site.empty_value_display = 'NULL'


@admin.register(PaymentType)
class PaymentTypeAdmin(admin.ModelAdmin):
    list_display = 'id', 'name',
    list_display_links = 'name',
    list_per_page = 50
    ordering = 'name',
    search_fields = '^name',

@admin.register(FreightCompany)
class FreightCompanyAdmin(admin.ModelAdmin):
    list_display = 'id', 'name',
    list_display_links = 'name',
    list_per_page = 50
    ordering = 'name',
    search_fields = '^name',

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = 'id', 'sale_price', 'sale_date'
    list_display_links = 'id',
    list_per_page = 50
    list_select_related = 'user', 'product', 'freight_company', 'payment_type'
    ordering = 'sale_date',
    search_fields = 'sale_date', 'product__name'
