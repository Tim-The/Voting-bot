import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
from urbandictionary_top import udtop
class misc:

 def __init__(self, bot):
     # creation of the cog, do init stuff here, also gets and stores the bot
     self.bot: commands.Bot = bot

 def __unload(self):
     # cog unloading, cleaup if needed
     pass
 
#521388774375161861 - Pain Designer ID
 @commands.command()
 async def urban(self, ctx, message):
     """gives the urban result of the given word"""
     role = discord.utils.get(ctx.guild.roles, id=521388774375161861)
     if role in ctx.message.author.roles:
         #test = message        #also debug option
         #await ctx.send(test)  #debug option
         term = udtop(message)
         embed = discord.Embed(title=message+":", colour=discord.Colour(0x2773cc), description=term.definition+"\n\n examples: \n"+term.example)
         embed.set_footer(text="powered by urbandictionary.com", icon_url="https://i.imgur.com/RvNANOu.png")
         await ctx.send(content="", embed=embed)
     else:
         await ctx.send("This command is restricted to \"Pain Designers\" role or above")


def setup(bot):
 bot.add_cog(misc(bot))