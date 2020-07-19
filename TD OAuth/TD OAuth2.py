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