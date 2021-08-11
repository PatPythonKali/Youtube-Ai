import json

def load_json():

    # with open('/home/ubuntu/Documents/JSON/FLM JSON PROCESSED/FLMMAYAMANCHALLENGE20.JSON') as json_file:
    with open('/home/ubuntu/Documents/JSON/FLM JSON PROCESSED/FRANCISMARCOSAFTERDARK.JSON') as json_file:
        obj = json_file.read()
        obj2 = json.loads(obj)
        return obj2