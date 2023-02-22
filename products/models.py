from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)
    display_order = models.IntegerField()

    def __str__(self):
        return self.name

class Option(models.Model):
    portion = models.CharField(max_length=20)
    price = models.IntegerField() # in euro cents

    def __str__(self):
        return f'Option {self.portion} at {self.price/100} euros'

class Product(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    info = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    options = models.ManyToManyField(Option)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title