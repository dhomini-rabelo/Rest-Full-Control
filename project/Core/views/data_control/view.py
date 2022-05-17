from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models.query import QuerySet
from collections.abc import Iterable
from Fast.utils.main import get_type_name


class DataControlApi(APIView):
    # require filter_function, selector_function

    def get(self, request):
        body = request.data if request.data and isinstance(request.data, dict) else {}
        initial_queryset  = self.get_queryset()

        try:
            new_queryset = self.filter_function(initial_queryset, body)
            response = self.selector_function(new_queryset, self.get_serializer_class(), body)
        except Exception as error:
            return Response({get_type_name(error): str(error)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(response)

    def notify_subscribers(self, current_queryset, request_body) -> QuerySet | Iterable | dict:
        queryset_or_object = current_queryset
        for subscriber in self.subscribers:
            queryset_or_object = subscriber(queryset_or_object, request_body)
        return queryset_or_object


    def get_queryset(self) -> QuerySet:
        return self.initial_queryset

    def get_serializer_class(self):
        return self.serializer_class