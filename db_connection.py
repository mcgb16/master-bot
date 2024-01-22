import sqlite3
import extras
import add_ons

# Métodos iniciais

def create_tables():
    create_table_players = """
    CREATE TABLE IF NOT EXISTS players (
        player_id INTEGER PRIMARY KEY AUTOINCREMENT,
        player_name VARCHAR(45) NOT NULL,
        dexterity INTEGER NOT NULL,
        strength INTEGER NOT NULL,
        constitution INTEGER NOT NULL,
        intelligence INTEGER NOT NULL,
        wisdom INTEGER NOT NULL,
        charisma INTEGER NOT NULL,
        hp INTEGER NOT NULL,
        gold INTEGER DEFAULT 0,
        owner VARCHAR(18)
    )
    """
    create_table_npcs = """
    CREATE TABLE IF NOT EXISTS npcs (
        npc_id INTEGER PRIMARY KEY AUTOINCREMENT,
        npc_name VARCHAR(45) NOT NULL,
        dexterity INTEGER NOT NULL,
        strength INTEGER NOT NULL,
        constitution INTEGER NOT NULL,
        intelligence INTEGER NOT NULL,
        wisdom INTEGER NOT NULL,
        charisma INTEGER NOT NULL,
        hp INTEGER NOT NULL,
        gold INTEGER DEFAULT 0,
        owner VARCHAR(18)
    )
    """
    create_table_items = """
    CREATE TABLE IF NOT EXISTS items (
        item_id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_name VARCHAR(45) NOT NULL,
        id_npc INTEGER,
        id_player INTEGER,
        owner VARCHAR(18),
        FOREIGN KEY (id_npc) REFERENCES npcs (npc_id),
        FOREIGN KEY (id_player) REFERENCES players (player_id)
    )
    """
    create_table_weapons = """
    CREATE TABLE IF NOT EXISTS weapons (
        weapon_id INTEGER PRIMARY KEY AUTOINCREMENT,
        weapon_name VARCHAR(45) NOT NULL,
        damage integer NOT NULL,
        damage_type VARCHAR (45) NOT NULL,
        id_npc INTEGER,
        id_player INTEGER,
        owner VARCHAR(18),
        FOREIGN KEY (id_npc) REFERENCES npcs (npc_id),
        FOREIGN KEY (id_player) REFERENCES players (player_id)
    )
    """
    return create_table_players, create_table_npcs, create_table_items, create_table_weapons

with sqlite3.connect(extras.sqlite_db) as conn:
    activate_fk = "PRAGMA foreign_keys = ON;"
    cursor = conn.cursor()

    create_table_players, create_table_npcs, create_table_items, create_table_weapons = create_tables()

    try:
        cursor.execute(activate_fk)
        cursor.execute(create_table_players)
        cursor.execute(create_table_npcs)
        cursor.execute(create_table_items)
        cursor.execute(create_table_weapons)
        conn.commit()
    except sqlite3.Error as e:
        print("Erro SQLite:", e)
        conn.rollback()

# Player

