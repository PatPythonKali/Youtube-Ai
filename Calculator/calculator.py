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

    new_date_time = date_time[0:10].replace("-", "")

    if amount != 0 and new_date_time == "20210822":

        if currency == "₱":
            x = round(amount)
            gross_profit_total += x
            super_chat_counter += 1

            # print(f"{x} | {round(gross_profit_total, 2)} | {super_chat_counter}")

        if currency == "USD":
            x = 50.45 * round(amount)
            gross_profit_total += x
            super_chat_counter += 1

            # print(f"{x} | {round(gross_profit_total, 2)} | {super_chat_counter}")

        if currency == "CAD":
            x = 40.26 * round(amount)
            gross_profit_total += x
            super_chat_counter += 1

            # print(f"{x} | {round(gross_profit_total, 2)} | {super_chat_counter}")

        if currency == "¥":
            x = 0.46 * round(amount)
            gross_profit_total += x
            super_chat_counter += 1

            # print(f"{x} | {round(gross_profit_total, 2)} | {super_chat_counter}")

        if currency == "HKD":
            x = 6.48  * round(amount)
            gross_profit_total += x
            super_chat_counter += 1

            # print(f"{x} | {round(gross_profit_total, 2)} | {super_chat_counter}")

        if currency == "EUR":
            x = 59.10 * round(amount)
            gross_profit_total += x
            super_chat_counter += 1

            # print(f"{x} | {round(gross_profit_total, 2)} | {super_chat_counter}")

        if currency == "GBP":
            x = 69.70  * round(amount)
            gross_profit_total += x
            super_chat_counter += 1

            # print(f"{x} | {round(gross_profit_total, 2)} | {super_chat_counter}")

        if currency == "AUD":
            x = 36.97 * round(amount)
            gross_profit_total += x
            super_chat_counter += 1

            # print(f"{x} | {round(gross_profit_total, 2)} | {super_chat_counter}")

        if currency == "SGD":
            x = 37.08 * round(amount)
            gross_profit_total += x
            super_chat_counter += 1

            # print(f"{x} | {round(gross_profit_total, 2)} | {super_chat_counter}")

        if currency == "CHF":
            x = 54.61 * round(amount)
            gross_profit_total += x
            super_chat_counter += 1

            # print(f"{x} | {round(gross_profit_total, 2)} | {super_chat_counter}")

        if currency == "QAR\u00a0":
            x = 13.86 * round(amount)
            gross_profit_total += x
            super_chat_counter += 1

            # print(f"{x} | {round(gross_profit_total, 2)} | {super_chat_counter}")

        if currency == "TWD":
            x = 1.81 * round(amount)
            gross_profit_total += x
            super_chat_counter += 1

            # print(f"{x} | {round(gross_profit_total, 2)} | {super_chat_counter}")

        if currency == "₪":
            x = 15.64 * round(amount)
            gross_profit_total += x
            super_chat_counter += 1

            # print(f"{x} | {round(gross_profit_total, 2)} | {super_chat_counter}")

        if currency == "AED\u00a0":
            x = 13.73 * round(amount)
            gross_profit_total += x
            super_chat_counter += 1

            # print(f"{x} | {round(gross_profit_total, 2)} | {super_chat_counter}")

        if currency == "KRW":
            x = .044 * round(amount)
            gross_profit_total += x
            super_chat_counter += 1

            # print(f"{x} | {round(gross_profit_total, 2)} | {super_chat_counter}")

        if currency == "SEK":
            x = 5.78 * round(amount)
            gross_profit_total += x
            super_chat_counter += 1

            # print(f"{x} | {round(gross_profit_total, 2)} | {super_chat_counter}")

        if currency == "NOK":
            x = 5.65 * round(amount)
            gross_profit_total += x
            super_chat_counter += 1

            # print(f"{x} | {round(gross_profit_total, 2)} | {super_chat_counter}")

        if currency == "NZD":
            x = 35.31 * round(amount)
            gross_profit_total += x
            super_chat_counter += 1

            # print(f"{x} | {round(gross_profit_total, 2)} | {super_chat_counter}")

        if currency == "RUB":
            x = 0.68 * round(amount)
            gross_profit_total += x
            super_chat_counter += 1

            # print(f"{x} | {round(gross_profit_total, 2)} | {super_chat_counter}")

        if currency == "SAR\u00a0":
            x = 13.45 * round(amount)
            gross_profit_total += x
            super_chat_counter += 1

            # print(f"{x} | {round(gross_profit_total, 2)} | {super_chat_counter}")

        if currency == "INR":
            x = 0.68 * round(amount)
            gross_profit_total += x
            super_chat_counter += 1

            # print(f"{x} | {round(gross_profit_total, 2)} | {super_chat_counter}")

        if currency == "MAD\u00a0":
            x = 5.62 * round(amount)
            gross_profit_total += x
            super_chat_counter += 1

            # print(f"{x} | {round(gross_profit_total, 2)} | {super_chat_counter}")

        if currency == "DKK\u00a0":
            x = 7.95 * round(amount)
            gross_profit_total += x
            super_chat_counter += 1

            # print(f"{x} | {round(gross_profit_total, 2)} | {super_chat_counter}")

        print(f"{author_name} : P{round(x, 2)} - {date_time}")

print(f"Gross Total Profit : {round(gross_profit_total,2)} ")



end = time.time()
result = round(end - start, 2)
print(f"Runtime of the program is {result}")
