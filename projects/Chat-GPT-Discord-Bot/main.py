import discord
from discord import app_commands
import sys
import os
from dotenv import load_dotenv
from Chat_GPT_Function import gpt, dalle3, dalle2
import json
from datetime import datetime, timedelta
import time
import asyncio

load_dotenv(override=True)

with open("projects/Chat-GPT-Discord-Bot/GPT_Parameters.json") as f:
    data = json.load(f)  # Loads the gpt system prompts

char_limit = data["system_content"][0][
    "character_limit_prompt"
]  # Makes sure that the gpt output won't exceed the discord embed character limit of 4096 characters

try:
    token = os.getenv("BOT_TOKEN")  # returns a str
    owner_uid = int(os.getenv("OWNER_ID"))  # returns an int
    gpt_key = os.getenv("GPT_API_KEY")  # returns a str
    discord_server_1 = int(
        os.getenv("DISCORD_SERVER_1")
    )  # Discord Server ID 1 returns int
    discord_server_2 = int(
        os.getenv("DISCORD_SERVER_2")
    )  # Discord Server ID 2 returns int (this one is optional)
except (TypeError, ValueError):
    sys.exit(
        "Error: One or more environment variables are not set or contain invalid values."
    )  # Stops the bot from starting if the .env is formatted wrong

discord_server_1 = discord.Object(
    id=discord_server_1
)  # Discord Server ID 1 returns int
discord_server_2 = discord.Object(
    id=discord_server_2
)  # Discord Server ID 2 returns int (this one is optional)


class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        # A CommandTree is a special type that holds all the application command
        # state required to make it work. This is a separate class because it
        # allows all the extra states to be opt-in.
        # Whenever you want to work with application commands, your tree is used
        # to store and work with them.
        # Note: When using commands.Bot instead of discord.Client, the bot will
        # maintain its own tree instead.
        self.tree = app_commands.CommandTree(self)

    # In this, we just synchronize the app commands to specified guilds.
    # Instead of specifying a guild to every command, we copy over our global commands instead.
    # By doing so, we don't have to wait up to an hour until they are shown to the end-user.
    # This allows for faster bot testing and development.
    async def setup_hook(self):
        # This copies the global commands over to your guild(s).
        self.tree.clear_commands(
            guild=discord_server_1
        )  # Prevents command duplication.
        await self.tree.sync(guild=discord_server_1)
        self.tree.clear_commands(guild=discord_server_2)
        await self.tree.sync(guild=discord_server_2)  # Prevents command duplication.
        # You can replace these 4 lines with "await self.tree.sync()" if you want the bots commands to...
        # be added to all servers its in (won't take long if your bot isn't in many servers otherwise it could take up to an hour)


intents = discord.Intents.default()
client = MyClient(intents=intents)


@client.event
async def on_ready():
    print(
        f"--------------------------------------------- \nLogged in as {client.user} (ID: {client.user.id}) \n---------------------------------------------"
    )
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, name="For Slash Commands"
        )
    )  # This changes the activity that is displayed under the bots name in the members list.

    # dm_user = await client.fetch_user(
    #     owner_uid
    # )
    # await dm_user.send("Bot Online!")
    # Uncomment this if you want the bot to dm you when it turns on


# -------------------------- HELP COMMAND ----------------------------------
@client.tree.command(name="help", description="Lists all commands")
async def send(interaction: discord.Interaction):
    try:
        await interaction.response.defer(
            ephemeral=False
        )  # Defer the response to prevent command timeout
        embed = discord.Embed(
            title="Command List",
            description="-----------------------------------------",
            color=0x002AFF,
        )
        embed.set_author(
            name="GPT Bot",
            url="https://www.alby08.com",
            icon_url=client.user.avatar.url,
        )
        for slash_command in client.tree.walk_commands():
            embed.add_field(
                name=slash_command.name,
                value=(
                    f"- {slash_command.description}\n-----------------------------------------"
                    if slash_command.description
                    else slash_command.name
                ),
                inline=False,
            )
        # Send as followup message
        await interaction.followup.send(embed=embed)
    except Exception as e:
        # Handle exceptions
        print(f"An error occurred: {str(e)}")
        await interaction.followup.send(
            "An error occurred while processing the command."
        )


