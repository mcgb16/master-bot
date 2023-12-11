import extras
import bot_methods

intents = bot_methods.discord.Intents.default()
intents.message_content = True
bot = bot_methods.commands.Bot(command_prefix='#', intents=intents)

@bot.command(name='roll')
async def roll_dice(ctx, *, content: bot_methods.command_roll_dice):
    await ctx.send(await content)

# Não finalizado (devido as funções de criação)
@bot.command(name='help')
async def bot_help(ctx,*, content: bot_methods.command_help = None):
    if ctx.author.bot:
        return 

    error_message = f'Não foi possível enviar mensagem privada para {ctx.author}. Talvez as mensagens privadas estejam desativadas ou eu não tenho permissão para fazer isso.'
    
    success_message = 'Te mandei um zap, rs.'

    if content == None:
        return

    try:
        await ctx.author.send(await content)
        if not isinstance(ctx.channel, bot_methods.discord.DMChannel):
            await ctx.send(success_message)
    except bot_methods.discord.Forbidden as e:
        await ctx.send(error_message)

bot.run(extras.dsc_tkn)
