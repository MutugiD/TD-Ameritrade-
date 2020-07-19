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

prices = df['close']
df['mu'] = [df['close'][:i].mean() for i in range(len(prices))]
plt.figure(figsize=(15,7))
plt.plot(df['close'])
plt.plot(df['mu']);
plt.show()

df['x'] = [df.close[i]/df.mu[i] for i in range(len(df.close))]

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

r1 = c.get_price_history('GOOG',
        period_type=client.Client.PriceHistory.PeriodType.YEAR,
        period=client.Client.PriceHistory.Period.TWENTY_YEARS,
        frequency_type=client.Client.PriceHistory.FrequencyType.DAILY,
        frequency=client.Client.PriceHistory.Frequency.DAILY)
from pandas.io.json import json_normalize 
df1 = json_normalize(r1.json(), 'candles')

r2 = c.get_price_history('AIG',
        period_type=client.Client.PriceHistory.PeriodType.YEAR,
        period=client.Client.PriceHistory.Period.TWENTY_YEARS,
        frequency_type=client.Client.PriceHistory.FrequencyType.DAILY,
        frequency=client.Client.PriceHistory.Frequency.DAILY)
from pandas.io.json import json_normalize 
df2 = json_normalize(r2.json(), 'candles')

r3 = c.get_price_history('C',
        period_type=client.Client.PriceHistory.PeriodType.YEAR,
        period=client.Client.PriceHistory.Period.TWENTY_YEARS,
        frequency_type=client.Client.PriceHistory.FrequencyType.DAILY,
        frequency=client.Client.PriceHistory.Frequency.DAILY)
from pandas.io.json import json_normalize 
df3 = json_normalize(r3.json(), 'candles')

r4 = c.get_price_history('T',
        period_type=client.Client.PriceHistory.PeriodType.YEAR,
        period=client.Client.PriceHistory.Period.TWENTY_YEARS,
        frequency_type=client.Client.PriceHistory.FrequencyType.DAILY,
        frequency=client.Client.PriceHistory.Frequency.DAILY)
from pandas.io.json import json_normalize 
df4 = json_normalize(r4.json(), 'candles')

r5 = c.get_price_history('PG',
        period_type=client.Client.PriceHistory.PeriodType.YEAR,
        period=client.Client.PriceHistory.Period.TWENTY_YEARS,
        frequency_type=client.Client.PriceHistory.FrequencyType.DAILY,
        frequency=client.Client.PriceHistory.Frequency.DAILY)
from pandas.io.json import json_normalize 
df5 = json_normalize(r5.json(), 'candles')

r6 = c.get_price_history('PG',
        period_type=client.Client.PriceHistory.PeriodType.YEAR,
        period=client.Client.PriceHistory.Period.TWENTY_YEARS,
        frequency_type=client.Client.PriceHistory.FrequencyType.DAILY,
        frequency=client.Client.PriceHistory.Frequency.DAILY)
from pandas.io.json import json_normalize 
df6 = json_normalize(r6.json(), 'candles')

r7 = c.get_price_history('DOW',
        period_type=client.Client.PriceHistory.PeriodType.YEAR,
        period=client.Client.PriceHistory.Period.TWENTY_YEARS,
        frequency_type=client.Client.PriceHistory.FrequencyType.DAILY,
        frequency=client.Client.PriceHistory.Frequency.DAILY)
from pandas.io.json import json_normalize 
df7 = json_normalize(r7.json(), 'candles')
    

data = [df['close'], df1['close'], df2['close'], df3['close'], df4['close'], df5['close'], df6['close'], df7['close']]
prices = pd.DataFrame(data)


from collections import namedtuple
prices = namedtuple("data", "close")


