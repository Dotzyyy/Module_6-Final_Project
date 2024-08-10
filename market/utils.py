from decimal import Decimal
from datetime import date
from .models import CurrentMetalPrice

def final_metal_price(product,user):
    troy_to_gram = Decimal(31.1035)
    shorten_result = Decimal('0.01')
    current_metal_price = CurrentMetalPrice.objects.filter(date=date.today()).first()

    if hasattr(user, 'profile') and user.profile.account_type == 'wholesale':
        profit_margin = Decimal('1.06')  # 6% profit margin for wholesale users
    else:
        profit_margin = Decimal('1.20')  # 20% profit margin for personal users

    metal_price = None
    if current_metal_price:
        if product.metal_type == 'gold':
            if product.pk == 2:
                metal_price = (current_metal_price.gold_price * Decimal('0.375') / troy_to_gram).quantize(shorten_result)
            elif product.pk == 1:
                metal_price = (current_metal_price.gold_price * Decimal('0.750') / troy_to_gram).quantize(shorten_result)
            else:
                metal_price = (current_metal_price.gold_price / troy_to_gram).quantize(shorten_result)
        elif product.metal_type == 'silver':
            metal_price = (current_metal_price.silver_price / troy_to_gram).quantize(shorten_result)
        elif product.metal_type == 'platinum':
            metal_price = (current_metal_price.platinum_price / troy_to_gram).quantize(shorten_result)
        elif product.metal_type == 'palladium':
            metal_price = (current_metal_price.palladium_price / troy_to_gram).quantize(shorten_result)

        metal_price = (metal_price * profit_margin).quantize(shorten_result)

    return metal_price