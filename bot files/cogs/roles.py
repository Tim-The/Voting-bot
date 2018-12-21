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
     role = discord.utils.get(ctx.guild.roles, id=524947192306204673)
     if role in ctx.message.author.roles:
         try:
             await ctx.message.author.remove_roles(role)
         except (discord.Forbidden, discord.HTTPException) as error:
             await ctx.send("Got an error: {}".format(error))
         else:
             await ctx.send(":ok_hand: Removed Role `{}`".format(role.name))
             return
     else:
         try:
             await ctx.message.author.add_roles(role)
         except (discord.Forbidden, discord.HTTPException) as error:
             await ctx.send("Got an error: {}".format(error))
         else:
             await ctx.send(":ok_hand: Added Role `{}`".format(role.name))
             return


def setup(bot):
 bot.add_cog(roles(bot))
