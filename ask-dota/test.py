import requests
import herolist
import random
import json

from random import randint
steamID = input(": ")

#steamid 56091566
odPath = f"https://api.opendota.com/api/players/{steamID}/matches?limit=5&win=0"
#print(odPath)
r = requests.get(odPath)
#print(r.content)
response_info = json.loads(r.content)

for match in response_info:
    print(match['match_id'])



#print(len(herolist.dotadict))


#print last hero
dict = herolist.dotadict
lastID = list(dict)[-1]
lastHero = dict[lastID]
#print(lastHero)

#random a hero from herolist
num = randint(0, len(dict))
#print(num)
response = dict[num]
#print(response)

