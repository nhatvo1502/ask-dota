import requests
import herolist

#steamID = input(": ")

#odPath = f"https://api.opendota.com/api/players/130494014/recentMatches"
#print(odPath)
#r = requests.get(odPath)

print(len(herolist.dotadict))


dict = herolist.dotadict
lastID = list(dict)[-1]
lastHero = dict[lastID]
print(lastHero)
