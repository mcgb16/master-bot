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
