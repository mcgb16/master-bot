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
""",
        '?uplayer': """
""",
        '?splayer': """
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
Utilizado para rodar dados. Ele deve ser utilizado da seguinte forma:
    ?roll {número}d{número}
O número da esquerda indica a quantidade de dados que serão rodados (caso não seja informado, será considerado o número 1 por padrão).
Já o número da direita indica o número de faces do dado.
""",
    }

    if help_command == 'all':
        initial_phrase = ':wave: Aqui estão todos os comandos que eu posso executar para você e a funcionalidade deles:\n'
        help_commands_presentation = '\nComandos de Ajuda!\n\n'
        player_commands_presentation = '\nComandos de Players!\n\n'
        npc_commands_presentation = '\nComandos de NPCs!\n\n'
        item_commands_presentation = '\nComandos de Itens!\n\n'
        weapon_commands_presentation = '\nComandos de Armas!\n\n'
        dice_commands_presentation = '\nComandos de Dados!\n\n'

        help_command_response = initial_phrase

        help_command_response += help_commands_presentation
        for key, value in all_help_commands.items():
            help_command_response += f"{key} ------> {value}\n"

        help_command_response += player_commands_presentation
        for key, value in all_player_commands.items():
            help_command_response += f"{key} ------> {value}\n"

        help_command_response += npc_commands_presentation
        for key, value in all_npc_commands.items():
            help_command_response += f"{key} ------> {value}\n"

        help_command_response += item_commands_presentation
        for key, value in all_item_commands.items():
            help_command_response += f"{key} ------> {value}\n"

        help_command_response += weapon_commands_presentation
        for key, value in all_weapon_commands.items():
            help_command_response += f"{key} ------> {value}\n"

        help_command_response += dice_commands_presentation
        for key, value in all_dice_commands.items():
            help_command_response += f"{key} ------> {value}\n"

    elif help_command == 'player':
        initial_phrase = ':wave: Aqui estão todos os comandos que eu posso executar para você, no âmbito de players, e a funcionalidade deles:\n\n'

        help_command_response = initial_phrase
        for key, value in all_player_commands.items():
            help_command_response += f"{key} ------> {value}\n"

    elif help_command == 'npc':
        initial_phrase = ':wave: Aqui estão todos os comandos que eu posso executar para você, no âmbito de npcs, e a funcionalidade deles:\n\n'

        help_command_response = initial_phrase
        for key, value in all_npc_commands.items():
            help_command_response += f"{key} ------> {value}\n"

    elif help_command == 'item':
        initial_phrase = ':wave: Aqui estão todos os comandos que eu posso executar para você, no âmbito de itens, e a funcionalidade deles:\n\n'

        help_command_response = initial_phrase
        for key, value in all_item_commands.items():
            help_command_response += f"{key} ------> {value}\n"

    elif help_command == 'weapon':
        initial_phrase = ':wave: Aqui estão todos os comandos que eu posso executar para você e a funcionalidade deles:\n\n'

        help_command_response = initial_phrase
        for key, value in all_weapon_commands.items():
            help_command_response += f"{key} ------> {value}\n"

    elif help_command == 'dice':
        initial_phrase = ':wave: Aqui estão todos os comandos que eu posso executar para você e a funcionalidade deles:\n\n'

        help_command_response = initial_phrase
        for key, value in all_dice_commands.items():
            help_command_response += f"{key} ------> {value}\n"

    final_phrase = 'Qualquer coisa pode contar comigo que estou aqui para ajudar! :wink:'
    
    help_command_response += final_phrase
    
    return help_command_response