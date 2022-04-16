from rest_framework import serializers

from .models import Ads, Category, Subcategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubcategorySerialier(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = '__all__'


class AdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = '__all__'
