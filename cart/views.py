from django.shortcuts import render, redirect, get_object_or_404
from .models import CheckoutItem
from market.models import Product
from market.utils import final_metal_price
from decimal import Decimal
# Create your views here.



def view_cart(request):
    checkout_items = CheckoutItem.objects.filter(user=request.user)

   
    cart_items = [
        {
            'pk' : item.pk,
            'product': item.product,
            'weight': item.weight,
            'metal_price': final_metal_price(item.product, request.user),
            'total_price': final_metal_price(item.product, request.user) * item.weight
        }
        for item in checkout_items
    ]

    
    final_price = sum(item['total_price'] for item in cart_items)
    vat_price = final_price * (Decimal(1.23)) #Price with Irish VAT

    vat_price = vat_price.quantize(Decimal('0.01'))

   
    context = {
        'checkout_items': cart_items,
        'final_price': final_price,
        'vat_price': vat_price,
    }

    return render(request, 'cart/checkout.html', context)

def add_item(request, pk):
    product = Product.objects.get(pk=pk)
    weight = request.GET.get('weight', 1)
    
    checkout_item, created = CheckoutItem.objects.get_or_create(product=product,user=request.user)
    checkout_item.weight += Decimal(weight)
    checkout_item.save()
    return redirect('cart:view-cart')

def remove_item(request, pk):
    checkout_item = get_object_or_404(CheckoutItem, pk=pk, user=request.user)
    checkout_item.delete()
    return redirect('cart:view-cart')


def order_confirmed(request):
    checkout_items = CheckoutItem.objects.filter(user=request.user)

   
    cart_items = [
        {
            'pk' : item.pk,
            'product': item.product,
            'weight': item.weight,
            'metal_price': final_metal_price(item.product, request.user),
            'total_price': final_metal_price(item.product, request.user) * item.weight
        }
        for item in checkout_items
    ]

    
    final_price = sum(item['total_price'] for item in cart_items)
    vat_price = final_price * (Decimal(1.23)) #Price with Irish VAT

    vat_price = vat_price.quantize(Decimal('0.01'))

   
    context = {
        'checkout_items': cart_items,
        'final_price': final_price,
        'vat_price': vat_price,
    }

    
    return render(request,'cart/order_confirmed.html', context)


def clear_cart(request):
    """View to clear the user's cart and redirect to the product page."""
    CheckoutItem.objects.filter(user=request.user).delete() 
    return redirect('all-products') 