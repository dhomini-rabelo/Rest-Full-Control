from rest_framework import serializers
from backend.accounts import UserSerializer
from backend.products import Feedback, Rating



class FeedbackSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Feedback
        fields = 'id', 'user', 'commentary'


class RatingSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Rating
        fields = 'id', 'user', 'commentary', 'value'
