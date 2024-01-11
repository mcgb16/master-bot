import extras
import bot_methods

intents = bot_methods.discord.Intents.default()
intents.message_content = True
bot = bot_methods.commands.Bot(command_prefix='?', intents=intents)

# Comando Dado

@bot.command(name='roll')
async def roll_dice(ctx, *, content: bot_methods.command_roll_dice = None):
    if bot_methods.help_methods.verify_bot_message(ctx) == None:
        return
    elif bot_methods.help_methods.verify_none(content) == None:
        return
    
    await ctx.send(embed=content)

# Comando Help

@bot.command(name='h')
async def bot_help(ctx,*, content: bot_methods.command_help = None):
    if bot_methods.help_methods.verify_bot_message(ctx) == None:
        return

    if content == None:
        content = bot_methods.command_help(None)

    error_message = f'Não foi possível enviar mensagem privada para {ctx.author}. Talvez as mensagens privadas estejam desativadas ou eu não tenho permissão para fazer isso.'   
    success_message = 'Te enviei uma DM!'

    try:
        await ctx.author.send(await content)
        if not isinstance(ctx.channel, bot_methods.discord.DMChannel):
            await ctx.send(success_message)
    except bot_methods.discord.Forbidden as e:
        print(e)
        await ctx.send(error_message)

# Comandos Player

@bot.command(name='cplayer')
async def create_player(ctx, *, content: bot_methods.command_create_player = None):
    if bot_methods.help_methods.verify_bot_message(ctx) == None:
        return
    elif bot_methods.help_methods.verify_none(content) == None:
        return
    
    await ctx.send(await content)

@bot.command(name='splayer')
async def search_player(ctx, *, content: bot_methods.command_search_player = None):
    if bot_methods.help_methods.verify_bot_message(ctx) == None:
        return
    elif bot_methods.help_methods.verify_none(content) == None:
        return
    
    await ctx.send(embed=content)

@bot.command(name='uplayer')
async def update_player(ctx, *, content: bot_methods.command_update_player = None):
    if bot_methods.help_methods.verify_bot_message(ctx) == None:
        return
    elif bot_methods.help_methods.verify_none(content) == None:
        return
    
    await ctx.send(await content)

# Comandos NPC

@bot.command(name='cnpc')
async def create_npc(ctx, *, content: bot_methods.command_create_npc = None):
    if bot_methods.help_methods.verify_bot_message(ctx) == None:
        return
    elif bot_methods.help_methods.verify_none(content) == None:
        return
    
    await ctx.send(await content)

@bot.command(name='snpc')
async def search_npc(ctx, *, content: bot_methods.command_search_npc = None):
    if bot_methods.help_methods.verify_bot_message(ctx) == None:
        return
    elif bot_methods.help_methods.verify_none(content) == None:
        return
    
    await ctx.send(embed=content)

@bot.command(name='unpc')
async def update_npc(ctx, *, content: bot_methods.command_update_npc = None):
    if bot_methods.help_methods.verify_bot_message(ctx) == None:
        return
    elif bot_methods.help_methods.verify_none(content) == None:
        return
    
    await ctx.send(await content)

# Comandos Itens

@bot.command(name='citem')
async def create_item(ctx, *, content: bot_methods.command_create_item = None):
    if bot_methods.help_methods.verify_bot_message(ctx) == None:
        return
    elif bot_methods.help_methods.verify_none(content) == None:
        return
    
    await ctx.send(await content)

@bot.command(name='sitem')
async def search_item(ctx, *, content: bot_methods.command_search_item = None):
    if bot_methods.help_methods.verify_bot_message(ctx) == None:
        return
    elif bot_methods.help_methods.verify_none(content) == None:
        return
    
    await ctx.send(embed=content)

@bot.command(name='uitem')
async def update_item(ctx, *, content: bot_methods.command_update_item = None):
    if bot_methods.help_methods.verify_bot_message(ctx) == None:
        return
    elif bot_methods.help_methods.verify_none(content) == None:
        return
    
    await ctx.send(await content)

@bot.command(name='bitem')
async def bond_item(ctx, *, content: bot_methods.command_bond_item = None):
    if bot_methods.help_methods.verify_bot_message(ctx) == None:
        return
    elif bot_methods.help_methods.verify_none(content) == None:
        return
    
    await ctx.send(await content)

# Comandos Armas

@bot.command(name='cweapon')
async def create_weapon(ctx, *, content: bot_methods.command_create_weapon = None):
    if bot_methods.help_methods.verify_bot_message(ctx) == None:
        return
    elif bot_methods.help_methods.verify_none(content) == None:
        return
    
    await ctx.send(await content)

@bot.command(name='sweapon')
async def search_weapon(ctx, *, content: bot_methods.command_search_weapon = None):
    if bot_methods.help_methods.verify_bot_message(ctx) == None:
        return
    elif bot_methods.help_methods.verify_none(content) == None:
        return
    
    await ctx.send(embed=content)

@bot.command(name='uweapon')
async def update_weapon(ctx, *, content: bot_methods.command_update_weapon = None):
    if bot_methods.help_methods.verify_bot_message(ctx) == None:
        return
    elif bot_methods.help_methods.verify_none(content) == None:
        return
    
    await ctx.send(await content)

@bot.command(name='bweapon')
async def bond_weapon(ctx, *, content: bot_methods.command_bond_weapon = None):
    if bot_methods.help_methods.verify_bot_message(ctx) == None:
        return
    elif bot_methods.help_methods.verify_none(content) == None:
        return
    
    await ctx.send(await content)

bot.run(extras.dsc_tkn)
