import discord
from discord.ext.commands import bot
from discord.guild import Guild
from discord.ext import commands, tasks
from discord.utils import get

import requests


client = commands.Bot(command_prefix = '.')



#check if bot is ready + start loop
@client.event
async def on_ready():
    print('bot is ready')
    priceloop.start()


@tasks.loop(seconds = 120)
async def priceloop():

 
    r = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=sail&vs_currencies=usd")

    
    price = r.json()
    

    guild = client.get_guild()  #your server id
    pricebot = guild.get_member()  #your bot id
    await pricebot.edit(nick="SAIL %.3f$" % price['sail']['usd'] )
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="SAIL Price bot made by @_Onga_"))
    



client.run('') #your bot token
