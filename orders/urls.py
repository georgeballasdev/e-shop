from django.urls import path
from . import views


app_name = 'orders'
urlpatterns = [
    path('', views.orders, name='orders'),
    path('basket/', views.basket, name='basket'),
    path('cancel/', views.cancel_order, name='cancer_order')
    path('new/', views.new_order, name='new_order'),
]