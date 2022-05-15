from django.contrib import admin
from .models import Product, Company, Category, Coupon, Feedback, Rating


admin.site.empty_value_display = 'NULL'

class FeedbackInlineAdmin(admin.StackedInline):
    model = Feedback
    extra = 1


class RatingInlineAdmin(admin.StackedInline):
    model = Rating
    extra = 1


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = 'id', 'product_name'
    list_display_links = 'product_name',
    list_select_related = 'product', 'user'
    list_per_page = 50
    ordering = 'id',
    search_fields = '^product__name',

    @admin.display(description='Product name')
    def product_name(self, feedback: Feedback):
        return str(feedback.product.name)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = 'id', 'product_name'
    list_display_links = 'product_name',
    list_select_related = 'product', 'user'
    list_per_page = 50
    ordering = 'id',
    search_fields = '^product__name',

    @admin.display(description='Product name')
    def product_name(self, rating: Rating):
        return str(rating.product.name)


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
    inlines = FeedbackInlineAdmin, RatingInlineAdmin
