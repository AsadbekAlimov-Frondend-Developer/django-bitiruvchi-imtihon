from django.urls import path
from .views import ProductListAPIView, ProductCreateAPIView, ProductDetailView, ProductDeleteView, ProductMixedAPIView, ProductUpdateAPIView

urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='product_list'),
    path('products/create/', ProductCreateAPIView.as_view(), name='product_create'),
    path('products/detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('products/update/<int:pk>/', ProductUpdateAPIView.as_view(), name='product_update'),
    path('products/mixed/<int:pk>/', ProductMixedAPIView.as_view(), name='product_mixed'),
]
