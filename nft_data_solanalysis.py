
# needs discord py and requests installed 

import discord
from discord.guild import Guild
from discord.ext import commands, tasks

import requests

client = commands.Bot(command_prefix = '.')



#check if bot is ready + start loop
@client.event
async def on_ready():
    print('bot is ready')
    priceloop.start()


@tasks.loop(seconds = 120)
async def priceloop():


    data = requests.get("https://solanalysis-dot-feliz-finance.uc.r.appspot.com/projects/get_all_project_stats") #getting solanalysis data


    data = data.json()

    project_number = 1 # open the link that we request earlier and get your desired project number ! 

    name = data['Projects'][project_number]['DisplayName']
    floor = data['Projects'][project_number]['FloorPrice']


    
    


    

    guild = client.get_guild()  #your server id
    pricebot = guild.get_member()  #your bot id
    await pricebot.edit(nick= "Floor: "+str(floor)+" SOL")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=name+" floor price Bot made by @_Onga_" ))




@client.command()
async def data(ctx):
    
    
    channel = client.get_channel(850734532209410059)# suggest setting up a channel were people can get this data, having it everywhere may result spammy! 
                                                    # if you want it aviable in every channel change line 106 and 107 to ctx.send instead of channel.send
    
    

    data = requests.get("https://solanalysis-dot-feliz-finance.uc.r.appspot.com/projects/get_all_project_stats") 


    data = data.json()

    project_number = 1 # open the link that we request earlier and get your desired project number !

    name = data['Projects'][project_number]['DisplayName']
    floor = data['Projects'][project_number]['FloorPrice']
    
    avg_price = data['Projects'][project_number]['AveragePrice']
    avg_priceD = data['Projects'][project_number]['AveragePrice_1D_CHG']
    
    MktCap = data['Projects'][project_number]['MarketCap']
    MaxPrice = data['Projects'][project_number]['MaxPrice']
    
    VolD =data['Projects'][project_number]['Volume_1D_CHG']
    Vol7d =data['Projects'][project_number]['Volume_7D']

    img= data['Projects'][project_number]['ImageUrl']

  
    
    embed=discord.Embed(title="Stats for " + name , color=discord.Color.darker_gray())

    embed.add_field(name="Floor", value=floor, inline=False)  
            
    embed.add_field(name="Average Price", value="%.2f" % avg_price, inline=True)
    embed.add_field(name="Daily average price change", value="%.2f" %avg_priceD + "%", inline=True)
    embed.add_field(name="\u200b", value="\u200b", inline=True)


    embed.add_field(name="Weekly Volume", value="%.0f" %Vol7d, inline=True)
    embed.add_field(name="Daily Volume Change", value="%.2f" %VolD + "%", inline=True)
    embed.add_field(name="\u200b", value="\u200b", inline=True)

    embed.add_field(name="Market Cap", value="%.0f" %MktCap, inline=True)
    embed.add_field(name="Max sell", value=MaxPrice, inline=True)

    embed.add_field(name="\u200b", value="\u200b", inline=True)



    embed.set_footer(text="© Always DYOR made by @_Onga_ powered by https://solanalysis.com/")
            
    embed.set_thumbnail(url = img)

    await channel.send(f"Here is your data! <@{ctx.author.id}>!")
    await channel.send(embed=embed)



client.run('') #your bot token







