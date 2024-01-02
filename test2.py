from binance.client import Client
from datetime import datetime, timedelta
from config import api_key, secret_key

def get_historical_data(api_key, api_secret, symbol, interval='15m', limit=15):
    # Binance API client oluştur
    client = Client(api_key, api_secret)

    # Şu anki tarihi al
    end_time = datetime.now()

    # 15 mum önceki tarihi hesapla
    start_time = end_time - timedelta(minutes=15 * limit)

    # Tarih formatını Binance API için uygun formata çevir ve milisaniye cinsinden dönüştür
    start_time_ms = int(start_time.timestamp() * 1000)
    end_time_ms = int(end_time.timestamp() * 1000)

    # Geçmiş veriyi çek
    klines = client.get_klines(symbol=symbol, interval=interval, limit=limit, startTime=start_time_ms, endTime=end_time_ms)

    # Açılış, kapanış, en yüksek ve en düşük fiyatları içeren bir liste oluştur
    historical_data = [(float(kline[1]), float(kline[4]), float(kline[3]), float(kline[2])) for kline in klines]

    return historical_data

historical_data = get_historical_data(api_key, secret_key, "ETHUSDT")
print(historical_data)
