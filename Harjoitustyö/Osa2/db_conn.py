from pathlib import Path
import sqlite3
import sys

DB_FILEPATH = Path('./notes.db')
DB_CONN: sqlite3.Connection = sqlite3.connect(str(DB_FILEPATH))


class DB:
      def __init__(self) -> None:
        return None
      @staticmethod #static method means, you do not have to create an instance, you can use it inside the class
      def loadSqlScript(filepath: str) -> str:
        content = ""
        try:
            with open(filepath, 'r', encoding='UTF-8') as file:
                content = file.read()
        except Exception:
            print(f"Failed to read '{filepath}' file.")
            sys.exit(-1)
        return content

      @staticmethod
      def initializeDB() -> None:
         script: str = DB.loadSqlScript('setup.sql')
         DB_CONN.executescript(script)
         DB_CONN.commit()
         DB_CONN.close()