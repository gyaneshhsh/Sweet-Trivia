import discord
from discord.ext import commands
from discord.utils import get

bot=commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print('Online')

@bot.event
async def on_member_join(member):
    welcome_channel=get(member.guild.channels , name='general')
    await welcome_channel.send(f'''Welcome to {member.guild.name} {member.mention}''')


@bot.event
async def on_member_rmeove(member):
    left_channel=get(member.guild.channels , name='general')
    await left_channel.send(f'''{member.mention} just left the server''')


@bot.command()
async def announce(ctx,*,message):
    await ctx.send(message)




@bot.command()
async def purge(ctx,amount=50):
	if 'Owner' in [i.name for i in ctx.message.author.roles]:
		await ctx.channel.purge(limit=amount+1)


	else:
		await ctx.send(f'''You don't have perms {ctx.message.author.mention}''')


bot.run('NjI2NDQ4NjU5NjU1MDMyODQ1.XYuPzg.YlWlNC74O7DvnZ56-dTI-UFYIz4')
