import csv

def save_new_row(file_path, current_indicators, old_indicators1, old_indicators2, old_indicators3, 
                 old_indicators4, old_indicators5, old_indicators6, old_indicators7, old_indicators8, 
                 old_indicators9, old_indicators10, old_indicators11 , old_indicators12, old_indicators13,
                 old_indicators14, result):
    row = [current_indicators, old_indicators1, old_indicators2, old_indicators3, old_indicators4, 
                 old_indicators5, old_indicators6, old_indicators7, old_indicators8, old_indicators9, 
                 old_indicators10, old_indicators11 , old_indicators12, old_indicators13,
                 old_indicators14, result]
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row)

def save_log(file_path, date, account_balance_before, account_balance_after, position_type, scikit_prediction, result, status):
    print("Hello World")


