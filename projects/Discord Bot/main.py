# build a simple discord bot

import discord
from discord.ext import commands  # importing commands module from discord extensions
import os
import random

token = "Your Token Here"

bot = discord.bot(comand_prefix="!")

# The list below is a list that contains all the responses the bot can randomly choose from for the "ask" command
# Scroll down to see the "ask" command's functionality

responses_list = [
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes, definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Reply hazy try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful",
]


@bot.event
async def on_ready():
    print("Bot is ready")


@bot.event
async def on_message(message: discord.Message):
    if message.author == bot.user:
        return

    if message.content.startswith("!hello"):
        await message.channel.send(f"Hello {message.author.mention}!")
        return

    if message.content.startswith("!random"):
        await message.channel.send(random.randint(1, 100))


# adding a "@bot.command" decorator which creates a command for the discord bot which can be then invoked by the user
# "aliases" parameter inside the "@bot.command" decorator makes it so that the user can use different names to call
# that particular command


@bot.command(aliases=["ASK", "Ask"])
async def ask(ctx: commands.Context, *, question: str):

    # Note:- If we don't put a ( * ) before the question paramter, the bot will only take the first word from the user
    # input. For example: Running the command like this:- "!ask how are you?"
    # The bot will read that command as:- "how"

    await ctx.reply(
        f"{ctx.author.mention} asks: **{question}**\nMy reply: **{random.choice(responses_list)}**"
    )


# There's one last thing to do now.. which is handling error. As we can see, the "ask" commands needs a question
# parameter.. but what if the user just uses the command and never provide the bot with the question parameter?
# This situation will throw an error called "MissingRequiredArgument". In order to avoid this, we can locally
# create a error handler for this "ask" command. You can also use a try and except block to catch the error.


@ask.error
async def ask_error(ctx: commands.Context, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply("You didn't provide me with a question!")


# the above error handler checks specifically for the error "MissingRequiredArgument". If the command encounters with
# this error, the bot will just reply to the user's message with the sentence pasted above in the error handler

bot.run(token)
