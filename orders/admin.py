from django.contrib import admin
from .models import Basket, Order

admin.site.register((Basket, Order))
