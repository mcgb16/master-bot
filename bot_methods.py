import discord
from discord.ext import commands
from random import randint
import help_methods
# import db_connection

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
        print(type(player_info_dict))
        
        return player_info_dict
    except Exception as e:
        print(e)