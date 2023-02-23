from django.db import models
from django.db.models.functions import Length
from django.shortcuts import get_object_or_404


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
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    options = models.ManyToManyField(Option)
    available = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def serialized(self):
        return {
            'title': self.title,
            'image': self.image,
            'link': self.get_absolute_url()
        }

    @classmethod
    def get_featured(cls):
        return cls.objects.filter(featured=True)

    @classmethod
    def get_products(cls, category_name):
        category = get_object_or_404(Category, kwargs={'name':category_name})
        return cls.objects.filter(category=category)

    @classmethod
    def get_search_results(cls, query, is_ajax=False):
        products = cls.objects.filter(
            title__istartswith=query
            ).order_by(Length('title').asc())
        if is_ajax:
            return {'products': [product.serialized() for product in products]}
        return products