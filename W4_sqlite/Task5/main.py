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
        from db_conn import DB_CONN, DB_CUR
        print("Program starting.")
        print("Insert product details below:")
        # Get parameters: 
        manufacturer: str = input("- Insert manufacturer: ")
        brand: str = input("- Insert brand: ")
        cost: float = float(input("- Insert cost: "))
        price: float = float(input("- Insert price: "))
        parameters = {"manufacturer": manufacturer, "brand": brand, "cost": cost, "price": price}


        # #create table
        DB_CUR.execute(self.PRODUCT_TABLE_STATEMENT)
        print("Storing product details into the database...")
        DB_CUR.execute("INSERT INTO product (manufacturer, brand, cost, price) VALUES (:manufacturer, :brand, :cost, :price)", parameters)
        DB_CONN.commit()
        # DB_CONN.close() # dont close, or the tests wont pass!!!!
        print("Program ending.")
        return None


if __name__ == "__main__":

    Main()

