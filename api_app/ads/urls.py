from django.urls import path

from .views import AdsByCategoryView, AdsBySubCategoryView, AdsView, CategoryView, SubcategoryView


urlpatterns = [
    path('category/', CategoryView.as_view(), name='category'),
    path('subcategory/', SubcategoryView.as_view(), name='subcategory'),
    path('ads/', AdsView.as_view(), name='ads'),
    path('ads/category/<int:id>/', AdsByCategoryView.as_view(), name='ads by category'),
    path('ads/subcategory/<int:id>/', AdsBySubCategoryView.as_view(), name='ads by subcategory'),
]