import discord
from discord.ext.commands import Bot
import os, logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

bot = Bot(command_prefix='.', intents=discord.Intents.all())

try:
    token = os.environ["token"]
    channel_id = os.environ["channel_id"]
except KeyError:
    SOME_SECRET = "Token and id not available!"

    

@bot.event
async def on_ready():
    await bot.wait_until_ready()
    
    logger.info(f'{bot.user} is online')
    await bot.get_channel(channel_id).send('hello discord from github')
    
    exit()

if __name__ == '__main__':
    logger.info(f"Token value: {token}")
    bot.run(token)