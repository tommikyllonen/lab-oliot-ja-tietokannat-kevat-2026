from pathlib import Path
import sqlite3

DB_FILEPATH = Path('./notes.db')
DB_CONN: sqlite3.Connection = sqlite3.connect(str(DB_FILEPATH))
# DB_CUR = DB_CONN.cursor()