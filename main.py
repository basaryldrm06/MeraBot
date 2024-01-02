from indicators.fetch_all_indicators import fetch_all_indicators
from indicators.IndicatorData import IndicatorData
from time import sleep
from binanceAPI.position_utilities import enter_long, enter_short
from data.data_functions import save_new_row, save_log
from binance.client import Client
from config import api_key, secret_key
from ai_modules.ai_voting import vote 
import datetime
from data import io_utilities

position_types = [None, None]
tp_prices = [0, 0]
sl_prices = [0, 0]
scikit_predictions = [0, 0]
tensorflow_predictions = [0, 0]
pytorch_predictions = [0, 0]
vote_results = [0 , 0]
do_not_enter_long = [0, 0]
do_not_enter_short = [0, 0]

current_price = 0
ema_100 = 0
macd_12 = 0
macd_26 = 0
rsi_6 = 0
indicator_array = []

client = Client(api_key, secret_key)

print("Program successfully started")

def close_position(index, state, file_path):
    global indicator_array
    tp_prices[index] = 0
    sl_prices[index] = 0
    position_types[index] = None
    save_new_row(file_path, state, indicator_array)

def modify_global_array(new_element):
    global indicator_object_array
    indicator_object_array.insert(0, new_element)
    
    if len(indicator_object_array) >= 1351:
        del indicator_object_array[1350]

def get_current_date_string(format="%Y-%m-%d %H:%M:%S"):
    current_date = datetime.datetime.now()
    date_string = current_date.strftime(format)
    return date_string

# INITIALIZATION
current_price, macd_12, macd_26, rsi_6, ema_100 = fetch_all_indicators(client)
if (macd_12 > macd_26) and (macd_12 < 0):
    do_not_enter_long[0] = True
elif (macd_12 > macd_26) and (macd_26 > 0):
    do_not_enter_long[1] = True
elif (macd_12 < macd_26) and (macd_12 > 0):
    do_not_enter_short[0] = True
elif (macd_12 < macd_26) and (macd_26 < 0):
    do_not_enter_short[1] = True

