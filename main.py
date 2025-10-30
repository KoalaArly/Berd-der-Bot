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

bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f"{bot.user.name} is starting")

# !help - liste aller funktionen
@bot.command()
async def help(ctx):
    await ctx.send("```ansi\n"
        "\u001b[1;35mBernd's Funktionen\u001b[0m\n"
        "\u001b[37m───────────────────────────────\u001b[0m\n"
        "Bernd Basics:\n"
        "\u001b[33m!help        \u001b[0m– Zeigt diese Liste an\n"
        "\n"
        "Movement Ressourcen:\n"
        "\u001b[33m!bhop        \u001b[0m– Listet bugged FPS-Bereiche für Bhop auf\n"
        "\u001b[33m!lurch       \u001b[0m– Verlinkt guten Lurch Guide\n"
        "\u001b[33m!mantlejump  \u001b[0m– Verlinkt guten Mantlejump Guide\n"
        "\u001b[33m!superglide  \u001b[0m– Verlinkt nützliche Superglide-Ressourcen\n"
        "\u001b[33m!wallzones   \u001b[0m– Verlinkt gutes Wallzone Video\n"
        "\u001b[33m!wiki        \u001b[0m– Verlinkt das Movement-Wiki\n"
        "\u001b[37m───────────────────────────────\u001b[0m\n"
        "```"
)

# !wiki - link zur apex movement wiki
@bot.command()
async def wiki(ctx):
    await ctx.send("Hier der Link zur Movement Wiki: \nhttps://apexmovement.tech/wiki")

# !superglide - link zum trainer und mokey video
@bot.command()
async def superglide(ctx):
    await ctx.send("Hier der Link zum Superglide Trainer & Guide: \nTrainer - https://apexmovement.tech/superglidetrainer/ \nGuide - https://www.youtube.com/watch?v=_cP1YO5Idts")

# !mantlejump - link zum theeb video
@bot.command()
async def mantlejump(ctx):
    await ctx.send("Hier der Link zum Mantlejump Guide: \nGuide - https://www.youtube.com/watch?v=69_lfGZz52Q")

# !lurch - link zum xzylas video
@bot.command()
async def lurch(ctx):
    await ctx.send("Hier der Link zum Lurch Guide: \nGuide - https://www.youtube.com/watch?v=JonGQ6F_p6E")

# !wallzones - link zum eraiseddd video
@bot.command()
async def wallzones(ctx):
    await ctx.send("Hier der Link zum Wallzone Guide: \nGuide - https://www.youtube.com/watch?v=RWEO8mERoCE")

# !bhop - angabe der bugged fps-bereiche
@bot.command()
async def bhop(ctx):
    await ctx.send("```ansi\n"
    "Diese \u001b[35mFPS-Bereiche\u001b[0m sind bugged:\n"
    "\u001b[33m67 - 79 \u001b[0m\n"
    "\u001b[33m141 - 155 \u001b[0m\n"
    "\u001b[33m207 - 230 \u001b[0m\n"
    "\u001b[33m275 - 300 \u001b[0m\n"
    "```")

bot.run(token, log_handler=handler, log_level=logging.DEBUG)