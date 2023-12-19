import sqlite3
import extras

def create_tables():
    create_table_players = """
    CREATE TABLE IF NOT EXISTS players (
        player_id INTEGER PRIMARY KEY AUTOINCREMENT,
        player_name VARCHAR(45) NOT NULL,
        dexterity INTEGER NOT NULL,
        strenght INTEGER NOT NULL,
        constitution INTEGER NOT NULL,
        intelligence INTEGER NOT NULL,
        wisdom INTEGER NOT NULL,
        charisma INTEGER NOT NULL,
        hp INTEGER NOT NULL,
        gold INTEGER DEFAULT 0
    )
    """
    create_table_npcs = """
    CREATE TABLE IF NOT EXISTS npcs (
        npc_id INTEGER PRIMARY KEY AUTOINCREMENT,
        npc_name VARCHAR(45) NOT NULL,
        dexterity INTEGER NOT NULL,
        strenght INTEGER NOT NULL,
        constitution INTEGER NOT NULL,
        intelligence INTEGER NOT NULL,
        wisdom INTEGER NOT NULL,
        charisma INTEGER NOT NULL,
        hp INTEGER NOT NULL,
        gold INTEGER DEFAULT 0
    )
    """
    return create_table_players, create_table_npcs

with sqlite3.connect(extras.sqlite_db) as conn:
    cursor = conn.cursor()

    create_table_players, create_table_npcs = create_tables()

    try:
        cursor.execute(create_table_players)
        cursor.execute(create_table_npcs)
        conn.commit()
    except sqlite3.Error as e:
        print("Erro SQLite:", e)
        conn.rollback()

def create_player_db(player_dict):
    missing_information = 'Estão faltando informações para criar seu personagem. Em caso de dúvidas utilize o comando: ?h player'
    error_convert_int = 'Por favor, digite apenas números para os atributos.'
    name = ''
    dexterity = ''
    strenght = ''
    constitution = ''
    intelligence = ''
    wisdom = ''
    charisma = ''
    hp = ''
    gold = ''
    verify_cont = 0

    try: 
        for k, v in player_dict.items():
            if k.lower() == 'nome':
                name = v
                verify_cont += 1
            elif k.lower() == 'destreza':
                dexterity = int(v)
                verify_cont += 1
            elif k.lower() == 'força':
                strenght = int(v)
                verify_cont += 1
            elif k.lower() == 'constituição':
                constitution = int(v)
                verify_cont += 1
            elif k.lower() == 'inteligência':
                intelligence = int(v)
                verify_cont += 1
            elif k.lower() == 'sabedoria':
                wisdom = int(v)
                verify_cont += 1
            elif k.lower() == 'carisma':
                charisma = int(v)
                verify_cont += 1
            elif k.lower() == 'hp':
                hp = int(v)
                verify_cont += 1
            elif k.lower() == 'ouro':
                gold = int(v)
    except Exception as e:
        print(e)
        return error_convert_int
    
    if verify_cont != 8:
        return missing_information
    elif gold == '':
        insert_player = f"""
        INSERT INTO players (player_name, dexterity, strenght, constitution, intelligence, wisdom, charisma, hp) VALUES ('{name}', {dexterity}, {strenght}, {constitution}, {intelligence}, {wisdom}, {charisma}, {hp})
        """
    else:
        insert_player = f"""
        INSERT INTO players (player_name, dexterity, strenght, constitution, intelligence, wisdom, charisma, hp, gold) VALUES ('{name}', {dexterity}, {strenght}, {constitution}, {intelligence}, {wisdom}, {charisma}, {hp}, {gold})
        """
    save_db = execute_sqlite_commands(insert_player)
    
    if save_db == True:
        return True
    else:
        return save_db

