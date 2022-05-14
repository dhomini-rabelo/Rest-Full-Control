from django.db.models import (Model, CharField, DateTimeField, TextField, EmailField, ForeignKey, PositiveIntegerField, ImageField, RESTRICT, DecimalField, DateField, BooleanField, SET_NULL, CASCADE, ManyToManyField)
from backend.accounts import User
from .products import Product


class Feedback(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    commentary = TextField()
    product = ForeignKey(Product, on_delete=CASCADE)


class Rating(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    commentary = TextField()
    product = ForeignKey(Product, on_delete=CASCADE)
    value = DecimalField(decimal_places=1, max_digits=20)
    