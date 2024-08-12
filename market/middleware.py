import datetime
from django.utils import timezone
from .models import CurrentMetalPrice
from .metal_api import fetch_prices

class MetalPriceUpdateMiddleware:      #Custom Middleware that triggers an API call if there are no metal prices for the current date
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        today = timezone.now().date()
        latest_price = CurrentMetalPrice.objects.order_by('date').last()
        
        if not latest_price or latest_price.date < today:
            fetch_prices()

        response = self.get_response(request)
        return response