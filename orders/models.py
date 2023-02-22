from django.contrib.auth.models import User
from django.db import models
from products.models import Option, Product


class ItemQuery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def get_total(self):
        return self.option.price * self.quantity

class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(ItemQuery)
    total = models.IntegerField(default=0) # in euro cents

    def get_basket_total(self):
        return sum(item.get_total() for item in self.items)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(ItemQuery)
    total = models.IntegerField(default=0) # in euro cents
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)

    def get_order_total(self):
        return sum(item.get_total() for item in self.items)

    def __str__(self):
        return f'Order of {self.user.username} for {self.total/100} euros at {str(self.timestamp)}'