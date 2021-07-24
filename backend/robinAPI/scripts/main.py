import stockFetcher
from stockTrader import StockTrader
from Variables import *
from stockPicker import StockPicker

# Commented out the weekly data stuff. I think the button click is broken.
# stockFetcher.getDailyWeeklyData()
stockP = StockPicker(2, 2, parentDir + dailyDataDir)
# First variable is sell Depth and second is Buy Depth but printed in console in opposite order.
# stockFetcher.getDailyWeeklyData()
picks = stockP.run()
stockT = StockTrader(picks)

print("Finished!")
quit()

"""
This will be for daily trades. Only one trade will be completed every 24 hrs.
Need the script to first pull data and get freshest information on wanted stocks.
Then needs to choose the best two stocks and buy more of those from the current pool. For simplicity at this time,
I will just buy the two favored stocks and sell them next day to buy the next favored stocks.
"""

