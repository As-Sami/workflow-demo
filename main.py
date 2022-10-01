import discord
from discord.ext.commands import Bot
import os

bot = Bot(command_prefix='.', intents=discord.Intents.all())

try:
    token = os.environ["token"]
    channel_id = os.environ["channel_id"]
except KeyError:
    SOME_SECRET = "Token and id not available!"

    

@bot.event
async def on_ready():
    await bot.wait_until_ready()
    
    print.info(f'{bot.user} is online')
    await bot.get_channel(channel_id).send('hello discord from github')
    
    exit()

if __name__ == '__main__':
    print('token =', token)
    bot.run(token)