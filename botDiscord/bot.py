# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py
import discord
import random
import asyncio
import aiohttp
import os
import time
import numpy as np
from discord import Game
from discord.ext.commands import Bot

log_file = np.genfromtxt(os.environ['HOME']+'/dat.log',dtype=str)
print (log_file)
BOT_PREFIX = ("?", "!")

TOKEN = log_file[0] 
FAIM = log_file[1]
TIME = log_file[0]


class Duck_bot(Bot):
    def __init__(self,command_prefix,faim = 100,time = None):
        Bot.__init__(self,command_prefix)
        self.faim = faim
        self.intern_clock = time
        self.faim_time = 5
         
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
        
    elif 'ducky' in str(message.content).lower():
        msg = 'Coin?'.format(message)
        await message.channel.send(msg)
        
    elif 'faim' in str(message.content).lower():
        msg = ('FAIM! genre '+str(bot.get_faim()))+"%".format(message)
        await message.channel.send(msg)
    
    elif 'snack' in str(message.content).lower():
        possible_responses = ['Naaaaa',
                            'Coin...',
                            'Bofbof!',
                            'Miam!',
                            'Très!',
                            'Owiiiiiii',
                            ]
        msg = possible_responses[int(0.5+((len(possible_responses)-1)*bot.get_faim()/100))]
        await message.channel.send(msg)
    await bot.process_commands(message)


@bot.command()
async def start_faim(ctx):
    
    time_ref = time.localtime()[4]
    print(time.localtime()[4])
    if time_ref == 0:
        asyncio.sleep(60)
        time_ref = time.localtime()[4]
        
    while True:
        if np.abs(time_ref-time.localtime()[4])>bot.faim_time and bot.get_faim()<100:
            time_ref = time.localtime()[4]
            bot.set_faim(bot.get_faim()+1)
        await asyncio.sleep(10)


@bot.command()
async def snack(ctx, a : int = 1):
    if a>5:
        msg = "Arblaghbla...!"
        await ctx.send(msg):
    else:        
        bot.set_faim(bot.get_faim()-a)
        await ctx.send("*scrounch scrouch*")

@bot.command()
async def meal(ctx):
    
    bot.set_faim(bot.get_faim()+50)
    await ctx.send("*Miam!*")

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
