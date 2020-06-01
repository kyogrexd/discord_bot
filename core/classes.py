import discord
from discord.ext import commands

#在main/react 省略重複的程式
class Cog_Extension(commands.Cog):
    def __init__(self,bot): #初始化
        self.bot = bot