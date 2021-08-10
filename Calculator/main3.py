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

    chat_sponsor = x['author']['isChatSponsor']
    chat_moderator = x['isChatModerator']

    channel_owner = x['author']['channelOwner']
    channel_url = x['author']['channelUrl']

    if chat_sponsor:
        chat_sponsor_counter += 1
        print(author_name)

        # if superchat_type == "superChat":
        #     super_chat_counter += 1
        # elif superchat_type == "superSticker":
        #     super_sticker_counter += 1
        # print(f"Total Super Chat = {super_chat_counter}, Total Super Sticker = {super_sticker_counter}")
        # print(date_time)

        # if currency == "MAD\u00a0":
        #     print()
        #     print(f"{author_name} | {superchat_type} | {date_time}")

        # if currency == "₱":
        #     print(currency)
            # gross_profit_total += amount
            # php_superchatters += 1
            # print(f"{php_superchatters} SuperChats from Philippines!")
            # print("Grand Total: ₱", round(gross_profit_total, 2))

        # else:
        #     print(currency)

end = time.time()
result = round(end - start, 2)
print(f"Runtime of the program is {result}")
