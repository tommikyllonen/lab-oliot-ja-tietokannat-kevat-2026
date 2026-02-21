from pathlib import Path
import sqlite3

DB_FILEPATH = Path('./dev.db')
DB_CONN: sqlite3.Connection = sqlite3.connect(str(DB_FILEPATH))
DB_CUR:sqlite3.Cursor = DB_CONN.cursor()
PRODUCT_TABLE_STATEMENT = f'''
                   CREATE TABLE IF NOT EXISTS product(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   manufacturer VARCHAR(255) NOT NULL,
                   brand VARCHAR(255) NOT NULL, 
                   cost REAL NOT NULL,
                   price REAL NOT NULL)
                   '''
DB_CUR.execute(PRODUCT_TABLE_STATEMENT)
DB_CONN.commit()