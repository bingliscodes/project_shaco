import requests
import os
import json
from dotenv import load_dotenv
from collections import defaultdict
import pandas as pd
load_dotenv()
#get_top_players.py gets the top Shaco players for each NA, EUW, and Korea



regions = ['na1', 'euw1', 'kr']
api_key = os.getenv('API_KEY')
player_df = pd.DataFrame()
#Step 1: get players from the top divisions in each region
get_players_url = '.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/CHALLENGER/I' #may need to add other divisions and tiers
get_puuid_url = '.api.riotgames.com/lol/summoner/v4/summoners/'

def get_puuid(summonerId, region):
    """Takes in a summonerId and a region and returns the puuid for the summoner"""
    request_url = 'https://' + region + get_puuid_url + summonerId + '?api_key=' + api_key
    request_json = requests.get(request_url).json()
    return request_json['puuid'] if request_json['puuid'] else None

for region in regions:
    request_url = 'https://' + region + get_players_url + '?api_key=' + api_key
    request_json = requests.get(request_url).json()
    region_df = pd.DataFrame(request_json)
    region_df['Region'] = region
    player_df = pd.concat([player_df, region_df])

#TODO: Add the puuid to the dataframe
for _, player in player_df.iterrows():
    player_df['puuid'] = get_puuid(player_df['summonerId'], player_df['Region'])




