from django.shortcuts import render, get_object_or_404
from .models import Product
import logging
from .utils import final_metal_price

# Create your views here.

logger = logging.getLogger(__name__)

def home(request):
    products = Product.objects.all()
    return render(request, 'market/home.html', {'products': products})

def about(request):
    return render (request, 'market/about.html')

#View that displays a given product using pk id and the matching metal price
def product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    metal_price = final_metal_price(product, request.user)

    logger.debug(f"Product: {product.name}, Metal Type: {product.metal_type}, Metal Price: {metal_price}")

    context = {
        'product': product,
        'metal_price': metal_price,
    }
    return render(request, 'market/product.html', context)

# View that displays a list of all the products. Seperate from the list seen on the homepage.

def all_products(request):
    products = Product.objects.all()
    product_list = [
        {
            'product': product,
            'metal_price': final_metal_price(product, request.user)
        }
        for product in products
    ]

    return render(request, 'market/all_products.html', {'product_list': product_list})
