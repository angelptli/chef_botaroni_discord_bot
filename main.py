import discord
import os
import re

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if re.search('[H|h]([a|e]llo|i|ey|owdy)', message.content):
        await message.channel.send('Hello to you too!')

client.run(os.getenv('TOKEN'))
