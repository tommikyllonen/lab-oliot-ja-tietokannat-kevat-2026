from db_conn import DB_CONN, DB_CUR

class Main:
    PRODUCT_TABLE_STATEMENT = f'''
                       CREATE TABLE IF NOT EXISTS product(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       manufacturer VARCHAR(255) NOT NULL,
                       brand VARCHAR(255) NOT NULL, 
                       cost REAL NOT NULL,
                       price REAL NOT NULL)
                       '''
    def __init__(self)-> None:
        print("Program starting.")
        #create table
        DB_CUR.execute(self.PRODUCT_TABLE_STATEMENT)
        DB_CONN.commit()
        DB_CONN.close()
        print("Program ending.")

        return None


if __name__ == "__main__":
    Main()

