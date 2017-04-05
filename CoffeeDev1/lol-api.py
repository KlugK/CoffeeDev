from settings import API_KEY
import os, requests

def get_matches(summoner_id):
    url = 'https://euw.api.riotgames.com/api/lol/EUW/v2.2/matchlist/by-summoner/{}?api_key={}'.format(summoner_id, API_KEY)
    r = requests.get(url)
    result = r.json()
    for match in result["matches"]:
        print(match["champion"])

def get_summoner(summoner_name):
    url = 'https://euw.api.riotgames.com/api/lol/EUW/v1.4/summoner/by-name/{}?api_key={}'.format(summoner_name, API_KEY)
    r = requests.get(url)
    result = r.json()
    return result[summoner_name.lower()]["id"]

summoner_id = get_summoner('KlugKevin')
get_matches(summoner_id)

os.system("pause")