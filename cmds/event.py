import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channle = self.bot.get_channel(int(jdata['WC&LC']))
        await channle.send(f'新成員 {member} 已加入!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channle = self.bot.get_channel(int(jdata['WC&LC']))
        await channle.send(f'成員 {member} 已離開')

#--------------關鍵字觸發--------------#

    @commands.Cog.listener()
    async def on_message(self, msg):
        keyword = ['apple', 'pen', 'pie']
        if msg.content in keyword and msg.author !=  self.bot.user:
            await msg.channel.send('apple')


def setup(bot):
    bot.add_cog(Event(bot))