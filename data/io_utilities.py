import datetime

def print_position_message(date, current_price, macd_12, macd_26, rsi_6, ema_100, position):
    print("DATE: " + str(date) + " PRICE: " + str(current_price) + " MACD_12: " + str(macd_12) + 
          " MACD_26: " + str(macd_26) + " EMA_100: " + str(ema_100) + " RSI_6: " + str(rsi_6) + 
          " Position " + str(position))
    
def get_current_date_string(format="%Y-%m-%d %H:%M:%S"):
    current_date = datetime.datetime.now()
    date_string = current_date.strftime(format)
    return date_string