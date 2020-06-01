import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json 
import random

#                             讀取
with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

#繼承
class React(Cog_Extension):

    #傳送圖片
    @commands.command()
    async def pic(self,ctx):
        # pic = discord.File(jdata['PIC'])
        # await ctx.send(file=pic)
        #隨機選圖片
        random_pic = random.choice(jdata['PIC'])
        pic = discord.File(random_pic)
        await ctx.send(file=pic)

    @commands.command()
    async def web(self,ctx):
        random_pic = random.choice(jdata['URL_PIC'])
        await ctx.send(random_pic)

    # @commands.command()
    # async def vd(self,cxt):
    #     video = discord.File(jdata['VIDEO'])
    #     await cxt.send(file=video)        

def setup(bot):
    bot.add_cog(React(bot))

