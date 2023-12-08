import discord
from discord.ext import commands
from random import randint
# Não finalizada
class PrivateMessage(commands.Converter):
    async def convert(self, ctx, argument):
        if ctx.author.bot:
            return
        user = ctx.author
        return 

# Não finalizada
async def command_help(arg):
    pass

async def command_roll_dice(dice):
    wrong_command = """
Para rodar um dado, digite da seguinte forma o comando (variando o valor do dado que deseja rodar):
#roll d20
"""
    
    if dice[0] != 'd':
        return wrong_command
    else:
        dice_number = dice.replace('d', '')
        dice_result = randint(1,int(dice_number))
        return dice_result

# Não finalizada
async def command_create_player(arg):
    pass

# Não finalizada
async def command_create_npc(arg):
    pass
