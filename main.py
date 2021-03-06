import discord
import os
import re
import requests
import json
import random
from replit import db
from keep_online import keep_online

client = discord.Client()

trigger_phrases = ["agon", "angry", "bad", "beat", "bleak", "cry", "depress",
                   "diss", "down", "freak", "furious", "fury", "fustrat",
                   "hate", "help", "less", "loser", "mean", "miser", "miss"
                   "murk", "never", "regret", "sad", "shi", "sorr", "stop",
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
    "Milk or cereal first in the bowl?",
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

random_words = ["embarrass", "permanent", "contract", "market", "telephone",
                "consciousness", "fantasy", "stake", "help", "obligation",
                "mean", "offend", "valid", "remix", "nuclear", "resource",
                "buy", "deputy", "trance", "paralyzed", "employee", "crop",
                "band", "castle", "hypothesis", "candle", "site", "situation",
                "wilderness", "dump", "gene", "appointment", "crown", "please",
                "cinema", "climate", "continental", "resort", "wealth", "rank",
                "fixture", "deter", "ambiguous", "frog", "partner", "slipper",
                "pedestrian", "theme", "gravity", "obstacle", "appoint",
                "explain", "other", "round", "opposed", "egg", "character",
                "teacher", "stage", "health", "omission", "impound", "eaux",
                "authorise", "bag", "dependence" "welcome", "picture", "cow",
                "approach", "definite", "instruction", "celebration", "spend",
                "discuss", "fleet", "mine", "copper", "blackmail", "invisible",
                "proportion", "double", "victory", "increase", "behave",
                "safe", "reason", "acid", "drill", "joy", "element", "praise",
                "demonstrate", "hook", "cunning", "roof", "ground", "stitch",
                "president", "elaborate", "chef", "botaroni"]

random_replies = [
    "With a serving of vegan chicken balls.",
    "Delicious...imitation meat...",
    "Beep boop where can I buy almond ice cream :icecream:?",
    "I'm craving fake bacon and ham.",
    "I like grilling my BBQ until everything is burnt.",
    "Sometimes I sit under a tree to eat my super processed vegan stuff.",
    "Why enjoy a boiled hot dog when you can enjoy a boiled sausage?",
    "What's hidden behind the door? A single bowl of ramen :ramen:.",
    "I like onigiri :rice_ball: with cheese on top more than anyone else.",
    "The second I saw the sun today, I thought soft boiled egg.",
    "Traveling became almost extinct. I was eating alone at Ichiran Ramen's.",
    "What's underneath your seat? A potato wedge.",
    "Yesterday's weather was chilly, so I made hot fish soup.",
    "These lyrics remind me of the watercress sandwich I made today.",
    "I made baked potato soup.",
    "The green tea :seedling: and avocado :avocado: shake turned out great.",
    "Ever had oysters rockefeller :oyster:? Me netiher.",
    "This flan :flan: is frozen.",
    "Potato wedges are best for repairing relationships.",
    "With maple bacon doughnuts? :doughnut:",
    "I found a persimmon.",
    "I like my pomelo `BONELESS`.",
    "It ain't right without ph??? :triumph:.",
    "Pineapple and ravioli?",
    "Psst...arugula and yuzu wasabi dressing.",
    "I make mango lassi `BONELESS`.",
    "People who wander find bubble tea :bubble_tea:.",
    "Lamb chops and corn chowder!",
    "Enjoy a banh mi.",
    "Help yourself to crab rangoon.",
    "Enjoy a scalding hot cup of ume plum tea :tea:.",
    "How about a cup of lychee tea with brown sugar and ginger?",
    "Pickled bean curd in the house!...What is a house again?",
    "Beep boop congee.",
    "Beep boopp spicy bean sprouts.",
    "Everything I manifested: salad with argula, baby greens, "
    + "steamed corn, avocado, edible flowers, and salmon fish skin.",
    "Why not some biryani?",
    "I added steamed salmon with fresh caponata.",
    "My energy balls are healthy and tasty.",
    "Slap some bean curd on it.",
    "Gogi berries would be nice."
    ]

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote

## If using replit's db:
def update_trigs(trig_reply):
    if "trigs" in db.keys():
        trigs = db["trigs"]
        trigs.append(trig_reply)
        db["trigs"] = trigs
    else:
        db["trigs"] = [trig_reply]

def delete_trigs(index):
    trigs = db["trigs"]
    if len(trigs) > index:
        del trigs[index]
    db["trigs"] = trigs

if "chef_botaroni_responding" not in db.keys():
    db["chef_botaroni_responding"] = True

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()

    if re.match('\s*h(ello|ey|owdy)', msg):
        await message.channel.send('Hello! :)')
    elif re.search('h(ello|ey|owdy)', msg):
        # Check that there is no alpha char before the re result
        greetings_set = {'hello', 'hey', 'howdy'}
        greetings = [msg.index(item) for item in greetings_set if item in msg]
        for i in greetings:
            if re.match('[^A-Za-z]|[ Hh]', msg[i - 1]):
                await message.channel.send('Hello there. :)')
                break
    elif re.match("[ h]i", msg):
        await message.channel.send('Hi :)')

    if re.search('\$inspire', msg):
        await message.channel.send(get_quote())

    if any(word in msg for word in random_words):
        if not msg.startswith('$'):
            await message.channel.send(random.choice(random_replies))
    # elif any(word in msg for word in trigger_phrases):
    #     if not msg.startswith('$'):
    #         await message.channel.send(random.choice(trigger_replies))

    # # If using replit's db, uncomment the code below:
    if db["chef_botaroni_responding"]:
        options = trigger_replies
        if "trigs" in db.keys():
            options.extend(db["trigs"])

        # Comment out this exact line from above if using replit db
        if any(word in msg for word in trigger_phrases):
            if not msg.startswith('$'):
                await message.channel.send(random.choice(options))

    if msg.startswith("$chef_botaroni_new"):
        trigger_message = msg.split("$chef_botaroni_new ",1)[1]
        update_trigs(trigger_message)
        await message.channel.send("New trigger message added.")

    if msg.startswith("$chef_botaroni_del"):
        trigs = []
        if "trigs" in db.keys():
            index = int(msg.split("$chef_botaroni_del",1)[1])
            delete_trigs(index)
            trigs = db["trigs"]
        await message.channel.send(trigs)

    if msg.startswith("$chef_botaroni_list"):
        trigs = []
        if "trigs" in db.keys():
            trigs = db["trigs"]
        await message.channel.send(trigs)
    
    if msg.startswith("$chef_botaroni_responding"):
        value = msg.split("$chef_botaroni_responding ", 1)[1]

        if value == "true":
            db["chef_botaroni_responding"] = True
            await message.channel.send("Chef Botaroni's responding is on.")
        else:
            db["chef_botaroni_responding"] = False
            await message.channel.send("Chef Botaroni's responding is off.")

keep_online()
client.run(os.getenv('TOKEN'))
