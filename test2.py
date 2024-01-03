from indicators.bar_prices import get_historical_data
from config import api_key, secret_key
from binance.client import Client

client = Client(api_key, secret_key)

myList = get_historical_data(client)
print(myList)

print()

for element in myList:
    for tmp in element:
        print(tmp)