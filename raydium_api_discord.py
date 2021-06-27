import requests, json
import discord
from discord.ext import commands
from discord import channel, embeds


client = commands.Bot(command_prefix = '.')



@client.event
async def on_ready():
    print('bot is ready')

@client.command()
async def lp(ctx, tokenMint: str):
    
    channel = client.get_channel() #your chat channel id (make sure you have enabled dev console and then right click on the channel and click copy id
    
    r = requests.get('https://api.raydium.io/pairs')   #raydium official api
    api = r.json()

    apin= len(api)
    
    for i in range(apin):
        api_pair = api[i]['pair_id']
        
        if api_pair[:6] == tokenMint[:6]:  #find the token asked
            
           #discord basic embed
            
            embed=discord.Embed(title="Raydium LP for " + api[i]['name'] , color=discord.Color.dark_green())
            

            
            embed.add_field(name="Price", value=api[i]['price'], inline=False)
            
            embed.add_field(name="Market ID:", value=api[i]['market'], inline=False)
            
            embed.add_field(name="AMM ID:", value=api[i]['amm_id'], inline=False)
            
            embed.add_field(name="LP Mint:", value=api[i]['lp_mint'], inline=False)
           
            embed.add_field(name="Liquidity:", value=api[i]['liquidity'], inline=False)
            
            embed.add_field(name="24h Fees:", value=api[i]['fee_24h'], inline=False)
            
            embed.add_field(name="7days Fee:", value= api[i]['fee_7d'], inline=False)
            
            embed.add_field(name="24h Volume:", value=api[i]['volume_24h'], inline=False)
            
            embed.add_field(name="7D Volume:", value=api[i]['volume_7d'], inline=False)
            
            embed.add_field(name="APY (1y Fees/Liquidity):", value=api[i]['apy'], inline=False)

            embed.set_footer(text="© Always DYOR, number may change + impermanent loss")
            
            embed.set_thumbnail(url = "https://s2.coinmarketcap.com/static/img/coins/200x200/8526.png")

            await channel.send(embed=embed)
            
            
   
client.run('') #your bot key
