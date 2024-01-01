def print_position_message(indicatorDataObj, position):
    print("DATE: " + indicatorDataObj.date + "PRICE: " + indicatorDataObj.price + 
          "MACD_12: " + indicatorDataObj.macd_12 + "MACD_26: " + indicatorDataObj.macd_26 + 
          "EMA_100: " + indicatorDataObj.ema_100 + "RSI_6: " + indicatorDataObj.rsi_6 + 
          "Position " + position)