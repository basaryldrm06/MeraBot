from binanceAPI.account_utilities import get_account_balance, convert_usdt_to_coin, enter_position, place_tp_order, place_sl_order
import sys
import os 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from indicators.price import fetch_price
from config import coin_precision, tp_percentage, sl_percentage, test_mode

def enter_long(client):
    account_balance = get_account_balance(client)
    coin_amount = convert_usdt_to_coin(client, "ETHUSDT", account_balance * (95 / 100)) 
    coin_price = fetch_price(client, "ETHUSDT")

    tp_price = float(round(coin_price * (1 + tp_percentage), coin_precision))
    sl_price = float(round(coin_price * (1 - sl_percentage), coin_precision))

    if not test_mode:
        enter_position(client, "LONG", coin_amount, "ETHUSDT")
        place_tp_order(client, "LONG", coin_amount, "ETHUSDT", tp_price)
        place_sl_order(client, "LONG", coin_amount, "ETHUSDT", sl_price)

    return tp_price, sl_price

def enter_short(client):
    account_balance = get_account_balance(client)
    coin_amount = convert_usdt_to_coin(client, "ETHUSDT", account_balance * (95 / 100)) 
    coin_price = fetch_price(client, "ETHUSDT")
    
    tp_price = float(round(coin_price * (1 - tp_percentage), coin_precision))
    sl_price = float(round(coin_price * (1 + sl_percentage), coin_precision))

    if not test_mode:
        enter_position(client, "SHORT", coin_amount, "ETHUSDT")
        place_tp_order(client, "SHORT", coin_amount, "ETHUSDT", tp_price)
        place_sl_order(client, "SHORT", coin_amount, "ETHUSDT", sl_price)

    return tp_price, sl_price