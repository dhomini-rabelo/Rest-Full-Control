from django.db.models.query import QuerySet
from django.db.models import Q


class FilterSubscriber:
    filter_body_name = 'filters'

    def __init__(self, queries_obj: dict):
        self.queries_obj = queries_obj

    def filter_queryset(self, queryset: QuerySet, body: dict):
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
            return Q(**{ self.queries_obj[k]: v for k, v in queries.items() if isinstance(v, (str, int, bool)) })
        except KeyError as error:
            raise KeyError(f'{error} not in: {list(self.queries_obj.keys())}')

    def get_many_queries(self, queries_obj: list[dict] | dict | list[list]):
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

