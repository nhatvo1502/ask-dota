# bot.py
import os
import discord

#import
from discord.ext import commands
from dotenv import load_dotenv

#connect discord ToKen
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#BOT PREFIX
bot = commands.Bot(command_prefix='!#')

client = discord.Client()

#succesfully message
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

### FUNCTION ###
#!info
@bot.command(name='info', help='bot info')
async def test(ctx):
    response = 'ASK-DOTA BOT'
    await ctx.send(response)








client.run(TOKEN)