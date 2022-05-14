from django.contrib import admin
from .models import Product, Company, Category, Coupon


admin.site.empty_value_display = 'NULL'


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = 'id', 'name',
    list_display_links = 'name',
    list_per_page = 50
    ordering = 'name',
    search_fields = '^name',


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'name',
    list_display_links = 'name',
    list_per_page = 50
    ordering = 'name',
    search_fields = '^name',


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = 'id', 'name',
    list_display_links = 'name',
    list_per_page = 50
    ordering = 'name',
    search_fields = '^name',


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = 'id', 'name',
    list_display_links = 'name',
    list_per_page = 50
    list_select_related = 'company',
    ordering = 'name',
    search_fields = '^name',
