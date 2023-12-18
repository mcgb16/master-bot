import discord
from discord.ext import commands
from random import randint
import help_methods
import db_connection

async def command_help(arg):
    if arg == 'player':
        player_creation = help_methods.create_player_help()
        return player_creation
    elif arg == 'npc':
        npc_creation = help_methods.create_npc_help()
        return npc_creation
    elif arg == None:
        help_all_in_one = help_methods.all_in_one_help()
        return help_all_in_one

async def command_roll_dice(dice):
    wrong_command = """
Para rodar um dado, digite da seguinte forma o comando (variando o valor do dado que deseja rodar):
?roll d20
"""
    
    if dice[0] != 'd':
        return wrong_command
    else:
        try:
            dice_number = dice.replace('d', '')
            dice_result = randint(1,int(dice_number))
            return dice_result
        except:
            return wrong_command

async def command_create_player(player_info):
    get_player_id = 'SELECT player_id, player_name FROM players ORDER BY player_id DESC LIMIT 1'

    player_info_dict = create_dict(player_info)

    if player_info_dict == None:
        help_message = help_methods.create_player_help()

        return help_message

    insert_player_db = db_connection.create_player_db(player_info_dict)
    
    if insert_player_db == True:
        player_id = db_connection.execute_sqlite_select(get_player_id)

        return_message = f"Personagem [{str(player_id[0][1])}] criado com sucesso! Seu ID é: [{str(player_id[0][0])}]"

        return return_message
    else:
        return insert_player_db

async def command_update_player(upd_info):    
    upd_player_dict = create_dict(upd_info)

    if upd_player_dict == None:
        help_message = help_methods.update_player_help()

        return help_message

    update_player_db = db_connection.update_player_db(upd_player_dict)
    
    if update_player_db == True:
        return_message = 'Personagem atualizado.'

        return return_message
    else:
        return update_player_db


async def command_create_npc(npc_info):
    get_npc_id = 'SELECT npc_id, npc_name FROM npcs ORDER BY npc_id DESC LIMIT 1'
    
    npc_info_dict = create_dict(npc_info)

    if npc_info_dict == None:
        help_message = help_methods.create_npc_help()

        return help_message

    insert_npc_db = db_connection.create_npc_db(npc_info_dict)
    
    if insert_npc_db == True:
        npc_id = db_connection.execute_sqlite_select(get_npc_id)

        return_message = f"NPC [{str(npc_id[0][1])}] criado com sucesso! Seu ID é: [{str(npc_id[0][0])}]"

        return return_message
    else:
        return insert_npc_db


def create_dict(str_dict):
    all_info = str_dict.split()
    string_to_dict = ''
    
    for i in all_info:
        if i == ":":
            string_to_dict += i
        elif i == ",":
            string_to_dict += i
        elif ":" in i:
            j = i.split(':')
            string_to_dict += f"'{j[0]}':"
        elif "," in i:
            j = i.split(',')
            string_to_dict += f"'{j[0]}',"
        else:
            string_to_dict += f"'{i}'"
    string_to_dict_formatted = "{" + string_to_dict + "}"

    try:
        dict_created = eval(string_to_dict_formatted)
        return dict_created
    except:
        return None


def command_search_player(player_id):
    search_command = f'SELECT * FROM players WHERE player_id = {player_id}'
    
    search_player_result  = db_connection.execute_sqlite_select(search_command)

    p_id = search_player_result[0][0]
    name = search_player_result[0][1]
    dex = search_player_result[0][2]
    strenght = search_player_result[0][3]
    cons = search_player_result[0][4]
    intelligence = search_player_result[0][5]
    wis = search_player_result[0][6]
    charisma = search_player_result[0][7]
    hp = search_player_result[0][8]
    gold = search_player_result[0][9]


    player_result = discord.Embed(
        title=f'ID do Player: {p_id}',
        color= discord.Colour.random()
    )
    player_result.add_field(name='Nome do Player', value=name, inline=False)
    player_result.add_field(name='Destreza', value=dex, inline=True)
    player_result.add_field(name='Força', value=strenght, inline=True)
    player_result.add_field(name='Constituição', value=cons, inline=True)
    player_result.add_field(name='Inteligência', value=intelligence, inline=True)
    player_result.add_field(name='Sabedoria', value=wis, inline=True)
    player_result.add_field(name='Carisma', value=charisma, inline=True)
    player_result.add_field(name='HP', value=hp, inline=True)
    player_result.add_field(name='Ouro', value=gold, inline=True)

    return player_result

def command_search_npc(npc_id):
    search_command = f'SELECT * FROM npcs WHERE npc_id = {npc_id}'
    
    search_npc_result  = db_connection.execute_sqlite_select(search_command)

    n_id = search_npc_result[0][0]
    name = search_npc_result[0][1]
    dex = search_npc_result[0][2]
    strenght = search_npc_result[0][3]
    cons = search_npc_result[0][4]
    intelligence = search_npc_result[0][5]
    wis = search_npc_result[0][6]
    charisma = search_npc_result[0][7]
    hp = search_npc_result[0][8]
    gold = search_npc_result[0][9]


    npc_result = discord.Embed(
        title=f'ID do npc: {n_id}',
        color= discord.Colour.random()
    )
    npc_result.add_field(name='Nome do npc', value=name, inline=False)
    npc_result.add_field(name='Destreza', value=dex, inline=True)
    npc_result.add_field(name='Força', value=strenght, inline=True)
    npc_result.add_field(name='Constituição', value=cons, inline=True)
    npc_result.add_field(name='Inteligência', value=intelligence, inline=True)
    npc_result.add_field(name='Sabedoria', value=wis, inline=True)
    npc_result.add_field(name='Carisma', value=charisma, inline=True)
    npc_result.add_field(name='HP', value=hp, inline=True)
    npc_result.add_field(name='Ouro', value=gold, inline=True)

    return npc_result