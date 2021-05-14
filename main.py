import discord
from discord.ext import commands
import os
from discord.ext.commands.core import command
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!")

# add list of builds


@bot.command()
async def builds(link):
    await link.channel.send("List of builds from Lost Ark discord channel - https://tinyurl.com/tx6rauyn")

# add how to play guide


@bot.command()
async def howto(link):
    await link.channel.send("How to play Lost Ark - https://discord.com/channels/842026072773623838/842027776088604692/842341898956963861")


# @bot.event
# async def on_message(message):
#    if message.content == "!howto":
#        await message.channel.send("How to play Lost Ark - https://discord.com/channels/842026072773623838/842027776088604692/842341898956963861")

bot.run(DISCORD_TOKEN)
