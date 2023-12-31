from indicators.fetch_all_indicators import fetch_all_indicators
from time import sleep
from binanceAPI.position_utilities import enter_long, enter_short

mera_current_dataset_arr = []
position_types = [None, None]
tp_prices = [0, 0]
sl_prices = [0, 0]

current_price = 0
ema_100 = 0
macd_12 = 0
macd_26 = 0
rsi_6 = 0
 
client = None

def close_position(index):
    tp_prices[index] = 0
    sl_prices[index] = 0
    position_types[index] = None

while True:
    current_price, macd_12, macd_26, rsi_6, ema_100 = fetch_all_indicators(client)

    if position_types[0] == None:
        if (macd_12 > macd_26) and (macd_12 < 0) and (rsi_6 > 50) and (current_price < ema_100):
            tp_prices[0], sl_prices[0] = enter_long(client)
            position_types[0] = "LONG"
        elif (macd_12 < macd_26) and (macd_12 > 0) and (rsi_6 < 50) and (current_price > ema_100):
            tp_prices[0], sl_prices[0] = enter_short(client)
            position_types[0] = "SHORT"
    if position_types[1] == None:
        if (macd_12 > macd_26) and (macd_26 > 0) and (rsi_6 > 50) and (current_price > ema_100):
            tp_prices[1], sl_prices[1] = enter_long(client)
            position_types[1] = "LONG"
        elif (macd_12 < macd_26) and (macd_26 < 0) and (rsi_6 < 50) and (current_price < ema_100):
            tp_prices[1], sl_prices[1] = enter_short(client)
            position_types[1] = "SHORT"

    if position_types[0] == "LONG":
        if current_price > tp_prices[0]:
            save_data()
            close_position(0)
        elif current_price < sl_prices[0]:
            save_data()
            close_position(0)
    elif position_types[0] == "SHORT":
        if current_price < tp_prices[0]:
            save_data()
            close_position(0)
        elif current_price > sl_prices[0]:
            save_data()
            close_position(0)
    if position_types[1] == "LONG":
        if current_price > tp_prices[1]:
            save_data()
            close_position(1)
        elif current_price < sl_prices[1]:
            save_data()
            close_position(1)
    elif position_types[1] == "SHORT":
        if current_price < tp_prices[1]:
            save_data()
            close_position(1)
        elif current_price > sl_prices[1]:
            save_data()
            close_position(1)

    sleep(5)