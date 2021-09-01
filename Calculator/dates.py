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
        date_time = date_time[0:10].replace("-", "")

        # if date_time:
        #     print(date_time)

        if date_time > "20210501":
            print(f"{date_time} | {channel_owner}")

        # if date_time > "20210430" and date_time < "20210516":
        #     print(f"{date_time} | {channel_owner}")

        # if date_time > "20210515" and date_time < "20210601":
        #     print(f"{date_time} | {channel_owner}")

        # if date_time > "20210531" and date_time < "20210616":
        #     print(f"{date_time} | {channel_owner}")

        # if date_time > "20210615" and date_time < "20210701":
        #     print(f"{date_time} | {channel_owner}")

        # if date_time > "20210630" and date_time < "20210716":
        #     print(f"{date_time} | {channel_owner}")

        # if date_time > "20210715" and date_time < "20210801":
        #     print(f"{date_time} | {channel_owner}")

        # if date_time >= "20210801":
        #     print(f"{date_time} | {channel_owner}")