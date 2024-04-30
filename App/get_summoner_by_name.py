import requests

api_key = 'RGAPI-f01f9637-f7a9-477e-a710-6950923641c5'
tagLine = 'NA1'
gameName = 'ye qiue'
api_url = 'https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/'
request_url = api_url + gameName + '/' + tagLine + '?api_key=' + api_key
res = requests.get(request_url)

#returns a puuid
print(res.json())