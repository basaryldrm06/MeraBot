from binance.client import Client
from binanceAPI.position_utilities import enter_long, enter_short
from config import api_key, secret_key
from indicators.fetch_all_indicators import fetch_all_indicators
from data.io_utilities import get_current_date_string, print_position_message
from data.IndicatorData import IndicatorData
from indicators.bar_prices import get_historical_data
from data import io_utilities
from time import sleep
from ai_modules.ai_voting import vote
from data.data_functions import save_position_infos, save_position_result

# BinanceAPI Connection
client = Client(api_key, secret_key)

# Global Variable Declarations
indicatorDataObj = [None, None, None]

tp_prices = [0, 0]
sl_prices = [0, 0]
do_not_enter_long = [0, 0]
do_not_enter_short = [0, 0]
position_types = [None, None]

scikit_predictions = [None, None]
tensorflow_predictions = [None, None]
pytorch_predictions = [None, None]
overall_predictions = [None, None]

# Global method Declarations
def handle_position_closure(index):
    global position_types
    position_types[index] = None    

# Greeting Message
print("Program successfully started")

# Initialization
indicatorDataObj[2] = fetch_all_indicators(client)
if (indicatorDataObj[2].macd_12 > indicatorDataObj[2].macd_26) and \
  (indicatorDataObj[2].macd_12 < 0):
    do_not_enter_long[0] = True
    print("LONG 0 is blocked")
elif (indicatorDataObj[2].macd_12 > indicatorDataObj[2].macd_26) and \
  (indicatorDataObj[2].macd_26 > 0):
    do_not_enter_long[1] = True
    print("LONG 1 is blocked")
elif (indicatorDataObj[2].macd_12 < indicatorDataObj[2].macd_26) and \
  (indicatorDataObj[2].macd_12 > 0):
    do_not_enter_short[0] = True
    print("SHORT 0 is blocked")
elif (indicatorDataObj[2].macd_12 < indicatorDataObj[2].macd_26) and \
  (indicatorDataObj[2].macd_26 < 0):
    do_not_enter_short[1] = True
    print("SHORT 1 is blocked")

