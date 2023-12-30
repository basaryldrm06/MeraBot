mera_current_dataset_arr1 = []
mera_current_dataset_arr2 = []

while True:
    # fetch indicators
    if (macd_12 > macd_26) and (macd_12 < 0) and (rsi_6 > 50) and (current_price < ema_100):
        print("Enter long here")
    elif (macd_12 < macd_26) and (macd_12 > 0) and (rsi_6 < 50) and (current_price > ema_100):
        print("Enter short here")
    elif (macd_12 > macd_26) and (macd_26 > 0) and (rsi_6 > 50) and (current_price > ema_100):
        print("Enter long here")
    elif (macd_12 < macd_26) and (macd_26 < 0) and (rsi_6 < 50) and (current_price < ema_100):
        print("Enter short here")