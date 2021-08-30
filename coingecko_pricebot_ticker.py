import discord
from discord.ext.commands import bot
from discord.guild import Guild
from discord.ext import commands, tasks
from discord.utils import get

import pprint
import requests


client = commands.Bot(command_prefix = '.')



#check if bot is ready + start loop
@client.event
async def on_ready():
    print('bot is ready')
    priceloop.start()


@tasks.loop(seconds = 120)
async def priceloop():

 
    r = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=solanasail-governance-token&vs_currencies=usd&include_24hr_change=true")


    
    
    price = r.json()

    guild = client.get_guild()  #your server id
    pricebot = guild.get_member()  #your bot id
    if(price['solanasail-governance-token']['usd_24h_change'] > 0 ):
        await pricebot.edit(nick="gSAIL %.2f$" % price['solanasail-governance-token']['usd'])
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="24h Change 🔺%.2f" % price['solanasail-governance-token']['usd_24h_change']+ "%")) 

    if(price['solanasail-governance-token']['usd_24h_change'] < 0 ):
        await pricebot.edit(nick="gSAIL %.2f$" % price['solanasail-governance-token']['usd']) 
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="24h Change 🔻%.2f" % price['solanasail-governance-token']['usd_24h_change']+ "%")) 

    



client.run('') #your bot token




