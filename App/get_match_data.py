#gets the match data from a dataframe containing high rank summonerId's and puuids
from get_top_players import requests, api_key
test_puuid = 'Zim3e2onm6Q2ZgbEAUlkacrlnJ_I8Kwncb7Z8G5bpCY6NR62FqksR1tLZkK6_TbCztvj15daxi2Gzg'
#Step 1: Get a list of match ids by puuid. Note that the 'type=ranked' filters for only ranked games
def get_match_ids(region, puuid, count):
    """Returns a list of match ids from a region and puuid"""
    request_url = ('https://' + region + '.api.riotgames.com/lol/match/v5/matches/by-puuid/' + puuid + '/ids?type=ranked&start=0' + '&count=' + str(count) + '&api_key=' + api_key)
    try:
        response = requests.get(request_url)
        if response.status_code == 200:
            response_json = response.json()
            return response_json
        else:
            print(f"Failed to get match data: {response.status_code} {response.text}")
            return None
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None
    
# test = get_match_ids('americas', 'Zim3e2onm6Q2ZgbEAUlkacrlnJ_I8Kwncb7Z8G5bpCY6NR62FqksR1tLZkK6_TbCztvj15daxi2Gzg', 20)
# print(test)

#Step 2: get the match data from the match id

