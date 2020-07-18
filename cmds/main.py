import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Main(Cog_Extension):

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(bot.latency*1000)} 毫秒')

def setup(bot):
    bot.add_cog(Mian(bot))