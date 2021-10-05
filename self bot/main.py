from discord.ext import commands
import asyncio
import os

bot = commands.Bot("!", self_bot=True)

karsten = os.environ["users"].split(",")

print(karsten)

print("Ost")

@bot.event
async def on_ready():
    print("Bot on")

@bot.event
async def on_message(message):
    if str(message.author.id) in karsten and str(message.channel.type) == 'private':
        print("Sent message")
        await message.channel.send(os.environ["text"])

bot.run(os.environ["token"], bot=False)