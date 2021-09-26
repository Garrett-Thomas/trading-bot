import sys
import os.path
# Added the dir that variables is in to Python path. used export PYTHONPATH="" and 
# echo $PYTHONPATH to check if it worked.
import robin_stocks.robinhood as r
import pyotp
import json
from pathlib import Path
import math
import time

initial_deposit = 500
transDir = "/stockData/trans.json"
email = "garrett.p.thomas@icloud.com"
password = "Happyclown1!"
passSeed = "GGJT4LZYFC4LS5UR"
# TODO: The following data needs to be compiled as a json object when printing out
#     - totalGains
#     - portValue
#     - stocksBought
#     - stocksSold

# Temporary for now. Other account has nothing bought.
# password = "Happyclown1!"
# email =  "mindymthomas@gmail.com"  
# passSeed = "OTCTSLVYSUP464IO"

yarn = pyotp.TOTP(passSeed).now()

login = r.login(email, password, mfa_code=yarn)


# while True:
#     # print(789.2)
#     # PortData holds all information relative to my stock positions.
#     time.sleep(2)
#     portData = r.build_holdings()

#     # Portfolio only has the names of all the stocks I own.
#     portfolio = list(portData)

#     totalEquity = 0
#     for stock in portfolio:
#         totalEquity = float(portData[stock]["equity"]) + totalEquity
    
#     print(str(totalEquity))
#     sys.stdout.flush()
#     sys.stderr.flush()

while True:
    time.sleep(2)
    tempDict = dict()

    with open(str(Path(__file__).parent.absolute()) + "/robinAPI" + transDir, 'r') as file:
            currHoldings = json.load(file)
            currHoldings = currHoldings[list(currHoldings).pop()]

    portoflio_value = float(r.load_phoenix_account()['portfolio_equity']['amount'])
    tempDict["totalGains"] = round(portoflio_value - initial_deposit, 2)
    tempDict["portVal"] = round(portoflio_value, 2)
    tempDict["data"] = [{"value": round(portoflio_value, 2), "time": int(time.time())}]
    tempDict["stocksBought"] = currHoldings['Buy']
    tempDict["stocksSold"] = currHoldings['Sell']
    print(json.dumps(tempDict, ensure_ascii=True, indent=4), flush=True)
    sys.stdout.flush()