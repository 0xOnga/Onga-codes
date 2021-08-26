import discord
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix = '!', intents= intents)





@client.event
async def on_ready():
    print('bot is ready')
    

@client.command()
async def cat(ctx, catId:int):

    
    
    e=discord.Embed(title="MoonCats #%d" % catId, color=discord.Color.orange())

    e.set_image(url="https://www.mooncatfantom.com/api/image?id=%d" % catId)

    await ctx.send(embed = e)

   



client.run('') #your bot token
