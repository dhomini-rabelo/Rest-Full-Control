from django.db.models import (Model, CharField, DateTimeField, TextField, EmailField, ForeignKey, PositiveIntegerField, ImageField, RESTRICT, DecimalField, DateField, BooleanField, SET_NULL, CASCADE, ManyToManyField)
from backend.accounts import User
from .products import Product


class Feedback(Model):
    user = ForeignKey(User, on_delete=CASCADE, related_name='feedbacks')
    commentary = TextField()
    product = ForeignKey(Product, on_delete=CASCADE, related_name='feedbacks')

    def __str__(self):
        return f'Feedback of {self.product.name}'


class Rating(Model):
    user = ForeignKey(User, on_delete=CASCADE, related_name='ratings')
    commentary = TextField()
    product = ForeignKey(Product, on_delete=CASCADE, related_name='ratings')
    value = DecimalField(decimal_places=1, max_digits=20)

    def __str__(self):
        return f'Rating of {self.product.name}'
    