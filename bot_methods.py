import discord
from discord.ext import commands
from random import randint
import help_methods
import db_connection
import add_ons

# Dado

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
            wrong_command = help_methods.all_in_one_help('dice')
            return wrong_command
    else:
        try:
            dice_number = int(dice_list[1])
            dice_result = randint(1,int(dice_number))

            dice_return.add_field(name=f'Dado 1', value=dice_result)

            dice_return.title = f'Total: {dice_result}'

            return dice_return
        except:
            wrong_command = help_methods.all_in_one_help('dice')
            return wrong_command

# Help

def command_help(arg):
    if arg == 'player':
        player_help = help_methods.all_in_one_help('player')
        return player_help
    elif arg == 'npc':
        npc_help = help_methods.all_in_one_help('npc')
        return npc_help
    elif arg == 'dice':
        dice_help = help_methods.all_in_one_help('dice')
        return dice_help
    elif arg == 'item':
        item_help = help_methods.all_in_one_help('item')
        return item_help
    elif arg == 'weapon':
        weapon_help = help_methods.all_in_one_help('weapon')
        return weapon_help
    elif arg == None:
        help_all_in_one = help_methods.all_in_one_help()
        return help_all_in_one

# Player

async def command_create_player(player_info):
    get_player_id = 'SELECT player_id, player_name FROM players ORDER BY player_id DESC LIMIT 1'

    player_info_dict = create_dict(player_info)

    if player_info_dict == None:
        help_message = help_methods.all_in_one_help('player')

        return help_message

    insert_player_db = db_connection.create_player_db(player_info_dict)
    
    if insert_player_db == True:
        player_id = db_connection.execute_sqlite_select(get_player_id)

        return_message = f"Personagem [{str(player_id[0][1])}] criado com sucesso! Seu ID é: [{str(player_id[0][0])}]"

        return return_message, player_id[0][0], 'player'
    else:
        return insert_player_db

async def command_update_player(upd_info):    
    upd_player_dict = create_dict(upd_info)

    if upd_player_dict == None:
        help_message = help_methods.all_in_one_help('player')

        return help_message

    update_player_db = db_connection.update_player_db(upd_player_dict)
    
    if update_player_db == True:
        player_id = ''
        for k, v in upd_player_dict.items():
            if k.lower() in add_ons.id_values:
                player_id = int(v)

        return_message = f'Personagem {player_id} atualizado.'

        return return_message
    else:
        return update_player_db

def command_search_player(player_id):
    search_command = f"""
    SELECT * FROM players
    LEFT JOIN weapons ON weapons.id_player = players.player_id
    LEFT JOIN items ON items.id_player = players.player_id
    WHERE player_id = {player_id}"""
    
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

    verify_weapon_id = []

    for n,i in enumerate(search_player_result):
        weapon_id = i[10]
        weapon_name = i[11]
        weapon_dmg = i[12]
        weapon_dmg_type = i[13]
        
        if weapon_id:
            if weapon_id not in verify_weapon_id:
                player_result.add_field(name=f'Arma {n+1}', value=f'**ID:** {weapon_id} | **Nome:** {weapon_name} | **Dano:** {weapon_dmg} | **Tipo de Dano:** {weapon_dmg_type}', inline=False)

                verify_weapon_id.append(weapon_id)
            else:
                pass

    verify_item_id = []

    for n,i in enumerate(search_player_result):
        item_id = i[16]
        item_name = i[17]

        if item_id:
            if item_id not in verify_item_id:
                player_result.add_field(name=f'Item {n+1}', value=f'**ID:** {item_id} | **Nome:** {item_name}', inline=False)

                verify_item_id.append(item_id)
            else:
                pass
    
    return player_result

# NPC

