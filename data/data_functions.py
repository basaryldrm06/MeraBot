import csv

def save_position(file_path, state, indicatorDataObj):
    row = [state, indicatorDataObj.date, indicatorDataObj.price, indicatorDataObj.macd_12,
           indicatorDataObj.macd_26, indicatorDataObj.ema_100, indicatorDataObj.rsi_6]
    
    for bar in indicatorDataObj.bar_list:
        for element in bar:
            row.append(element)
        
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row)

def save_result(file_path, date, position_result, prediction):
    row = [date, position_result, prediction]
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row)