# -------------------------- TEST COMMAND ----------------------------------
@client.tree.command(name="test_bot", description="Replies with 'Hello!'")
async def running_test(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"Hello, {interaction.user.mention}", ephemeral=True
    )  # ephemeral=True means the bots response is only visible
    # to the user who used the command.


# -------------------------- SHUTDOWN ----------------------------------
@client.tree.command(
    name="shutdown", description="Shuts down the bot if you are the bot owner"
)  # Shuts down the bot if the user matches the owner_uid
async def shutdown_bot(interaction: discord.Interaction):
    if interaction.user.id == owner_uid:
        await interaction.response.send_message("Shutting down the bot...")
        await client.close()
    else:
        await interaction.response.send_message(
            "You don't have permission to shut down the bot.", ephemeral=True
        )


# -------------------------- DELETE MESSAGES ----------------------------------
@client.tree.command(
    name="clear",
    description="Deletes defined number of messages from the current channel.",
)
@app_commands.rename(to_delete="messages")
@app_commands.describe(to_delete="Number of messages to delete")
async def send(interaction: discord.Interaction, to_delete: int):  # noqa: F811
    await interaction.response.defer(ephemeral=True)
    if not interaction.user.guild_permissions.manage_messages:
        await interaction.followup.send("Invalid permissions")
        return
    if to_delete <= 0:
        await interaction.followup.send("Invalid number")
        return
    else:
        await interaction.followup.send("Deleting...")
        await interaction.channel.purge(limit=to_delete)
        await interaction.edit_original_response(
            content=f"Deleted {to_delete} messages."
        )


# -------------------------- BOT LATENCY ----------------------------------
@client.tree.command(name="ping", description="Get bot latency")
async def ping(interaction: discord.Interaction):
    try:
        await interaction.response.defer(
            ephemeral=True
        )  # Defer the response to prevent command timeout

        # Get bot latency
        latency = round(client.latency * 1000)

        # Send as followup message
        await interaction.followup.send(f"Pong! Latency: {latency}ms")
    except Exception as e:
        # Handle exceptions
        print(f"An error occurred: {str(e)}")
        await interaction.followup.send(
            "An error occurred while processing the command."
        )


# -------------------------- CORRECT GRAMMAR ----------------------------------
@client.tree.command(
    name="gpt_correct_grammar", description="Corrects grammar of inputted text"
)
@app_commands.rename(text="text_to_correct")
@app_commands.describe(text="Text to grammar correct")
async def send(interaction: discord.Interaction, text: str):  # noqa: F811
    try:
        await interaction.response.defer(
            ephemeral=False
        )  # Defer the response to prevent command timeout

        # It is best to use discord embeds for gpt commands as discord embed descriptions allow for 4096 characters instead of 2000 characters for normal messages
        embed = discord.Embed(
            title="Correct Grammar",
            description=gpt(
                "gpt-3.5-turbo-16k",
                text,
                data["system_content"][0]["correct_grammar"] + char_limit,
                0,
            ),
            color=0x002AFF,
        )
        embed.set_author(
            name="GPT Bot",
            url="https://www.alby08.com",
            icon_url=client.user.avatar.url,
        )

        # Send as followup message
        await interaction.followup.send(embed=embed)
    except Exception as e:
        # Handle exceptions
        print(f"An error occurred: {str(e)}")
        await interaction.followup.send(
            "An error occurred while processing the command."
        )


