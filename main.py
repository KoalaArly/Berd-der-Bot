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
@bot.command(help="Verlinkt das Movement Wiki")
async def wiki(ctx):
    await ctx.send("Hier der Link zur Movement Wiki: \nhttps://apexmovement.tech/wiki")

# !superglide - link zum trainer und mokey video
@bot.command(help="Verlinkt nützliche Superglide Ressourcen")
async def superglide(ctx):
    await ctx.send("Hier der Link zum Superglide Trainer & Guide: \nTrainer - https://apexmovement.tech/superglidetrainer/ \nGuide - https://www.youtube.com/watch?v=_cP1YO5Idts")

# !mantlejump - link zum theeb video
@bot.command(help="Verlinkt nützliche Mantlejump Ressourcen")
async def mantlejump(ctx):
    await ctx.send("Hier der Link zum Mantlejump Guide: \nGuide - https://www.youtube.com/watch?v=69_lfGZz52Q")

# !lurch - link zum xzylas video
@bot.command(help="Verlinkt nützliche Lurch Ressourcen")
async def lurch(ctx):
    await ctx.send("Hier der Link zum Lurch Guide: \nGuide - https://www.youtube.com/watch?v=JonGQ6F_p6E")

# !wallzones - link zum eraiseddd video
@bot.command(help="Verlinkt nützliche Wallzone Ressourcen")
async def wallzones(ctx):
    await ctx.send("Hier der Link zum Wallzone Guide: \nGuide - https://www.youtube.com/watch?v=RWEO8mERoCE")

bot.run(token, log_handler=handler, log_level=logging.DEBUG)