import requests
import herolist

steamID = input(": ")

odPath = f"https://api.opendota.com/api/players/130494014/recentMatches"
print(odPath)
r = requests.get(odPath)

print (r.text)
