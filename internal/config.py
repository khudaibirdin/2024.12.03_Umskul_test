import json


with open('./configs/config.json', mode='r', encoding='utf-8') as config_file:
    config = json.load(config_file)