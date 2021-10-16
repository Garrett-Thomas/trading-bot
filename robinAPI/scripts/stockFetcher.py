from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from os import path
from datetime import datetime
from Variables import *

import time
import re
import os
import json

start = time.perf_counter()

baseUrl = "https://www.tradingview.com/symbols/"
afterUrl = "/technicals/"

# List of all my stocks I am watching. Tradingview's url strucutre is as follows
# baseUrl + myStocks[any] + afterUrl. Makes it really simple to get the data.
portfolio = open(parentDir + portfolioDir, 'r')
myStocks = portfolio.readlines()

for x in range(len(myStocks)):
    myStocks[x] = myStocks[x].replace("\n", "")

myThreads = []
results = {}

# Executes Chrome headlessly.

chrome_options = Options()
chrome_options.add_argument("--headless")

# Regex expression to identify tags where data is stored.
indReg = re.compile("counterNumber-DPgs-R4s.{4,8}Color.{5,20}")
# Opens up a headless chrome browser!

driverPath = parentDir + "/chromedriver"
driver = webdriver.Chrome(executable_path=driverPath, options=chrome_options)

weekButton = None


def saveData(type, saveDict, date):
    fileName = parentDir + dailyDataDir
    temp = dict()
    temp[date] = saveDict
    saveDict = temp
    if type == "week":
        fileName = parentDir + weeklyDataDir
    if(path.exists(fileName)):
        with open(fileName, "r+") as outfile:
            temp = json.load(outfile)
            temp.update(saveDict)
            outfile.seek(0)
            json.dump(temp, outfile, indent=4, sort_keys=False)

    else:

        with open(fileName, "w") as outfile:
            json.dump(saveDict, outfile, indent=4, sort_keys=False)


def getHTML(stock, sleepVar=2, retryCount=0):
    # What is actually getting the data from the website.
    driver.get(baseUrl + stock + afterUrl)
    # The time.sleep() is incredibly important. Time is needed to run javascript in the browser
    # and for html to reach final state.
    time.sleep(sleepVar)
    # page_source attribute allows you to access raw html. BeautifulSoup parses it.
    data = driver.page_source
    soup = BeautifulSoup(data, "html.parser")

    # This searches the html for <span> tags with classes matching the regex. Returns a list.
    print("Getting data from " + stock)

    indTags = soup.findAll('span', class_=indReg)

    try:
        results[stock] = {'Sell': str(indTags[3].contents[0]), 'Neutral': str(
            indTags[4].contents[0]), 'Buy': str(indTags[5].contents[0])}
    except Exception as e:
        if(retryCount < 3):
            print("Received error. Will retry with longer sleep time")
            getHTML(stock, sleepVar + 2, retryCount + 1)
        else:    
            print(e)
            quit()


def getDailyWeeklyData():
    for x in range(len(myStocks)):
        getHTML(myStocks[x], 1, False)
    saveData("day", results, datetime.now().strftime("%m/%d/%Y %H:%M:%S"))
    end = time.perf_counter()
    print("Operation finished in " + str(end - start) + " seconds!")
# Orignally multithreaded, but the webdriver itself is single threaded and
# cause synchronization issues.
# Timing purposes.