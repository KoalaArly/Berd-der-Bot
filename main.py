import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} is starting")

# !wiki - link zur apex movement wiki
@bot.command()
async def wiki(ctx):
    await ctx.send("Hier der Link zur Movement Wiki: \nhttps://apexmovement.tech/wiki")

# !superglide - link zum trainer und mokey video
@bot.command()
async def superglide(ctx):
    await ctx.send("Hier der Link zum Superglide Trainer & Guide: \nTrainer - https://apexmovement.tech/superglidetrainer/ \nGuide - https://www.youtube.com/watch?v=_cP1YO5Idts")

bot.run(token, log_handler=handler, log_level=logging.DEBUG)

