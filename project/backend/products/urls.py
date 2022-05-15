from django.urls import path
from .views import *

urlpatterns = [
    path('products', ProductDataControl.as_view(), name='products_data_control'),
]
