class IndicatorData:
    def __init__(self, date, current_price, macd_12, macd_26, rsi_6, ema_100):
        self.date = date
        self.current_price = current_price
        self.macd_12 = macd_12
        self.macd_26 = macd_26
        self.rsi_6 = rsi_6
        self.ema_100 = ema_100