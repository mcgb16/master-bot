import discord
from discord.ext import commands
from random import randint

async def command_help(arg):
    if arg == 'player':
        player_creation = create_player()
        return player_creation
    elif arg == 'npc':
        npc_creation = create_npc()
        return npc_creation

async def command_roll_dice(dice):
    wrong_command = """
Para rodar um dado, digite da seguinte forma o comando (variando o valor do dado que deseja rodar):
#roll d20
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

# Não Iniciada
def create_player():
    temporary_message = "Works"
    return temporary_message

# Não Iniciada
def create_npc():
    temporary_message = "Works"
    return temporary_message

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