async def command_create_npc(npc_info):
    get_npc_id = 'SELECT npc_id, npc_name FROM npcs ORDER BY npc_id DESC LIMIT 1'
    
    npc_info_dict = create_dict(npc_info)

    if npc_info_dict == None:
        help_message = help_methods.all_in_one_help('npc')

        return help_message

    insert_npc_db = db_connection.create_npc_db(npc_info_dict)
    
    if insert_npc_db == True:
        npc_id = db_connection.execute_sqlite_select(get_npc_id)

        return_message = f"NPC [{str(npc_id[0][1])}] criado com sucesso! Seu ID é: [{str(npc_id[0][0])}]"

        return return_message, npc_id[0][0], 'npc'
    else:
        return insert_npc_db

async def command_update_npc(upd_info):
    upd_npc_dict = create_dict(upd_info)

    if upd_npc_dict == None:
        help_message = help_methods.all_in_one_help('npc')

        return help_message

    update_npc_db = db_connection.update_npc_db(upd_npc_dict)
    
    if update_npc_db == True:
        npc_id = ''
        for k, v in upd_npc_dict.items():
            if k.lower() in add_ons.id_values:
                npc_id = int(v)

        return_message = f'NPC {npc_id} atualizado.'

        return return_message
    else:
        return update_npc_db
    
def command_search_npc(npc_id):
    search_command = f"""
    SELECT * FROM npcs
    LEFT JOIN weapons ON weapons.id_npc = npcs.npc_id
    LEFT JOIN items ON items.id_npc = npcs.npc_id
    WHERE npc_id = {npc_id}"""
    
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
    
    verify_weapon_id = []

    for n,i in enumerate(search_npc_result):
        weapon_id = i[10]
        weapon_name = i[11]
        weapon_dmg = i[12]
        weapon_dmg_type = i[13]
        
        if weapon_id:
            if weapon_id not in verify_weapon_id:
                npc_result.add_field(name=f'Arma {n+1}', value=f'**ID:** {weapon_id} | **Nome:** {weapon_name} | **Dano:** {weapon_dmg} | **Tipo de Dano:** {weapon_dmg_type}', inline=False)

                verify_weapon_id.append(weapon_id)
            else:
                pass

    verify_item_id = []

    for n,i in enumerate(search_npc_result):
        item_id = i[16]
        item_name = i[17]

        if item_id:
            if item_id not in verify_item_id:
                npc_result.add_field(name=f'Item {n+1}', value=f'**ID:** {item_id} | **Nome:** {item_name}', inline=False)

                verify_item_id.append(item_id)
            else:
                pass

    return npc_result

# Item

async def command_create_item(item_info):
    get_item_id = 'SELECT item_id, item_name FROM items ORDER BY item_id DESC LIMIT 1'

    item_info_dict = create_dict(item_info)

    if item_info_dict == None:
        help_message = help_methods.all_in_one_help('item')

        return help_message
    
    insert_item_db = db_connection.create_item_db(item_info_dict)
    
    if insert_item_db == True:
        item_id = db_connection.execute_sqlite_select(get_item_id)

        return_message = f"Item [{str(item_id[0][1])}] criado com sucesso! Seu ID é: [{str(item_id[0][0])}]"

        return return_message, item_id[0][0], 'item'
    else:
        return insert_item_db

def command_search_item(item_id):
    search_command = f'SELECT * FROM items WHERE item_id = {item_id}'
    
    search_item_result  = db_connection.execute_sqlite_select(search_command)

    i_id = search_item_result[0][0]
    name = search_item_result[0][1]
    id_npc = search_item_result[0][2]
    id_player = search_item_result[0][3]

    item_result = discord.Embed(
        title=f'ID do item: {i_id}',
        color= discord.Colour.random()
    )
    item_result.add_field(name='Nome do Item', value=name, inline=False)
    if id_npc:
        item_result.add_field(name='Npc', value=id_npc, inline=False)
    else:
        item_result.add_field(name='Npc', value='Nenhum', inline=False)

    if id_player:
        item_result.add_field(name='Player', value=id_player, inline=False)
    else:
        item_result.add_field(name='Player', value='Nenhum', inline=False)

    return item_result

