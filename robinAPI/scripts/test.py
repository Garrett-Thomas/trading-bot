from Variables import *
import robin_stocks.robinhood as r

import time
import sys

# x = 0
# while True:
#     print('Numbers: {0}'.format(x))
#     if x >= 100:
#         quit()
#     time.sleep(.1)
#     x = x + 1


totp = pyotp.TOTP("GGJT4LZYFC4LS5UR").now()
login = r.login(email, password, mfa_code=totp)

r.orders.cancel_all_stock_orders()