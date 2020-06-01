import discord
from discord.ext import commands
from core.classes import Cog_Extension  #導入core資料夾的classes.py
import json 
import random
import datetime


#https://www.youtube.com/watch?v=4JptXXkqiKU&list=PLSCgthA1Anif1w6mKM3O6xlBGGypXtrtN&index=10
#屬性定義
#繼承
# class Cog_Extension(commands.Cog):
#                       從setup()傳進去的bot
    # def __init__(self,bot): #初始化
    #     self.bot = bot
class Main(Cog_Extension):

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}(ms)')

    @commands.command()
    async def hi(self,ctx):
        await ctx.send('拉進勞改營!!')

    @commands.command()
    async def em(self,ctx): 
        embed=discord.Embed(title="介紹", url="https://www.youtube.com/watch?v=NnxgnMOmMF4&list=PLSCgthA1Anif1w6mKM3O6xlBGGypXtrtN&index=12", description="測試用", color=0x00ff40
        ,timestamp=datetime.datetime.now()-datetime.timedelta(hours=8))
        embed.set_author(name="yuhao_huang", url="https://www.youtube.com/watch?v=NnxgnMOmMF4&list=PLSCgthA1Anif1w6mKM3O6xlBGGypXtrtN&index=12",icon_url="https://image.gameapps.hk/images/201912/15/1.jpg")
        embed.set_thumbnail(url="https://image.gameapps.hk/images/201912/15/1.jpg")
        embed.add_field(name="1", value="92", inline=True)
        embed.add_field(name="2", value="60", inline=False)
        embed.add_field(name="3", value="88", inline=False)
        embed.set_footer(text="Tifa")
        await ctx.send(embed=embed)

    # * 表示後面arg 都是msg
    @commands.command()         
    async def sayd(self,ctx,*,msg):    
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def clear(self,ctx,num : int):
        await ctx.channel.purge(limit=num+1)

#啟動bot.py時 這功能就會啟動
#         是 bot.py 裡的 bot
def setup(bot):
    bot.add_cog(Main(bot)) #新增 Main的bot...


