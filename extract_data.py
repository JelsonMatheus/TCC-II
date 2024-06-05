import MetaTrader5 as mt5
from datetime import datetime
from decouple import config
import pandas as pd


def start():
    LOGIN = config('LOGIN', cast=int)
    PASSWORD = config('PASSWORD')
    SERVER = config('SERVER')
    TIMEFRAME = mt5.TIMEFRAME_H1
    SYMBOL = 'WINM24'

    print(mt5.initialize(login=LOGIN, server=SERVER, password=PASSWORD))
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 5, 17, 20)
    data = pd.DataFrame(mt5.copy_rates_range(SYMBOL, TIMEFRAME, start_date, end_date))
    data['datetime'] = pd.to_datetime(data['time'], unit='s')
    data = data[['datetime', 'open','high','low','close','tick_volume','spread','real_volume']]
    data.to_csv('data/WINM24_30_MIN.csv', index=False)


if __name__ == '__main__':
    start()