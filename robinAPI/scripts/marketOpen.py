from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from collections import OrderedDict
from operator import getitem

from Variables import *

def is_market_open():
    try:
        base_url = "https://www.tradinghours.com/"

        chrome_options = Options()
        chrome_options.add_argument("--headless")

        driverPath = parentDir + "/chromedriver"
        driver = webdriver.Chrome(executable_path=driverPath, options=chrome_options)

        driver.get(base_url)

        soup = BeautifulSoup(driver.page_source, "html.parser")

        return True if soup.find('span', attrs={'data-exchange-status' : 'US.NYSE'}).contents[0] == "open" else False

    except Exception:
        return None