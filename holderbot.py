import requests
import json

import discord
from discord.ext.commands import bot
from discord.guild import Guild
from discord.ext import commands, tasks
from discord.utils import get

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('bot is ready')
    holdersloop.start()

@tasks.loop(seconds = 3600)
async def holdersloop():
    mint = "" #token mint
    endpoint = "https://api.mainnet-beta.solana.com"
    headers = {
            'Content-Type': 'application/json',
        }   
    data = ' { "jsonrpc": "2.0", "id": 1, "method": "getProgramAccounts", "params": [ "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA", { "encoding": "jsonParsed", "filters": [ { "dataSize": 165 }, { "memcmp": { "offset": 0, "bytes": "' + f"{mint}" + '" } } ] } ] } '
    response = requests.post(endpoint, headers=headers, data=data)

    r = response.json()

    rstr = json.dumps(r)


    n = rstr.count('pubkey')

    guild = client.get_guild()  #your server id
    pricebot = guild.get_member()  #your bot id
    await pricebot.edit(nick=f'{n:,} HOLDERS')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Holders made by @_Onga_" ))


client.run('') #your bot token
