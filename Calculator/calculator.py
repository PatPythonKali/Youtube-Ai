from forex_python.converter import CurrencyRates
import time
start = time.time()

from Variables.initialize_currency import *
from Variables.load_json import load_json

c = CurrencyRates()

for x in load_json():

    amount = (x["amountValue"])
    currency = x["currency"]
    amount = x["amountValue"]
    currency_amount = x["amountString"]
    author_name = x['author']['name']
    superchat_type = x['type']
    message = x['message']
    date_time = x['datetime']
    id = x['id']

    chat_sponsor = x['author']['isChatSponsor']
    chat_moderator = x['author']['isChatModerator']

    channel_owner = x['author']['channelOwner']
    channel_url = x['author']['channelUrl']

    if amount != 0:
        if currency == "USD":
            usd = c.get_rate('usd', 'PHP')
            amount_usd = usd * amount
            gross_profit_total += amount_usd
            usd_superchatters += 1
            print(f"{usd_superchatters} SuperChats from USA!")
            print("Grand Total: ₱", round(gross_profit_total, 2))




end = time.time()
result = round(end - start, 2)
print(f"Runtime of the program is {result}")