# -------------------------- WEBSITE ----------------------------------
@client.tree.command(
    name="gpt_single_page_website",
    description="Creates a single paged website with embedded Javascript and CSS",
)
@app_commands.rename(text="website_prompt")
@app_commands.describe(text="Website page specifications")
async def send(interaction: discord.Interaction, text: str):  # noqa: F811
    try:
        await interaction.response.defer(
            ephemeral=False
        )  # Defer the response to prevent command timeout

        # It is best to use discord embeds for gpt commands as discord embed descriptions allow for 4096 characters instead of 2000 characters for normal messages
        embed = discord.Embed(
            title="Single Page Website",
            description=gpt(
                "gpt-3.5-turbo-16k",
                text,
                data["system_content"][0]["single_page_website"] + char_limit,
                0.7,
            ),
            color=0x002AFF,
        )
        embed.set_author(
            name="GPT Bot",
            url="https://www.alby08.com",
            icon_url=client.user.avatar.url,
        )

        # Send as followup message
        await interaction.followup.send(embed=embed)
    except Exception as e:
        # Handle exceptions
        print(f"An error occurred: {str(e)}")
        await interaction.followup.send(
            "An error occurred while processing the command."
        )


# -------------------------- TEXT TO EMOJI ----------------------------------
@client.tree.command(name="gpt_text_to_emoji", description="Converts text to emojis")
@app_commands.rename(text="text")
@app_commands.describe(text="Text to convert to emojis")
async def send(interaction: discord.Interaction, text: str):  # noqa: F811
    try:
        await interaction.response.defer(
            ephemeral=False
        )  # Defer the response to prevent command timeout

        if len(text) > 230:
            await interaction.followup.send(
                "GPT prompt is too long please try again (max prompt length is 230 characters)"
            )
            return
        else:
            gpt_prompt = text

        # It is best to use discord embeds for gpt commands as discord embed descriptions allow for 4096 characters instead of 2000 characters for normal messages
        embed = discord.Embed(
            title=f'Text to Emoji - "{text}"',
            description=gpt(
                "gpt-3.5-turbo-16k",
                gpt_prompt,
                data["system_content"][0]["text_to_emoji"] + char_limit,
                0.7,
            ),
            color=0x002AFF,
        )
        embed.set_author(
            name="GPT Bot",
            url="https://www.alby08.com",
            icon_url=client.user.avatar.url,
        )

        # Send as followup message
        await interaction.followup.send(embed=embed)
    except Exception as e:
        # Handle exceptions
        print(f"An error occurred: {str(e)}")
        await interaction.followup.send(
            "An error occurred while processing the command."
        )


# -------------------------- TEXT TO BLOCK LETTERS ----------------------------------
@client.tree.command(
    name="gpt_text_to_block_letters", description="Converts text into block letters"
)
@app_commands.rename(text="text")
@app_commands.describe(text="Text to convert into block letters")
async def send(interaction: discord.Interaction, text: str):  # noqa: F811
    try:
        await interaction.response.defer(
            ephemeral=False
        )  # Defer the response to prevent command timeout

        # It is best to use discord embeds for gpt commands as discord embed descriptions allow for 4096 characters instead of 2000 characters for normal messages
        embed = discord.Embed(
            title="Text to block letter emojis",
            description=gpt(
                "gpt-3.5-turbo-16k",
                text,
                data["system_content"][0]["text_to_block_letters"] + char_limit,
                0.7,
            ),
            color=0x002AFF,
        )
        embed.set_author(
            name="GPT Bot",
            url="https://www.alby08.com",
            icon_url=client.user.avatar.url,
        )

        # Send as followup message
        await interaction.followup.send(embed=embed)
    except Exception as e:
        # Handle exceptions
        print(f"An error occurred: {str(e)}")
        await interaction.followup.send(
            "An error occurred while processing the command."
        )


