from rest_framework.response import Response
from rest_framework import generics, status

from .models import Category, Subcategory, Ads
from .serializers import CategorySerializer, SubcategorySerialier, AdsSerializer


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubcategoryView(generics.ListAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerialier


class AdsView(generics.ListAPIView):
    queryset = Ads.objects.all().order_by('date')
    serializer_class = AdsSerializer

class AdsByCategoryView(generics.ListAPIView):

    serializer_class = AdsSerializer

    def get_queryset(self):
        ads = Ads.objects.filter(category=self.kwargs['id'])
        
        return ads


class AdsBySubCategoryView(generics.ListAPIView):

    serializer_class = AdsSerializer

    def get_queryset(self):
        ads = Ads.objects.filter(subcategory=self.kwargs['id'])
        
        return ads