async def command_update_item(upd_info):
    upd_item_dict = create_dict(upd_info)

    if upd_item_dict == None:
        help_message = help_methods.all_in_one_help('item')

        return help_message

    update_item_db = db_connection.update_item_db(upd_item_dict)
    
    if update_item_db == True:
        item_id = ''
        for k, v in upd_item_dict.items():
            if k.lower() in add_ons.id_values:
                item_id = int(v)

        return_message = f'Item {item_id} atualizado.'

        return return_message
    else:
        return update_item_db

async def command_bond_item(bond_info):
    bond_dict = create_dict(bond_info)

    if bond_dict == None:
        help_message = help_methods.all_in_one_help('item')
        return help_message
    
    error_missing_id = 'Eu preciso saber tanto o ID do item quanto o ID do player ou npc que irá recebê-lo, por gentileza.'
    error_convert_int = 'Por favor, digite apenas números para os IDs.'
    bond_command = 'UPDATE items SET '
    success_message = 'Vinculação efetuada com sucesso.'
    item_id = ''
    npc_id = ''
    player_id = ''
    verify_cont = 0
    update_command_list = []

    try:
        for k,v in bond_dict.items():
            if k in add_ons.id_values:
                item_id = int(v)
            elif k in add_ons.player:
                player_id = int(v)
                verify_cont += 1
                update_command_list.append(f'id_player = {player_id}')
            elif k in add_ons.npc:
                npc_id = int(v)
                verify_cont += 1
                update_command_list.append(f'id_npc = {npc_id}')
        
        if item_id == '' or verify_cont == 0:        
            return error_missing_id
        else:
            for i,v in enumerate(update_command_list):
                if i == (len(update_command_list) - 1):
                    bond_command += v
                else:
                    bond_command += v + ', '
                
            bond_command += f' WHERE item_id = {item_id}'

            save_on_db = db_connection.execute_sqlite_commands(bond_command)

            if save_on_db:
                return success_message
            else:
                return save_on_db
    except Exception as e:
        print(e)
        return error_convert_int

# Arma

async def command_create_weapon(weapon_info):
    get_weapon_id = 'SELECT weapon_id, weapon_name FROM weapons ORDER BY weapon_id DESC LIMIT 1'

    weapon_info_dict = create_dict(weapon_info)

    if weapon_info_dict == None:
        help_message = help_methods.all_in_one_help('weapon')

        return help_message
    
    insert_weapon_db = db_connection.create_weapon_db(weapon_info_dict)
    
    if insert_weapon_db == True:
        weapon_id = db_connection.execute_sqlite_select(get_weapon_id)

        return_message = f"Arma [{str(weapon_id[0][1])}] criada com sucesso! Seu ID é: [{str(weapon_id[0][0])}]"

        return return_message, weapon_id[0][0], 'weapon'
    else:
        return insert_weapon_db
    
def command_search_weapon(weapon_id):
    search_command = f'SELECT * FROM weapons WHERE weapon_id = {weapon_id}'
    
    search_weapon_result  = db_connection.execute_sqlite_select(search_command)

    w_id = search_weapon_result[0][0]
    name = search_weapon_result[0][1]
    dmg = search_weapon_result[0][2]
    dmg_type = search_weapon_result[0][3]
    id_npc = search_weapon_result[0][4]
    id_player = search_weapon_result[0][5]

    weapon_result = discord.Embed(
        title=f'ID da Arma: {w_id}',
        color= discord.Colour.random()
    )
    weapon_result.add_field(name='Nome da Arma', value=name, inline=False)
    weapon_result.add_field(name='Dano', value=dmg, inline=True)
    weapon_result.add_field(name='Tipo de Dano', value=dmg_type, inline=True)
    if id_npc:
        weapon_result.add_field(name='Npc', value=id_npc, inline=False)
    else:
        weapon_result.add_field(name='Npc', value='Nenhum', inline=False)

    if id_player:
        weapon_result.add_field(name='Player', value=id_player, inline=False)
    else:
        weapon_result.add_field(name='Player', value='Nenhum', inline=False)

    return weapon_result

