#champion_mapping.py
#TODO: Figure out how to map the id to champion name (may not be a necessary step for now since shaco's id is static)
import json
import requests

ddragon_url = 'https://ddragon.leagueoflegends.com/cdn/14.8.1/data/en_US/champion.json'

champs_json = requests.get(ddragon_url)
print(champs_json)