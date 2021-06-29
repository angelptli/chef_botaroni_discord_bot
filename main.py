import discord
import os
import re
import requests
import json

client = discord.Client()

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if re.search('[H|h]([a|e]llo|i|ey|owdy)', message.content):
        await message.channel.send('Hello to you too!')
    elif re.search('$inspire', message.content):
        await message.channel.send(get_quote())

client.run(os.getenv('TOKEN'))
