from django.db.models.query import QuerySet
from rest_framework.serializers import ModelSerializer
from rest_framework.utils.serializer_helpers import BindingDict


class SelectorQueryset:
    selector_name_in_body = 'selector'

    def function(self, queryset: QuerySet, SerializerClass: ModelSerializer, body: dict):
        selector = body.get(self.selector_name_in_body)
        simple_fields = selector.get('simple_fields')
        fks = selector.get('fks')
        
        SerializerCopy = self.get_serializer_copy_class(SerializerClass, simple_fields, fks)
        serializer = SerializerCopy(queryset, many=True)

        return serializer.data

    def get_serializer_copy_class(self, SerializerClass: ModelSerializer, serializer_fields: list, fks: None | dict[str, list] = None):

        if fks is None:

            class SerializerCopy(SerializerClass):

                class Meta:
                    model = SerializerClass.Meta.model
                    fields = serializer_fields

            
        else:
            fields = SerializerClass().get_fields()
            fks_serializers = { key: self.get_serializer_copy_class(fields[key].__class__, value) for key, value in fks.items() }
            

            class SerializerCopy(SerializerClass):
                for fk, value in fks_serializers.items():
                    vars()[fk] = value()
                
                class Meta:
                    model = SerializerClass.Meta.model
                    fields = serializer_fields
            


        return SerializerCopy