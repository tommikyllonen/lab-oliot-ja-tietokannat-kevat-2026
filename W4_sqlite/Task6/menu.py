

class Menu:
    def __init__(self) -> None:
        return None
    
    def menu(self) -> int:    
        while True:
            print("Options:")
            print("1 - Add product")
            print("2 - Show products")
            print("0 - Exit")
            userSelection = input("Your choice: ")
            if (userSelection == "0" or userSelection == "1" or userSelection == "2"):
                return int(userSelection)
            print("Select 1, 2 or 3\n")
