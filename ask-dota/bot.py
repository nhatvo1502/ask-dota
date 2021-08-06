# bot.py
from random import randint
from dotenv import load_dotenv
from discord.ext import commands
import os
import discord
import herolist
import random
import requests
import json

from requests.models import Response

# pass dota hero list dict
dict = herolist.dotadict

# import

# connect discord ToKen
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = os.getenv('PREFIX')
bot = discord.Client()

### PREFIX ###
bot = commands.Bot(command_prefix=PREFIX)

# succesfully message


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

    odPath = f"https://api.opendota.com/api/players/{steamid3}/matches?limit=5&win=0"
    r = requests.get(odPath)
    response_info = json.loads(r.content)
    response = ''
    for match in response_info:
        for item in match:
            response = f'{response} {item}'
    await ctx.send(response)


@bot.command(name='pstat', help='return player stats')
async def text(ctx, steamid32):
    embed = playerinfo(steamid32)

    await ctx.send(embed=embed)


@bot.command(name='last20picks')
async def test(ctx, steamid3):
    odPath = f"https://api.opendota.com/api/players/{steamid3}/matches?limit=20"
    r = requests.get(odPath)
    response_info = json.loads(r.content)
    response = ''
    for match in response_info:
        for item in match:
            if item == 'hero_id':
                response = f'{response}, {dict[match[item]]}'
    await ctx.send(response)

#!last20winpicks


@bot.command(name='winpick20')
async def test(ctx, steamid3):
    odPath = f"https://api.opendota.com/api/players/{steamid3}/matches?limit=20&win=1"
    r = requests.get(odPath)
    response_info = json.loads(r.content)
    response = ''
    for match in response_info:
        for item in match:
            if item == 'hero_id':
                response = f'{response}, {dict[match[item]]}'
    await ctx.send(response)

#!last20lostpicks


@bot.command(name='lostpick20')
async def test(ctx, steamid3):
    odPath = f"https://api.opendota.com/api/players/{steamid3}/matches?limit=20&win=0"
    r = requests.get(odPath)
    response_info = json.loads(r.content)
    response = ''
    for match in response_info:
        for item in match:
            if item == 'hero_id':
                response = f'{response}, {dict[match[item]]}'
    await ctx.send(response)

#! most picked hero last 100 games


@bot.command(name='most100')
async def test(ctx, steamid3):
    odPath = f"https://api.opendota.com/api/players/{steamid3}/matches?limit=100"
    r = requests.get(odPath)
    response_info = json.loads(r.content)
    response = ''
    pickedlist = []
    for match in response_info:
        for item in match:
            if item == 'hero_id':
                hero = dict[match[item]]
                pickedlist.append(hero)
    hero, counts = most_frequent(pickedlist)
    response = f'Player picked {hero} for {counts} times in the last 100 games.'
    await ctx.send(response)

### FUNCTIONS ###

# F take a list and return the most repeated item


def most_frequent(List):
    counter = 0
    num = List[0]

    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency > counter):
            counter = curr_frequency
            num = i

    return num, counter

#F take steamid3 and game_counts then return last x amount of games into jason variable
def last_x_game_jason(steamid3, game_counts):
    odPath = f"https://api.opendota.com/api/players/{steamid3}/matches?limit={game_counts}"
    r = requests.get(odPath)
    result = json.loads(r.content)
    
    return result

#F KDA
# Get KDA for each game then medium them out
def kda(x_game):
    game_counts = len(x_game)
    kills, deaths, assists = 0, 0, 0
    
    for match in x_game:
        kills+=match['kills']
        deaths+=match['deaths']
        assists+=match['assists']
    
    mkills = round(kills/game_counts)
    mdeaths = round(deaths/game_counts)
    massists = round(assists/game_counts)

    return mkills, mdeaths, massists

# F take a steamid32bit and return *more variables when needed*
def playerinfo(steamid32):
    odPath = f'https://api.opendota.com/api/players/{steamid32}'
    r = requests.get(odPath)
    content_jason = json.loads(r.content)
    account_id = f"{content_jason['profile']['account_id']}"
    personaname = f"{content_jason['profile']['personaname']}"
    avatarfull = f"{content_jason['profile']['avatarfull']}"
    mmr_estimate = f"{content_jason['mmr_estimate']['estimate']}"
    competitive_rank = f"{content_jason['competitive_rank']}"
    profileurl = f"{content_jason['profile']['profileurl']}"

    #KDA
    x_game = last_x_game_jason(steamid32, 100)
    k, d, a = kda(x_game)

    embed = discord.Embed(
        title=personaname, description=account_id, color=0x077369)
    embed.set_thumbnail(url=avatarfull)
    embed.add_field(name="MMR", value=mmr_estimate, inline=True)
    embed.add_field(name="KDA", value=f'{k}/{d}/{a}', inline=True)
    embed.add_field(name="Main role", value="'coming soon'", inline=True)
    embed.add_field(name="Competive Rank",
                    value=competitive_rank, inline=False)

    embed.add_field(name="[Pos1: 30%]--[Pos2: 20%]--", value=".", inline=True)
    embed.add_field(name="[Pos3: 10%]--[Pos4: 30%]--", value=".", inline=True)
    embed.add_field(name="[Pos5: 10%]", value=".", inline=True)

    embed.add_field(name="Profile URL", value=profileurl, inline=False)
    embed.set_footer(text="@copyright bytheorderofPeakyBlinders")

    return embed


bot.run(TOKEN)
