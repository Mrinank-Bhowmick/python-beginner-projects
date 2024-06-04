import json

def extract_key_value_from_file( key):
    with open("countryCode.json", 'r') as file:
        data = json.load(file)
        value = data.get(key)
        return value

