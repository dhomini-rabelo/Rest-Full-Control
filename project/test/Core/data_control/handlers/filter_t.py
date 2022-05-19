from django.test import TestCase
from unittest import expectedFailure
from decimal import Decimal
from Core.views.data_control.handlers.filter import FilterForQueryset
from backend.products import Company, Category, Coupon, Product
from random import randint
from test.main import ObjFake
from test.support.data import SupportForData


class FilterForQuerysetTest(TestCase, SupportForData):
    
    @classmethod
    def setUpTestData(cls):
        cls.create_models(cls)
        cls.filters = {
            'name': 'name__icontains',
            'company': 'company__name__startswith',
            'not_has_promotion': 'promotion_price__isnull',
        }
        cls.models = {
            "promotion": [
                {
                    "not_has_promotion": False
                }
            ]
        }
        cls.instance = FilterForQueryset(cls.filters, cls.models)

    def test__get_filter_obj__with_simple_body(self):
        response = self.instance._get_filter_obj({})
        self.assertIs(response, None)

    def test__get_filter_obj__with_model(self):
        models_key = 'promotion'
        response = self.instance._get_filter_obj({self.instance.filter_models_name_in_body: models_key})
        self.assertEqual(response, self.models[models_key])

    @expectedFailure
    def test__get_filter_obj__with_invalid_model(self):
        models_key = 'invalid_model_name'
        response = self.instance._get_filter_obj({self.instance.filter_models_name_in_body: models_key})

    def test__get_filter_obj__with_filters(self):
        custom_filter = {
            self.instance.filter_name_in_body: [
                {
                    'name': 'notebook'
                }
            ]
        }
        response = self.instance._get_filter_obj(custom_filter)
        self.assertEqual(response, custom_filter[self.instance.filter_name_in_body])

    



