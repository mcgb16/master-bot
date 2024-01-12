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
Utilizado para efetuar a criação de personagens jogáveis. Para isto, alguns atributos são obrigatórios, como: nome, força, destreza, constituição, sabedoria, inteligência, vida e carisma. Além destes 8 atributos, temos o de ouro, que por sua vez não é obrigatório. **Recomendação de uso do comando:**

    ?cplayer nome: Player,
    destreza: 10,
    força: 5,
    constituição: 2,
    inteligência: 5,
    sabedOria: 9,
    carisma: 7,
    HP: 10,
    ouro: 88

**Observação:** é de suma importância não negligenciar o espaçamento correto entre os dois pontos (:) e o valor, assim como a vírgula (,) e o nome do atributo seguinte. Caso tenha dúvidas de como aplicar a quebra de linha em uma mensagem do discord, apenas segure a tecla CTRL e aperte a tecla ENTER.
""",
        '?uplayer': """
Utilizado para efetuar atualizações nos personagens jogáveis já criados. Para isto, o único atributo obrigatório é o ID, o qual é fornecido logo após efetuar a criação de um personagem jogável. Os IDs são únicos, ou seja, cada personagem tem o seu próprio ID. Após dizer o ID, basta escrever o nome do atributo e seu valor novo. **Recomendação de uso do comando:**

    ?uplayer id: 1,
    destreza: 15

**Observação:** é de suma importância não negligenciar o espaçamento correto entre os dois pontos (:) e o valor, assim como a vírgula (,) e o nome do atributo seguinte. Caso tenha dúvidas de como aplicar a quebra de linha em uma mensagem do discord, apenas segure a tecla CTRL e aperte a tecla ENTER.
**Observação 2:** é possível efetuar a atualização de quantos atributos quiser de uma vez, não precisando fazer um por vez.
""",
        '?splayer': """
Utilizado para efetuar buscas de personagens jogáveis na base de dados do bot. Para isto, a única informação que é preciso de ser passada é o número do ID do personagem, o qual é fornecido logo após efetuar a criação de um personagem jogável. Os IDs são únicos, ou seja, cada personagem tem o seu próprio ID. **Recomendação de uso do comando:**

    ?splayer 1
"""
    }

    all_npc_commands = {
        '?cnpc': """
""",
        '?unpc': """
""",
        '?snpc': """
"""
    }

    all_item_commands = {
        '?citem': """
""",
        '?uitem': """
""",
        '?sitem': """
""",
        '?bitem': """
"""
    }

    all_weapon_commands = {
        '?cweapon': """
""",
        '?uweapon': """
""",
        '?sweapon': """
""",
        '?bweapon': """
"""
    }

    all_dice_commands = {
        '?roll': """
Utilizado para rodar dados. **Ele deve ser utilizado da seguinte forma:**

    ?roll {número}d{número}

O número da esquerda indica a quantidade de dados que serão rodados (caso não seja informado, será considerado o número 1 por padrão).
Já o número da direita indica o número de faces do dado.
""",
    }

    embed_description = ':wave: Aqui estão todos os comandos que eu posso executar para você e a funcionalidade deles:\n'
    embed_footer = 'Qualquer coisa pode contar comigo que estou aqui para ajudar!'

    help_embed = discord.Embed(
        title='Ajuda',
        description=embed_description,
    )

    help_embed.set_footer(text=embed_footer)

    if help_command == 'all':
        for key, value in all_help_commands.items():
            help_embed.add_field(name=f'❄ {key}', value=value,inline=False)

        for key, value in all_player_commands.items():
            help_embed.add_field(name=f'🎮 {key}', value=value,inline=False)

        for key, value in all_npc_commands.items():
            help_embed.add_field(name=f'🖥 {key}', value=value,inline=False)

        for key, value in all_item_commands.items():
            help_embed.add_field(name=f'🥇 {key}', value=value,inline=False)

        for key, value in all_weapon_commands.items():
            help_embed.add_field(name=f'⚔ {key}', value=value,inline=False)

        for key, value in all_dice_commands.items():
            help_embed.add_field(name=f'🎲 {key}', value=value,inline=False)

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