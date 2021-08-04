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

def most_frequent(List):
    counter = 0
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num, curr_frequency

#steamid 56091566
odPath = f"https://api.opendota.com/api/players/{steamID}/matches?limit=40"
r = requests.get(odPath)
#print(r.content)
response_info = json.loads(r.content)
response=''
pickedlist = []
for match in response_info:
    for item in match:
        if item=='hero_id':
            #hero = dict[match[item]]
            #pickedlist.append(hero)
            print(match[item], dict[match[item]])

#print(pickedlist)
#print(most_frequent(pickedlist))




#print(len(herolist.dotadict))




#random a hero from herolist
num = randint(0, len(dict))
#print(num)
response = dict[num]
#print(response)

