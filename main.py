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

    # bernd terminal start message
    print(f"{bot.user.name} is starting")

    # custom status
    await bot.change_presence(
        activity=discord.Game(name="!help - lists all features")
    )

    # bermd restart message
    channel = bot.get_channel(1428566367350554764)
    if channel:
        await channel.send("Bin wieder da, mein Akh.")

# added custom rolle bei neuem user join
@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name="Movement Atze")

    if role:
        await member.add_roles(role)
        
# honey-pot auto ban und new member join emoji reaction
@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        return

    # Honeypot-Check
    if msg.channel.id == 1522030924403839237:
        try:
            await msg.author.ban(reason="honey-pot", delete_message_seconds=86400)
            print(f"{msg.author} wurde gebannt (honey-pot).")
        except discord.Forbidden:
            print(f"{msg.author} konnte nicht gebannt werden (honey-pot).")
        try:
            await msg.delete()
        except discord.NotFound:
            pass
        return

    # emoji bei neuem user join
    if msg.type == discord.MessageType.new_member:
        emoji = discord.utils.get(msg.guild.emojis, name="pepeFlower")
        if emoji:
            await msg.add_reaction(emoji)

    await bot.process_commands(msg)
            
# !help - liste aller funktionen
@bot.command()
async def help(ctx):
    await ctx.send("```ansi\n"
        "\u001b[1;35mBernd's Features\u001b[0m\n"
        "\u001b[37m────────────────────────────────\u001b[0m\n"
        "Bernd Basics:\n"
        "\u001b[33m!help        \u001b[0m– shows this overview\n"
        "\n"
        "Movement Resources:\n"
        "\u001b[33m!bhop        \u001b[0m– lists the bugged fps ranges for Bhops\n"
        "\u001b[33m!climbspace  \u001b[0m– sends the 'Climb Space' graphic\n"
        "\u001b[33m!lurch       \u001b[0m– links useful lurch resources\n"
        "\u001b[33m!mantlejump  \u001b[0m– links good Mantlejump guide\n"
        "\u001b[33m!superglide  \u001b[0m– links useful Superglide resources\n"
        "\u001b[33m!ubounce     \u001b[0m– links good 'Climb Zone' video\n"
        "\u001b[33m!wiki        \u001b[0m– links the movement wiki\n"
        "\n"
        "Apex Stuff:\n"
        "\u001b[33m!launch      \u001b[0m– lists useful launch options\n"
        "\u001b[37m────────────────────────────────\u001b[0m\n"
        "```"
)

# !wiki - link zur apex movement wiki
@bot.command()
async def wiki(ctx):
    await ctx.send("link to the movement wiki: \nhttps://apexmovement.tech/wiki")

# !superglide - link zum trainer und mokey video
@bot.command()
async def superglide(ctx):
    await ctx.send("link to the superglide trainer & guide: \ntrainer - https://apexmovement.tech/superglidetrainer/ \nguide - https://www.youtube.com/watch?v=_cP1YO5Idts")

# !mantlejump - link zum theeb video
@bot.command()
async def mantlejump(ctx):
    await ctx.send("link to the mantlejump guide: \nhttps://www.youtube.com/watch?v=69_lfGZz52Q")

# !lurch - link zum xzylas video
@bot.command()
async def lurch(ctx):
    await ctx.send("link good lurch resources: \nguide - https://www.youtube.com/watch?v=JonGQ6F_p6E\n"
                   "lurch trainer made by LiTTle - https://lurch-trainer.web.app/trainer")

# !ubounce - link zum eraiseddd video
@bot.command()
async def ubounce(ctx):
    await ctx.send("link to a good guide: \nhttps://www.youtube.com/watch?v=RWEO8mERoCE")

# !bhop - angabe der bugged fps-bereiche
@bot.command()
async def bhop(ctx):
    await ctx.send("```ansi\n"
    "Diese \u001b[35mFPS-Bereiche\u001b[0m sind bugged:\n"
    "These \u001b[35mfps ranges\u001b[0m are bugged:\n"
    "\u001b[37m───────────────────────────────\u001b[0m\n"
    "\u001b[35m 67 - 79 \u001b[0m\n"
    "\u001b[35m141 - 155 \u001b[0m\n"
    "\u001b[35m207 - 230 \u001b[0m\n"
    "\u001b[35m275 - 300 \u001b[0m\n"
    "\u001b[37m───────────────────────────────\u001b[0m\n"
    "```")

# !launch - liste von launch optionen
@bot.command()
async def launch(ctx):
    await ctx.send("```ansi\n"
    "Nützliche \u001b[35mLaunch Optionen\u001b[0m:\n"
    "useful \u001b[35mlaunch options\u001b[0m:\n"
    "\u001b[37m──────────────────────────\u001b[0m\n"
    "\u001b[35mcl_showpos  1 \u001b[0m       - shows useful ingame stats (like Velocity)\n"
    "\u001b[35mcl_showfps  4 \u001b[0m       - shows your fps and more\n"
    "\u001b[35mcl_fovscale 1.7 \u001b[0m     - sets fov to 120\n"
    "\u001b[37m──────────────────────────\u001b[0m\n"
    "```")

# !climbspace - sendet climbspace png
@bot.command()
async def climbspace(ctx):
    file_path = os.path.join(
        os.path.dirname(__file__),
        "graphics",
        "graphic_climb_space_with_zones_light.png"
    )
    await ctx.send(file=discord.File(file_path))

#------------------------------ADMIN---------------------------------#
# !clear - cleart n + 1 der letzten nachrichten
@bot.command()
@commands.has_role("Guides")
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)

bot.run(token, log_handler=handler, log_level=logging.DEBUG)