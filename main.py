from indicators.fetch_all_indicators import fetch_all_indicators
from time import sleep
from binanceAPI.position_utilities import enter_long, enter_short
from data.data_functions import save_new_row, save_log
from binance.client import Client
from config import api_key, secret_key

mera_current_dataset_arr = []
position_types = [None, None]
tp_prices = [0, 0]
sl_prices = [0, 0]

current_price = 0
ema_100 = 0
macd_12 = 0
macd_26 = 0
rsi_6 = 0
indicator_array = []

client = Client(api_key, secret_key)

def close_position(index, state, file_path):
    global indicator_array
    tp_prices[index] = 0
    sl_prices[index] = 0
    position_types[index] = None
    save_new_row(file_path, state, indicator_array)

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
            close_position(0, "LONG", "./data/dataset-mera-1.csv")
            save_log("./data/result-mera-1.csv", date, "LONG", scikit_prediction, "LONG")
        elif current_price < sl_prices[0]:
            close_position(0, "SHORT", "./data/dataset-mera-1.csv")
            save_log("./data/result-mera-1.csv", date, "LONG", scikit_prediction, "SHORT")
    elif position_types[0] == "SHORT":
        if current_price < tp_prices[0]:
            close_position(0, "SHORT", "./data/dataset-mera-1.csv")
            save_log("./data/result-mera-1.csv", date, "SHORT", scikit_prediction, "SHORT")
        elif current_price > sl_prices[0]:
            close_position(0, "LONG", "./data/dataset-mera-1.csv")
            save_log("./data/result-mera-1.csv", date, "SHORT", scikit_prediction, "LONG")
    if position_types[1] == "LONG":
        if current_price > tp_prices[1]:
            close_position(1, "LONG", "./data/dataset-mera-2.csv")
            save_log("./data/result-mera-2.csv", date, "LONG", scikit_prediction, "LONG")
        elif current_price < sl_prices[1]:
            close_position(1, "SHORT", "./data/dataset-mera-2.csv")
            save_log("./data/result-mera-2.csv", date, "LONG", scikit_prediction, "SHORT")
    elif position_types[1] == "SHORT":
        if current_price < tp_prices[1]:
            close_position(1, "SHORT", "./data/dataset-mera-2.csv")
            save_log("./data/result-mera-2.csv", date, "SHORT", scikit_prediction, "SHORT")
        elif current_price > sl_prices[1]:
            close_position(1, "LONG", "./data/dataset-mera-2.csv")
            save_log("./data/result-mera-2.csv", date, "SHORT", scikit_prediction, "LONG")

    sleep(10)