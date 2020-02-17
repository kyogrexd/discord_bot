import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

bot.run('Njc4ODc0MTUzNTU3Njg4MzUy.XkpI2g.FqQdzetCm7YeLGCFt6Ih7Q_-vKc')