# Main Algorithm
while True:
    try:
        indicatorDataObj[2] = fetch_all_indicators(client)

        # Check if the position has arrived
        if (not do_not_enter_long[0]) and (indicatorDataObj[2].macd_12 > indicatorDataObj[2].macd_26) and \
          (indicatorDataObj[2].macd_12 < 0) and (indicatorDataObj[2].rsi_6 > 50) and \
          (indicatorDataObj[2].price < indicatorDataObj[2].ema_100):
            do_not_enter_short[0] = False
            do_not_enter_long[0] = True
            if position_types[0] == None:  
                position_types[0] = "LONG"
                indicatorDataObj[0] = indicatorDataObj[2].copy()
                indicatorDataObj[0].bar_list = get_historical_data(client)
                scikit_predictions[0], tensorflow_predictions[0], pytorch_predictions[0], overall_predictions[0] = \
                    vote("./data/dataset-mera-1.csv", indicatorDataObj[0])
                if overall_predictions[0] == "LONG":
                    tp_prices[0], sl_prices[0] = enter_long(client, True)
                    print_position_message(indicatorDataObj[0], "LONG", True)
                else:
                    tp_prices[0], sl_prices[0] = enter_long(client, False)
                    print_position_message(indicatorDataObj[0], "LONG", False)

        elif (not do_not_enter_short[0]) and (indicatorDataObj[2].macd_12 < indicatorDataObj[2].macd_26) and \
          (indicatorDataObj[2].macd_12 > 0) and (indicatorDataObj[2].rsi_6 < 50) and  \
          (indicatorDataObj[2].price > indicatorDataObj[2].ema_100):
            do_not_enter_long[0] = False
            do_not_enter_short[0] = True
            if position_types[0] == None:
                position_types[0] = "SHORT"
                indicatorDataObj[0] = indicatorDataObj[2].copy()
                indicatorDataObj[0].bar_list = get_historical_data(client)
                scikit_predictions[0], tensorflow_predictions[0], pytorch_predictions[0], overall_predictions[0] = \
                    vote("./data/dataset-mera-1.csv", indicatorDataObj[0])
                if overall_predictions[0] == "SHORT":
                    tp_prices[0], sl_prices[0] = enter_short(client, True)
                    print_position_message(indicatorDataObj[0], "SHORT", True)
                else:
                    tp_prices[0], sl_prices[0] = enter_short(client, False)
                    print_position_message(indicatorDataObj[0], "SHORT", False)

        if (not do_not_enter_long[1]) and (indicatorDataObj[2].macd_12 > indicatorDataObj[2].macd_26) and \
          (indicatorDataObj[2].macd_26 > 0) and (indicatorDataObj[2].rsi_6 > 50) and \
          (indicatorDataObj[2].current_price > indicatorDataObj[2].ema_100):
            do_not_enter_short[1] = False
            do_not_enter_long[1] = True
            if position_types[1] == None:
                position_types[1] = "LONG"
                indicatorDataObj[1] = indicatorDataObj[2].copy()
                indicatorDataObj[1].bar_list = get_historical_data(client)
                scikit_predictions[1], tensorflow_predictions[1], pytorch_predictions[1], overall_predictions[1] = \
                    vote("./data/dataset-mera-2.csv", indicatorDataObj[1])
                if overall_predictions[1] == "LONG":
                    tp_prices[1], sl_prices[1] = enter_long(client, True)
                    print_position_message(indicatorDataObj[1], "LONG", True)
                else:
                    tp_prices[1], sl_prices[1] = enter_long(client, False)
                    print_position_message(indicatorDataObj[1], "LONG", False)

        elif (not do_not_enter_short[1]) and (indicatorDataObj[2].macd_12 < indicatorDataObj[2].macd_26) and \
          (indicatorDataObj[2].macd_26 < 0) and (indicatorDataObj[2].rsi_6 < 50) and \
          (indicatorDataObj[2].price < indicatorDataObj[2].ema_100):
            do_not_enter_long[1] = False
            do_not_enter_short[1] = True
            if position_types[1] == None:
                position_types[0] = "SHORT"
                indicatorDataObj[1] = indicatorDataObj[2].copy()
                indicatorDataObj[1].bar_list = get_historical_data(client)
                scikit_predictions[1], tensorflow_predictions[1], pytorch_predictions[1], overall_predictions[1] = \
                    vote("./data/dataset-mera-2.csv", indicatorDataObj[1])
                if overall_predictions[1] == "SHORT":
                    tp_prices[1], sl_prices[1] = enter_short(client, True)
                    print_position_message(indicatorDataObj[1], "SHORT", True)
                else:
                    tp_prices[1], sl_prices[1] = enter_short(client, False)
                    print_position_message(indicatorDataObj[1], "SHORT", False)

        # Check if the position is closed or not
        if not (position_types[0] == None):
            if position_types[0] == "LONG":
                if indicatorDataObj[2].price > tp_prices[0]:
                    print("Your Position (LONG 0) is closed with TP")
                    handle_position_closure(0)
                    save_position_infos("./data/dataset-mera-1.csv", "LONG", indicatorDataObj[0])
                    save_position_result(".data/result-mera-1.csv", indicatorDataObj.date , "LONG", 
                                        overall_predictions[0], scikit_predictions[0], 
                                        pytorch_predictions[0], tensorflow_predictions[0])
                elif indicatorDataObj[2].price < sl_prices[0]:
                    print("Your Position (LONG 0) is closed with SL")
                    handle_position_closure(0)
                    save_position_infos("./data/dataset-mera-1.csv", "SHORT", indicatorDataObj[0])
                    save_position_result(".data/result-mera-1.csv", indicatorDataObj.date , "SHORT", 
                                        overall_predictions[0], scikit_predictions[0], 
                                        pytorch_predictions[0], tensorflow_predictions[0])
            if position_types[0] == "SHORT":
                if indicatorDataObj[2].price < tp_prices[0]:
                    print("Your Position (SHORT 0) is closed with TP")
                    handle_position_closure(0)
                    save_position_infos("./data/dataset-mera-1.csv", "SHORT", indicatorDataObj[0])
                    save_position_result(".data/result-mera-1.csv", indicatorDataObj.date , "SHORT", 
                                        overall_predictions[0], scikit_predictions[0], 
                                        pytorch_predictions[0], tensorflow_predictions[0])
                elif indicatorDataObj[2].price > sl_prices[0]:
                    print("Your Position (SHORT 0) is closed with SL")
                    handle_position_closure(0)
                    save_position_infos("./data/dataset-mera-1.csv", "LONG", indicatorDataObj[0])
                    save_position_result(".data/result-mera-1.csv", indicatorDataObj.date , "LONG", 
                                        overall_predictions[0], scikit_predictions[0], 
                                        pytorch_predictions[0], tensorflow_predictions[0])
        if not (position_types[1] == None):
            if position_types[1] == "LONG":
                if indicatorDataObj[2].price > tp_prices[1]:
                    print("Your Position (LONG 1) is closed with TP")
                    handle_position_closure(1)
                    save_position_infos("./data/dataset-mera-2.csv", "LONG", indicatorDataObj[1])
                    save_position_result(".data/result-mera-2.csv", indicatorDataObj.date , "LONG", 
                                        overall_predictions[1], scikit_predictions[1], 
                                        pytorch_predictions[1], tensorflow_predictions[1])
                elif indicatorDataObj[2].price < sl_prices[1]:
                    print("Your Position (LONG 1) is closed with SL")
                    handle_position_closure(1)
                    save_position_infos("./data/dataset-mera-2.csv", "SHORT", indicatorDataObj[1])
                    save_position_result(".data/result-mera-2.csv", indicatorDataObj.date , "SHORT", 
                                        overall_predictions[1], scikit_predictions[1], 
                                        pytorch_predictions[1], tensorflow_predictions[1])
            if position_types[1] == "SHORT":
                if indicatorDataObj[2].price < tp_prices[1]:
                    print("Your Position (SHORT 1) is closed with TP")
                    handle_position_closure(1)
                    save_position_infos("./data/dataset-mera-2.csv", "SHORT", indicatorDataObj[1])
                    save_position_result(".data/result-mera-2.csv", indicatorDataObj.date , "SHORT", 
                                        overall_predictions[1], scikit_predictions[1], 
                                        pytorch_predictions[1], tensorflow_predictions[1])
                elif indicatorDataObj[2].price > sl_prices[1]:
                    print("Your Position (SHORT 1) is closed with SL")
                    handle_position_closure(1)
                    save_position_infos("./data/dataset-mera-2.csv", "LONG", indicatorDataObj[1])
                    save_position_result(".data/result-mera-2.csv", indicatorDataObj.date , "LONG", 
                                        overall_predictions[1], scikit_predictions[1], 
                                        pytorch_predictions[1], tensorflow_predictions[1])
    except:
        print("Some kind of error has occured")
    sleep(10)