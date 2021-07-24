from datetime import datetime
from collections import OrderedDict
from Variables import *

import json
# print(datetime.now().strftime("%m/%d/%Y %H:%M:%S"))
key_value = {}
my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
# Initializing the value
key_value["Noms"] = 56
key_value[1] = 2
key_value[5] = 12
key_value[4] = 24
key_value[6] = 18
key_value[3] = 323

results = dict([])
portfolio = open(parentDir + portfolioDir, 'r')
myStocks = portfolio.readlines()

for x in range(len(myStocks)):
    myStocks[x] = myStocks[x].replace("\n", "")

with open(parentDir + dailyDataDir, 'r') as day:
    data = json.load(day)
    keys = list(data)

# print(list(data[keys[len(keys)-1]].items())[1][1]['Buy'])
data = sorted(data[keys[len(keys)-1]].items(), key = lambda kv: int(kv[1]['Buy']), reverse=True)
print(json.dumps(dict(data)))
# print(sorted(list(data[keys[len(keys)-1]].items()), key=lambda kv: data[keys[3]][kv[0]][1]['Buy']))
# print(data[keys[len(keys)-1]].items())
# print({k: v for k, v in sorted(data[keys[len(keys)-1]].items(), key=lambda item: item[0])})

# print(sorted(data, key=lambda x: list(data[x].keys())[0]))
# for x in data[keys[len(keys)-1]].items():
    # print(x[1]['Buy'])
