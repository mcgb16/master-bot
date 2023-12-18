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
            if k == 'nome':
                name = v
                verify_cont += 1
            elif k == 'destreza':
                dexterity = int(v)
                verify_cont += 1
            elif k == 'força':
                strenght = int(v)
                verify_cont += 1
            elif k == 'constituição':
                constitution = int(v)
                verify_cont += 1
            elif k == 'inteligência':
                intelligence = int(v)
                verify_cont += 1
            elif k == 'sabedoria':
                wisdom = int(v)
                verify_cont += 1
            elif k == 'carisma':
                charisma = int(v)
                verify_cont += 1
            elif k == 'hp':
                hp = int(v)
                verify_cont += 1
            elif k == 'ouro':
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
    pass

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
            if k == 'nome':
                name = v
                verify_cont += 1
            elif k == 'destreza':
                dexterity = int(v)
                verify_cont += 1
            elif k == 'força':
                strenght = int(v)
                verify_cont += 1
            elif k == 'constituição':
                constitution = int(v)
                verify_cont += 1
            elif k == 'inteligência':
                intelligence = int(v)
                verify_cont += 1
            elif k == 'sabedoria':
                wisdom = int(v)
                verify_cont += 1
            elif k == 'carisma':
                charisma = int(v)
                verify_cont += 1
            elif k == 'hp':
                hp = int(v)
                verify_cont += 1
            elif k == 'ouro':
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