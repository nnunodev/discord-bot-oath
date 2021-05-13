import discord
import os
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
bot = discord.Client()

@bot.event
async def on_message(message):
    if message.content =="hello":
        await message.channel.send("hey")

bot.run(DISCORD_TOKEN)