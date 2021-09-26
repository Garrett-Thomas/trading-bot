from Variables import *
import robin_stocks.robinhood as r
from random import randint

import time
import pyotp
import json

class StockTrader:
    """
    TODO:

    [] REFACTOR so I can understand what the hell is happening in w/ this code
    
    [] Need to figure out how to get liquid cash in account. Not all cash
    will be used in trades and will eventually collect. Need to reintroduce it.

    """
    def writeDict(self, tradedStocks):
        # Assigns the current date as new parent key
        interDict = dict()
        interDict[currentDate] = tradedStocks
        tradedStocks = interDict

        if(path.exists(parentDir + transDir)):
            with open(parentDir + transDir, "r+") as file:
                temp = json.load(file)
                temp.update(tradedStocks)
                file.seek(0)
                json.dump(temp, file, indent=4, sort_keys=False)
        else:
            with open(parentDir + transDir, "w") as file:
                json.dump(tradedStocks, file, indent=4, sort_keys=False)
        print('Transactions saved successfully')

    def __init__(self,  toTrade):

        # This is part of my two-factor auth. The string below serves as 
        # a seed to generate a code to be used upon login.
        totp = pyotp.TOTP("GGJT4LZYFC4LS5UR").now()
        login = r.login(email, password, mfa_code=totp)
        my_stocks = r.build_holdings()
        repoDict = dict()

        repoDict['Value'] = r.account.load_phoenix_account('account_buying_power')['amount']
        toTrade['Portfolio'] = list(my_stocks.keys())
        toTradeCopyWithValues = toTrade
        toTrade['Sell'] = list(map(removeExchange, toTrade['Sell']))
        toTrade['Buy'] = list(map(removeExchange, toTrade['Buy']))

        for stock in toTrade['Sell']:

            # Saves how many shares I have of x stock to a dictionary with stock name as key.
            try:
                repoDict[stock] = my_stocks[stock]['quantity']
            except KeyError as e:
                print("Cannot sell {0} because you don't own any shares.".format(stock))
                print(e)
                quit()
            # Saves the dollar value of all stocks sold. This allows money to be distributed equally 
            # amongst the stocks to be bought.
            repoDict['Value'] = int(repoDict['Value']) + int(my_stocks[stock]['Equity'])
            r.order_sell_fractional_by_quantity(repoDict[stock]["Quantity"])
            toTrade['Portfolio'].remove(stock)
            print('Sold ' + stock)

            # Since this isn't an official API, I doubt I can make to many requests in a given time.
            # The time.sleep is used to slow down the program and have a few seconds between the buying and selling.
            time.sleep(randint(1, 6))

        # Checks to make sure I actually sold something and will have money to make a purchase.
        for stock in toTrade['Buy']:

                # Iterates and buys the stocks
            r.order_buy_fractional_by_price(stock, float(repoDict['Value']) / len(toTrade['Buy']))
            print('Bought ' + stock)
            time.sleep(randint(3,6))

        self.writeDict(toTradeCopyWithValues)