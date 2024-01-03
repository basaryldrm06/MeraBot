from binance.client import Client
from binanceAPI.position_utilities import enter_long, enter_short
from config import api_key, secret_key
from indicators.fetch_all_indicators import fetch_all_indicators
from data.io_utilities import get_current_date_string, print_position_message
from data.IndicatorData import IndicatorData
from data import io_utilities
from time import sleep

# BinanceAPI Connection
client = Client(api_key, secret_key)

# Global Variable Declarations
tp_prices = [0, 0]
sl_prices = [0, 0]
do_not_enter_long = [0, 0]
do_not_enter_short = [0, 0]
position_types = [None, None]
current_price = 0
ema_100 = 0
macd_12 = 0
macd_26 = 0
rsi_6 = 0

# Greeting Message
print("Program successfully started")

# Initialization
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

# Main Algorithm
while True:
    indicatorDataObj = fetch_all_indicators(client)
    date = get_current_date_string()

    if position_types[0] == None:
        if (not do_not_enter_long[0]) and (macd_12 > macd_26) and \
          (macd_12 < 0) and (rsi_6 > 50) and (current_price < ema_100):
            do_not_enter_short[0] = False
            do_not_enter_long[0] = True
            tp_prices[0], sl_prices[0] = enter_long(client)
            print_position_message(indicatorDataObj, "LONG")
        elif (not do_not_enter_short[0]) and (macd_12 < macd_26) and \
          (macd_12 > 0) and (rsi_6 < 50) and (current_price > ema_100):
            do_not_enter_long[0] = False
            do_not_enter_short[0] = True
            tp_prices[0], sl_prices[0] = enter_short(client)
            print_position_message(indicatorDataObj, "SHORT")

    if position_types[1] == None:
        if (not do_not_enter_long[1]) and (macd_12 > macd_26) and \
          (macd_26 > 0) and (rsi_6 > 50) and (current_price > ema_100):
            do_not_enter_short[1] = False
            do_not_enter_long[1] = True
            tp_prices[1], sl_prices[1] = enter_long(client)
            print_position_message(indicatorDataObj, "LONG")
        elif (not do_not_enter_short[1]) and (macd_12 < macd_26) and \
          (macd_26 < 0) and (rsi_6 < 50) and (current_price < ema_100):
            do_not_enter_long[1] = False
            do_not_enter_short[1] = True
            tp_prices[1], sl_prices[1] = enter_short(client)
            print_position_message(indicatorDataObj, "SHORT")

    sleep(10)