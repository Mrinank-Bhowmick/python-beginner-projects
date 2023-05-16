# build a simple discord bot

import discord
import os
import random

token = "Your Token Here"

bot = discord.bot(comand_prefix="!")


@bot.event
async def on_ready():
    print("Bot is ready")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith("!hello"):
        await message.channel.send("Hello!")

    if message.content.startswith("!random"):
        await message.channel.send(random.randint(1, 100))


bot.run(token)
