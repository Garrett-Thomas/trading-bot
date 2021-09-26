from os import path
from pathlib import Path
from datetime import datetime
import robin_stocks.robinhood as r

import pyotp
import os

parentDir = str(Path(os.path.realpath(__file__)).parent.parent)

dailyDataDir = "/stockData/dailyData.json"
weeklyDataDir = "/stockData/weeklyData.json"
portfolioDir = "/stockData/sp500.txt"
picksDir = "/stockData/picks.json"
transDir = "/stockData/trans.json"

currentDate = datetime.now().strftime("%m/%d/%Y %H:%M:%S")

email = "garrett.p.thomas@icloud.com"
password = "Happyclown1!"
passSeed = "GGJT4LZYFC4LS5UR"
# totp = pyotp.TOTP("GGJT4LZYFC4LS5UR").now()
# login = r.login(email, password, mfa_code=totp)
# my_stocks = list(r.build_holdings().keys())

def removeExchange(stock):
    return stock.replace("AMEX-", "").replace("NASDAQ-", "").replace("NYSE-", "").replace("USD", "")