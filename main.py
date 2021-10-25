from discord.ext import commands
from webserver import keep_alive
import os

bot = commands.Bot(command_prefix='?')

bot.lava_nodes = [
    {
        'host': 'lava.link',
        'port': 80,
        'rest_uri': f'http://lava.link:80',
        'identifier': 'MAIN',
        'password': 'anything',
        'region': 'singapore'

    }
]

@bot.event 
async def on_ready():
    print('Bot con dang dc test')
    bot.load_extension('dismusic')
    bot.load_extension('dch')

keep_alive()
TOKEN = os.environ.get("OTAxODc4NTI3ODc0NDM3MTQw.YXWR1Q.ldL1IA6aTGbs3y0yVKu0SezelBI")
bot.run("OTAxODc4NTI3ODc0NDM3MTQw.YXWR1Q.ldL1IA6aTGbs3y0yVKu0SezelBI")