from django.contrib.auth.models import User
from django.db import models
from products.models import Product


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, default='')
    street = models.CharField(max_length=50)
    postal = models.CharField(max_length=10)
    floor = models.IntegerField(default=0)
    notes = models.CharField(max_length=100, blank=True)

    def get_name(self):
        return self.street if self.name == '' else self.name
    
    def __str__(self):
        return f'{self.get_name()} address of {self.user.username}'

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    active_address = models.ForeignKey(Address, blank=True)
    favourites = models.ManyToManyField(Product, blank=True, related_name='favourites')

    def get_recent_orders(self):
        return self.orders.order_by('-timestamp')[:10]
    
    def __str__(self):
        return f'Account of {self.user.username}'