import requests
import herolist
import random
import json

from random import randint
#steamID = input(": ")

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
        print(num, curr_frequency)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
    return num, curr_frequency

def most_frequent1(List):
    counter = 0
    hero = List[0]
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency>counter):
            counter=curr_frequency
            hero = i
            
    return hero, counter





list = ['Slardar', 'Legion Commander', 'Mars', 'Slardar', 'Grimstroke', 'Tusk', 'Grimstroke', 'Grimstroke', 'Earth Spirit', 'Underlord', 'Tusk', 'Lion', 'Tusk', 'Clockwerk', 'Viper', 'Invoker', 'Disruptor', 
'Dragon Knight', 'Silencer', 'Tusk', 'Viper', 'Jakiro', 'Disruptor', 'Crystal Maiden', 'Medusa', 'Dragon Knight', 'Drow Ranger', 'Slardar', 'Invoker', 'Mars', 'Terrorblade', 'Centaur Warrunner', 'Luna', 'Invoker', 'Underlord', 'Underlord', 'Centaur Warrunner', 'Tusk', 'Tusk', 'Vengeful Spirit']
print(most_frequent1(list))




'''
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
            hero = dict[match[item]]
            pickedlist.append(hero)
            print(match[item], dict[match[item]])

print(pickedlist)
print(most_frequent(pickedlist))

'''


#print(len(herolist.dotadict))




#random a hero from herolist
num = randint(0, len(dict))
#print(num)
response = dict[num]
#print(response)

