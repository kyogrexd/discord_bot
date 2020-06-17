import discord
from discord.ext import commands
import json
from core.classes import Cog_Extension 
from cmds.main import Main
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
        await channel.send(f'{member} join!')
    
    @commands.Cog.listener()
    async def on_member_remove(self,member):
        print(f'{member}leave!')
        channel = self.bot.get_channel(int(jdata["CHAANEL"]))
        await channel.send(f'{member} leave!')

    @commands.Cog.listener()
    async def on_message(self,msg):
        keyword = jdata["KEYWORD"]
        if msg.content in keyword and msg.author != self.bot.user:
            await msg.channel.send('是白癡')

    #處理"指令"發生的錯誤 Error Handler
    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        #await ctx.send(error)
        # await ctx.send(ctx.command) #輸出 輸入的指令
        #檢查指令是否有自己的error handler:如果有就略過
        if hasattr(ctx.command,'on_error'):
            return    #直接跳出函數

        if isinstance(error,commands.errors.MissingRequiredArgument):
            await ctx.send("請輸入參數")  #cmd1的錯誤
        elif isinstance(error,commands.errors.CommandNotFound):
            await ctx.send("沒有這cmd")
        else:
            await ctx.send(error)

    #處理個別專用的錯誤處理
    @Main.cmd2.error
    async def cmd2_error(self,ctx,error):
        if isinstance(error,commands.errors.MissingRequiredArgument):
            await ctx.send("請輸入 cmd2 參數")  
          

    @commands.Cog.listener()
    async def on_raw_reaction_add(self,data):   #on_raw_reaction_add 抓discord cache     #on_reacrion_add 抓 bot cache(bot關機 就沒了)
        #print(data)
        print(data.emoji)
        # print(data.user_id)
        #print(data.member)
    #新增反應貼圖獲取身分組
    # 1.使用者反應
    # 2.判斷反應貼圖 
    # if 使用者新增貼圖 == 某個指定貼圖
        if data.message_id == 718364870973587547:
            if str(data.emoji) == '<:1a80e4e99dcf5d7383c8c02e3a969c72:718701778501369856>':
                print("ok")
                guild = self.bot.get_guild(data.guild_id) #取得當前所在伺服器
                role=guild.get_role(717286661628756009) #取得伺服器內的指定身分組
                await data.member.add_roles(role)  #給予該成員身分組
                                        #身分組
                await data.member.send("取得身分組")

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self,data):   
        #print(data)
        print(data.emoji)
        #判斷指定訊息是否指定訊息
        #if 使用者新增反映的訊息==指定訊息
        if data.message_id == 718364870973587547:
            if str(data.emoji) == '<:1a80e4e99dcf5d7383c8c02e3a969c72:718701778501369856>':
                print("ok")
                guild = self.bot.get_guild(data.guild_id) #取得當前所在伺服器
                user = guild.get_member(data.user_id)   #取得使用者
                role=guild.get_role(717286661628756009) #取得伺服器內的指定身分組
                await user.remove_roles(role)  #移除該成員身分組
                                    #身分組
                await user.send("移除身分組")      
            

    
        
        

def setup(bot):
    bot.add_cog(Event(bot))
