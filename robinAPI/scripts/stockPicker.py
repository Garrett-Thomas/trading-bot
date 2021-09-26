from Variables import *
from os import path

import json

class StockPicker():
    """
    TODO:

    [] Need to save to trans.json using full names of the stocks.

    """
    def __init__(self, sdepth, bdepth, filePath):
        self.sDepth = sdepth
        self.bDepth = bdepth
        self.filePath = filePath
        self.picksDict = dict()
        self.keys = None
        self.buy_sell = None
    
    # Function to convert a list to a dict then get the keys from the dict and return it as a list.
    def getStockNameFromData(self, aList):
        return list(dict(json.loads(json.dumps(aList))).keys())

    def chooseBest(self):

        with open(self.filePath, 'r') as file:
            # Stands for stocks with indicator data
            stocksWithIndcData = json.load(file)
            self.keys = list(stocksWithIndcData)

        with open(parentDir + transDir, 'r') as file:
            currHoldings = json.load(file)
            currHoldings = currHoldings[list(currHoldings).pop()]['Portfolio']
        
        """
        This took a while for me to figure out how to sort a nested dictionary.
        Looking back at this code I can't make sense of it. Grrr. Should have 
        commented when it was fresh in my mind. I know it sorts all the stock data by the 
        buy value, neutral value, and sell value in that order. If there is a tie between stocks,
        then the neutral value is looked at. If x stock has a larger neautral value then stock y, 
        stock x is placed in front. If there is a tie between buy and neutral, then the lowest sell value
        is looked at. If stock X and Y had the same buy, neutral values but X's sell value was 3 and Y was 0, 
        Y would be placed in front of X.
        https://stackoverflow.com/questions/4110665/sort-nested-dictionary-by-value-and-remainder-by-another-value-in-python
        """
        # ^ above explains implementation. Data is a list of all the stocks I'm watching sorted by the Buy values.
        watchedStocksWithData = sorted(stocksWithIndcData[self.keys[len(self.keys)-1]].items(), key = lambda kv: (int(kv[1]['Buy']), int(kv[1]['Neutral']), int(kv[1]['Sell']) * -1), reverse=True)
        
        # the stocks in toBuy are from 0-bDepth.
        toBuy = [x for x in watchedStocksWithData[0:self.bDepth]]
        toSell = [y for y in watchedStocksWithData[self.bDepth: len(watchedStocksWithData)]]
        
        toBuy = self.getStockNameFromData(toBuy)
        toSell = self.getStockNameFromData(toSell)

        confirmedSellStocks = []
        """
        Simple loop to find what stocks I need to sell. Because toSell is sorted from best to worst, I loop 
        through it reversed to start with the worst stock first. It sees what I have in currHoldings that 
        I can sell to buy the stocks in toBuy with.
        """
        for heldStock in reversed(toSell):
            for stock in currHoldings:
                if(heldStock == stock and len(confirmedSellStocks) < self.sDepth):

                    confirmedSellStocks.append(heldStock)

        currPicks = dict()
        currPicks['Sell'] = {}
        currPicks['Buy'] = {}

        for stock in confirmedSellStocks:

            currPicks['Sell'][stock] = stocksWithIndcData[self.keys[len(self.keys)-1]][stock]

        # Don't want to buy unless I have stocks to sell or explicity made sDepth 0
        if len(confirmedSellStocks) > 0 or self.sDepth == 0:
            for stock in toBuy:

                currPicks['Buy'][stock] = stocksWithIndcData[self.keys[len(self.keys)-1]][stock]

        currPicksWithDate = dict()
        currPicksWithDate[datetime.now().strftime("%m/%d/%Y %H:%M:%S")] = currPicks

        if(path.exists(parentDir + picksDir)):
            with open(parentDir + picksDir, "r+") as file:

                picksFile = json.load(file)
                picksFile.update(currPicksWithDate)

                file.seek(0)

                json.dump(picksFile, file, indent=4, sort_keys=False)

        else:
            with open(parentDir + picksDir, "w") as file:

                json.dump(currPicksWithDate, file, indent=4, sort_keys=False)

        print('Stock picks saved successfully!')

        return currPicks

# How do I want this to work?
# Assume I'm holding ['AAPL', 'MARA', 'BYND', 'COIN', 'TSLA', 'NVDA', 'TQQQ', 'AMZN']
# The best buy is AAPL and MARA and to sell is BYND and COIN. Sell BYND and Coin. Buy AAPL and MARA
# Assume I'm holding ['AAPL', 'MARA', BYND']
# The best buy is AAPL and COIN and I'm to sell TSLA. Don't own any TSLA so it jumps to the next best 
# option which is BYND. Sell TSLA then buy more AAPL and COIN.