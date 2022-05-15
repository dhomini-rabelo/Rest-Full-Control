from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models.query import QuerySet
from collections.abc import Iterable


class DataControlApi(APIView):
    subscribers = []

    def get(self, request):
        body = request.data if request.data and isinstance(request.data, dict) else {}
        initial_queryset  = self.get_queryset()

        new_queryset_or_custom_object = self.notify_subscribers(initial_queryset, body)

        response = self.get_response(new_queryset_or_custom_object)
        return Response(response)

    def get_response(self, obj: QuerySet | Iterable | dict) -> QuerySet | Iterable | dict:
        try:
            if isinstance(obj, QuerySet):
                SerializerClass = self.get_serializer_class()
                serializer = SerializerClass(obj, many=True)
                return serializer.data
        except KeyError:
                pass
        
        if isinstance(obj, Iterable) or isinstance(obj, dict):
            return obj
        else:
            raise ValueError('Object type not found')

    def notify_subscribers(self, current_queryset, request_body) -> QuerySet | Iterable | dict:
        queryset_or_object = current_queryset
        for subscriber in self.subscribers:
            queryset_or_object = subscriber(queryset_or_object, request_body)
        return queryset_or_object


    def get_queryset(self) -> QuerySet:
        return self.initial_queryset

    def get_serializer_class(self):
        return self.serializer_class