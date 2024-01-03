from binance.client import Client
from config import api_key, secret_key
from indicators.fetch_all_indicators import fetch_all_indicators

# BinanceAPI Connection
client = Client(api_key, secret_key)

# Global Variable Declarations
tp_prices = [0, 0]
sl_prices = [0, 0]
do_not_enter_long = [0, 0]
do_not_enter_short = [0, 0]
current_price = 0
ema_100 = 0
macd_12 = 0
macd_26 = 0
rsi_6 = 0

# Greeting Message
print("Program successfully started")

# INITIALIZATION
current_price, macd_12, macd_26, rsi_6, ema_100 = fetch_all_indicators(client)
if (macd_12 > macd_26) and (macd_12 < 0):
    do_not_enter_long[0] = True
    print("LONG 0 is blocked")
elif (macd_12 > macd_26) and (macd_26 > 0):
    do_not_enter_long[1] = True
    print("LONG 1 is blocked")
elif (macd_12 < macd_26) and (macd_12 > 0):
    do_not_enter_short[0] = True
    print("SHORT 0 is blocked")
elif (macd_12 < macd_26) and (macd_26 < 0):
    do_not_enter_short[1] = True
    print("SHORT 1 is blocked")