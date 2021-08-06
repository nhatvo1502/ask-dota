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
    return num, counter

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
#print(most_frequent1(list))


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


######### EMBEDED #######################
#f to catch player info from opendata api
def playerinfo(steamid32):
    odPath = f'https://api.opendota.com/api/players/{steamid32}'
    r = requests.get(odPath)
    content_jason = json.loads(r.content)
    account_id= f"{content_jason['profile']['account_id']}"
    personaname = f"{content_jason['profile']['personaname']}"
    avatarfull = f"{content_jason['profile']['avatarfull']}"
    mmr_estimate = f"{content_jason['mmr_estimate']['estimate']}"
    competitive_rank = f"{content_jason['competitive_rank']}"



    return account_id, personaname, avatarfull, mmr_estimate, competitive_rank

#print(playerinfo(56091566))

######### KDA #######################
#F take steamid3 and game_counts then return last 5 game info as jason
def last_x_game_jason(steamid3, game_counts):
    odPath = f"https://api.opendota.com/api/players/{steamid3}/matches?limit={game_counts}"
    r = requests.get(odPath)
    result = json.loads(r.content)
    
    return result

def kda(steamid3, game_counts):
    x_game = last_x_game_jason(steamid3, game_counts)
    kills, deaths, assists = 0, 0, 0
    
    for match in x_game:
        kills+=match['kills']
        deaths+=match['deaths']
        assists+=match['assists']
    
    mkills = round(kills/game_counts)
    mdeaths = round(deaths/game_counts)
    massists = round(assists/game_counts)

    return mkills, mdeaths, massists


print(kda(86745912, 5))

#last 5 games for 86745912
#k=27, d=19, 51
#mk=5.4->5, md=3.8->4, ma=10.2->10
#kda=5/4/10

