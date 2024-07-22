from metalpriceapi.client import Client

api_key = '92d9559404fbd0cad14dbfaf7cf74c44'
client = Client(api_key)


def CurrentMetalPrice():

    client.fetchLive(base='EUR', currencies=['XAU', 'XAG', 'XPD', 'XPT','XRH'])
    print(CurrentMetalPrice)