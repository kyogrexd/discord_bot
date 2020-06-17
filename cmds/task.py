import discord
from discord.ext import commands
from core.classes import Cog_Extension #導入core資料夾的classes.py
import json, asyncio, datetime

class Task(Cog_Extension):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        #父類別.初始化屬性

        #間隔時間指令
        # async def interval():
        #     await self.bot.wait_until_ready() #等bot
        #     self.channel = self.bot.get_channel(679567127463591957)
        #     while not self.bot.is_closed(): #當bot沒關閉
        #         await self.channel.send("hi I'm running")
        #         await asyncio.sleep(5) #秒

        # self.bg_task = self.bot.loop.create_task(interval())
        self.counter = 0

        async def time_tasks():
            await self.bot.wait_until_ready() #等bot
            self.channel = self.bot.get_channel(679567076989730877)
            while not self.bot.is_closed(): #當bot沒關閉
                now_time = datetime.datetime.now().strftime("%H%M")
                with open('setting.json',mode='r',encoding='utf8') as jfile:
                    jdata = json.load(jfile)
                if(now_time == jdata['time']and self.counter == 0):
                    await self.channel.send('指令時間到了!')
                    self.counter = 1
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)  #一定要讓這行 為了不讓bot卡住 要等bot

        self.bg_task = self.bot.loop.create_task(time_tasks())

#改頻道
    @commands.command()
    async def set_channel(self,ctx,ch:int):
        self.channel = self.bot.get_channel(ch)
        await ctx.send(f'Set channel:{self.channel.mention}')

#改時間
    @commands.command()
    async def set_time(self,ctx,time):
        self.counter = 0
        with open('setting.json',mode='r',encoding='utf8') as jfile:
            jdata = json.load(jfile)

        jdata["time"] = time

        with open('setting.json',mode='w',encoding='utf8') as jfile:
            json.dump(jdata,jfile,indent=4)






def setup(bot):
    bot.add_cog(Task(bot))
