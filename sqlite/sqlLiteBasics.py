import sqlite3

DB_NAME: str = './accounts.db'
DB_TABLE: str = 'account' 
DB_CONN: sqlite3.Connection = sqlite3.connect(DB_NAME)
DB_CUR:sqlite3.Cursor = DB_CONN.cursor()

#Lets find out if the table exists
DB_CUR.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{DB_TABLE}';")

if DB_CUR.fetchone() is None:
    print(f"Table '{DB_TABLE}' exists")


    #create table
    DB_CUR.execute(f'''CREATE TABLE IF NOT EXISTS {DB_TABLE}(
                   account_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   owner_name VARCHAR(255) NOT NULL, 
                   balance NUMBER NOT NULL,
                   city TEXT NOT NULL)
                   ''')

    #insert row data:
    DB_CUR.execute(
        f'''
        INSERT INTO {DB_TABLE} 
        ( account_id, owner_name, balance, city )
        VALUES (NULL,'John Doe', 1000, 'New York');
    ''')

    DB_CUR.execute(
        f'''
        INSERT INTO {DB_TABLE} 
        ( account_id, owner_name, balance, city )
        VALUES (NULL,'Jane Doe', 2000, 'Lahti');
    ''')
    
    DB_CONN.commit()

DB_CUR.execute(
    f'''SELECT * FROM {DB_TABLE};
    ''')

# #prints all in list of tupples format
# print(DB_CUR.fetchall())

sqlItems = DB_CUR.fetchall()

for row in sqlItems:
    # print(row)
    print(f'Account ID: {row[0]}')
    print(f'Owner: {row[1]}')
    print(f'Balance: {row[2]}')
    print(f'City: {row[3]}')
    print("")


DB_CONN.close()
# VIDEON KOHTA 1:57
