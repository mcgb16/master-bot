import extras
import bot_methods

intents = bot_methods.discord.Intents.default()
intents.message_content = True
bot = bot_methods.commands.Bot(command_prefix='#', intents=intents)

@bot.command()
async def bot_help(ctx):
    pass

@bot.command(name='roll')
async def roll_dice(ctx, *, content: bot_methods.command_roll_dice):
    await ctx.send(await content)

@bot.command()
async def character_creation(ctx):
    pass

bot.run(extras.dsc_tkn)
