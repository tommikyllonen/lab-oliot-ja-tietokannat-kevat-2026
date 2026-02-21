from db_conn import DB_CONN, DB_CUR
class Product:
    def __init__(self, manufacturer: str, brand: str, cost: float, price: float) -> None:
        self.manufacturer = manufacturer
        self.brand = brand
        self.cost = cost
        self.price = price
        return None
    
    @staticmethod
    def createProduct() -> 'Product':
        print("Insert product details below:")
        # Get parameters: 
        manufacturer: str = input("- Insert manufacturer: ")
        brand: str = input("- Insert brand: ")
        cost: float = float(input("- Insert cost: "))
        price: float = float(input("- Insert price: "))
        newProduct:Product = Product(manufacturer, brand, cost, price)
        return newProduct

    def insertDB(self) -> None:
        print("Adding product...")
        parameters = {"manufacturer": self.manufacturer, "brand": self.brand, "cost": self.cost, "price": self.price}
        DB_CUR.execute("INSERT INTO product (manufacturer, brand, cost, price) VALUES (:manufacturer, :brand, :cost, :price)", parameters)
        print("Product added!\n")
        DB_CONN.commit()
        return None
    
    @staticmethod
    def queryProducts(products: 'list[Product]' = []) -> 'list[Product]':
        # Get products
        DB_CUR.execute("SELECT * FROM product")
        old_products: list[tuple] = DB_CUR.fetchall()
        # Fill the products list
        for product in old_products:
            temp_product = Product(product[1], product[2], product[3], product[4])
            products.append(temp_product)
        DB_CONN.commit()
        
        return products
