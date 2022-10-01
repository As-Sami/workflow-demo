import discord
from discord.ext.commands import Bot
import os

bot = Bot(command_prefix='.', intents=discord.Intents.all())

token = ''
channel_id = 1019963447280144475

try:
    token = os.environ["TOKEN"]
except:
    print('env theke token pai nai')

    

@bot.event
async def on_ready():
    await bot.wait_until_ready()
    
    print.info(f'{bot.user} is online')
    await bot.get_channel(channel_id).send('hello discord from github')
    
    exit()

if __name__ == '__main__':
    print('token =', token)
    bot.run(token)