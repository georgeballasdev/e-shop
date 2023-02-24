from django.urls import path
from . import views


app_name = 'orders'
urlpatterns = [
    path('', views.orders, name='orders'),
    path('basket/', views.BasketView.as_view(), name='basket'),
    path('cancel/', views.cancel, name='cancel'),
    path('new/', views.new, name='new'),
    path('new/<int:id>/', views.complete, name='complete')
]