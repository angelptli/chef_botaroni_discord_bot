import discord
import os
import re
import requests
import json
import random

client = discord.Client()

trigger_phrases = ["agon", "angry", "bad", "beat", "bleak", "cry", "depress",
                   "diss", "down", "freak", "furious", "fury", "fustrat",
                   "hate", "help", "less", "loser", "mad", "mean", "miser",
                   "murk", "not", "regret", "sad", "shi", "sorr", "stop",
                   "tear", "stress", "suck", "trigger", "weep", "unhappy",
                   "welp", "wimp", "worry"]

trigger_replies = [
    "Have a snickers",
    "When life gives you lemons, don't squeeze them directly in your eyes",
    "Keep going, I'm always here to lend a virtual pear",
    "How many times do I need to repeat this? Beep boop salad.",
    "Beep Boooooop...orange",
    "Beep Boop almonds",
    "Get well, or else I'll force feed you durian",
    "Do we need a bartender?",
    "We will break bread and dip it in sauce eventually",
    "Eventually there will be milk in our cereal bowls",
    "Milk or cereal first in the bowl?"
    "Don't drink too much, you have one liver",
    "Looking back...that egg was sunny side up",
    "Spit it out. The peas.",
    "Someone's crackling like pop rocks",
    "Breatheee...you can smell the salt in the air",
    "Remember, avocados are fruits, not veggies",
    "Say it with me: Beep carbs, boop carrots.",
    "I know right, I love burritos too.",
    "You like gold? How 'bout deez nuggets?",
    ":( french fries",
    "I don't know how to prepare a salad",
    ":l Soups",
    "Omg got milk?",
    "You dropped your hot pocket?",
    "Oh I dropped my hot pocket.",
    "Don't mind me. I'm just here eating popcorn."
    ]

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

    msg = message.content

    if re.search('[H|h]([a|e]llo|i|ey|owdy)', msg):
        await message.channel.send('Hello to you too!')
    elif re.search('\$inspire', msg):
        await message.channel.send(get_quote())
    elif any(word in msg for word in trigger_phrases):
        await message.channgel.send(random.choice(trigger_replies))

client.run(os.getenv('TOKEN'))
