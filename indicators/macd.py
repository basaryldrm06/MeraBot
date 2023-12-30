import talib
import pandas as pd

def fetch_MACD(client, symbol, macd_value_length, signal_value_length, interval):
    klines = client.get_historical_klines(symbol, interval, "1 month ago UTC")

    df = pd.DataFrame(klines, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume',
                                       'close_time', 'quote_asset_volume', 'number_of_trades',
                                       'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume',
                                       'ignore'])

    df['close'] = df['close'].astype(float)
    macd, signal, _ = talib.MACD(df['close'], fastperiod=macd_value_length, slowperiod=signal_value_length,
                                 signalperiod=signal_value_length)

    return macd.iloc[-1], signal.iloc[-1]