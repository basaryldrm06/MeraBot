import talib
import pandas as pd

def fetch_EMA(client, symbol, ema_value, interval):
    klines = client.get_historical_klines(symbol, interval, "1 month ago UTC")

    df = pd.DataFrame(klines, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume',
                                       'close_time', 'quote_asset_volume', 'number_of_trades',
                                       'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume',
                                       'ignore'])

    df['close'] = df['close'].astype(float)
    ema = talib.EMA(df['close'], timeperiod=ema_value)

    return ema.iloc[-1]