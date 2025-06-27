import discord
from discord.ext import commands
import os

TOKEN = os.getenv("DISCORD_TOKEN")  # This pulls the token from Railway

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send("Hey! I'm online and working.")
    
bot.run(TOKEN)
