import sys
import os 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from indicators.price import fetch_price

def convert_usdt_to_coin(client, symbol, amount):
    return amount / fetch_price(client, symbol)

def get_account_balance(client):
    account_info = client.futures_account_balance()
    for item in account_info:
        if item['asset'] == 'USDT':
            return float(item['balance'])
    return 0.0

def enter_position(client, order_type, quantity, symbol):
    if order_type == "LONG":
        client.futures_create_order(symbol=symbol, quantity=quantity, type="MARKET", side="BUY", positionSide="LONG")

    elif order_type == "SHORT":
        client.futures_create_order(symbol=symbol, quantity=quantity, type="MARKET", side="SELL", positionSide="SHORT")

def place_tp_order(client, order_type, quantity, symbol, take_profit_price):
    if order_type == "LONG":
        client.futures_create_order(symbol=symbol, quantity=quantity, type='TAKE_PROFIT_MARKET',
                                    positionSide="LONG", firstTrigger="PLACE_ORDER",
                                    timeInForce="GTE_GTC", stopPrice=take_profit_price,
                                    side='SELL', secondTrigger="CANCEL_ORDER",
                                    workingType="MARK_PRICE", priceProtect='true')

    elif order_type == "SHORT":
        client.futures_create_order(symbol=symbol, quantity=quantity, type='TAKE_PROFIT_MARKET',
                                    positionSide="SHORT", firstTrigger="PLACE_ORDER",
                                    timeInForce="GTE_GTC", stopPrice=take_profit_price,
                                    side='BUY', secondTrigger="CANCEL_ORDER",
                                    workingType="MARK_PRICE", priceProtect='true')


def place_sl_order(client, order_type, quantity, symbol, stop_lose_price):
    if order_type == "LONG":
        client.futures_create_order(symbol=symbol, quantity=quantity, type='STOP_MARKET',
                                    positionSide="LONG", firstTrigger="PLACE_ORDER",
                                    timeInForce="GTE_GTC", stopPrice=stop_lose_price,
                                    side='SELL', secondTrigger="CANCEL_ORDER",
                                    workingType="MARK_PRICE", priceProtect='true')

    elif order_type == "SHORT":
        client.futures_create_order(symbol=symbol, quantity=quantity, type='STOP_MARKET',
                                    positionSide="SHORT", firstTrigger="PLACE_ORDER",
                                    timeInForce="GTE_GTC", stopPrice=stop_lose_price,
                                    side='BUY', secondTrigger="CANCEL_ORDER",
                                    workingType="MARK_PRICE", priceProtect='true')