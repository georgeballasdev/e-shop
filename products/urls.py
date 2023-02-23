from django.urls import path
from . import views


app_name = 'products'
urlpatterns = [
    path('', views.home, name='home'),
    path('<str:category>/', views.category, name='category'),
    path('product/<int:id>/', views.ProductDetail.as_view(), name='product_detail'),
    path('search/', views.search, name='search')
]