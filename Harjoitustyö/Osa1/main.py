from db_conn import DB_CONN
from menu_note import MenuNote
import sqlite3
class Main:
    def __init__(self) -> None:
        print("Program starting.")
        cursor:sqlite3.Cursor = DB_CONN.cursor()

        menu:MenuNote = MenuNote()
        menu.activate()

        DB_CONN.close()
        print("Program ending.")
        return None


if __name__ == "__main__":
    app:Main = Main()