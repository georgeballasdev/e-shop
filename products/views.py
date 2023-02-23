from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Product

def home(request):
    featured = Product.get_featured()
    return render(request, 'products/home.html', {'featured': featured})

def category(request, category_name):
    products = Product.get_products(category_name)
    return render(request, 'products/category.html', {'products': products})

def search(request):
    if request.method == 'GET':
        query = request.GET['query']
        if 'X-Requested-With' in request.headers: # AJAX
            return JsonResponse(Product.get_search_results(query, is_ajax=True))
        context =  {'products': Product.get_search_results(query), 'query': query}
        return render(request, 'products/search.html', context)

class ProductDetail(DetailView):
    model = Product
    template_name = 'products/detail.html'