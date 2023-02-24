from django.contrib import admin
from .models import Category, Option, Product


admin.site.register((Category, Option, Product))
