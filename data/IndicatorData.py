class IndicatorData:
    def __init__(self, date, price, macd_12, macd_26, ema_100, rsi_6, bar_list):
        self.date = date
        self.price = price
        self.macd_12 = macd_12
        self.macd_26 = macd_26
        self.rsi_6 = rsi_6
        self.ema_100 = ema_100
        self.bar_list = bar_list