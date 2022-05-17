from rest_framework.serializers import ModelSerializer, ListSerializer
from typing import Union
from django.db.models.query import QuerySet
from django.db.models import Q
from ...data_control.exceptions import ModelNotFound


class FilterForQueryset:
    # Filter some ListSerializer
    filter_name_in_body = 'filters'
    filter_models_name_in_body = 'filters_model'

    def __init__(self, mediator: dict, models: dict = {}):
        self.mediator = mediator # returns query from simple filter key
        self.models = models # request.body models

    def filter_queryset(self, queryset: QuerySet, body: dict):
        model: str | None = body.get(self.filter_models_name_in_body)
        if model in self.models.keys():
            query_obj: dict = self._get_many_queries(self.models[model])
        elif model is not None:
            # invalid model name
            raise ModelNotFound(f'{model} not found in {list(self.models.keys())}')
        else:
            queries: list[dict | list | Union[dict, list]] = body.get(self.filter_name_in_body)
            if (not isinstance(queries, list)) or len(queries) == 0: return queryset
            query_obj =  self._get_query_obj(queries)
        return queryset.filter(query_obj).distinct()

    def _get_query_obj(self, queries: list[dict]):
        query_obj = Q()
        for queryset in queries:
            query_obj = query_obj | self._get_many_queries(queryset)
        return Q(query_obj)
            
    def _get_queries(self, queries: dict):
        try:
            return Q(**{ self.mediator[k]: v for k, v in queries.items() if isinstance(v, (str, int, bool)) })
        except KeyError as error:
            raise KeyError(f'{error} not in: {list(self.mediator.keys())}')

    def _get_many_queries(self, queries_obj: list[dict | list] | dict | list[Union[list, dict]]):
        if isinstance(queries_obj, dict):
            return self._get_queries(queries_obj)
        elif isinstance(queries_obj, list):
            query_obj = Q()
            many_queries_obj = [self._get_many_queries(query_obj) for query_obj in queries_obj]
            for or_query_obj in many_queries_obj:
                query_obj = query_obj | or_query_obj
            return Q(query_obj)
        else:
            raise TypeError('Invalid type for queries_obj, accept only list or dict')



class FilterQuerysetWithoutMediator(FilterForQueryset):

    def __init__(self, models: dict = {}):
        self.models = models # request.body models

    def _get_queries(self, queries: dict):
        return Q(**{ k: v for k, v in queries.items() if isinstance(v, (str, int, bool)) })
