from dataclasses import field
from django.db.models.query import QuerySet
from rest_framework.serializers import ModelSerializer, ListSerializer


class SelectorQueryset:
    selector_name_in_body = 'selector'
    simple_fields_name_in_body = 'simple_fields'
    relationship_fields_name_in_body = 'relationship_fields'

    def function(self, queryset: QuerySet, SerializerClass: ModelSerializer, body: dict):
        selector = body.get(self.selector_name_in_body)
        if not isinstance(selector, dict): return queryset

        simple_fields = selector.get(self.simple_fields_name_in_body)
        relationship_fields = selector.get(self.relationship_fields_name_in_body)
        if simple_fields is not None:
            SerializerCopy = self.get_serializer_copy_class(SerializerClass, simple_fields, relationship_fields, False)
            serializer = SerializerCopy(queryset, many=True)      
            return serializer.data

        return queryset

    def get_serializer_copy_class(
            self, SerializerClass: ModelSerializer, serializer_fields: list, 
            relationship_fields: None | dict[str, list] = None, is_instance: bool = True
        ):

        if relationship_fields is None:
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

        elif not all([field in serializer_fields for field in list(relationship_fields.keys())]):
            raise ValueError(f'Some relationship field not in {self.simple_fields_name_in_body}')
            
        else:
            fields = SerializerClass().get_fields()
            relationship_fields_serializers = {
                field: self.get_serializer_copy_class(fields[field], field_list) for field, field_list in relationship_fields.items() 
            }

            class SerializerCopy(SerializerClass):
                for field, serializer in relationship_fields_serializers.items():
                    is_many = isinstance(fields[field], ListSerializer)
                    vars()[field] = serializer(many=is_many)
                
                class Meta:
                    model = SerializerClass.Meta.model
                    fields = serializer_fields
            


        return SerializerCopy