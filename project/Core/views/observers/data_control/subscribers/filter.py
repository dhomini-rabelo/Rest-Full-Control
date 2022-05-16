from django.db.models.query import QuerySet
from django.db.models import Q


class FilterSubscriber:
    filter_body_name = 'filters'
    filter_models_name = 'filters_model'

    def __init__(self, mediator: dict, models: dict = {}):
        self.mediator = mediator
        self.models = models

    def filter_queryset(self, queryset: QuerySet, body: dict):
        model = body.get(self.filter_models_name)
        if model in self.models.keys():
            query_obj = self.get_many_queries(model)
        else:
            queries = body.get(self.filter_body_name)
            if (not isinstance(queries, list)) or len(queries) == 0: return queryset
            query_obj =  self.get_query_obj(queries)
        return queryset.filter(query_obj).distinct()

    def get_query_obj(self, queries: list[dict]):
        query_obj = Q()
        for queryset in queries:
            query_obj = query_obj | self.get_many_queries(queryset)
        return Q(query_obj)
            
    def get_queries(self, queries: dict):
        try:
            return Q(**{ self.mediator[k]: v for k, v in queries.items() if isinstance(v, (str, int, bool)) })
        except KeyError as error:
            raise KeyError(f'{error} not in: {list(self.mediator.keys())}')

    def get_many_queries(self, queries_obj: list[dict | list] | dict | list[list & dict]):
        if isinstance(queries_obj, dict):
            return self.get_queries(queries_obj)
        elif isinstance(queries_obj, list):
            query_obj = Q()
            many_queries_obj = [self.get_many_queries(query_obj) for query_obj in queries_obj]
            for or_query_obj in many_queries_obj:
                query_obj = query_obj | or_query_obj
            return Q(query_obj)
        else:
            raise TypeError('Invalid type for queries_obj, accept only list or dict')



class FilterSubscriberWithoutMediator(FilterSubscriber):

    def __init__(self, models: dict = {}):
        self.models = models

    def get_queries(self, queries: dict):
        return Q(**{ k: v for k, v in queries.items() if isinstance(v, (str, int, bool)) })
