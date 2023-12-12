import mysql.connector
import extras

conn = mysql.connector.connect(
    host=extras.mysql_host,
    user=extras.mysql_user,
    password=extras.mysql_pswd,
    database=extras.mysql_db
)
cursor = conn.cursor()

def create_tables():
    create_table_players = """
    CREATE TABLE IF NOT EXISTS players (
        player_id int NOT NULL AUTO_INCREMENT,
        player_name varchar(45) NOT NULL,
        dexterity int NOT NULL,
        strenght int NOT NULL,
        constitution int NOT NULL,
        intelligence int NOT NULL,
        wisdom int NOT NULL,
        charisma int NOT NULL,
        hp int NOT NULL,
        gold int DEFAULT 0,
        PRIMARY KEY (player_id),
        UNIQUE KEY player_id_UNIQUE (player_id)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
    """
    create_table_npcs = """
    CREATE TABLE IF NOT EXISTS npcs (
        npc_id int NOT NULL AUTO_INCREMENT,
        npc_name varchar(45) NOT NULL,
        dexterity int NOT NULL,
        strenght int NOT NULL,
        constitution int NOT NULL,
        intelligence int NOT NULL,
        wisdom int NOT NULL,
        charisma int NOT NULL,
        hp int NOT NULL,
        gold int DEFAULT 0,
        PRIMARY KEY (npc_id),
        UNIQUE KEY npc_id_UNIQUE (npc_id)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
    """
    try:
        cursor.execute(create_table_players)
        cursor.execute(create_table_npcs)
        conn.commit()
        return
    except Exception as e:
        print(e)
        conn.rollback()
        return

create_tables()

cursor.close()
conn.close()
