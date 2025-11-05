from django.urls import path
from .views import ProductListView, ProductCreateAPIView, ProductDeleteView, ProductDetailAPIView, ProductMixedAPIView, ProductUpdateAPIView
urlpatterns = [
    path('products/', ProductListView.as_view()),   
    path('products/create/', ProductCreateAPIView.as_view()),
    path('products/delete/<int:pk>/', ProductDeleteView.as_view()),
    path('products/detail/<int:pk>/', ProductDetailAPIView.as_view()),
    path('products/mixed/', ProductMixedAPIView.as_view()),
    path('products/mixed/<int:pk>/', ProductMixedAPIView.as_view()),
    path('products/update/<int:pk>/', ProductUpdateAPIView.as_view()),
]
