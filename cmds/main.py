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


    #隨機組隊
    @commands.command()
    async def rand_squad(self,ctx):
        # ctx.guild 所在伺服器
        # ctx.guild.members 列出所有成員清單
        # 判斷成員在線狀態:
        # if 成員狀態 == 在線:
        #   就把該成員加到 list(online)中

        #print(ctx.guild.members)

        offline = []
        for member in ctx.guild.members:
            #print(member.status)
            #await ctx.send(member)
            # await ctx.send(member.status)
            #print(type(member.status))
            if str(member.status) == "offline" and member.bot == False:
                offline.append(member.name)

        #print(random.choices(offline,k=5))

        random_offline = random.sample(offline,k=6) #sample 不重複 choices 會重複
        # await ctx.send(random.sample(random_offline,k=2)
        for squad in range(3):
            list2 = random.sample(random_offline,k=2)
            #print(list2)  
            for name in list2:
                random_offline.remove(name)
                #print(name)
            a = ','.join(list2)
            await ctx.send(f"{squad+1}小隊:" + str(a))

    @commands.command()
    async def test(self,ctx):
        print(ctx.guild.members)

    
    #group 群組
    #subcommand子命令
    @commands.group()
    async def codetest(self,ctx):
        # await ctx.send("group")
        pass
    @codetest.command()
    async def python(self,ctx):
        await ctx.send("python") 
    @codetest.command()
    async def java(self,ctx):
        await ctx.send("java")    
    @codetest.command()
    async def cpp(self,ctx):
        await ctx.send("cpp")   



    @commands.command()
    async def cmd1(sef,ctx,num):
        await ctx.send(num)

    @commands.command()
    async def cmd2(sef,ctx,n:int):
        await ctx.send(n)

    @commands.command()
    async def cmd3(self,ctx,num:int):
        try:
            await ctx.send(num)
        except Exception as e:
            await ctx.send(e)
     


           

        
        


        
        
    

#啟動bot.py時 這功能就會啟動
#         是 bot.py 裡的 bot
def setup(bot):
    bot.add_cog(Main(bot)) #新增 Main的bot...


