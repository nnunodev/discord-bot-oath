import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot = discord.Client()


@bot.event
async def on_message(message):
    if message.content == "!builds":
        await message.channel.send("List of builds from Lost Ark discord channel - https://tinyurl.com/tx6rauyn")

bot.run(DISCORD_TOKEN)
