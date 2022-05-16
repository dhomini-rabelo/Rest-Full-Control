from django.http import HttpRequest
from Core.views.observers.data_control.view import DataControlApi
from . import Product, ProductSerializer
from rest_framework.response import Response
from .actions.objects.subscribers.products.filter import product_filter_subscriber



class ProductDataControl(DataControlApi):
    serializer_class = ProductSerializer
    initial_queryset = Product.objects.select_related('company').prefetch_related('categories', 'coupons', 'feedbacks', 'ratings')
    subscribers = [product_filter_subscriber.filter_queryset]