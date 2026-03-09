from db import Db
from sqlite3 import Connection
class Main:
    CARS_DB = "cars.db"
    def __init__(self):
         db:Db = Db(self.CARS_DB) # This created the cars.db database file
         conn:Connection = db.connect()
         if conn:
            self.main_menu()
            db.close()
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
                        print("owners...")
                   case "2":
                        print("add owner...")
                   case "3":
                        print("remove owner...")
                   case "x":
                        print("Goodbye")
                        break
                   case _: # Under score means anything
                        print("invalid choice")
    def list_owners(self):
         sql: str = "SELECT id, fname, lname, email, created_at FROM owner"
         params: tuple[str] = ()
         1:47:47 jäätiin tähän.
        # https://youtu.be/wcTSyNim8Wg?si=VRYQg0wLQLtOL_hJ

                        
if __name__ == "__main__":
     app:Main = Main()

