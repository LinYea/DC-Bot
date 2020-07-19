import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime

class Main(Cog_Extension):

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)} 毫秒')

    @commands.command()
    async def hi(self, ctx):
        await ctx.send('1234')


    @commands.command()
    async def em(self, ctx):
        embed=discord.Embed(title="Join my discord club!", url="https://cdn.discordapp.com/attachments/605290629383192587/729622102302392400/68102556_p0_master1200.png", color=0x5900ff, 
        timestamp=datetime.datetime.utcnow())
        embed.set_author(name="ㄏ ㄏ#7516", url="https://discord.gg/x7qrbPJ", icon_url="https://cdn.discordapp.com/attachments/605290629383192587/729622102302392400/68102556_p0_master1200.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/605290629383192587/729622102302392400/68102556_p0_master1200.png")
        embed.add_field(name="1", value="3", inline=True)
        embed.add_field(name="2", value="4", inline=True)
        embed.set_footer(text="5")
        await ctx.send(embed=embed)

#--------------訊息複誦、清理訊息--------------#

    @commands.command()    #訊息複誦
    async def sayd(self, ctx, *,msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()    #清理訊息
    async def clear(self, ctx, mg: int):
        await ctx.channel.purge(limit=mg+1)

    

def setup(bot):
    bot.add_cog(Main(bot))