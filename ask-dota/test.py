import requests
import herolist
import random
import json

from random import randint
steamID = input(": ")

#print last hero
dict = herolist.dotadict
lastID = list(dict)[-1]
lastHero = dict[lastID]
#print(lastHero)

#steamid 56091566
odPath = f"https://api.opendota.com/api/players/{steamID}/matches?limit=20&win=0"
r = requests.get(odPath)
#print(r.content)
response_info = json.loads(r.content)
response=''
for match in response_info:
    for item in match:
        if item=='hero_id':
            response = f'{response} {dict[match[item]]}'

print(response)



#print(len(herolist.dotadict))




#random a hero from herolist
num = randint(0, len(dict))
#print(num)
response = dict[num]
#print(response)

