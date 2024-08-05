import logging
from metalpriceapi.client import Client


logger = logging.getLogger(__name__)

def fetch_prices_test():
        api_key = 'METAL_API_KEY'
        client = Client(api_key)
        client.fetchLive(base='EUR', currencies=['XAU', 'XAG', 'XPT', 'XPD', 'XRH'])
        logger.info(f"API Response: {client}")