# -------------------------- CODE DEBUG ----------------------------------
@client.tree.command(name="gpt_debug_code", description="Debugs your code")
@app_commands.rename(text="code")
@app_commands.describe(text="Code to debug")
async def send(interaction: discord.Interaction, text: str):  # noqa: F811
    try:
        await interaction.response.defer(
            ephemeral=False
        )  # Defer the response to prevent command timeout

        # It is best to use discord embeds for gpt commands as discord embed descriptions allow for 4096 characters instead of 2000 characters for normal messages
        embed = discord.Embed(
            title="Code Debug",
            description=gpt(
                "gpt-4",
                text,
                data["system_content"][0]["code_debug"] + char_limit,
                0,
            ),
            color=0x002AFF,
        )
        embed.set_author(
            name="GPT Bot",
            url="https://www.alby08.com",
            icon_url=client.user.avatar.url,
        )

        # Send as followup message
        await interaction.followup.send(embed=embed)
    except Exception as e:
        # Handle exceptions
        print(f"An error occurred: {str(e)}")
        await interaction.followup.send(
            "An error occurred while processing the command."
        )


# -------------------------- SHORT STORY ----------------------------------
@client.tree.command(
    name="gpt_short_story", description="Writes a short story about a topic"
)
@app_commands.rename(text="story_prompt")
@app_commands.describe(text="What do you want the story to be about?")
async def send(interaction: discord.Interaction, text: str):  # noqa: F811
    try:
        await interaction.response.defer(
            ephemeral=False
        )  # Defer the response to prevent command timeout

        # It is best to use discord embeds for gpt commands as discord embed descriptions allow for 4096 characters instead of 2000 characters for normal messages
        embed = discord.Embed(
            title="Short Story",
            description=gpt(
                "gpt-4",
                text,
                data["system_content"][0]["short_story"],
                0.7,
            ),
            color=0x002AFF,
        )
        embed.set_author(
            name="GPT Bot",
            url="https://www.alby08.com",
            icon_url=client.user.avatar.url,
        )

        # Send as followup message
        await interaction.followup.send(embed=embed)
    except Exception as e:
        # Handle exceptions
        print(f"An error occurred: {str(e)}")
        await interaction.followup.send(
            "An error occurred while processing the command."
        )


# -------------------------- GENERAL QUESTION ----------------------------------
@client.tree.command(name="gpt_general_question", description="For all your questions")
@app_commands.rename(text="prompt")
@app_commands.describe(text="What do you want to ask chatGPT?")
@app_commands.describe(
    gpt_model="Possible options = gpt-4 or gpt-3.5 (gpt-3.5-turbo-16k abbreviated)"
)
async def send(
    interaction: discord.Interaction,
    text: str,
    gpt_model: str,
):  # noqa: F811
    try:
        await interaction.response.defer(
            ephemeral=False
        )  # Defer the response to prevent command timeout

        if len(text) > 230:
            await interaction.followup.send(
                "GPT prompt is too long please try again (max prompt length is 230 characters)"
            )
            return
        else:
            gpt_prompt = text

        if gpt_model.lower() not in ("gpt-4", "gpt-3.5"):
            await interaction.followup.send(
                "Invalid GPT model. Must be either gpt-4 or gpt-3.5."
            )
            return
        else:
            if gpt_model.lower() == "gpt-3.5":
                gpt_model = "gpt-3.5-turbo-16k"
            else:
                gpt_model = gpt_model.lower()

        # It is best to use discord embeds for gpt commands as discord embed descriptions allow for 4096 characters instead of 2000 characters for normal messages
        embed = discord.Embed(
            title=f'General Question - "{text}"',
            description=gpt(
                gpt_model,
                gpt_prompt,
                data["system_content"][0]["general_questions"],
                0.7,
            ),
            color=0x002AFF,
        )
        embed.set_author(
            name="GPT Bot",
            url="https://www.alby08.com",
            icon_url=client.user.avatar.url,
        )

        # Send as followup message
        await interaction.followup.send(embed=embed)
    except Exception as e:
        # Handle exceptions
        print(f"An error occurred: {str(e)}")
        await interaction.followup.send(
            "An error occurred while processing the command."
        )


