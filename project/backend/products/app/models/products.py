from django.db.models import (Model, CharField, DateTimeField, TextField, EmailField, ForeignKey, PositiveIntegerField, ImageField, RESTRICT, DecimalField, DateField, BooleanField, SET_NULL, CASCADE, ManyToManyField)


class Company(Model):
    name = CharField(max_length=256)


class Category(Model):
    name = CharField(max_length=256)


class Coupon(Model):
    name = CharField(max_length=256)
    value = DecimalField(decimal_places=2, max_digits=20)
    is_percent = BooleanField(default=True)
    is_for_all_products = BooleanField(default=False)


class Product(Model):
    name = CharField(max_length=256)
    description = TextField()
    current_price = DecimalField(decimal_places=2, max_digits=20)
    promotion_price = DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)
    cashback_value = DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)
    cashback_is_percent = BooleanField(blank=True, null=True)
    quantity = PositiveIntegerField()
    company = ForeignKey(Company, on_delete=SET_NULL, null=True)
    categories = ManyToManyField(Category, related_name='products')
    coupons = ManyToManyField(Coupon, related_name='products')
