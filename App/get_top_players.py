import requests
import os
import time
import json
from dotenv import load_dotenv
from collections import defaultdict
import pandas as pd
load_dotenv()

regions = ['na1', 'euw1', 'kr']
api_key = os.getenv('API_KEY')
player_df = pd.DataFrame()

#Step 1: get players from the top divisions in each region
get_players_url = '.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/CHALLENGER/I' #may need to add other divisions and tiers
get_puuid_url = '.api.riotgames.com/lol/summoner/v4/summoners/'

def safe_request(url):
    response = requests.get(url)
    if response.status_code == 429:  # HTTP 429 means Too Many Requests
        retry_after = int(response.headers.get('Retry-After', 60))  # Default to 60 seconds if header is missing
        print(f"Rate limit exceeded. Sleeping for {retry_after} seconds.")
        time.sleep(retry_after)
        return safe_request(url)  # Recursively retry the request
    return response
    
def get_puuid(summonerId, region):
    """Takes in a summonerId and a region and returns the puuid for the summoner"""
    request_url = 'https://' + region + get_puuid_url + summonerId + '?api_key=' + api_key
    try:
        response = requests.get(request_url)
        if response.status_code == 200:
            request_json = response.json()
            return request_json['puuid'] if 'puuid' in request_json else None
        else:
            print(f"Failed to fetch puuid: {response.status_code} {response.text}")
            return None
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None

#combine all regions into one central dataframe
for region in regions:
    request_url = 'https://' + region + get_players_url + '?api_key=' + api_key
    request_json = requests.get(request_url).json()
    region_df = pd.DataFrame(request_json)
    region_df['Region'] = region
    player_df = pd.concat([player_df, region_df])


# Test with a smaller subset to ensure it works
def process_batch(df_batch):
    """Process a batch of data frame rows, setting a delay between each batch to avoid rate limiting issues"""
    batch_copy = df_batch.copy()
    #use .loc to safely assign values
    batch_copy['puuid'] = batch_copy.apply(lambda x: get_puuid(x['summonerId'], x['Region']), axis=1)
    time.sleep(2) #sleep 1 second between batches to respect rate limites
    return batch_copy

#split dataframe into smaller batches
#batch_size = 5 #Adjust based on rate limit
#batches = [player_df.iloc[i:i + batch_size].copy() for i in range(0, len(player_df), batch_size)]
#process each batch
#result_batches = [process_batch(batch) for batch in batches]
# Concatenate all processed batches back into one DataFrame
#full_result_df = pd.concat(result_batches)
#print(full_result_df)

small_sample_df = player_df.head(10)
small_sample_df['puuid'] = small_sample_df.apply(lambda x: get_puuid(x['summonerId'], x['Region']), axis=1)
print(small_sample_df)



