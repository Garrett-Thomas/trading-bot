from Variables import *
from os import path
from collections import OrderedDict

import os.path
import json

class stockPicker():


    def __init__(self, sdepth, bdepth, filePath):
        self.sDepth = sdepth
        self.bDepth = bdepth
        self.filePath = filePath
        self.picksDict = dict()
    # Do not forget to put back in self.* for filename
    # Choose best stocks and put into dict. Update dict with Time. Save dict as json

    def chooseBest(self):
        # results = dict([])
        portfolio = open(self.filePath, 'r')
        myStocks = portfolio.readlines()

        for x in range(len(myStocks)):
            myStocks[x] = myStocks[x].replace("\n", "")

        with open(self.filePath, 'r') as day:
            data = json.load(day)
            keys = list(data)
        leader = []
        """
        for stock in myStocks:
            buy = int(data[keys[len(keys) - 1]][stock]["Buy"])
            sell = int(data[keys[len(keys) - 1]][stock]["Sell"]

            # Logic for determinig to buy or sell.
            results[stock] = buy - sell
        """
        data = sorted(data[keys[len(keys)-1]].items(), key = lambda kv: int(kv[1]['Buy']), reverse=True)
        # for key in keys[0:2]:
        toBuy = [x for x in data[0:self.bDepth]]
        toSell = [y for y in data[len(data)-self.sDepth: len(data)]]
        """
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
        # return allStocks[0:self.sDepth], allStocks[len(allStocks) - self.sDepth - 1:len(allStocks)
        self.picksDict['Buy'] = dict(toBuy)
        self.picksDict['Sell'] = dict(toSell)
        temp2 = dict()
        temp2[currentDate] = self.picksDict
        return temp2

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
        print('Operation completed successfully')
    def run(self):
        self.writeDict(self.chooseBest())

# Currently picks stocks from the dailyData json file.
yum = stockPicker(2, 2, parentDir + dailyDataDir);
yum.run()
