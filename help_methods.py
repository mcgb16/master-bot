import discord

def verify_none(content):
    if content == None:
        return
    else:
        return True

def verify_bot_message(ctx):
    if ctx.author.bot:
        return
    else:
        return True

def all_in_one_help(help_command = 'all'):
    all_help_commands = {
        '?h player': 'Ajuda com atividades relacionadas aos personagens jogáveis.',
        '?h item': 'Ajuda com atividades relacionadas aos itens.',
        '?h weapon': 'Ajuda com atividades relacionadas às armas.',
        '?h dice': 'Ajuda com atividades relacionadas aos dados.',
        '?h npc': 'Ajuda com atividades relacionadas aos personagens não jogáveis.'
    }

    all_player_commands = {
        '?cplayer': """
Utilizado para efetuar a criação de personagens jogáveis. Para isto, alguns atributos são obrigatórios, como: nome, força, destreza, constituição, sabedoria, inteligência, vida e carisma. Além destes 8 atributos, temos o de ouro, que por sua vez não é obrigatório.
""",
        '?uplayer': """
Utilizado para efetuar atualizações nos personagens jogáveis já criados. Para isto, o único atributo obrigatório é o ID. Após dizer o ID, basta escrever o nome do atributo e seu valor novo.
""",
        '?splayer': """
Utilizado para efetuar buscas de personagens jogáveis na base de dados do bot. Para isto, a única informação que é preciso de ser passada é o número do ID do personagem.
"""
    }

    all_npc_commands = {
        '?cnpc': """
Utilizado para efetuar a criação de personagens não jogáveis. Para isto, alguns atributos são obrigatórios, como: nome, força, destreza, constituição, sabedoria, inteligência, vida e carisma. Além destes 8 atributos, temos o de ouro, que por sua vez não é obrigatório.
""",
        '?unpc': """
Utilizado para efetuar atualizações nos personagens não jogáveis já criados. Para isto, o único atributo obrigatório é o ID. Após dizer o ID, basta escrever o nome do atributo e seu valor novo.
""",
        '?snpc': """
Utilizado para efetuar buscas de personagens não jogáveis na base de dados do bot. Para isto, a única informação que é preciso de ser passada é o número do ID do personagem.
"""
    }

    all_item_commands = {
        '?citem': """
Utilizado para efetuar a criação de itens. Neste comando, apenas o atributo 'nome' é necessário.
""",
        '?uitem': """
Utilizado para efetuar atualizações nos itens já criados. Para isto, o único atributo obrigatório é o ID. Após dizer o ID, basta escrever o atributo 'nome' e seu valor novo.
""",
        '?sitem': """
Utilizado para efetuar buscas de itens na base de dados do bot. Para isto, a única informação que é preciso de ser passada é o número do ID do item.
""",
        '?bitem': """
Utilizado para efetuar a vinculação de um item a um personagem jogável e/ou npc (personagem não jogável). Para efetuar essa vinculação ambos os IDs do item e do player/npc são obrigatórios e necessários.
"""
    }

    all_weapon_commands = {
        '?cweapon': """
Utilizado para efetuar a criação de armas. Neste comando, os atributos nome, dano e tipo são obrigatórios.
""",
        '?uweapon': """
Utilizado para efetuar atualizações nas armas já criadas. Para isto, o único atributo obrigatório é o ID. Após dizer o ID, basta escrever o atributo e seu valor novo.
""",
        '?sweapon': """
Utilizado para efetuar buscas de armas na base de dados do bot. Para isto, a única informação que é preciso de ser passada é o número do ID da arma.
""",
        '?bweapon': """
Utilizado para efetuar a vinculação de uma arma a um personagem jogável e/ou npc (personagem não jogável). Para efetuar essa vinculação ambos os IDs da arma e do player/npc são obrigatórios e necessários.
"""
    }

    all_dice_commands = {
        '?roll': """
Utilizado para rodar dados.
""",
    }

    embed_description = ':wave: **Para mais informações, acesse a [documentação oficial](https://github.com/mcgb16/master-bot).**'
    embed_footer = 'Qualquer ajuda, pode contar comigo!'

    help_embed = discord.Embed(
        title='Ajuda',
        description=embed_description,
    )

    help_embed.set_footer(text=embed_footer)

    if help_command == 'all':
        for key, value in all_help_commands.items():
            help_embed.add_field(name=f'❄ {key}', value=value,inline=False)

    elif help_command == 'player':
        for key, value in all_player_commands.items():
            help_embed.add_field(name=f'🎮 {key}', value=value,inline=False)

    elif help_command == 'npc':
        for key, value in all_npc_commands.items():
            help_embed.add_field(name=f'🖥 {key}', value=value,inline=False)

    elif help_command == 'item':
        for key, value in all_item_commands.items():
            help_embed.add_field(name=f'🥇 {key}', value=value,inline=False)

    elif help_command == 'weapon':
        for key, value in all_weapon_commands.items():
            help_embed.add_field(name=f'⚔ {key}', value=value,inline=False)

    elif help_command == 'dice':
        for key, value in all_dice_commands.items():
            help_embed.add_field(name=f'🎲 {key}', value=value,inline=False)
    
    return help_embed