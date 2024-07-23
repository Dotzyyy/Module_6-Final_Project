from metalpriceapi.client import Client

api_key = 'METAL_API_KEY'
client = Client(api_key)


def CurrentMetalPrice():

    client.fetchLive(base='EUR', currencies=['XAU', 'XAG', 'XPD', 'XPT','XRH'])
    print(CurrentMetalPrice)