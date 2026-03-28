from sqlite3 import Connection, Cursor, Error, connect


class Db:
    def __init__ (self, db_name:str) -> None:
        self.db_name:  str = db_name
        self.connection: Connection = None
        return None
    
    def connect(self) -> Connection:
        try:
            print(f"Connection to db: '{self.db_name}'")    
            self.connection = connect(self.db_name)
            print("Connected!")
        except Exception as e:
            print(f"Error connecting to {self.db_name}")
            print("Exception:", e)
        return self.connection
    
    def close(self) -> None:
        if self.connection:
            print("Closing connection...")
            self.connection.close()
            self.connection = None
            print("Connection closed")
    
    def execute(self, sql:str, params:tuple[str]) -> Cursor:
        if not self.connection:
            print("No connection")
            return None
        try:
            cursor:Cursor = self.connection.cursor()
            cursor.execute(sql, params)
            self.connection.commit()
            # no we return Cursor objectwhich can be used outside:
            # sql SELECT: cursor.fetchall(), cursor.fetchone()
            # sql INSERT, UPDATE & DELETE: cursor.rowcount (how many rows affected)
            return cursor
            
        except Error as e: # this is the Error that we inported
            print(f"Error executing '{sql}'")
            print("Error: ", e)
            return None



        return None