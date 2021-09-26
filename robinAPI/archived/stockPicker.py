from Variables import *
from os import path
from collections import OrderedDict

import os.path
import json

class StockPicker():
    """
    TODO:

    [] See notes in StockTrader.py

    """
    def __init__(self, sdepth, bdepth, filePath):
        self.sDepth = sdepth
        self.bDepth = bdepth
        self.filePath = filePath
        self.picksDict = dict()
        self.keys = None
        self.buy_sell = None
    # Do not forget to put back in self.* for filename
    # Choose best stocks and put into dict. Update dict with Time. Save dict as json

    def chooseBest(self):

        with open(self.filePath, 'r') as file:
            data = json.load(file)
            self.keys = list(data)

        with open(parentDir + transDir, 'r') as currHolding:
            holdings = json.load(currHolding)
            # If you make a list from a dict it returns all the parent keys. I want to get the latest data entry
            thisdata = holdings[list(holdings).pop()]['Portfolio']
            print(str(thisdata))
        """
        This took a while for me to figure out how to sort a nested dictionary.
        Looking back at this code I can't make sense of it. Grrr. Should have 
        commented when it was fresh in my mind. I know it sorts all the stock data by the 
        Buy value. Biggest buy values should go in front and smallest in the back. I think 
        this simple approach could be improved upon by further sorting using the 
        neutral and sell values. Perhaps if neutral + sell values where greater than the buy, 
        the buy value would have less weight. Something like that.
        """
        data = sorted(data[self.keys[len(self.keys)-1]].items(), key = lambda kv: int(kv[1]['Buy']), reverse=True)

        # List comprehension that takes the sorted data and simply "removes" either ends of the list
        # Because it is sorted you only need the ends of the list to get the stocks you should buy and sell.
        toBuy = [x for x in data[0:self.bDepth]]
        toSell = [y for y in data[len(data)-self.sDepth: len(data)]]
        print("This is the data: " + str(data))
        # Makes a dictionary of my stocks I want to buy and sell with the keys "Buy" and "Sell" used 
        # accordingly. Temp2 is used so I can use the current date as the parent key for the data.
        self.picksDict['Buy'] = dict(toBuy)
        self.picksDict['Sell'] = dict(toSell)
        temp2 = dict()
        temp2[currentDate] = self.picksDict
        
        # Stupid name I know. And yes I know this all needs to be refactored.
        # Have a dictionary and the Buy and Sell key values are actually lists.
        # This is for ease of iteration when adding stock names. Then the stock 
        # names are added and self.buy_sell is reassigned to htfStocks value.
        htfStocks = dict()
        htfStocks["Buy"], htfStocks["Sell"] = [],[]
        for x in range(self.bDepth):
            htfStocks["Buy"].append(removeExchange(list(toBuy)[x][0]))
            htfStocks["Sell"].append(removeExchange(list(toSell)[x][0]))

        
        # This is a dirty little trick I found on Stack. Converting a list to the set datatype
        # lets you take the difference of each. Also can show the intersections between two sets.
        # htfStocks['Buy'] = list(set(htfStocks['Buy']) - set(thisdata))
        htfStocks['Sell'] = set(htfStocks['Sell'])
        htfStocks['Sell'].intersection_update(set(thisdata))
        htfStocks['Sell'] = list(htfStocks['Sell'])
      
        self.buy_sell = htfStocks
        return temp2

# Currently picks stocks from the dailyData json file.
    def writeDict(self, currPicks):
        if(path.exists(parentDir + picksDir)):
            with open(parentDir + picksDir, "r+") as file:
                temp = json.load(file)
                temp.update(currPicks)
                file.seek(0)
                json.dump(temp, file, indent=4, sort_keys=False)
        else:
            with open(parentDir + picksDir, "w") as file:
                json.dump(currPicks, file, indent=4, sort_keys=False)
        print('Stock picks saved successfully')

    def run(self):
        temp = self.chooseBest()
        self.writeDict(temp)
        return self.buy_sell






"""
        for stock in myStocks:
            buy = int(data[keys[len(keys) - 1]][stock]["Buy"])
            sell = int(data[keys[len(keys) - 1]][stock]["Sell"]

            # Logic for determinig to buy or sell.
            results[stock] = buy - sell
"""
"""
        results = dict([])
        portfolio = open(self.filePath, 'r')
        myStocks = portfolio.readlines()

        for x in range(len(myStocks)):
            myStocks[x] = myStocks[x].replace("\n", "")
        results = dict(sorted(results.items(), key=lambda item: item[1]))
        allStocks = OrderedDict(results)
        toSell = list(allStocks.items())[0:self.sDepth]
        toBuy = list(allStocks.items())[len(allStocks) - self.sDepth:len(allStocks)]
        it = iter(toSell)
        res_dct = dict(zip(toSell[0], toSell))
        print(res_dct)
        # print(allStocks)
        quit()
"""

