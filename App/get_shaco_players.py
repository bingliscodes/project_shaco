#get_shaco_players.py 
from get_top_players import requests, api_key

#Step 1: Check champion mastery for all top players
shaco_id = 35

def get_mastery(puuid, n):
    """Takes in a puuid and returns a specified number of top n champion mastery entries"""
    request_url = (
        'https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/' + puuid + '/top?count=' + str(n) + '&api_key=' + api_key
    )

    try:
        response = requests.get(request_url)
        if response.status_code == 200:
            response_json = response.json()
            return response_json
        else:
            print(f"Failed to get champion mastery: {response.status_code} {response.text}")
            return None
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None
    
def identify_helper(mastery, championId):
    """Takes in a list of champ mastery and returns True if Shaco is in it, False otherwise"""
    for champion in mastery:
        if champion['championId'] == championId:
            return True
    return False


def identify_shaco_players(player_df):
    """Takes in a dataframe of highly-ranked players and checks if they play a lot of shaco based on the get mastery function, which arbitrarily checks their top 5 champion mastery"""
    pass
    #player_df['Shaco Main'] = player_df.apply(lambda x: x[])

