import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
from discord.utils import get
import logging


class roles:

 def __init__(self, bot):
     # creation of the cog, do init stuff here, also gets and stores the bot
     self.bot: commands.Bot = bot

 def __unload(self):
     # cog unloading, cleaup if needed
     pass
 
 @commands.command()
 async def updates(self, ctx):
         def has_role(author):
             for role in author.roles:
                 if role.id == 524947192306204673:
                     return True
                 return False

# Check role
         if has_role(ctx.message.author) is True:
             role = discord.utils.get(ctx.guild.roles, id=524947192306204673)
             user = ctx.message.author
             await user.remove_roles(role)
             await ctx.send(":ok_hand: Removed \"Emote updates\" role")
             return
         role = discord.utils.get(ctx.guild.roles, id=524947192306204673)
         user = ctx.message.author
         await user.add_roles(role)
         await ctx.send(":ok_hand: Added \"Emote updates\" role")
         return


def setup(bot):
 bot.add_cog(roles(bot))
