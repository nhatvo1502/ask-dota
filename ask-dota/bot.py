# bot.py
import os
import discord
import herolist

#import
from discord.ext import commands
from dotenv import load_dotenv

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
    


bot.run(TOKEN)