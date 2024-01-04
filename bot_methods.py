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

def command_roll_dice(dice):
    dice_list = dice.split('d')

    dice_return = discord.Embed(
        color= discord.Colour.random()
    )
    
    if dice_list[0] != '':
        try:
            number_of_dices = int(dice_list[0])
            dice_number = int(dice_list[1])

            dice_total = 0

            for i in range(number_of_dices):
                dice_result = randint(1,int(dice_number))
                dice_total += dice_result
                dice_return.add_field(name=f'Dado {i+1}', value=dice_result, inline=False)
            
            dice_return.title = f'Total: {dice_total}'
            
            return dice_return
        except:
            wrong_command = help_methods.roll_dice_help()
            return wrong_command
    else:
        try:
            dice_number = int(dice_list[1])
            dice_result = randint(1,int(dice_number))

            dice_return.add_field(name=f'Dado 1', value=dice_result)

            dice_return.title = f'Total: {dice_total}'

            return dice_return
        except:
            wrong_command = help_methods.roll_dice_help()
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

async def command_update_npc(upd_info):
    upd_npc_dict = create_dict(upd_info)

    if upd_npc_dict == None:
        help_message = help_methods.update_npc_help()

        return help_message

    update_npc_db = db_connection.update_npc_db(upd_npc_dict)
    
    if update_npc_db == True:
        return_message = 'NPC atualizado.'

        return return_message
    else:
        return update_npc_db

async def command_create_item(item_info):
    get_item_id = 'SELECT item_id, item_name FROM items ORDER BY item_id DESC LIMIT 1'

    item_info_dict = create_dict(item_info)

    if item_info_dict == None:
        help_message = help_methods.create_item_help()

        return help_message
    
    insert_item_db = db_connection.create_item_db(item_info_dict)
    
    if insert_item_db == True:
        item_id = db_connection.execute_sqlite_select(get_item_id)

        return_message = f"Item [{str(item_id[0][1])}] criado com sucesso! Seu ID é: [{str(item_id[0][0])}]"

        return return_message
    else:
        return insert_item_db

async def command_create_weapon(weapon_info):
    get_weapon_id = 'SELECT weapon_id, weapon_name FROM weapons ORDER BY weapon_id DESC LIMIT 1'

    weapon_info_dict = create_dict(weapon_info)

    if weapon_info_dict == None:
        help_message = help_methods.create_weapon_help()

        return help_message
    
    insert_weapon_db = db_connection.create_weapon_db(weapon_info_dict)
    
    if insert_weapon_db == True:
        weapon_id = db_connection.execute_sqlite_select(get_weapon_id)

        return_message = f"Arma [{str(weapon_id[0][1])}] criada com sucesso! Seu ID é: [{str(weapon_id[0][0])}]"

        return return_message
    else:
        return insert_weapon_db

def create_dict(str_dict):
    all_info = str_dict.split()
    print(all_info)
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