def update_player_db(upd_dict):
    error_convert_int = 'Por favor, digite apenas números para os atributos e ID.'
    error_missing_id = 'Por favor, preciso saber qual o ID do personagem.'
    update_player = 'UPDATE players SET '
    attr_to_update = []
    player_id = ''


    for k, v in upd_dict.items():
        if k.lower() == 'id':
            player_id = v
    
    if player_id == '':
        return error_missing_id
    else:
        try:
            player_id = int(player_id)
            for k, v in upd_dict.items():
                if k.lower() == 'nome':
                    name_upd = f"player_name = '{v}'"
                    attr_to_update.append(name_upd)
                elif k.lower() == 'destreza':
                    dexterity = int(v)
                    dex_upd = f"dexterity = {dexterity}"
                    attr_to_update.append(dex_upd)
                elif k.lower() == 'força':
                    strenght = int(v)
                    str_upd = f"strenght = {strenght}"
                    attr_to_update.append(str_upd)
                elif k.lower() == 'constituição':
                    constitution = int(v)
                    cons_upd = f"constitution = {constitution}"
                    attr_to_update.append(cons_upd)
                elif k.lower() == 'inteligência':
                    intelligence = int(v)
                    int_upd = f"intelligence = {intelligence}"
                    attr_to_update.append(int_upd)
                elif k.lower() == 'sabedoria':
                    wisdom = int(v)
                    wis_upd = f"wisdom = {wisdom}"
                    attr_to_update.append(wis_upd)
                elif k.lower() == 'carisma':
                    charisma = int(v)
                    char_upd = f"charisma = {charisma}"
                    attr_to_update.append(char_upd)
                elif k.lower() == 'hp':
                    hp = int(v)
                    hp_upd = f"hp = {hp}"
                    attr_to_update.append(hp_upd)
                elif k.lower() == 'ouro':
                    gold = int(v)
                    gold_upd = f"gold = {gold}"
                    attr_to_update.append(gold_upd)
        except Exception as e:
            print(e)
            return error_convert_int
        
        update_player_command = update_player

        for i,v in enumerate(attr_to_update):
            if i == len(attr_to_update)- 1:
                update_player_command += v
            else:
                update_player_command += v + ', '
        
        update_player_command += f" WHERE player_id = {player_id}"

        save_db = execute_sqlite_commands(update_player_command)

        if save_db == True:
            return True
        else:
            return save_db

def create_npc_db(npc_dict):
    missing_information = 'Estão faltando informações para criar seu NPC. Em caso de dúvidas utilize o comando: ?h npc'
    error_convert_int = 'Por favor, digite apenas números para os atributos.'
    name = ''
    dexterity = ''
    strenght = ''
    constitution = ''
    intelligence = ''
    wisdom = ''
    charisma = ''
    hp = ''
    gold = ''
    verify_cont = 0

    try: 
        for k, v in npc_dict.items():
            if k.lower() == 'nome':
                name = v
                verify_cont += 1
            elif k.lower() == 'destreza':
                dexterity = int(v)
                verify_cont += 1
            elif k.lower() == 'força':
                strenght = int(v)
                verify_cont += 1
            elif k.lower() == 'constituição':
                constitution = int(v)
                verify_cont += 1
            elif k.lower() == 'inteligência':
                intelligence = int(v)
                verify_cont += 1
            elif k.lower() == 'sabedoria':
                wisdom = int(v)
                verify_cont += 1
            elif k.lower() == 'carisma':
                charisma = int(v)
                verify_cont += 1
            elif k.lower() == 'hp':
                hp = int(v)
                verify_cont += 1
            elif k.lower() == 'ouro':
                gold = int(v)
    except Exception as e:
        print(e)
        return error_convert_int
    
    if verify_cont != 8:
        return missing_information
    elif gold == '':
        insert_npc = f"""
        INSERT INTO npcs (npc_name, dexterity, strenght, constitution, intelligence, wisdom, charisma, hp) VALUES ('{name}', {dexterity}, {strenght}, {constitution}, {intelligence}, {wisdom}, {charisma}, {hp})
        """
    else:
        insert_npc = f"""
        INSERT INTO npcs (npc_name, dexterity, strenght, constitution, intelligence, wisdom, charisma, hp, gold) VALUES ('{name}', {dexterity}, {strenght}, {constitution}, {intelligence}, {wisdom}, {charisma}, {hp}, {gold})
        """
    save_db = execute_sqlite_commands(insert_npc)
    
    if save_db == True:
        return True
    else:
        return save_db

def execute_sqlite_commands(cmd):
    error_msg = "Houve um erro ao salvar no banco de dados."
    
    with sqlite3.connect(extras.sqlite_db) as conn:
        cursor = conn.cursor()

        try:
            cursor.execute(cmd)
            conn.commit()
            return True
        except sqlite3.Error as e:
            print("Erro SQLite:", e)
            conn.rollback()
            return error_msg

def execute_sqlite_select(cmd):
    error_msg = "Houve um erro ao efetuar a busca no banco de dados."
    
    with sqlite3.connect(extras.sqlite_db) as conn:
        cursor = conn.cursor()

        try:
            cursor.execute(cmd)
            return cursor.fetchall()        
        except sqlite3.Error as e:
            print("Erro SQLite:", e)
            return error_msg