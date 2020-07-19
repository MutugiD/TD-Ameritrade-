from tda import auth, client
import json
import TDConfig
import time
import urllib



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