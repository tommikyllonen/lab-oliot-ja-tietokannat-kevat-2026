from db import Db
from sqlite3 import Connection, Cursor
from owner import Owner


class Main:
    CARS_DB = "cars.db"

    def __init__(self):
        self.CARS_DB
        self.CREATE_OWNER_TABLE = "car_owner_create.sql"
        self.CREATE_CAR_TABLE = "car_create.sql"
        self.CREATE_ENGINE_TABLE = "engine_create.sql"

        self.db: Db = Db(self.CARS_DB)  # This created the cars.db database file

        self.conn: Connection = self.db.connect()
        if self.conn:
            self.create_tables()
            self.main_menu()
            self.db.close()

    def create_tables(self) -> None:
        with open(self.CREATE_OWNER_TABLE) as file:
            sql: str = file.read()
            self.db.execute(sql, ())
        with open(self.CREATE_CAR_TABLE) as file:
            sql: str = file.read()
            self.db.execute(sql, ())
        with open(self.CREATE_ENGINE_TABLE) as file:
            sql: str = file.read()
            self.db.execute(sql, ())
        return None

    def strInput(self, prompt: str, default: str) -> str:
        s: str = input(f"{prompt} or <enter> for default: '{default}': ").strip()
        if s == "":
            return default
        return s

    def intInput(self, prompt: str, default: int) -> int:
        while True:
            try:

                s:str = input(f"{prompt} or <enter> for default: '{default}': ").strip()
                if s == "":
                    return default
                return int(s)
            except ValueError:
                print("invalid input!")

    def add_owner(self) -> None:
        fname: str = self.strInput("Owner fname", "Keijo")
        lname: str = self.strInput("Owner lname", "Rosberg")
        email: str = self.strInput("Owner email", "keijo@rosberg.com")
        sql: str = "INSERT INTO owner (fname, lname, email) VALUES(?,?,?);"
        cursor: Cursor = self.db.execute(sql, (fname, lname, email))
        if cursor:
            print(f"Owner{fname} {lname} {email} added. Rows affected: {cursor.rowcount}")
        else:
            print("Owner not added!")
        return None
        

    def main_menu(self) -> None:
        while True:
            print("Main menu")
            print("1. List Owners")
            print("2. Add Owner")
            print("3. Remove Owner")
            print("x. Exit")
            choice = input("Enter choice: ").lower()
            match choice:

                case "1":
                    self.list_owners()
                case "2":
                    self.add_owner()
                case "3":
                    print("remove owner...")
                case "x":
                    print("Goodbye")
                    break
                case _:  # Under score means anything
                    print("invalid choice")

    def list_owners(self):
        print("listing owners")
        sql: str = "SELECT id, fname, lname, email, created_at FROM owner"
        params: tuple[str] = ()
        cursor: Cursor = self.db.execute(sql, params)
        if cursor:
            rows = cursor.fetchall()
            if len(rows) == 0:
                print("No owners found!")
            else:
                for row in rows:
                    id, fname, lname, email, created_at = row  # FASTER WAY TO: id = row[0] fname = row[1] lname = row[2] email = row[3] created_at = row[4]
                    owner: Owner = Owner(fname, lname, email)
                    print(f"id: {id} {owner} {created_at}")
        else:
            print("Error listing owners!")




if __name__ == "__main__":
    app: Main = Main()
