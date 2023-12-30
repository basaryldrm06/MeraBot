from rsi import fetch_RSI
from ema import fetch_EMA
from macd import fetch_MACD
from price import fetch_price

interval = "15m"
symbol = "ETHUSDT"

def fetch_all_indicators(client):
    macd_12, macd_26 = fetch_MACD(client, symbol, 12, 26, interval)
    ema_100 = fetch_EMA(client, symbol, 100, interval)
    rsi_6 = fetch_RSI(client, symbol, 6, interval)
    current_price = fetch_price(client, "ETHUSDT")

    return current_price, macd_12, macd_26, ema_100, rsi_6

