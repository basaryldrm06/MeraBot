import talib
import pandas as pd

def fetch_RSI(client, symbol, rsi_value_length, interval):
    klines = client.get_historical_klines(symbol, interval, "1 month ago UTC")

    df = pd.DataFrame(klines, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume',
                                       'close_time', 'quote_asset_volume', 'number_of_trades',
                                       'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume',
                                       'ignore'])

    df['close'] = df['close'].astype(float)
    return talib.RSI(df['close'], timeperiod=rsi_value_length).iloc[-1]