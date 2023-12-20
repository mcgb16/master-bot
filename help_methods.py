def create_player_help():
    temporary_message = "Works"
    return temporary_message

def update_player_help():
    pass

def create_npc_help():
    temporary_message = "Works"
    return temporary_message

def update_npc_help():
    pass

def all_in_one_help():
    all_commands = {
        '?roll d{número}': 'Roda dado',
        '?h player': 'Ajuda na criação de um personagem jogável.',
        '?h npc': 'Ajuda na criação de um personagem não jogável.'
    }
    initial_phrase = ':wave: Aqui estão todos os comandos que eu posso executar para você e a funcionalidade deles:\n\n'
    final_phrase = 'Qualquer coisa pode contar comigo que estou aqui para ajudar! :wink:'

    help_command_response = initial_phrase
    for key, value in all_commands.items():
        help_command_response += f"{key} ------> {value}\n\n"
    help_command_response += final_phrase
    
    return help_command_response

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
