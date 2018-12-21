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
 async def updaterole(self, ctx):
     if "Emotes updates" in ctx.message.author.roles:
         member = ctx.message.author
         role = get(member.guild.roles, name="Emote updates")
         await  member.remove_roles(member, role)
         await ctx.send(":ok_hand: Removed \"Emote updates\" role")
     else:
         member = ctx.message.author
         role = get(member.guild.roles, name="Emote updates")
         await member.add_roles(member, role)
         await ctx.send(":ok_hand: Added \"Emote updates\" role")


def setup(bot):
 bot.add_cog(roles(bot))
