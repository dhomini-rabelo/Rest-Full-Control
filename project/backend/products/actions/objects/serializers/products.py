from rest_framework import serializers
from backend.products import Company, Category, Coupon, Product
from .feedbacks import FeedbackSerializer, RatingSerializer



class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = 'id', 'name'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = 'id', 'name'


class CouponSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coupon
        fields = 'id', 'name', 'value', 'is_percent', 'is_for_all_products'


class ProductSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    categories = CategorySerializer(many=True)
    coupons = CouponSerializer(many=True)
    feedbacks = FeedbackSerializer(many=True)
    ratings = RatingSerializer(many=True)


    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'current_price', 'promotion_price', 'cashback_value',
            'cashback_is_percent', 'quantity', 'company', 'categories', 'coupons',
            # m2o
            'feedbacks', 'ratings'
        ] 