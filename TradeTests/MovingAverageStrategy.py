from tda import auth, client
import json
import config
import time
import pandas as pd
import matplotlib.pyplot as plt
try:
    c = auth.client_from_token_file(config.token_path, config.api_key)
except FileNotFoundError:
    from selenium import webdriver
    with webdriver.Chrome(executable_path=config.chromedriver_path) as driver:
        c = auth.client_from_login_flow(
            driver, config.api_key, config.redirect_uri, config.token_path)
        
r = c.get_price_history('AAPL',
        period_type=client.Client.PriceHistory.PeriodType.YEAR,
        period=client.Client.PriceHistory.Period.TWENTY_YEARS,
        frequency_type=client.Client.PriceHistory.FrequencyType.DAILY,
        frequency=client.Client.PriceHistory.Frequency.DAILY)
print(r.json())
#normalize the json responses to pandas output 
from pandas.io.json import json_normalize 
df = json_normalize(r.json(), 'candles')
df.to_excel(r'C:\Users\user\Desktop\Grad\PY Modules\Excel\IEXCloud\AAPLFile.xlsx')

import pandas as pd 
import numpy as np
df = pd.read_excel(r'C:\Users\user\Desktop\Grad\PY Modules\Excel\IEXCloud\AAPLFile.xlsx')
df.head()


class Strategy:
    def __init__(self): 
        self.t_name =  t_name 
        self.short_win = short_win
        self.long_win = long_win
        self.cond = df.index > self.long_win
        self.trade_price = df['open']
        self.close = df['close']
        
    def smav(self): 
        self.smav = np.where(Strategy().cond, Strategy().close.rolling(window =Strategy().short_win).mean(), 0)
        return self.smav
    
    def lmav(self): 
        self.lmav = np.where(Strategy().cond, Strategy().close.rolling(window =Strategy().long_win).mean(), 0)
        return self.lmav
    
    def trend_day(self): 
        self.trend_day = np.where(Strategy().lmav() > Strategy().smav(), 1, 
                            np.where(Strategy().lmav() < Strategy().smav(),-1,0))
        return self.trend_day
    
    def prev_trend_day (self):
        self.prev_trend_day = np.where(Strategy().cond, np.roll(Strategy().trend_day(), 1), 0)
        return self.prev_trend_day 
    def diff_trend_day (self): 
        self.diff_trend_day = Strategy().trend_day() + Strategy().prev_trend_day()
        return self.diff_trend_day
     
                             
                             
#global variable 
t_name = 'mav'
short_win = 5
long_win = 20

s= Strategy()

df ['smav'] = s.smav()
df ['lmav'] = s.lmav()
df ['trend_day'] = s.trend_day()
df['prev_trend_day'] = s.prev_trend_day()
df['diff_trend_day'] = s.diff_trend_day ()


class Signal:
    def __init__(self):
        pass
    def trade_signal(self):
        self.trade_signal = np.where(Strategy().diff_trend_day() ==0, Strategy().trend_day(), 0)
        return self.trade_signal 
    def order (self): 
        self.order = np.where(Strategy().cond, np.roll(Signal().trade_signal(), 1), 0)
        return self.order 
    
    
    
ts = Signal()
    
df['trade_signal'] =  ts.trade_signal()
df['order'] = ts.order()


class Portfolio:
    def __init__(self):
        self.lot_size_short = 1
        self.lot_size_long = 1
        self.contract_size = 1
        self.initial_cash = 10000
        self.short_amt = (1)* np.where (Signal().order()== -1, self.lot_size_short*
                                        self.contract_size*Strategy().trade_price, 0)
        self.long_amt = (-1)* np.where (Signal().order()==1, self.lot_size_long*
                                        self.contract_size*Strategy().trade_price, 0)
        
    def cash_delta(self): 
        self.cash_delta = Portfolio().long_amt + Portfolio().short_amt 
        return self.cash_delta
    def end_bal(self): 
        self.end_bal = Portfolio().initial_cash + Portfolio().cash_delta().cumsum()
        return self.end_bal
    def end_pos(self): 
        self.end_pos = Signal().order().cumsum()
        return self.end_pos 
    
              
p = Portfolio()
df['long_amt'] = p.long_amt
df['short_amt'] = p.short_amt
df['cash_delta'] = p.cash_delta()
df['end_bal'] = p.end_bal()
df['end_pos'] =  p.end_pos ()


df['pnl'] = df['end_bal'] + (Portfolio().end_pos() * Strategy().trade_price*Portfolio().contract_size)
df[:-1]

import matplotlib.pyplot as plt
df1 = df.set_index('datetime')
BBands = df1[['close','smav','lmav']].plot()

df1 = df.set_index('datetime')
print_pnl = df1['pnl'].plot()