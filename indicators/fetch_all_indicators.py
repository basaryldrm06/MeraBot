from indicators.rsi import fetch_RSI
from indicators.ema import fetch_EMA
from indicators.macd import fetch_MACD
from indicators.price import fetch_price
from indicators.bar_prices import get_historical_data
from data.io_utilities import get_current_date_string
from data.IndicatorData import IndicatorData

interval = "15m"
symbol = "ETHUSDT"

def fetch_all_indicators(client):
    date = get_current_date_string()
    price = fetch_price(client, "ETHUSDT")
    macd_12, macd_26 = fetch_MACD(client, symbol, 12, 26, interval)
    ema_100 = fetch_EMA(client, symbol, 100, interval)
    rsi_6 = fetch_RSI(client, symbol, 6, interval)
    bar_list = get_historical_data(client)

    indicatorDataObj = IndicatorData(date, price, macd_12, macd_26, ema_100, rsi_6, bar_list)

    return indicatorDataObj

