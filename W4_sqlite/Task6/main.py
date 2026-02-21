from db_conn import DB_CONN, DB_CUR
from menu import Menu

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
        
        menu: Menu = Menu()
        while True:
            userSelection: int = menu.menu()

            match userSelection:
                case 0:
                    break
                case 1:
                    self.add_product()
                case 2:
                    self.show_products()
        DB_CONN.close()
        print("Program ending.")
        return None
     
    def add_product(self):

        print("Insert product details below:")
        # Get parameters: 
        manufacturer: str = input("- Insert manufacturer: ")
        brand: str = input("- Insert brand: ")
        cost: float = float(input("- Insert cost: "))
        price: float = float(input("- Insert price: "))
        parameters = {"manufacturer": manufacturer, "brand": brand, "cost": cost, "price": price}

        #create table
        DB_CUR.execute(self.PRODUCT_TABLE_STATEMENT)

        print("Adding product...")
        DB_CUR.execute("INSERT INTO product (manufacturer, brand, cost, price) VALUES (:manufacturer, :brand, :cost, :price)", parameters)
        print("Product added!\n")
        DB_CONN.commit()
        return None


    def show_products(self):
        
        #create table
        DB_CUR.execute(self.PRODUCT_TABLE_STATEMENT)

        # Get column names
        DB_CUR.execute("SELECT name FROM pragma_table_info('product')")
        column_names = DB_CUR.fetchall()
        column_name_string = ""
        for column_name in column_names:
            column_name_string += column_name[0].capitalize() + ", "
        column_name_string = "No." + column_name_string[2:-2]
        print(column_name_string)

        # Get products
        DB_CUR.execute("SELECT * FROM product")
        products = DB_CUR.fetchall()
        for product in products:
            product_string = ""
            for attribute in product:
                product_string += str(attribute) + ", "
            product_string = product_string[:-2]
            print(product_string)
        print()

        DB_CONN.commit()
        return None




if __name__ == "__main__":

    Main()

