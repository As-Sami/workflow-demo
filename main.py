import discord
from discord.ext.commands import Bot
import os

bot = Bot(command_prefix='.', intents=discord.Intents.all())

token = ''
channel_id = 0

try:
    token = os.environ["token"]
    channel_id = os.environ["channel_id"]
except KeyError:
    print('token not available')
    token = 'ODI0NjIzMDI1MTU1NzM1NTYy.GZVlW_._ZY2ahiEHdf0U_VscMgor8QXEquzpVhB4H1mxg'
    channel_id = 1019963447280144475

    

@bot.event
async def on_ready():
    await bot.wait_until_ready()
    
    print.info(f'{bot.user} is online')
    await bot.get_channel(channel_id).send('hello discord from github')
    
    exit()

if __name__ == '__main__':
    print('token =', token)
    bot.run(token)