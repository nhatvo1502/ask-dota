# bot.py
import os
import discord
import herolist
import random
import requests
import json

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

#BOT PREFIX
bot = commands.Bot(command_prefix='!#')

#succesfully message
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

### FUNCTION ###
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
    response=f'json {response_info}'
    await ctx.send(response)


bot.run(TOKEN)