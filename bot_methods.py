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
    success_message = "Jogador criado com sucesso! O seu ID é: "
    get_player_id = 'SELECT player_id FROM players ORDER BY player_id DESC LIMIT 1'
    
    all_players_info = player_info.split()
    string_to_dict = ''
    
    for i in all_players_info:
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
        player_info_dict = eval(string_to_dict_formatted)

        insert_player_db = db_connection.create_player_db(player_info_dict)
        
        if insert_player_db == True:
            player_id = db_connection.execute_sqlite_select(get_player_id)

            return_message = success_message + str(player_id[0][0])

            return return_message
        else:
            return insert_player_db
    except Exception as e:
        print(e)

        help_player_msg = help_methods.create_player_help()

        return help_player_msg

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