# -------------------------- DALLE 3 ----------------------------------
@client.tree.command(name="dalle_3", description="Generates an image with DALL·E 3")
@app_commands.describe(prompt="Describe the image you want DALL·E 3 to create")
@app_commands.describe(
    img_dimensions="Must be either 1024x1024, 1792x1024, or 1024x1792 for dall-e-3"
)
@app_commands.describe(
    img_quality="Must be either hd or standard. HD = images with finer details and greater consistency across the image."
)
@app_commands.describe(
    img_style="Must be either vivid or natural. Vivid = hyper-real and dramatic images. Natural = more natural, less hyper-real looking images."
)
async def send(
    interaction: discord.Interaction,
    prompt: str,
    img_dimensions: str,
    img_quality: str,
    img_style: str,
):  # noqa: F811
    try:
        await interaction.response.defer(
            ephemeral=False
        )  # Defer the response to prevent command timeout

        # Get the current time
        current_time = datetime.now()

        # Add 1 hour to the current time
        future_time = current_time + timedelta(hours=1)

        if img_dimensions.lower() not in ("1024x1024", "1792x1024", "1024x1792"):
            await interaction.followup.send(
                "Invalid image dimension. Must be either 1024x1024, 1792x1024, or 1024x1792."
            )
            return
        else:
            img_dimensions = img_dimensions.lower()

        if img_quality.lower() not in ("hd", "standard"):
            await interaction.followup.send(
                "Invalid image quality. Must be either hd or standard."
            )
            return
        else:
            img_quality = img_quality.lower()

        if img_style.lower() not in ("vivid", "natural"):
            await interaction.followup.send(
                "Invalid image style. Must be either vivid or natural."
            )
            return
        else:
            img_style = img_style.lower()

        loop = (
            asyncio.get_event_loop()
        )  # Prevents heartbeat block warning and bot disconnecting from discord error
        image_url = await loop.run_in_executor(
            None, dalle3, prompt, img_quality, img_dimensions, img_style
        )  # Prevents heartbeat block warning and bot disconnecting from discord error

        # Send as followup message
        await interaction.followup.send(
            f"{image_url} IMAGE LINK EXPIRES IN <t:{int(time.mktime(future_time.timetuple()))}:R>"
        )
    except Exception as e:
        # Handle exceptions
        print(f"An error occurred: {str(e)}")
        await interaction.followup.send(
            "An error occurred while processing the command."
        )


# -------------------------- DALLE 2 ----------------------------------
@client.tree.command(name="dalle_2", description="Generates an image with DALL·E 2")
@app_commands.describe(prompt="Describe the image you want DALL·E 2 to create")
@app_commands.describe(
    img_dimensions="Must be either 256x256, 512x512, or 1024x1024 for dall-e-2"
)
async def send(
    interaction: discord.Interaction, prompt: str, img_dimensions: str
):  # noqa: F811
    try:
        await interaction.response.defer(
            ephemeral=False
        )  # Defer the response to prevent command timeout

        # Get the current time
        current_time = datetime.now()

        # Add 1 hour to the current time
        future_time = current_time + timedelta(hours=1)

        if img_dimensions.lower() not in ("256x256", "512x512", "1024x1024"):
            await interaction.followup.send(
                "Invalid image dimension. Must be either 256x256, 512x512, or 1024x1024."
            )
            return
        else:
            img_dimensions = img_dimensions.lower()

        loop = (
            asyncio.get_event_loop()
        )  # Prevents heartbeat block warning and bot disconnecting from discord error
        image_url = await loop.run_in_executor(
            None, dalle2, prompt, img_dimensions
        )  # Prevents heartbeat block warning and bot disconnecting from discord error

        # Send as followup message
        await interaction.followup.send(
            f"{image_url} IMAGE LINK EXPIRES IN <t:{int(time.mktime(future_time.timetuple()))}:R>"
        )  # Convert future_time to unix timestamp.
    except Exception as e:
        # Handle exceptions
        print(f"An error occurred: {str(e)}")
        await interaction.followup.send(
            "An error occurred while processing the command."
        )


client.run(token)
