from tda import auth, client
import json
import TDConfig
import time
import urllib
import pandas as pd
import matplotlib.pyplot as plt


try:
    c = auth.client_from_token_file(TDConfig.token_path, TDConfig.api_key)
except FileNotFoundError:
    from selenium import webdriver
    with webdriver.Chrome(executable_path = 'C:/Users/user/Desktop/TD AMR/chromedriver') as driver:
            c = auth.client_from_login_flow(
            driver, TDConfig.api_key, TDConfig.redirect_uri, TDConfig.token_path)
            
            
r = c.get_price_history('UFAB',
        period_type=client.Client.PriceHistory.PeriodType.YEAR,
        period=client.Client.PriceHistory.Period.TWENTY_YEARS,
        frequency_type=client.Client.PriceHistory.FrequencyType.DAILY,
        frequency=client.Client.PriceHistory.Frequency.DAILY)
assert r.ok, r.raise_for_status()
print(json.dumps(r.json(), indent=4))

from pandas.io.json import json_normalize 
df = json_normalize(r.json(), 'candles')
df.to_excel(r'C:\Users\user\Desktop\Grad\PY Modules\Excel\IEXCloud\UFAB.xlsx')


r1 = c.get_price_history('GOOG',
        period_type=client.Client.PriceHistory.PeriodType.YEAR,
        period=client.Client.PriceHistory.Period.TWENTY_YEARS,
        frequency_type=client.Client.PriceHistory.FrequencyType.DAILY,
        frequency=client.Client.PriceHistory.Frequency.DAILY)
assert r.ok, r.raise_for_status()
print(json.dumps(r.json(), indent=4))

from pandas.io.json import json_normalize 
df = json_normalize(r.json(), 'candles')
df.to_excel(r'C:\Users\user\Desktop\Grad\PY Modules\Excel\IEXCloud\GOOG.xlsx')

r2 = c.get_price_history('AAPL',
        period_type=client.Client.PriceHistory.PeriodType.YEAR,
        period=client.Client.PriceHistory.Period.TWENTY_YEARS,
        frequency_type=client.Client.PriceHistory.FrequencyType.DAILY,
        frequency=client.Client.PriceHistory.Frequency.DAILY)
assert r.ok, r.raise_for_status()
print(json.dumps(r.json(), indent=4))


from pandas.io.json import json_normalize 
df = json_normalize(r.json(), 'candles')
df.to_excel(r'C:\Users\user\Desktop\Grad\PY Modules\Excel\IEXCloud\AAPL.xlsx')


#try UFAB, GOOG, AAPL, etc 
prices = df['close']
df['mu'] = [df['close'][:i].mean() for i in range(len(prices))]
plt.figure(figsize=(15,7))
plt.plot(df['close'])
plt.plot(df['mu']);
plt.show()

df['x'] = [df.close[i]/df.mu[i] for i in range(len(df.close))]


#money as of now()
money = 0
count = 0
for i in range(len(df.close)):
    # Sell short if the CMA is > 7%
    if x[i] > 1.07:
        money += df.close[i]
        count -= 1
    # Buy long if the CMA is <7%
    elif x[i] < 1.07:
        money -= df.close[i]
        count += 1
    # Clear positions if the CMA = 7%
    elif abs(x[i]) ==1.07:
        money += count*df.close[i]
        count = 0
print (money)
