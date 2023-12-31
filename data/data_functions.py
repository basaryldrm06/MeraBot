import csv

def save_new_row(file_path, state, indicator_array):
    row = [state]
    for i in range(15):
        row.append(indicator_array[i * 15].date)
        row.append(indicator_array[i * 15].price)
        row.append(indicator_array[i * 15].macd_12)
        row.append(indicator_array[i * 15].macd_26)
        row.append(indicator_array[i * 15].ema_100)
        row.append(indicator_array[i * 15].rsi_6)

    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row)

def save_log(file_path, date, position_type, scikit_prediction, status):
    row = [date, position_type, scikit_prediction, status]
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row)