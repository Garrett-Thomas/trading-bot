# Stock Fetcher

Grabs technical data from Tradingview's website. Really just a project for my Econ class.
Tradingview already computes the data and gives a recommendation as to wether or not to buy the stock.
Based on this, I assign the stock a numerical value from -2 to 2 with -2 being sell and 2 being buy.
Doing it this way to make judgements about what stocks I want to buy and sell from within my own
portfolio.

# Dependencies
You will need to install the following:
```python
Selenium
BeautifulSoup4
```
You also need to download the webdriver for your browser of choice. Put it in the root 
directory of the project. Necessary for automation. [Chromium Web Driver](https://chromedriver.chromium.org/downloads)

#Usage

Takes no arguments. 
