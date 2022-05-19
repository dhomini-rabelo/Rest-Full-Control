from django.http import HttpRequest
from Core.views.data_control.view import DataControlApi
from django.test import SimpleTestCase
from unittest import expectedFailure
from test.main import ObjFake



def filter_function_fake(fake_self, queryset, body):
    if not isinstance(body, dict): raise Exception('body is not dict')
    return {}

def selector_function_fake(fake_self, queryset, serializer_class, body):
    if not isinstance(body, dict): raise Exception('body is not dict')
    return {}


class DataControlApiFake(DataControlApi):
    serializer_class = {}
    initial_queryset = {}
    filter_function = filter_function_fake
    selector_function = selector_function_fake


class DataControlApiTest(SimpleTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.view = DataControlApiFake()
        cls.request = HttpRequest()
        cls.request.data = {}

    def test_get_body_with_empty_body(self):
        request = ObjFake()
        request.data = None
        body = self.view._get_body(request)
        self.assertEqual(body, {})

    @expectedFailure
    def test_invalid_body(self):
        request = ObjFake()
        request.data = ["none"]
        body = self.view._get_body(request)

    def test_response_with_error(self):
        error_message = 'Error test'
        new_view = DataControlApiFake()

        def filter_function_with_error(queryset, body): 
            raise Exception(error_message)

        new_view.filter_function = filter_function_with_error
        request = new_view.get(self.request)

        self.assertEqual(request.status_code, 400)
        self.assertEqual(request.data, {
            "Exception": error_message,
        })

    def test_response(self):
        view = DataControlApiFake()
        request = view.get(self.request)
        self.assertEqual(request.status_code, 200)
        self.assertEqual(request.data, {})
    