from os import path
from pathlib import Path
from datetime import datetime
import os

parentDir = str(Path(os.path.abspath('')).parent)

dailyDataDir = "/myData/dailyData.json"
weeklyDataDir = "/myData/weeklyData.json"
portfolioDir = "/myData/myPortfolio.txt"
picksDir = "/myData/picks.json"

currentDate = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
# credentialsDir = "/"
