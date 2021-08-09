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
with open('/home/ubuntu/pCloudDrive/FLM JSON PROCESSED V2 BACKUP/FLM_MASTER.JSON') as json_file:
    obj = json_file.read()
    obj2 = json.loads(obj)

    c = CurrencyRates()

    # yt_verified = obj2['isVerified']
    for x in obj2:
        yt_author_name = x['author']['name']
        yt_message = x['message']
        yt_datetime = x['datetime']
        string_date = yt_datetime

        yt_elapsed_time = x['elapsedTime']
        yt_channel_owner = x['author']['channelOwner']
        yt_channel_url = x['author']['channelUrl']

        amount = x['amountString']


        print(amount)