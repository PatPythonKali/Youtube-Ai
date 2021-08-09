import json
from forex_python.converter import CurrencyRates

gross_profit_total = 0

hk_superchatters = 0
cad_superchatters = 0
usd_superchatters = 0
php_superchatters = 0
gbp_superchatters = 0
aud_superchatters = 0
qar_superchatters = 0
sgd_superchatters = 0

# with open('/home/ubuntu/Documents/youtube_ai_json/master.json') as json_file:
with open('/home/ubuntu/Documents/JSON/FLM JSON PROCESSED/FRANCISLEOMARCOSUPDATES.JSON') as json_file:
    obj = json_file.read()
    obj2 = json.loads(obj)

    c = CurrencyRates()

    # yt_verified = obj2['isVerified']
    for x in obj2:
        amount = (x["amountValue"])
        currency = x["currency"]
        amount = x["amountValue"]
        currency_amount = x["amountString"]
        author_name = x['author']['name']
        superchat_type = x['type']

        if amount != 0.0:

            if currency == "₱":
                gross_profit_total += amount
                php_superchatters += 1
                print(f"{php_superchatters} SuperChats from Philippines!")
                print("Grand Total: ₱", round(gross_profit_total, 2))

            elif currency == "USD":
                usd = c.get_rate('usd', 'PHP')
                amount_usd = usd * amount
                gross_profit_total += amount_usd
                usd_superchatters += 1
                print(f"{usd_superchatters} SuperChats from USA!")
                print("Grand Total: ₱", round(gross_profit_total, 2))

            elif currency == "CAD":
                cad = c.get_rate('CAD', 'PHP')
                amount_cad = cad * amount
                gross_profit_total += amount_cad
                cad_superchatters += 1
                print(f"{cad_superchatters} SuperChats from Canada!")
                print("Grand Total: ₱", round(gross_profit_total, 2))

            elif currency == "HKD":
                hkd = c.get_rate('HKD', 'PHP')
                amount_hkd = hkd * amount
                gross_profit_total += amount_hkd
                hk_superchatters += 1
                print(f"{hk_superchatters} SuperChats from Hong Kong!")
                print("Grand Total: ₱", round(gross_profit_total, 2))

            elif currency == "GBP":
                gbp = c.get_rate('GBP', 'PHP')
                amount_gbp = gbp * amount
                gross_profit_total += amount_gbp
                gbp_superchatters += 1
                print(f"{gbp_superchatters} SuperChats from United Kingdom!")
                print("Grand Total: ₱", round(gross_profit_total, 2))

            elif currency == "AUD":
                aud = c.get_rate('AUD', 'PHP')
                amount_aud = aud * amount
                gross_profit_total += amount_aud
                aud_superchatters += 1
                print(f"{aud_superchatters} SuperChats from Australia!")
                print("Grand Total: ₱", round(gross_profit_total, 2))

            elif currency == "QAR":
                qar = c.get_rate('QAR', 'PHP')
                amount_qar = qar * amount
                gross_profit_total += amount_qar
                qar_superchatters += 1
                print(f"{qar_superchatters} SuperChats from Quatar!")
                print("Grand Total: ₱", round(gross_profit_total, 2))

            elif currency == "SGD":
                sgd = c.get_rate('SGD', 'PHP')
                amount_sgd = sgd * amount
                gross_profit_total += amount_sgd
                gross_profit_total = round(gross_profit_total, 2)
                sgd_superchatters += 1
                # print(f"{sgd_superchatters} SuperChats from Singapore!")
                print(f"{currency_amount} is P{gross_profit_total} | {author_name} | "
                      f"{sgd_superchatters} from Singapore | {superchat_type}")
                print("Grand Total: ₱", round(gross_profit_total, 2))

            else:
                print(f"{currency_amount} is P{gross_profit_total} | {author_name} | "
                      f"{sgd_superchatters} Uknown | {superchat_type}")
