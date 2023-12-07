import discord
import extras
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='#', intents=intents)

@bot.command(name='h')
async def bot_help(ctx):
    help_message = """

    """
    await ctx.send(help_message)

@bot.command(name='roll')
async def roll_dice(ctx, arg):
    if arg == 'd20':
        await ctx.send(random.randint(1,20))

bot.run(extras.dsc_tkn)
