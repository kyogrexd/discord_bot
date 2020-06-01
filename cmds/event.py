import discord
from discord.ext import commands
import json
from core.classes import Cog_Extension 

#叫出設定黨
#                             讀取
with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):

    #事件處理 目前有BUG
    @commands.Cog.listener()
    async def on_member_join(self,member):
        print(f'{member}join!')
        channel = self.bot.get_channel(int(jdata["CHAANEL"]))
        await channel.send("2222222")
    
    @commands.Cog.listener()
    async def on_member_remove(self,member):
        print('leave!')
        channel = self.bot.get_channel(int(jdata["CHAANEL"]))
        await channel.send("2222222")

    @commands.Cog.listener()
    async def on_message(self,msg):
        keyword = jdata["KEYWORD"]
        if msg.content in keyword and msg.author != self.bot.user:
            await msg.channel.send('是白癡')
            

def setup(bot):
    bot.add_cog(Event(bot))
