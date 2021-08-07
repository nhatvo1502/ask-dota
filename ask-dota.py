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
    print(content_jason)
    embed = discord.Embed(
        title=personaname, description=account_id, color=0x077369)
    embed.set_thumbnail(url=avatarfull)
    embed.add_field(name="MMR", value=mmr_estimate, inline=True)
    embed.add_field(name="KDA", value="'coming soon'", inline=True)
    embed.add_field(name="Main role", value="'coming soon'", inline=True)
    embed.add_field(name="Competive Rank",
                    value=competitive_rank, inline=False)

    embed.add_field(name="[Pos1: 30%]--[Pos2: 20%]--", value=".", inline=True)
    embed.add_field(name="[Pos3: 10%]--[Pos4: 30%]--", value=".", inline=True)
    embed.add_field(name="[Pos5: 10%]", value=".", inline=True)

    embed.add_field(name="Profile URL", value=profileurl, inline=False)
    embed.set_footer(text="@copyright bytheorderofPeakyBlinders")
    
    return embed

def getRecent100(steamid32):
    odPath = f"https://api.opendota.com/api/players/{steamid32}/matches?limit=100"
    r = requests.get(odPath)
    response_info = json.loads(r.content)
    
    return response_info

def getAvgKDA(response_info):
    k,d,a=0,0,0
    for r in response_info:
        k += r['kills']
        d += r['deaths']
        a += r['assists']
    
    kad = {}    
    kad['avg_k'] = int(round(k/len(response_info)))
    kad['avg_d'] = int(round(d/len(response_info)))
    kad['avg_a'] = int(round(a/len(response_info)))
    return kad

recent100 = getRecent100(86745912)
kda = getAvgKDA(recent100)
print(kda)
