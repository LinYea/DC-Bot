import discord
from discord.ext import commands
import json
import random
import os


with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


bot = commands.Bot(command_prefix= '[')

@bot.event
async def on_ready():
    print(">> 機器人以上線 <<")

@bot.event
async def on_member_join(member):
    channle = bot.get_channel(int(jdata['WC&LC']))
    await channle.send(f'新成員 {member} 已加入!')

@bot.event
async def on_member_remove(member):
    channle = bot.get_channel(int(jdata['WC&LC']))
    await channle.send(f'成員 {member} 已退出')


@bot.command()
async def load(ctx, extension):
    bot.reload_extension(F'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done.')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(F'cmds.{extension}')
    await ctx.send(f'Re - Loaded {extension} done.')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(F'cmds.{extension}')
    await ctx.send(f'Un - Loaded {extension} done.')


for fliename in os.listdir('./cmds'):
    if fliename.endswith('.py'):
        bot.load_extension(f'./cmds.{fliename[:-3]}')



if __name__ == "__main__":
    bot.run(jdata['TOKEN'])