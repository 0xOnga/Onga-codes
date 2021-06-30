import discord
from discord.ext.commands import bot
from discord.guild import Guild
from discord.ext import commands, tasks
from discord.utils import get

from pyserum.connection import conn
from pyserum.market import Market


client = commands.Bot(command_prefix = '.')



#check if bot is ready + start loop
@client.event
async def on_ready():
    print('bot is ready')
    priceloop.start()


@tasks.loop(seconds = 120)  #updating too frequently may lead to break discord api restrictions!
async def priceloop():

    cc = conn("https://api.mainnet-beta.solana.com/")
    market_address = "" # serum address of your coin
    market1 = Market.load(cc, market_address)


    #get first bid

    bids = market1.load_bids()
    for bid in list(bids)[-1:]:
        bidprice = bid.info.price
        

    
    #get first ask
    asks = market1.load_asks()
    
    
    for ask in list(asks)[:1]:
        askprice = ask.info.price
        


    guild = client.get_guild(4324324324324)  #your server id
    pricebot = guild.get_member(3243423424324)  #your bot id
    await pricebot.edit(nick=" %f$" % bidprice)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Sell order @ %f$ made by Onga#0185" % askprice))
    



client.run('BOT_TOKEN') #your bot token
