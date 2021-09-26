import requests
import random
import time

import bs4 as bs
from Variables import *
from multiprocessing.pool import ThreadPool

baseUrl = "https://www.tradingview.com/symbols/"
afterUrl = "/technicals/"
exchanges = ['NASDAQ', 'AMEX', 'NYSE']
thread_count = 40

# Following 3 lines get list of proxies to use.
list_of_proxies = requests.get("https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt").text.split("\n")
del list_of_proxies[len(list_of_proxies)-1]
list_of_proxies = list(map(lambda prx: "http://" + prx, list_of_proxies))

# Returns a random proxy as a dict object
def get_rand_proxy(myProxies):
    return {'http': random.choice(myProxies)}

# Found below function on this website:
# https://pythonprogramming.net/sp500-company-price-data-python-programming-for-finance/
def get_sp500_tickers():

    print('Getting SP500 stocks...')
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies', proxies=get_rand_proxy(list_of_proxies))
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:

        ticker = row.findAll('td')[0].text
        tickers.append(ticker.replace("\n", ""))
    print("...Recieved {0} stocks".format(len(tickers)))
    return tickers

def get_valid_exchange(tickers, tempProxies):

    validTickers = []
    if len(tickers) == 0 or tempProxies == 0:

        return validTickers

    for stock in tickers:

        for exchange in exchanges:

            time.sleep(2.5)
            
            if(requests.get(baseUrl + exchange + "-" + stock + afterUrl, proxies=get_rand_proxy(tempProxies)).status_code == 200):

                validTickers.append(exchange + "-" + stock)
                break

    return validTickers

def run():

    sp_tickers = get_sp500_tickers()

    # Gets avg. Not perfect as the last thread takes up
    thread_tank = []
    stock_per_thread = round(len(sp_tickers) / thread_count)
    proxy_per_thread = round(len(list_of_proxies) / thread_count)

    pool = ThreadPool(processes=thread_count)

    start = time.perf_counter()

    """
    Using "pool" library to manage threads. This library allows the threads to 
    store the return value of the function they call. Retrieve this value using get()

    """
    print("Starting {0} threads".format(thread_count))
    for x in range(thread_count):

        if x < thread_count - 1:

            thread_tank.append(pool.apply_async(get_valid_exchange, (sp_tickers[x * stock_per_thread: (x + 1) * stock_per_thread], list_of_proxies[x * proxy_per_thread: (x + 1) * proxy_per_thread])))
        else:

            thread_tank.append(pool.apply_async(get_valid_exchange, (sp_tickers[x * stock_per_thread: len(sp_tickers) - 1], list_of_proxies[x * proxy_per_thread: len(list_of_proxies) - 1])))

    stocks_with_exchanges = []
    for t in thread_tank:

        stocks_with_exchanges.extend(t.get())


    print("Collected {0} valid tickers with exchanges".format(len(stocks_with_exchanges)))

    print("...Saving Data...")
    with open(parentDir + portfolioDir, 'w') as file:
        for stock in stocks_with_exchanges:
            file.write("%s\n" % stock)

    end = time.perf_counter()
    print("Operation finished in {0}".format(end-start))

    print(stocks_with_exchanges)







# from datetime import datetime
# from collections import OrderedDict
# from Variables import *
# from stockPicker import StockPicker
# import json
# # print(datetime.now().strftime("%m/%d/%Y %H:%M:%S"))
# portfolio = open(parentDir + portfolioDir, 'r')
# stocks_with_exchanges = portfolio.readlines()

# totp = pyotp.TOTP(passSeed).now()
# login = r.login(email, password, mfa_code=totp)

# buying_power = r.load_phoenix_account()['account_buying_power']['amount']
# portfolioValue = r.load_phoenix_account()['portfolio_equity']['amount']


# print('You have {0} dollars to spend and your portfolio is worth {1} dollars'.format(buying_power, portfolioValue))



# for x in range(len(stocks_with_exchanges)):
#     stocks_with_exchanges[x] = stocks_with_exchanges[x].replace("\n", "")

# with open(parentDir + picksDir, 'r') as day:
#     data = json.load(day)
#     keys = list(data)

# data = data[keys[len(keys)-1]]

# print(json.dumps(data, indent=4))

# print(list(map(removeExchange, data['Sell'])))

# for stock in data['Sell']:
#     data['Sell'][stock] = removeExchange(stock)
#     print(data['Sell'][stock])