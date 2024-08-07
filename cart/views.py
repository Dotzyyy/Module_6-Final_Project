from django.shortcuts import render, redirect
from .models import CheckoutItem
from market.models import Product
from market.utils import final_metal_price
from decimal import Decimal
# Create your views here.



def view_cart(request):
    checkout_items = CheckoutItem.objects.filter(user=request.user)

    # Prepare the cart items with their calculated metal prices
    cart_items = [
        {
            'product': item.product,
            'quantity': item.quantity,
            'metal_price': final_metal_price(item.product),
            'total_price': final_metal_price(item.product) * item.quantity
        }
        for item in checkout_items
    ]

    # Calculate the final price for all items in the cart
    final_price = sum(item['total_price'] for item in cart_items)
    vat_price = final_price * (Decimal(1.23)) #Price with Irish VAT

    vat_price = vat_price.quantize(Decimal('0.01'))

    # Create context for rendering
    context = {
        'checkout_items': cart_items,
        'final_price': final_price,
        'vat_price': vat_price,
    }

    return render(request, 'cart/checkout.html', context)

def add_item(request, pk):
    product = Product.objects.get(pk=pk)
    checkout_item, created = CheckoutItem.objects.get_or_create(product=product,user=request.user)
    checkout_item.quantity += 1
    checkout_item.save()
    return redirect('cart:view-cart')

def remove_item(request, pk):
    checkout_item = CheckoutItem.objects.get(pk=pk)
    checkout_item.delete()
    return redirect('cart:view-cart')

