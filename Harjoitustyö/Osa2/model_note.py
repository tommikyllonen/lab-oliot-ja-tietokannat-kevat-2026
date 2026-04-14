from dataclasses import dataclass
from db_conn import DB_CONN
from sqlite3 import Cursor


@dataclass
class Note:
    id: int
    title: str
    content: str

class NoteDAO:
    def __init__(self) -> None:
        return None
    @staticmethod
    def addNote(title: str, content: str) -> None:
        try:
            sql = "INSERT INTO note (title, content) VALUES (?, ?)"
            inputs = (title, content)
            cursor: Cursor = DB_CONN.cursor()
            cursor.execute(sql, inputs)
            DB_CONN.commit()
            cursor.close()
            return None
        except Exception as e:
            print(f"Error while Inserting note.")
            return None
    @staticmethod # REMEMBER: static means no object creation needed for using this method !!therefore no self parameter!!
    def getNotes(limit:int = -1) -> list[Note]:
        notes: list[Note] = []
        cursor: Cursor = DB_CONN.cursor()
        sql = "SELECT id, title, content FROM note"
        cursor.execute(sql)
        records = cursor.fetchall()
        cursor.close()

        for record in records:
            note = Note(*record) # automatic mapper!!! BOOM!!!
            notes.append(note)

        return notes



