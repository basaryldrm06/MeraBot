import datetime
from termcolor import colored

def print_position_message(indicatorDataObj, position):
    print_with_color("yellow", "PRICE: " + str(round(indicatorDataObj.price, 2)) + 
          " MACD_12: " + str(round(indicatorDataObj.macd_12, 2)) + 
          " MACD_26: " + str(round(indicatorDataObj.macd_26, 2)) + 
          " EMA_100: " + str(round(indicatorDataObj.ema_100, 2)) + 
          " RSI_6: " + str(round(indicatorDataObj.rsi_6, 2)))
    
def get_current_date_string(format="%Y-%m-%d %H:%M:%S"):
    current_date = datetime.datetime.now()
    date_string = current_date.strftime(format)
    return date_string

def print_with_color(color, text):
    colored_text = text
    if color.lower() == 'cyan':
        colored_text = colored(text, 'cyan')
    elif color.lower() == 'green':
        colored_text = colored(text, 'green')
    elif color.lower() == 'yellow':
        colored_text = colored(text, 'yellow')
    elif color.lower() == 'red':
        colored_text = colored(text, 'red')

    print("[" + get_current_date_string() + "] " + colored_text)

def calculateWR(tp_count, sl_count):
    total_trades = tp_count + sl_count

    if total_trades == 0:
        return "0.00%"

    win_rate = tp_count / total_trades
    win_rate_percentage = round(win_rate * 100, 2)

    return f"{win_rate_percentage}%"