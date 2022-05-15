from django.http import HttpRequest
from Core.views.observers.data_control.view import DataControlApi
from . import Product, ProductSerializer
from rest_framework.response import Response


# def product_filter_subscriber(queryset, body: dict):
#     queries = {
#         'name': 'name__startswith',
#     }
#     queries_obj = { queries[k]: v for k, v in body['query'].items() }
#     return queryset.filter(**queries_obj)



class ProductDataControl(DataControlApi):
    # subscribers = [product_filter_subscriber]
    serializer_class = ProductSerializer
    initial_queryset = Product.objects.all()