#imports
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands

import logging

client = discord.Client()

#cog initiation
class voting:

 def __init__(self, bot):
     # creation of the cog, do init stuff here, also gets and stores the bot
     self.bot: commands.Bot = bot

 def __unload(self):
     # cog unloading, cleaup if needed
     pass


 @client.event
 async def on_message(self, message):
     if message.channel.id == 517026327673569290: 
         if len(message.attachments) > 0:
             await message.add_reaction(":painnope:521427455194693643") #deny reaction
             await message.add_reaction(":painyes:521427455257477156") #approve reaction
         else:
             return
     else:
         return

def setup(bot):
 bot.add_cog(voting(bot))