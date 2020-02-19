import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">>bot is online<<")

@bot.event
async def on_member_join(member):
    print(f'{member} join')
    chaanel = bot.get_channel(679208154034339860)
    await chaanel.send(f'{member} join')

@bot.event
async def on_member_leave(member):
    print(f'{member} leave')
    chaanel = bot.get_channel(679208154034339860)
    await chaanel.send(f'{member} leave')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')




bot.run('Njc4ODc0MTUzNTU3Njg4MzUy.Xkydkw.ldoixSSBY_AvAl1lp_W4jo7WbIA')