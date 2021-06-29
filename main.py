import discord
import os
import re
import requests
import json
import random
# from replit import db

client = discord.Client()

trigger_phrases = ["agon", "angry", "bad", "beat", "bleak", "cry", "depress",
                   "diss", "down", "freak", "furious", "fury", "fustrat",
                   "hate", "help", "less", "loser", "mad", "mean", "miser",
                   "murk", "not", "regret", "sad", "shi", "sorr", "stop",
                   "tear", "stress", "suck", "trigger", "weep", "unhappy",
                   "welp", "wimp", "worry"]

# If using replit, store trigger_replies in built-in db feature
trigger_replies = [
    "Have a snickers",
    "When life gives you lemons, don't squeeze them directly in your eyes",
    "Keep going, I'm always here to lend a virtual pear",
    "How many times do I need to repeat this? Beep boop salad.",
    "Beep Boooooop...orange",
    "Beep Boop almonds",
    "Get well, or else I'll force feed you fermented tofu",
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

## If using replit
# def update_trigger_replies(trigger_reply):
#     if "trigger_replies" in db.keys():
#         trigger_replies = db["trigger_replies"]
#         trigger_replies.append(trigger_reply)
#         db["trigger_replies"] = trigger_replies
#     else:
#         db["trigger_replies"] = [trigger_reply]

# def delete_encouragment(index):
#     trigger_replies = db["trigger_replies"]
#     if len(trigger_replies) > index:
#         del trigger_replies[index]
#     db["trigger_replies"] = trigger_replies

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if re.search('[H|h](ello|ey|owdy)', msg) or re.search(' [H|h]i', msg):
        await message.channel.send('Hello :)')
    if msg.startswith(('Hi', 'hi')):
        await message.channel.send('Hello :)')
    elif re.search('\$inspire', msg):
        await message.channel.send(get_quote())
    elif any(word in msg.lower() for word in trigger_phrases):
        await message.channgel.send(random.choice(trigger_replies))

    # options = trigger_replies
    # if "trigger_replies" in db.keys():
    #     options = options + db["trigger_replies"]
    # if any(word in msg for word in trigger_phrases):
    #     await message.channel.send(random.choice(options))
    # if msg.startswith("$new"):
    #     trigger_message = msg.split("$new ",1)[1]
    #     update_trigger_replies(trigger_message)
    #     await message.channel.send("New encouraging message added.")
    # if msg.startswith("$del"):
    #     trigger_replies = []
    #     if "trigger_replies" in db.keys():
    #         index = int(msg.split("$del",1)[1])
    #         delete_encouragment(index)
    #         trigger_replies = db["trigger_replies"]
    #     await message.channel.send(trigger_replies)

client.run(os.getenv('TOKEN'))
