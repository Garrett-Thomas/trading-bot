import robin_stocks
import pyotp
import robin_stocks.robinhood as r
from keys import *

# print(email, password)
totp = pyotp.TOTP("NLZG2URZMXSMVRLI").now()
login = r.login(email, password, mfa_code=totp)
my_stocks = r.build_holdings()
for key,value in my_stocks.items():
    print(key,value)
r.logout()
# print(login)