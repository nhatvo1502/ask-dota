# bot.py
import os
import discord
import herolist
import random
import requests
import json

from requests.models import Response

#pass dota hero list dict
dict = herolist.dotadict

#import
from discord.ext import commands
from dotenv import load_dotenv
from random import randint

#connect discord ToKen
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = discord.Client()

### PREFIX ###
bot = commands.Bot(command_prefix='!#')

#succesfully message
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

### CALL ###
#!info
@bot.command(name='info', help='bot info')
async def test(ctx):
    response = 'ASK-DOTA BOT'
    await ctx.send(response)

#!gethero
@bot.command(name='gethero')
async def test(ctx, msg):
    response = herolist.dotadict[int(msg)]
    await ctx.send(response)

#!lucky
@bot.command(name='lucky')
async def test(ctx):
    num = randint(0, len(dict))
    response = 'You should play '+dict[num]
    await ctx.send(response)

#!pstat
@bot.command(name='pstat')
async def text(ctx, steamid3):
    odPath = f"https://api.opendota.com/api/players/{steamid3}/matches?limit=5&win=0"
    r = requests.get(odPath)
    response_info = json.loads(r.content)
    response=''
    for match in response_info:
        for item in match:
            response=f'{response} {item}'
    await ctx.send(response)

    
@bot.command(name='last20picks')
async def test(ctx, steamid3):
    odPath = f"https://api.opendota.com/api/players/{steamid3}/matches?limit=20"
    r = requests.get(odPath)
    response_info = json.loads(r.content)
    response=''
    for match in response_info:
        for item in match:
            if item=='hero_id':
                response = f'{response}, {dict[match[item]]}'
    await ctx.send(response)

#!last20winpicks
@bot.command(name='last20wpicks')
async def test(ctx, steamid3):
    odPath = f"https://api.opendota.com/api/players/{steamid3}/matches?limit=20&win=1"
    r = requests.get(odPath)
    response_info = json.loads(r.content)
    response=''
    for match in response_info:
        for item in match:
            if item=='hero_id':
                response = f'{response}, {dict[match[item]]}'
    await ctx.send(response)

#!last20lostpicks
@bot.command(name='last20lpicks')
async def test(ctx, steamid3):
    odPath = f"https://api.opendota.com/api/players/{steamid3}/matches?limit=20&win=0"
    r = requests.get(odPath)
    response_info = json.loads(r.content)
    response=''
    for match in response_info:
        for item in match:
            if item=='hero_id':
                response = f'{response}, {dict[match[item]]}'
    await ctx.send(response)

#! most picked hero last 40 games
@bot.command(name='mostpicklast40')
async def test(ctx, steamid3):
    odPath = f"https://api.opendota.com/api/players/{steamid3}/matches?limit=40"
    r = requests.get(odPath)
    response_info = json.loads(r.content)
    response = ''
    pickedlist = []
    for match in response_info:
        for item in match:
            if item=='hero_id':
                hero = dict[match[item]]
                pickedlist.append(hero)
    hero, counts = most_frequent(pickedlist)
    response = f'Player picked {hero} for {counts} times'
    await ctx.send(response)

#FUNCTIONS
def most_frequent(List):
    counter = 0
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num, curr_frequency
bot.run(TOKEN)