async def command_update_weapon(upd_info):
    upd_weapon_dict = create_dict(upd_info)

    if upd_weapon_dict == None:
        help_message = help_methods.all_in_one_help('weapon')

        return help_message

    update_weapon_db = db_connection.update_weapon_db(upd_weapon_dict)
    
    if update_weapon_db == True:
        weapon_id = ''
        for k, v in upd_weapon_dict.items():
            if k.lower() in add_ons.id_values:
                weapon_id = int(v)

        return_message = f'Arma {weapon_id} atualizada.'

        return return_message
    else:
        return update_weapon_db

async def command_bond_weapon(bond_info):
    bond_dict = create_dict(bond_info)

    if bond_dict == None:
        help_message = help_methods.all_in_one_help('weapon')
        return help_message
    
    error_missing_id = 'Eu preciso saber tanto o ID da arma quanto o ID do player ou npc que irá recebê-la, por gentileza.'
    error_convert_int = 'Por favor, digite apenas números para os IDs.'
    bond_command = 'UPDATE weapons SET '
    success_message = 'Vinculação efetuada com sucesso.'
    weapon_id = ''
    npc_id = ''
    player_id = ''
    verify_cont = 0
    update_command_list = []

    try:
        for k,v in bond_dict.items():
            if k in add_ons.id_values:
                weapon_id = int(v)
            elif k in add_ons.player:
                player_id = int(v)
                verify_cont += 1
                update_command_list.append(f'id_player = {player_id}')
            elif k in add_ons.npc:
                npc_id = int(v)
                verify_cont += 1
                update_command_list.append(f'id_npc = {npc_id}')
        
        if weapon_id == '' or verify_cont == 0:        
            return error_missing_id
        else:
            for i,v in enumerate(update_command_list):
                if i == (len(update_command_list) - 1):
                    bond_command += v
                else:
                    bond_command += v + ', '
                
            bond_command += f' WHERE weapon_id = {weapon_id}'

            save_on_db = db_connection.execute_sqlite_commands(bond_command)

            if save_on_db:
                return success_message
            else:
                return save_on_db
    except Exception as e:
        print(e)
        return error_convert_int

# Métodos Gerais

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

def creation_controller(ctx, content):
    user_id = str(ctx.author.id)
    
    if len(content) > 1:
        return_message, cmd_id, cmd_type = content

        if cmd_type == 'player':
            set_owner_command = f'UPDATE players SET owner = {user_id} WHERE player_id = {cmd_id}'
            select_cmd = f'SELECT * FROM players WHERE player_id = {cmd_id}'

            set_owner = db_connection.execute_sqlite_commands(set_owner_command)

            if set_owner:
                print(db_connection.execute_sqlite_select(select_cmd))

            return return_message
        elif cmd_type == 'npc':
            set_owner_command = f'UPDATE npcs SET owner = {user_id} WHERE npc_id = {cmd_id}'
            select_cmd = f'SELECT * FROM npcs WHERE npc_id = {cmd_id}'

            set_owner = db_connection.execute_sqlite_commands(set_owner_command)

            if set_owner:
                print(db_connection.execute_sqlite_select(select_cmd))

            return return_message
        elif cmd_type == 'item':
            set_owner_command = f'UPDATE items SET owner = {user_id} WHERE item_id = {cmd_id}'
            select_cmd = f'SELECT * FROM items WHERE item_id = {cmd_id}'

            set_owner = db_connection.execute_sqlite_commands(set_owner_command)

            if set_owner:
                print(db_connection.execute_sqlite_select(select_cmd))

            return return_message
        elif cmd_type == 'weapon':
            set_owner_command = f'UPDATE weapons SET owner = {user_id} WHERE weapon_id = {cmd_id}'
            select_cmd = f'SELECT * FROM weapons WHERE weapon_id = {cmd_id}'

            set_owner = db_connection.execute_sqlite_commands(set_owner_command)

            if set_owner:
                print(db_connection.execute_sqlite_select(select_cmd))

            return return_message
    else:
        return content