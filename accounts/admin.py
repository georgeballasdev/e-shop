from django.contrib import admin
from .models import Account, Address


admin.site.register((Account, Address))
