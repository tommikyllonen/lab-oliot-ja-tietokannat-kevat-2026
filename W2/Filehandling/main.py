from item import Item
from file_handler import FileHandler


class Main:
    def __init__(self):
        #add initial items
        print("------------------------ First round!!! ------------------------")
        items = [Item("Apple", 0.99), Item("Banana", 0.59), Item("Orange", 0.79)]
        file_handler = FileHandler("Shopping_cart.txt", separator=';')
        file_handler.write_file(items)

        read_items = file_handler.read_file()
        for item in read_items:
            print(f"{item.name}: ${item.price:.2f}")

        # Add Grapes
        print("------------------------ Second round!!! ------------------------")
        file_handler.append_to_file([Item("Grapes", 2.99)])
        read_items = file_handler.read_file()
        for item in read_items:
            print(f"{item.name}: ${item.price:.2f}")


        file_handler = FileHandler("Shopping_cart.txt", separator='!')
        read_items = file_handler.read_file()
        for item in read_items:
            print(f"{item.name}: ${item.price:.2f}")



if __name__ == "__main__":
    main = Main()