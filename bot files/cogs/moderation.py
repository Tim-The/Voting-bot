import discord
from discord.ext import commands


class Moderationcog:

   def __init__(self, bot):
     # creation of the cog, do init stuff here, also gets and stores the bot
     self.bot: commands.Bot = bot

   def __unload(self):
     # cog unloading, cleaup if needed
     pass

   @commands.command()
   @commands.guild_only()
   @commands.has_permissions(ban_members=True)
   async def ban(self, ctx, user: discord.Member, *, reason = "No reason given"):
     if user == ctx.bot.user:
       await ctx.send("why you'd want to ban me")
     elif user == ctx.author:
       await ctx.send("can't ban yourself")
     elif user.top_role > ctx.guild.me.top_role:
       await ctx.send(f':no_entry_sign: {user.name} has role higher than me')
     elif user.top_role > ctx.author.top_role:
       await ctx.send(f':no_entry_sign: {user.name} has role higher than you')
     else:
       await ctx.guild.ban(user, reason=f"Moderator: {ctx.author.name} ({ctx.author.id}) reason: {reason}")
       await ctx.send(f":ok_hand: {user.name} ({user.id}) was banned `{reason}`")

   @commands.command()
   @commands.guild_only()
   @commands.has_permissions(ban_members=True)
   async def forceban(self, ctx, user_id: int, *, reason = "No reason given"):
     user = await ctx.bot.get_user_info(user_id)
     if user == ctx.bot.user:
       await ctx.send("why would you do that?")
     elif user == ctx.author:
       await ctx.send("can't ban yourself")
     else:
       await ctx.guild.ban(user, reason=f"Moderator: {ctx.author.name} ({ctx.author.id}) Reason: {reason}")
       await ctx.send(f":ok_hand: {user.name} ({user.id}) was banned. Reason: `{reason}`.")

   @commands.command()
   @commands.guild_only()
   @commands.has_permissions(ban_members=True)
   async def softban(self, ctx, member: discord.Member, *, reason = "No reason given"):
     if member == ctx.bot.user:
       await ctx.send("can't ban me, no more")
       return
     elif member == ctx.author:
       await ctx.send("can't softban yourself")
       return
     else:
       await ctx.guild.ban(member, reason=f"Moderator: {ctx.author.name} ({ctx.author.id}) reason: {reason}")
       await ctx.guild.unban(member)
       await ctx.send(f":ok_hand: {member.name} ({member.id}) was softbanned: `{reason}`.")

   @commands.command()
   @commands.guild_only()
   @commands.has_permissions(kick_members=True)
   async def kick(self, ctx, user: discord.Member, *, reason = "No reason given."):
     if user == ctx.bot.user:
       await ctx.send("why would you want to kick me dad")
     elif user == ctx.author:
       await ctx.send("can't kick yourself")
     elif user.top_role > ctx.guild.me.top_role:
       await ctx.send(f':no_entry_sign: {user.name} has role higher than me')
     elif user.top_role > ctx.author.top_role:
       await ctx.send(f':no_entry_sign: {user.name} has role higher than you')
     else:
       await ctx.guild.kick(user, reason=f"Moderator: {ctx.author.name} ({ctx.author.id}) reason: {reason}")
       await ctx.send(f":ok_hand: {user.name} ({user.id}) was kicked, reason: `{reason}`")

    
    
def setup(bot):
    bot.add_cog(Moderationcog(bot))
