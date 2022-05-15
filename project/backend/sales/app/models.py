from django.db.models import (Model, CharField, DateTimeField, TextField, EmailField, ForeignKey, PositiveIntegerField, ImageField, RESTRICT, DecimalField, DateField, BooleanField, SET_NULL, CASCADE, ManyToManyField)
from backend.accounts import User
from backend.products import Product


class PaymentType(Model):
    name = CharField(max_length=256)

    def __str__(self):
        return self.name


class FreightCompany(Model):
    name = CharField(max_length=256)
    coefficient = DecimalField(decimal_places=5, max_digits=10)

    def __str__(self):
        return self.name


class Sale(Model):
    user = ForeignKey(User, on_delete=CASCADE, related_name='sales')
    product = ForeignKey(Product, on_delete=SET_NULL, null=True, related_name='sales')
    quantity = PositiveIntegerField()
    sale_price = DecimalField(decimal_places=2, max_digits=20)
    end_price = DecimalField(decimal_places=2, max_digits=20)
    freight_price = DecimalField(decimal_places=2, max_digits=20)
    freight_company = ForeignKey(FreightCompany, on_delete=SET_NULL, null=True, related_name='sales')
    payment_type = ForeignKey(PaymentType, on_delete=SET_NULL, null=True, related_name='sales')
    is_finalized = BooleanField(default=False)
    sale_date = DateField(auto_now_add=True)
    delivery_date = DateField()

    def __str__(self):
        return f'Sale of {self.product.name}'