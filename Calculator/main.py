import time
start = time.time()

from Variables.initialize_currency import *
from Variables.load_json import load_json

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
        pass