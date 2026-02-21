from db_conn import DB_CONN, DB_CUR
from product import Product


class MenuProduct:
    
    def __init__(self) -> None:
        return None
    
    @staticmethod
    def showOptions() -> None:
        print("Options:")
        print("1 - Add product")
        print("2 - Show products")
        print("0 - Exit")
        return None

    def run(self) -> None:
        while True:
            self.showOptions()
            userSelection: int = self.askChoice()
            match userSelection:
                case 0:
                    break
                case 1:
                    self.add_product()
                case 2:
                    self.show_products()

        DB_CONN.close()
        return None

    def add_product(self) -> None:
        product: Product = Product.createProduct()
        product.insertDB()
        return None


    def show_products(self):
        print("No., Manufacturer, Brand, Cost, Price")
        products: list[Product] = Product.queryProducts()
        for index, product in enumerate(products, start=1):
            print(f"{index}, {product.manufacturer}, {product.brand}, {product.cost}, {product.price}")
        DB_CONN.commit()
        print()
        return None


    def askChoice(self) -> int:    
        userSelection = input("Your choice: ")
        return int(userSelection)