import discord
from discord.ext.commands import Bot
import os

bot = Bot(command_prefix='.', intents=discord.Intents.all())
token = os.environ["token"]
channel_id = os.environ["channel_id"]

@bot.event
async def on_ready():
    await bot.wait_until_ready()
    
    print(f'{bot.user} is online')
    await bot.get_channel(channel_id).send('hello discord from github')
    
    exit()
    
bot.run(token)