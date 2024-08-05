from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def home(request):
    products = Product.objects.all()
    return render(request, 'market/home.html', {'products': products})

def about(request):
    return render (request, 'market/about.html')

def product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'market/product.html', {'product': product})
