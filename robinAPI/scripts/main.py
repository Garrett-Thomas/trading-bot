import stockTrader
import marketOpen
from Variables import *
from stockPicker import StockPicker
import robin_stocks.robinhood as r
import spTickers
import stockFetcher
import sys
import time
import json

"""
TODO:

[x] I think I should make the robinhood object here and pass it into the other scripts. Change made?

[] Get an error when trying to trade cyrpto. For now I'll ignore it but try to implement 
    it later on.


"""
# if not marketOpen.is_market_open():
#     quit()


try:

    if sys.argv[1] != IndexError:

        # Will throw list out of range exception
        if sys.argv[1] == "populate":
            buyPower = float(r.account.load_phoenix_account("account_buying_power")['amount'])
            exPortfolio = []

            with open(parentDir + portfolioDir, 'r') as file:
                # Ton of random whitespace around the words. Maybe I just don't know
                # how txt files work
                exPortfolio = list(map(str.strip, file.readlines()))
                file.close()
            # Removes the exchange names from the list
            portfolio = list(map(removeExchange, exPortfolio))

            equalSplit = buyPower/len(portfolio)

            for stocks in portfolio:
                try:
                    order = r.order_buy_fractional_by_price(stocks, equalSplit, jsonify=False)
                except Exception:
                    r.order_buy_crypto_by_price(stocks, equalSplit)
                time.sleep(1)
                print("Bought ${0} worth of {1} stock.".format(equalSplit, stocks))

        # Use this if I wanted to get sell all of my stocks.
    if sys.argv[1] == "depopulate":
        heldStocks = list(r.build_holdings())
        for stock in heldStocks():
            r.order_sell

except Exception as e:
    print('\nNo args provided\n')
        

spTickers.run()
stockFetcher.getDailyWeeklyData()

# First variable is sell Depth and second is Buy Depth but printed in console in opposite order.
stockP = StockPicker(0, 5, parentDir + dailyDataDir)
picks = stockP.chooseBest()
print(json.dumps(picks, indent=4), flush=True)

stockT = stockTrader.StockTrader(picks)
print("Finished!")
quit()


"""
This will be for daily trades. Only one trade will be completed every 24 hrs.
Need the script to first pull data and get freshest information on wanted stocks.
Then needs to choose the best two stocks and buy more of those from the current pool. For simplicity at this time,
I will just buy the two favored stocks and sell them next day to buy the next favored stocks.
"""
