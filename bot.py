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
bot = commands.Bot(command_prefix=PREFIX, help_command=None, case_insensitive=True)

# succesfully message


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(f'{PREFIX}help'))

### CALL ###
#!info


@bot.command(name='info', help='bot info')
async def test(ctx):
    response = 'ASK-DOTA BOT'
    await ctx.send(response)


#test bot command list

@bot.command()
async def help(ctx):
    embed=discord.Embed(title="Help command", description=f'Prefix of bot: **`{PREFIX}`**',color=discord.Color.blurple())
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    #after this line, just want to test, not official, will use .json file for list of command
    embed.add_field(name="List of command: ", 
                value="`help\n` `info\n` `gethero\n` `last20picks\n` `lostpick20\n` `lucky\n` `most100\n` `pstat\n` `winpick20\n`", inline=False)
    
    await ctx.send(embed=embed)



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

### LANE ROLE #######################
def lane_role(steamid3):
    odPath = f"https://api.opendota.com/api/players/{steamid3}/counts"
    r = requests.get(odPath)
    result = json.loads(r.content)
    pos1g, pos1w, pos2g, pos2w, pos3g, pos3w, pos4g, pos4w, pos5g, pos5w = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    pos1g+=result['lane_role']['0']['games']
    pos1w+=result['lane_role']['0']['win']
    pos2g+=result['lane_role']['1']['games']
    pos2w+=result['lane_role']['1']['win']
    pos3g+=result['lane_role']['2']['games']
    pos3w+=result['lane_role']['2']['win']
    pos4g+=result['lane_role']['3']['games']
    pos4w+=result['lane_role']['3']['win']
    pos5g+=result['lane_role']['4']['games']
    pos5w+=result['lane_role']['4']['win']

    total_games = pos1g+pos2g+pos3g+pos4g+pos5g

    wrp1 = round((pos1w/pos1g)*100)
    wrp2 = round((pos2w/pos2g)*100)
    wrp3 = round((pos3w/pos3g)*100)
    wrp4 = round((pos4w/pos4g)*100)
    wrp5 = round((pos5w/pos5g)*100)
    
    return total_games, pos1g, pos2g, pos3g, pos4g, pos5g, wrp1, wrp2, wrp3, wrp4, wrp5

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

    #LANE ROLE
    total_games, pos1g, pos2g, pos3g, pos4g, pos5g, wrp1, wrp2, wrp3, wrp4, wrp5 = lane_role(steamid32)

    embed = discord.Embed(
        title=personaname, description=account_id, color=0x077369)
    embed.set_thumbnail(url=avatarfull)
    embed.add_field(name="MMR", value=mmr_estimate, inline=True)
    embed.add_field(name="KDA", value=f'{k}/{d}/{a}', inline=True)
    embed.add_field(name="Main role", value="'coming soon'", inline=True)
    embed.add_field(name="Competive Rank", value=competitive_rank, inline=False)
    embed.add_field(name=f"Total games", value=f"{total_games}", inline=True)
    embed.add_field(name=f"Pos1: {pos1g}", value=f"{wrp1}% win", inline=True)
    embed.add_field(name=f"Pos2: {pos2g}", value=f"{wrp2}% win", inline=True)
    embed.add_field(name=f"Pos3: {pos3g}", value=f"{wrp3}% win", inline=True)
    embed.add_field(name=f"Pos4: {pos4g}", value=f"{wrp4}% win", inline=True)
    embed.add_field(name=f"Pos5: {pos5g}", value=f"{wrp5}% win", inline=True)

    embed.add_field(name="Profile URL", value=profileurl, inline=False)
    embed.set_footer(text="@copyright bytheorderofPeakyBlinders")

    return embed


bot.run(TOKEN)