def create_player_db(player_dict):
    missing_information = 'Estão faltando informações para criar seu personagem. Em caso de dúvidas utilize o comando: ?h player'
    error_convert_int = 'Por favor, digite apenas números para os atributos.'
    name = ''
    dexterity = ''
    strength = ''
    constitution = ''
    intelligence = ''
    wisdom = ''
    charisma = ''
    hp = ''
    gold = ''
    verify_cont = 0

    try: 
        for k, v in player_dict.items():
            if k.lower() in add_ons.name:
                name = v
                verify_cont += 1
            elif k.lower() in add_ons.dexterity:
                dexterity = int(v)
                verify_cont += 1
            elif k.lower() in add_ons.strength:
                strength = int(v)
                verify_cont += 1
            elif k.lower() in add_ons.constitution:
                constitution = int(v)
                verify_cont += 1
            elif k.lower() in add_ons.intelligence:
                intelligence = int(v)
                verify_cont += 1
            elif k.lower() in add_ons.wisdom:
                wisdom = int(v)
                verify_cont += 1
            elif k.lower() in add_ons.charisma:
                charisma = int(v)
                verify_cont += 1
            elif k.lower() in add_ons.hp:
                hp = int(v)
                verify_cont += 1
            elif k.lower() in add_ons.gold:
                gold = int(v)
    except Exception as e:
        print(e)
        return error_convert_int
    
    if verify_cont != 8:
        return missing_information
    elif gold == '':
        insert_player = f"""
        INSERT INTO players (player_name, dexterity, strength, constitution, intelligence, wisdom, charisma, hp) VALUES ('{name}', {dexterity}, {strength}, {constitution}, {intelligence}, {wisdom}, {charisma}, {hp})
        """
    else:
        insert_player = f"""
        INSERT INTO players (player_name, dexterity, strength, constitution, intelligence, wisdom, charisma, hp, gold) VALUES ('{name}', {dexterity}, {strength}, {constitution}, {intelligence}, {wisdom}, {charisma}, {hp}, {gold})
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
        if k.lower() in add_ons.id_values:
            player_id = v
    
    if player_id == '':
        return error_missing_id
    else:
        try:
            player_id = int(player_id)
            for k, v in upd_dict.items():
                if k.lower() in add_ons.name:
                    name_upd = f"player_name = '{v}'"
                    attr_to_update.append(name_upd)
                elif k.lower() in add_ons.dexterity:
                    dexterity = int(v)
                    dex_upd = f"dexterity = {dexterity}"
                    attr_to_update.append(dex_upd)
                elif k.lower() in add_ons.strength:
                    strength = int(v)
                    str_upd = f"strength = {strength}"
                    attr_to_update.append(str_upd)
                elif k.lower() in add_ons.constitution:
                    constitution = int(v)
                    cons_upd = f"constitution = {constitution}"
                    attr_to_update.append(cons_upd)
                elif k.lower() in add_ons.intelligence:
                    intelligence = int(v)
                    int_upd = f"intelligence = {intelligence}"
                    attr_to_update.append(int_upd)
                elif k.lower() in add_ons.wisdom:
                    wisdom = int(v)
                    wis_upd = f"wisdom = {wisdom}"
                    attr_to_update.append(wis_upd)
                elif k.lower() in add_ons.charisma:
                    charisma = int(v)
                    char_upd = f"charisma = {charisma}"
                    attr_to_update.append(char_upd)
                elif k.lower() in add_ons.hp:
                    hp = int(v)
                    hp_upd = f"hp = {hp}"
                    attr_to_update.append(hp_upd)
                elif k.lower() in add_ons.gold:
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

# NPC

def create_npc_db(npc_dict):
    missing_information = 'Estão faltando informações para criar seu NPC. Em caso de dúvidas utilize o comando: ?h npc'
    error_convert_int = 'Por favor, digite apenas números para os atributos.'
    name = ''
    dexterity = ''
    strength = ''
    constitution = ''
    intelligence = ''
    wisdom = ''
    charisma = ''
    hp = ''
    gold = ''
    verify_cont = 0

    try: 
        for k, v in npc_dict.items():
            if k.lower() in add_ons.name:
                name = v
                verify_cont += 1
            elif k.lower() in add_ons.dexterity:
                dexterity = int(v)
                verify_cont += 1
            elif k.lower() in add_ons.strength:
                strength = int(v)
                verify_cont += 1
            elif k.lower() in add_ons.constitution:
                constitution = int(v)
                verify_cont += 1
            elif k.lower() in add_ons.intelligence:
                intelligence = int(v)
                verify_cont += 1
            elif k.lower() in add_ons.wisdom:
                wisdom = int(v)
                verify_cont += 1
            elif k.lower() in add_ons.charisma:
                charisma = int(v)
                verify_cont += 1
            elif k.lower() in add_ons.hp:
                hp = int(v)
                verify_cont += 1
            elif k.lower() in add_ons.gold:
                gold = int(v)
    except Exception as e:
        print(e)
        return error_convert_int
    
    if verify_cont != 8:
        return missing_information
    elif gold == '':
        insert_npc = f"""
        INSERT INTO npcs (npc_name, dexterity, strength, constitution, intelligence, wisdom, charisma, hp) VALUES ('{name}', {dexterity}, {strength}, {constitution}, {intelligence}, {wisdom}, {charisma}, {hp})
        """
    else:
        insert_npc = f"""
        INSERT INTO npcs (npc_name, dexterity, strength, constitution, intelligence, wisdom, charisma, hp, gold) VALUES ('{name}', {dexterity}, {strength}, {constitution}, {intelligence}, {wisdom}, {charisma}, {hp}, {gold})
        """
    save_db = execute_sqlite_commands(insert_npc)
    
    if save_db == True:
        return True
    else:
        return save_db

def update_npc_db(upd_dict):
    error_convert_int = 'Por favor, digite apenas números para os atributos e ID.'
    error_missing_id = 'Por favor, preciso saber qual o ID do NPC.'
    update_npc = 'UPDATE npcs SET '
    attr_to_update = []
    npc_id = ''


    for k, v in upd_dict.items():
        if k.lower() == 'id':
            npc_id = v
    
    if npc_id == '':
        return error_missing_id
    else:
        try:
            npc_id = int(npc_id)
            for k, v in upd_dict.items():
                if k.lower() in add_ons.name:
                    name_upd = f"npc_name = '{v}'"
                    attr_to_update.append(name_upd)
                elif k.lower() in add_ons.dexterity:
                    dexterity = int(v)
                    dex_upd = f"dexterity = {dexterity}"
                    attr_to_update.append(dex_upd)
                elif k.lower() in add_ons.strength:
                    strength = int(v)
                    str_upd = f"strength = {strength}"
                    attr_to_update.append(str_upd)
                elif k.lower() in add_ons.constitution:
                    constitution = int(v)
                    cons_upd = f"constitution = {constitution}"
                    attr_to_update.append(cons_upd)
                elif k.lower() in add_ons.intelligence:
                    intelligence = int(v)
                    int_upd = f"intelligence = {intelligence}"
                    attr_to_update.append(int_upd)
                elif k.lower() in add_ons.wisdom:
                    wisdom = int(v)
                    wis_upd = f"wisdom = {wisdom}"
                    attr_to_update.append(wis_upd)
                elif k.lower() in add_ons.charisma:
                    charisma = int(v)
                    char_upd = f"charisma = {charisma}"
                    attr_to_update.append(char_upd)
                elif k.lower() in add_ons.hp:
                    hp = int(v)
                    hp_upd = f"hp = {hp}"
                    attr_to_update.append(hp_upd)
                elif k.lower() in add_ons.gold:
                    gold = int(v)
                    gold_upd = f"gold = {gold}"
                    attr_to_update.append(gold_upd)
        except Exception as e:
            print(e)
            return error_convert_int
        
        update_npc_command = update_npc

        for i,v in enumerate(attr_to_update):
            if i == len(attr_to_update)- 1:
                update_npc_command += v
            else:
                update_npc_command += v + ', '
        
        update_npc_command += f" WHERE npc_id = {npc_id}"

        save_db = execute_sqlite_commands(update_npc_command)

        if save_db == True:
            return True
        else:
            return save_db

# Item

def create_item_db(item_dict):
    missing_information = 'Estão faltando informações para criar seu Item. Em caso de dúvidas utilize o comando: ?h item'
    name = ''
    verify_cont = 0

    for k, v in item_dict.items():
        if k.lower() in add_ons.name:
            name = v
            verify_cont += 1            

    if verify_cont != 1:
        return missing_information
    else:
        insert_item = f"""
        INSERT INTO items (item_name) VALUES ('{name}')
        """

    save_db = execute_sqlite_commands(insert_item)

    if save_db == True:
        return True
    else:
        return save_db

def update_item_db(upd_dict):
    error_convert_int = 'Por favor, digite apenas números para o ID.'
    error_missing_id = 'Por favor, preciso saber qual o ID do Item.'
    update_item = 'UPDATE items SET '
    attr_to_update = []
    item_id = ''


    for k, v in upd_dict.items():
        if k.lower() == 'id':
            item_id = v
    
    if item_id == '':
        return error_missing_id
    else:
        try:
            item_id = int(item_id)
            for k, v in upd_dict.items():
                if k.lower() in add_ons.name:
                    name_upd = f"item_name = '{v}'"
                    attr_to_update.append(name_upd)
        except Exception as e:
            print(e)
            return error_convert_int
        
        update_item_command = update_item

        for i,v in enumerate(attr_to_update):
            if i == len(attr_to_update)- 1:
                update_item_command += v
            else:
                update_item_command += v + ', '
        
        update_item_command += f" WHERE item_id = {item_id}"

        save_db = execute_sqlite_commands(update_item_command)

        if save_db == True:
            return True
        else:
            return save_db

# Arma

def create_weapon_db(weapon_dict):
    missing_information = 'Estão faltando informações para criar sua arma. Em caso de dúvidas utilize o comando: ?h weapon'
    error_convert_int = 'Por favor, digite apenas números para o dano.'
    name = ''
    dmg = ''
    dmg_type = ''
    verify_cont = 0
    try:
        for k, v in weapon_dict.items():
            if k.lower() in add_ons.name:
                name = v
                verify_cont += 1
            elif k.lower() in add_ons.dmg:
                dmg = int(v)
                verify_cont += 1
            elif k.lower() in add_ons.dmg_type:
                dmg_type = v
                verify_cont += 1
    except Exception as e:
        print(e)
        return error_convert_int

    if verify_cont != 3:
        return missing_information
    else:
        insert_weapon = f"""
        INSERT INTO weapons (weapon_name, damage, damage_type) VALUES ('{name}', '{dmg}', '{dmg_type}')
        """

    save_db = execute_sqlite_commands(insert_weapon)

    if save_db == True:
        return True
    else:
        return save_db

def update_weapon_db(upd_dict):
    error_convert_int = 'Por favor, digite apenas números para o dano e ID.'
    error_missing_id = 'Por favor, preciso saber qual o ID da Arma.'
    update_weapon = 'UPDATE weapons SET '
    attr_to_update = []
    weapon_id = ''


    for k, v in upd_dict.items():
        if k.lower() == 'id':
            weapon_id = v
    
    if weapon_id == '':
        return error_missing_id
    else:
        try:
            weapon_id = int(weapon_id)
            for k, v in upd_dict.items():
                if k.lower() in add_ons.name:
                    name_upd = f"weapon_name = '{v}'"
                    attr_to_update.append(name_upd)
                elif k.lower() in add_ons.dmg:
                    dmg = int(v)
                    dmg_upd = f"damage = '{dmg}'"
                    attr_to_update.append(dmg_upd)
                elif k.lower() in add_ons.dmg_type:
                    dmg_type_upd = f"damage_type = '{v}'"
                    attr_to_update.append(dmg_type_upd)
        except Exception as e:
            print(e)
            return error_convert_int
        
        update_weapon_command = update_weapon

        for i,v in enumerate(attr_to_update):
            if i == len(attr_to_update)- 1:
                update_weapon_command += v
            else:
                update_weapon_command += v + ', '
        
        update_weapon_command += f" WHERE weapon_id = {weapon_id}"

        save_db = execute_sqlite_commands(update_weapon_command)

        if save_db == True:
            return True
        else:
            return save_db

# Métodos Gerais

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