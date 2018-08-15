# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py
import discord
import random
import asyncio
import aiohttp
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("?", "!")
TOKEN = 'NDM1Nzk1NDk1ODM1OTI2NTI4.DbeK7g.-uOyUCdpRyA0IT_KG-VJcCAw1bk'


bot = Bot(command_prefix=BOT_PREFIX)

@bot.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == bot.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)
        
    if 'ducky' in str(message.content).lower():
        msg = 'Coin?'.format(message)
        await message.channel.send(msg)
        
    if 'faim' in str(message.content).lower():
        msg = 'FAIM!'.format(message)
        await message.channel.send(msg)
    
    if 'snack' in str(message.content).lower():
        possible_responses = ['Owiiiiii!!!',
                            'Miam!',
                            'Bofbof!',
                            'Coin...',
                            'Naaaaa',
                            ]
        msg = random.choice(possible_responses)
        await message.channel.send(msg)
    await bot.process_commands(message)

@bot.command()
async def snack(ctx):
    possible_responses = ['Owiiiiii!!!',
                        'Miam!',
                        'Bofbof!',
                        'Coin...',
                        'Naaaaa',
                        ]
    await ctx.send(random.choice(possible_responses))

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(TOKEN)