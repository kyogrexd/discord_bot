import discord
from discord.ext import commands
import json 
import random
import os


#叫出設定黨
#                             讀取
with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='/')  #建置實體

@bot.event
async def on_ready():
    print(">>bot is online<<")

# #事件處理 目前有BUG
# @bot.event
# async def on_member_join(member):
#     print(f'{member}join!')
#     print(jdata["CHAANEL"])
#     channel = bot.get_channel(int(jdata["CHAANEL"]))
#     await channel.send("加入")
    
# @bot.event
# async def on_member_remove(member):
#     print('leave!')
#     print(jdata["CHAANEL"])
#     channel = bot.get_channel(int(jdata["CHAANEL"]))
#     await channel.send("退出")

# #指令
# @bot.command()
# async def ping(ctx):
#     await ctx.send(f'{round(bot.latency*1000)}(ms)')


# #傳送圖片
# @bot.command()
# async def pic(ctx):
#     # pic = discord.File(jdata['PIC'])
#     # await ctx.send(file=pic)
#     #隨機選圖片
#     random_pic = random.choice(jdata['PIC'])
#     pic = discord.File(random_pic)
#     await ctx.send(file=pic)

# @bot.command()
# async def web(ctx):
#     random_pic = random.choice(jdata['URL_PIC'])
#     await ctx.send(random_pic)


@bot.command()
async def load(ctx,extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'loaded {extension} done!')

@bot.command()
async def unload(ctx,extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'un-loaded {extension} done!')

@bot.command()
async def reload(ctx,extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f're-Loaded {extension} done!')


#導入cmds 所有文件
for filename in os.listdir('./cmds'):
    print(filename)
    if filename.endswith('.py'): #取得尾數是 .py
        bot.load_extension(f'cmds.{filename[:-3]}')
                                        #  main.py去掉.py
  
if __name__=="__main__":
    bot.run(jdata['TOKEN'])



