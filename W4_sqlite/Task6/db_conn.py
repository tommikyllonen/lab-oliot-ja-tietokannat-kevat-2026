from pathlib import Path
import sqlite3

DB_FILEPATH = Path('./dev.db')
DB_CONN: sqlite3.Connection = sqlite3.connect(str(DB_FILEPATH))
DB_CUR:sqlite3.Cursor = DB_CONN.cursor()