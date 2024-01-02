from datetime import datetime, timedelta

def get_historical_data(client, interval='15m', limit=15):
    end_time = datetime.now()
    start_time = end_time - timedelta(minutes=15 * limit)
    start_time_ms = int(start_time.timestamp() * 1000)
    end_time_ms = int(end_time.timestamp() * 1000)

    klines = client.get_klines(symbol="ETHUSDT", interval=interval, limit=limit, startTime=start_time_ms, endTime=end_time_ms)
    historical_data = [(float(kline[1]), float(kline[4]), float(kline[3]), float(kline[2])) for kline in klines]

    return historical_data