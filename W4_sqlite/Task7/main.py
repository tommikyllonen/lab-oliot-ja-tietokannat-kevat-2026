from menu_product import MenuProduct
from db_conn import DB_CONN, DB_CUR, DB_FILEPATH

class Main:
    def __init__(self)-> None:
        print("Program starting.")
        menu: MenuProduct = MenuProduct()
        menu.run()
        print("Program ending.")
        return None
     




if __name__ == "__main__":

    Main()

