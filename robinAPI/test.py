from typing import KeysView
import robin_stocks
import pyotp
import robin_stocks.robinhood as r

# Really need to figure out an elegant way to store pass and text.
# Clear text cannot be used during deployment lol.

# If I do get a server with root, I might just ssh in and put in the credentials 
# myself. That way no passwords need to be stored on server. A fatal error would 
# bring it to a grinding halt as there would be no way to reauthenticate once the data is 
# lost in the ram.

# email = "garrett.p.thomas@icloud.com" 
# passSeed = "GGJT4LZYFC4LS5UR"
password = "Happyclown1!"
email =  "mindymthomas@gmail.com"  
passSeed = "OTCTSLVYSUP464IO"

totp = pyotp.TOTP(passSeed).now()
print(totp)

login = r.login(email, password, mfa_code=totp)

print(r.build_holdings())
print(r.account.filter_data(r.build_holdings(), "equity"))


# print(r.get_crypto_order_info(r.get_crypto_positions('currency')[0]['id']))

# print(r.account.load_phoenix_account("account_buying_power")['amount'])
# my_stocks = r.build_holdings()
# for key,value in my_stocks.items():
#     print(key,value)

# r.logout()
# print(login)
