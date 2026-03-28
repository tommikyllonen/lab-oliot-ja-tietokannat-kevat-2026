from car import Car
from db import Db
from sqlite3 import Connection, Cursor
from engine import Engine
from owner import Owner


class Main:

    def __init__(self):
        self.CARS_DB = "cars.db"
        self.CREATE_OWNER_TABLE = "car_owner_create.sql"
        self.CREATE_CAR_TABLE = "car_create.sql"
        self.CREATE_ENGINE_TABLE = "engine_create.sql"

        self.db: Db = Db(self.CARS_DB)  # This created the cars.db database file
        # self.db: Db = Db("tommidb.db")  # This created the tommidb.db database file

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


    def main_menu(self) -> None:
        while True:
            print("Main menu")
            print("1. List Owners")
            print("2. Add Owner")
            print("3. Remove Owner")
            print("4. List Engines")
            print("5. Add Engine")
            print("6. Remove Engine")
            print("7. List Cars")
            print("8. Add Car")
            print("9. Remove Car")
            print("10. Add owner to car")
            print("x. Exit")
            choice = input("Enter choice: ").lower()
            match choice:

                case "1":
                    self.list_owners()
                case "2":
                    self.add_owner()
                case "3":
                    self.remove_owner()
                case "4":
                    self.list_engines()
                case "5":
                    self.add_engine()
                case "6":
                    self.remove_engine()
                    print("remove engine...")
                case "7":
                    self.list_cars()
                case "8":
                    self.add_car()
                case "9":
                    self.delete_car()
                case "10":
                    self.add_owner_to_car()
                case "x":
                    print("Goodbye")
                    break
                case _:  # Under score means anything
                    print("invalid choice")

    def check_id_in_table(self, table: str, id: int) -> bool:
        sql: str = f"SELECT id FROM {table} WHERE id=?"
        cursor: Cursor | None = self.db.execute(sql, (id,))
        if cursor:
            row = cursor.fetchone()#returns one row or None if no rows
            if row:
                return True
        return False
    
    def add_car(self) -> None:
        print ("Existing engines:")
        self.list_engines()
        engine_id: int = self.intInput("Existing engine ID", 1)
        if not self.check_id_in_table("engine", engine_id):
            print(f"Engine id {engine_id} not found! Car cannont be added!")
            return
        brand: str = self.strInput("Brand", "MB")
        model: str = self.strInput("Model", "C200")
        year: int = self.intInput("Year", 2019)
        color: str = self.strInput("Color", "black")
        car: Car = Car(brand, model, year, color, engine_id)
        sql: str = "INSERT INTO car (brand, model, year, color, engine_id) VALUES(?,?,?,?,?);"
        cursor: Cursor | None = self.db.execute(sql, (brand, model, year, color, engine_id))
        if cursor:
            print(f"Car '{car} added. Rows affected: {cursor.rowcount}'")
        else:
            print(f"Car '{car}' not added!")
        return None
    
    def delete_car(self) -> None:
        self.list_cars()
        id: int = self.intInput("Car id to delete", 1)
        # if not self.check_id_in_table("car", car_id):
        #     print(f"Car id '{car_id}' not found! Car cannot be deleted!")
        #     return None
        sql: str = "DELETE FROM car WHERE id=?"
        cursor: Cursor | None = self.db.execute(sql, (id,))
        if cursor:
            if cursor.rowcount > 0:
                print(f"Car '{id}' deleted")
            else:
                print(f"Car '{id}' not found!")
        else:
            print("Error in deleting car!")
        return None

    def add_engine(self) -> None:
        fuel: str = self.strInput("Engine fuel", "petrol")
        cc: int = self.intInput("cc", 2000)
        hp: int = self.intInput("hp", 150)
        engine: Engine = Engine(fuel, cc, hp)
        sql: str = "INSERT INTO engine (fuel, cc, hp) VALUES(?,?,?);"
        cursor: Cursor | None = self.db.execute(sql, (fuel, cc, hp))
        if cursor:
            print(f"Engine '{engine}' added. Rows affected: {cursor.rowcount}")
        else:
            print(f"Engine '{engine}' not added!")
        return None
    
    def list_engines(self) -> None:
        sql: str = "SELECT id, fuel, cc, hp FROM engine"
        cursor: Cursor = self.db.execute(sql, ())
        if cursor:
            rows = cursor.fetchall()
            if len(rows) == 0:
                print("No engines in db")
            else:
                for row in rows:
                    id, fuel, cc, hp = row
                    engine: Engine = Engine(fuel, cc, hp)
                    print(f"id: {id} {engine}")
        else:
            print("Error listing engines!")
        return None

    def remove_engine(self) -> None:
        self.list_engines()
        engine_id: int = self.intInput("Engine id to delete", 1)
        if not self.check_id_in_table("engine", engine_id):
            print(f"Engine id '{engine_id}' not found!")
            return None
        sql: str = "SELECT id FROM car WHERE engine_id=?"
        cursor: Cursor | None = self.db.execute(sql, (engine_id,))
        if cursor:
            rows = cursor.fetchall()
            row_count = len(rows)
            if row_count > 0:
                print(f"Engine id '{engine_id}' is in use by {row_count} cars. Cannot remove!")
                return None
        else:
            print("Error during engine removal!")
        sql: str = "DELETE FROM engine WHERE id=?"
        cursor: Cursor | None = self.db.execute(sql, (engine_id,))
        if cursor:
            print(f"Engine id '{engine_id}' removed. ")
        else:
            print(f"Error removing engine!" )
        return None

    def add_owner(self) -> None:
        fname: str = self.strInput("Owner fname", "Keijo")
        lname: str = self.strInput("Owner lname", "Rosberg")
        email: str = self.strInput("Owner email", "keijo@rosberg.com")
        sql: str = "INSERT INTO owner (fname, lname, email) VALUES(?,?,?);"
        cursor: Cursor | None = self.db.execute(sql, (fname, lname, email))
        if cursor is not None:
            print(f"Owner{fname} {lname} {email} added. Rows affected: {cursor.rowcount}")
        else:
            print("Owner not added!")
        return None

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

    def remove_owner(self) -> None:
        self.list_owners()
        owner_id: int = self.intInput("Owner id to delete", 1)

        if not self.check_id_in_table("owner", owner_id):
            print(f"owner id '{owner_id}' not found!")
            return None
        self.remove_owner_from_cars(owner_id)
        sql:str = "DELETE FROM owner WHERE id = ?"
        cursor: Cursor = self.db.execute(sql, (owner_id,))
        if cursor:
            print(f"owner removed from")
        else:
            print("Error removing owner!")


    def remove_owner_from_cars(self, owner_id:int) -> None:
        sql:str = "UPDATE car SET owner_id = NULL WHERE owner_id = ?"
        cursor: Cursor = self.db.execute(sql, (owner_id,))
        if cursor:
            print(f"owner removed from all '{cursor.rowcount}' cars")
        else:
            print("Error removing owner from cars!")



        return None

    def list_cars(self) -> None:
        # version1
        # sql: str = "SELECT * FROM car"
        # cursor: Cursor = self.db.execute(sql, ())
        # if cursor:
        #     rows = cursor.fetchall()
        #     if len(rows) == 0:
        #         print("No cars found!")
        #     else:
        #         for row in rows:
        #             id, brand, model, year, color, engine_id, owner_id = row
        #             car: Car = Car(brand, model, year, color, engine_id)
        #             print(f"Car: '{car}' cid {id} engine_id: {engine_id} oid: {owner_id}")
        # else:
        #     print("Error listing cars!")
        # return None


        # version2 with JOIN
        sql: str = """SELECT * FROM car c
                    JOIN engine e ON c.engine_id = e.id
                    LEFT JOIN owner o ON c.owner_id = o.id
                    """
        cursor: Cursor = self.db.execute(sql, ())
        if cursor:
            rows = cursor.fetchall()
            if len(rows) == 0:
                print("No cars found!")
                
            else: 
                for row in rows:
                    (car_id, brand, model, year, color, engine_fk_id, c_owner_id, engine_id, fuel, cc, hp,
                    owner_id, fname, lname, email, created_at) = row
                    car: Car = Car(brand, model, year, color, engine_id)
                    engine: Engine = Engine(fuel, cc, hp)
                    owner: Owner = Owner(fname, lname, email) 
                    print(f"Car [{car_id}]{car}] Engine [{engine_id}{engine}] Owner [{owner_id if owner_id else '-'} {owner if owner_id else '-'}]")
        else:
            print("Error listing cars!")      

        return None




    def add_owner_to_car(self) -> None:
        #todo list cars 
        car_id: int = self.intInput("Car id", 1)
        if not self.check_id_in_table("car", car_id):
            print(f"Car id '{car_id}' not found!")
            return None
        owner_id: int = self.intInput("Owner id", 1)
        if not self.check_id_in_table("owner", owner_id):
            print(f"Owner id '{owner_id}' not found!")
            return None
        sql: str = "UPDATE car SET owner_id=? WHERE id=?"
        cursor: Cursor | None = self.db.execute(sql, (owner_id, car_id))
        if cursor:
            print(f"Owner id '{owner_id}' added to car id '{car_id}'. Rows affected: {cursor.rowcount}")
        else:
            print(f"Owner id '{owner_id}' not added to car id '{car_id}'!")
        return None



if __name__ == "__main__":
    app: Main = Main()
