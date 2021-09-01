import json

def load_json():

    with open('/home/ubuntu/PycharmProjects/Youtube-Ai/Harvest/FLM-Aug-1-31-Master.json') as json_file:
    # with open('/home/ubuntu/Documents/JSON/FLMJSONAug1-19PROCESSED/FLM-PROCESSED-AUG-1-19-MASTER.JSON') as json_file:
        obj = json_file.read()
        obj2 = json.loads(obj)
        return obj2