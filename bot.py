import discord
from discord.ext import commands
from bot_mantik import gen_pass
# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')


@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.command()
async def pasw(ctx):
    await ctx.send(gen_pass(10))

bot.run("MTM3NjI1NTg5MzIwMDcwMzUzOA.GQjdqm.Vg24PbZ5KqWgjH69t00G_k3yTmdJ6cfhtjScPQ")