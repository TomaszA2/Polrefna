import os
import discord
import asyncio
global str

client = discord.Client()
szukane="stand"

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.author.nick == 'Joseph':
        tmp = await client.send_message(message.channel, 'Impossible!')

client.run(os.getenv('TOKEN'))
