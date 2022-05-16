from Core.views.data_control.view import DataControlApi
from . import Product, ProductSerializer
from .actions.objects.subscribers.products.filter import product_filter



class ProductDataControl(DataControlApi):
    serializer_class = ProductSerializer
    initial_queryset = Product.objects.select_related('company').prefetch_related('categories', 'coupons', 'feedbacks', 'ratings')
    filter_function = product_filter.filter_queryset