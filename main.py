from binance.client import Client
from binanceAPI.position_utilities import enter_long, enter_short
from config import api_key, secret_key
from indicators.fetch_all_indicators import fetch_all_indicators
from data.io_utilities import print_with_color
from data.IndicatorData import IndicatorData
from indicators.bar_prices import get_historical_data
from data import io_utilities
from time import sleep
from ai_modules.ai_voting import vote
from data.data_functions import save_position_infos, save_position_result
import copy

# BinanceAPI Connection
client = Client(api_key, secret_key)

indicator_position = None
indicator_check = None

tp_price = 0
sl_price = 0
do_not_enter_long = False
do_not_enter_short = False
on_long = False
on_short = False

while True:
    try:
        sleep(10)
        indicator_check = fetch_all_indicators(client)

        if not (on_long or on_short):
            if (indicator_check.macd_12 > indicator_check.macd_26) and \
                (indicator_check.macd_12 < 0) and (indicator_check.rsi_6 > 50) and \
                (indicator_check.price < indicator_check.ema_100):
                do_not_enter_short = False
                do_not_enter_long = True
                prediction = "LONG"
                if prediction == "LONG":
                    tp_price, sl_price = enter_long(client)

            elif (indicator_check.macd_12 < indicator_check.macd_26) and \
                (indicator_check.macd_12 > 0) and (indicator_check.rsi_6 < 50) and \
                (indicator_check.price > indicator_check.ema_100):
                do_not_enter_long = False
                do_not_enter_short = True
                prediction = "SHORT"
                if prediction == "SHORT":
                    tp_price, sl_price = enter_short(client)

        else:
            if (on_long and  indicator_check.price > tp_price) or \
                  (on_short and indicator_check.price < tp_price):
                close_position(True)
            elif (on_long and indicator_check.price < sl_price) or \
                  (on_short and indicator_check.price > sl_price):
                close_position(False)
    
    except Exception as e:
        error_message = str(e)
        print_with_color("yellow", error_message)