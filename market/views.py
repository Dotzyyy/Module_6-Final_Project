from django.shortcuts import render, get_object_or_404
from .models import Product, CurrentMetalPrice
from datetime import date
import logging
from decimal import Decimal
# Create your views here.

logger = logging.getLogger(__name__)

def home(request):
    products = Product.objects.all()
    return render(request, 'market/home.html', {'products': products})

def about(request):
    return render (request, 'market/about.html')

def product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    current_metal_price = CurrentMetalPrice.objects.filter(date=date.today()).first() # objects.order_by('-date').first()


    troy_to_gram = Decimal(31.1035)

    shorten_result = Decimal('0.01')


    metal_price = None
    if current_metal_price:
        if product.metal_type == 'gold':
            if product.pk == 2:
                metal_price = (current_metal_price.gold_price * Decimal('0.375') / troy_to_gram ).quantize(shorten_result)
            elif product.pk == 1:
                metal_price = (current_metal_price.gold_price * Decimal('0.750') / troy_to_gram ).quantize(shorten_result)
            else:    
                metal_price = (current_metal_price.gold_price / troy_to_gram ).quantize(shorten_result)
        elif product.metal_type == 'silver':
            metal_price = (current_metal_price.silver_price / troy_to_gram).quantize(shorten_result)
        elif product.metal_type == 'platinum':
            metal_price = (current_metal_price.platinum_price / troy_to_gram).quantize(shorten_result)
        elif product.metal_type == 'palladium':
            metal_price = (current_metal_price.palladium_price / troy_to_gram).quantize(shorten_result)

    logger.debug(f"Product: {product.name}, Metal Type: {product.metal_type}, Metal Price: {metal_price}")        

    context = {
        'product': product,
        'metal_price': metal_price,
    }
    return render(request, 'market/product.html', context)
