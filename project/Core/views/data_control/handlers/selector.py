from django.db.models.query import QuerySet
from rest_framework.serializers import ModelSerializer, ListSerializer

from backend.products.app.models.feedbacks import Feedback


class SelectorQueryset:
    selector_name_in_body = 'selector'

    def function(self, queryset: QuerySet, SerializerClass: ModelSerializer, body: dict):
        selector = body.get(self.selector_name_in_body)
        simple_fields = selector.get('simple_fields')
        fks = selector.get('fks')
        
        SerializerCopy = self.get_serializer_copy_class(SerializerClass, simple_fields, fks, False)
        serializer = SerializerCopy(queryset, many=True)

        return serializer.data

    def get_serializer_copy_class(self, SerializerClass: ModelSerializer, serializer_fields: list, fks: None | dict[str, list] = None, is_instance: bool = True):

        if fks is None:
            if not is_instance:
                serializer_class, Dad = SerializerClass, SerializerClass
            elif isinstance(SerializerClass, ListSerializer):
                serializer_class, Dad = SerializerClass.child, SerializerClass.child.__class__
            else: 
                serializer_class, Dad = SerializerClass.__class__, SerializerClass.__class__
            

            class SerializerCopy(Dad):

                class Meta:
                    model = serializer_class.Meta.model
                    fields = serializer_fields

            
        else:
            fields = SerializerClass().get_fields()
            fks_serializers = { key: self.get_serializer_copy_class(fields[key], value) for key, value in fks.items() }

            class SerializerCopy(SerializerClass):
                for fk, value in fks_serializers.items():
                    is_many = isinstance(fields[fk], ListSerializer)
                    vars()[fk] = value(many=is_many)
                
                class Meta:
                    model = SerializerClass.Meta.model
                    fields = serializer_fields
            


        return SerializerCopy