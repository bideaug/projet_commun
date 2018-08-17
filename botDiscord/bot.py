# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py
import discord
import random
import asyncio
import aiohttp
import os
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("?", "!")
TOKEN = 'NDM1Nzk1NDk1ODM1OTI2NTI4.DbeK7g.-uOyUCdpRyA0IT_KG-VJcCAw1bk'

class Duck_bot(Bot):
    def __init__(self,command_prefix):
        Bot.__init__(self,command_prefix)
        self.faim = 100
    
    def get_faim(self):
        return self.faim

    def set_faim(self,new_faim):
        self.faim = new_faim
        if self.faim < 0:
            self.faim = 0


bot = Duck_bot(command_prefix=BOT_PREFIX)

@bot.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == bot.user:
        return

    if message.content.startswith('Hello Ducky'):
        msg = 'Hello {0.author.mention}! <3'.format(message)
        await message.channel.send(msg)
        
    if 'ducky' in str(message.content).lower():
        msg = 'Coin?'.format(message)
        await message.channel.send(msg)
        
    if 'faim' in str(message.content).lower():
        msg = ('FAIM! genre '+str(bot.get_faim()))+"%".format(message)
        await message.channel.send(msg)
    
    if 'snack' in str(message.content).lower():
        possible_responses = ['Naaaaa',
                            'Coin...',
                            'Bofbof!',
                            'Miam!',
                            'Owiiiiiii',
                            ]
        msg = possible_responses[int(0.5+(4*bot.get_faim()/100))]
        await message.channel.send(msg)
    await bot.process_commands(message)

@bot.command()
async def snack(ctx):
    bot.set_faim(bot.get_faim()-1)
    await ctx.send("*scrounch scrouch*")


@bot.command()
async def pict(ctx):
    direc = os.listdir(os.getcwd()+'/Pictures')
    msg ="Photos "
    for i in direc:
        msg += i
        if i != direc[-1]:
            msg+=", "
    msg += "?"
    await ctx.send(msg)

    def choice_check(m):
        return (m.content in direc)

    msg = await bot.wait_for('message',check = choice_check)
    direc = os.getcwd()+ "/Pictures/"+msg.content
    possible_pict = os.listdir(direc)
    pict = direc + '/'+random.choice(possible_pict) 

    await ctx.send(file=discord.File(pict))
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(TOKEN)
