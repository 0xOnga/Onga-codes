import requests
import json

import discord
from discord.ext.commands import bot
from discord.guild import Guild
from discord.ext import commands, tasks
from discord.utils import get

client = commands.Bot(command_prefix = '.')   #symbol before the command

@client.event
async def on_ready():
    print('bot is ready')
    holdersloop.start()

    
    #bot name loop
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
    
    data = json.loads(rstr)

    n = rstr.count('pubkey')

    #clear out 0 balance holders
    count = 0
    for i in range(n):
        if (data['result'][i]['account']['data']['parsed']['info']['tokenAmount']['uiAmount']) != 0:
            count= count + 1

    guild = client.get_guild()  #put your server id in the brackets
    pricebot = guild.get_member()  #put your bot id in the brackets
    await pricebot.edit(nick=f'{count:,} HOLDERS')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Holders made by @_Onga_" ))
    
    
    
    
    #command to retrieve holders
@client.command()
async def holders(ctx):    #name of the command
    mint = "" #token mint
    endpoint = "https://api.mainnet-beta.solana.com"
    headers = {
            'Content-Type': 'application/json',
        }   
    data = ' { "jsonrpc": "2.0", "id": 1, "method": "getProgramAccounts", "params": [ "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA", { "encoding": "jsonParsed", "filters": [ { "dataSize": 165 }, { "memcmp": { "offset": 0, "bytes": "' + f"{mint}" + '" } } ] } ] } '
    response = requests.post(endpoint, headers=headers, data=data)

    r = response.json()

    
    rstr = json.dumps(r)

    data = json.loads(rstr)

    n = rstr.count('pubkey')

    #clear out 0 balance holders
    count = 0
    for i in range(n):
        if (data['result'][i]['account']['data']['parsed']['info']['tokenAmount']['uiAmount']) != 0:
            count= count + 1

            
    
    await ctx.send('TOKEN_NAME currently has ' + f'{count:,}' + ' holders')


client.run('') #your bot token
