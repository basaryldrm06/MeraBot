from binance.client import Client
from binanceAPI.position_utilities import enter_long, enter_short
from config import api_key, secret_key
from indicators.fetch_all_indicators import fetch_all_indicators
from data.io_utilities import get_current_date_string, print_position_message
from data.IndicatorData import IndicatorData
from indicators.bar_prices import get_historical_data
from data import io_utilities
from time import sleep
from ai_modules.ai_voting import vote
from data.data_functions import save_position_infos, save_position_result
import copy