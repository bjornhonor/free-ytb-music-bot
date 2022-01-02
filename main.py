import discord
from discord.ext import commands
import music

with open('token.txt', 'r') as f:
    token = f.read()

cogs = [music]
client = commands.Bot(command_prefix='-', intents=discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)
client.run(token)
