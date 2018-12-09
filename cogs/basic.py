#imports time
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import time
from datetime import datetime

import logging


class basic:

 def __init__(self, bot):
     # creation of the cog, do init stuff here, also gets and stores the bot
     self.bot: commands.Bot = bot

 def __unload(self):
     # cog unloading, cleaup if needed
     pass




 @commands.command()
 @commands.guild_only()
 @commands.has_permissions(administrator=True)
 async def shutdown(self, ctx):
     await ctx.send("shutting down")
     await self.bot.logout()
     await self.bot.close()

 @commands.command()
 async def ping(self, ctx:commands.Context):
     t1 = time.perf_counter()
     await ctx.trigger_typing()
     t2 = time.perf_counter()
     await ctx.send(f":hourglass: gateway ping: {round((t2 - t1) * 1000)}ms :hourglass:")
def setup(bot):
 bot.add_cog(basic(bot))