import logging
import os
from decimal import Decimal, InvalidOperation
from metalpriceapi.client import Client
from .models import CurrentMetalPrice


logger = logging.getLogger(__name__)

def fetch_prices():
    api_key = (os.getenv('METAL_API_KEY'))
    client = Client(api_key)
    print(os.getenv('METAL_API_KEY'))

    try:
        response = client.fetchLive(base='EUR', currencies=['XAU', 'XAG', 'XPT', 'XPD'])

        logger.info("API Response: %s", response)

        if not response.get('success'):
            raise ValueError("API request was not successful")

        rates = response.get('rates', {})

        # Extract prices from the response
        gold_price = rates.get('EURXAU')
        silver_price = rates.get('EURXAG')
        platinum_price = rates.get('EURXPT')
        palladium_price = rates.get('EURXPD')
        

        # Convert to Decimal and handle potential errors
        def to_decimal(value):
            try:
                return Decimal(value)
            except (ValueError, InvalidOperation):
                return Decimal('0')

        gold_price = to_decimal(gold_price)
        silver_price = to_decimal(silver_price)
        platinum_price = to_decimal(platinum_price)
        palladium_price = to_decimal(palladium_price)

        # Save prices to the database
        CurrentMetalPrice.objects.create(
            gold_price=gold_price,
            silver_price=silver_price,
            platinum_price=platinum_price,
            palladium_price=palladium_price,
        )
            

        logger.info("Prices have been updated successfully.")

    except Exception as e:
            logger.error("Error fetching prices: %s", str(e))
       


