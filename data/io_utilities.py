import datetime

def print_position_message(indicatorDataObj, position, is_pseudo):
    print("DATE: " + str(indicatorDataObj.date) + 
          " PRICE: " + str(indicatorDataObj.price) + 
          " MACD_12: " + str(indicatorDataObj.macd_12) + 
          " MACD_26: " + str(indicatorDataObj.macd_26) + 
          " EMA_100: " + str(indicatorDataObj.ema_100) + 
          " RSI_6: " + str(indicatorDataObj.rsi_6) + 
          " Position " + str(position) + 
          " PSEUDO: " + str(is_pseudo))
    
def get_current_date_string(format="%Y-%m-%d %H:%M:%S"):
    current_date = datetime.datetime.now()
    date_string = current_date.strftime(format)
    return date_string