# MAIN ALGORITHM
while True:
    current_price, macd_12, macd_26, rsi_6, ema_100 = fetch_all_indicators(client)
    date = get_current_date_string()
    print("Line 69")
    io_utilities.print_position_message(date, current_price, macd_12, macd_26, rsi_6, ema_100, "LONG")

    if position_types[0] == None:
        if (not do_not_enter_long[0]) and (macd_12 > macd_26) and (macd_12 < 0) and (rsi_6 > 50) and (current_price < ema_100):
            do_not_enter_short[0] = False
            do_not_enter_long[0] = True
            scikit_predictions[0], tensorflow_predictions[0], pytorch_predictions[0], vote_results[0] = vote("./data/dataset-mera-1.csv", date, current_price, macd_12, macd_26, ema_100, rsi_6, list)
            position_types[0] = "LONG"
            io_utilities.print_position_message(date, current_price, macd_12, macd_26, rsi_6, ema_100, "LONG")
            if vote_results[0] == "LONG":
                tp_prices[0], sl_prices[0] = enter_long(client)
                
        elif (not do_not_enter_short[0]) and (macd_12 < macd_26) and (macd_12 > 0) and (rsi_6 < 50) and (current_price > ema_100):
            do_not_enter_long[0] = False
            do_not_enter_short[0] = True
            scikit_predictions[0], tensorflow_predictions[0], pytorch_predictions[0], vote_results[0] = vote("./data/dataset-mera-1.csv", date, current_price, macd_12, macd_26, ema_100, rsi_6, list)
            position_types[0] = "SHORT"
            io_utilities.print_position_message(date, current_price, macd_12, macd_26, rsi_6, ema_100, "SHORT")
            if vote_results[0] == "SHORT":
                tp_prices[0], sl_prices[0] = enter_short(client)
    if position_types[1] == None:
        if (not do_not_enter_long[1]) and (macd_12 > macd_26) and (macd_26 > 0) and (rsi_6 > 50) and (current_price > ema_100):
            do_not_enter_short[1] = False
            do_not_enter_long[1] = True
            scikit_predictions[1], tensorflow_predictions[1], pytorch_predictions[1], vote_results[1] = vote("./data/dataset-mera-2.csv", date, current_price, macd_12, macd_26, ema_100, rsi_6, list)
            position_types[1] = "LONG"
            io_utilities.print_position_message(date, current_price, macd_12, macd_26, rsi_6, ema_100, "LONG")
            if vote_results[1] == "LONG":
                tp_prices[1], sl_prices[1] = enter_long(client)
        elif (not do_not_enter_short[1]) and (macd_12 < macd_26) and (macd_26 < 0) and (rsi_6 < 50) and (current_price < ema_100):
            do_not_enter_long[1] = False
            do_not_enter_short[1] = True
            scikit_predictions[1], tensorflow_predictions[1], pytorch_predictions[1], vote_results[1] = vote("./data/dataset-mera-2.csv", date, current_price, macd_12, macd_26, ema_100, rsi_6, list)
            position_types[1] = "SHORT"
            io_utilities.print_position_message(date, current_price, macd_12, macd_26, rsi_6, ema_100, "SHORT")
            if vote_results[1] == "SHORT":
                tp_prices[1], sl_prices[1] = enter_short(client)

    if position_types[0] == "LONG":
        if current_price > tp_prices[0]:
            close_position(0, "LONG", "./data/dataset-mera-1.csv")
            save_log("./data/result-mera-1.csv", date, "LONG", scikit_predictions[0], tensorflow_predictions[0], pytorch_predictions[0], vote_results[0], "LONG")
        elif current_price < sl_prices[0]:
            close_position(0, "SHORT", "./data/dataset-mera-1.csv")
            save_log("./data/result-mera-1.csv", date, "LONG", scikit_predictions[0], tensorflow_predictions[0], pytorch_predictions[0], vote_results[0], "SHORT")
    elif position_types[0] == "SHORT":
        if current_price < tp_prices[0]:
            close_position(0, "SHORT", "./data/dataset-mera-1.csv")
            save_log("./data/result-mera-1.csv", date, "SHORT", scikit_predictions[0], tensorflow_predictions[0], pytorch_predictions[0], vote_results[0], "SHORT")
        elif current_price > sl_prices[0]:
            close_position(0, "LONG", "./data/dataset-mera-1.csv")
            save_log("./data/result-mera-1.csv", date, "SHORT", scikit_predictions[0], tensorflow_predictions[0], pytorch_predictions[0], vote_results[0], "LONG")
    if position_types[1] == "LONG":
        if current_price > tp_prices[1]:
            close_position(1, "LONG", "./data/dataset-mera-2.csv")
            save_log("./data/result-mera-2.csv", date, "LONG", scikit_predictions[1], tensorflow_predictions[1], pytorch_predictions[1], vote_results[1], "LONG")
        elif current_price < sl_prices[1]:
            close_position(1, "SHORT", "./data/dataset-mera-2.csv")
            save_log("./data/result-mera-2.csv", date, "LONG", scikit_predictions[1], tensorflow_predictions[1], pytorch_predictions[1], vote_results[1], "SHORT")
    elif position_types[1] == "SHORT":
        if current_price < tp_prices[1]:
            close_position(1, "SHORT", "./data/dataset-mera-2.csv")
            save_log("./data/result-mera-2.csv", date, "SHORT", scikit_predictions[1], tensorflow_predictions[1], pytorch_predictions[1], vote_results[1], "SHORT")
        elif current_price > sl_prices[1]:
            close_position(1, "LONG", "./data/dataset-mera-2.csv")
            save_log("./data/result-mera-2.csv", date, "SHORT", scikit_predictions[1], tensorflow_predictions[1], pytorch_predictions[1], vote_results[1], "LONG")

    sleep(10)