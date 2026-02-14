from soda_bottle import SodaBottle

class Menu:
    def __init__(self, sodaBottles: list[SodaBottle] = []) -> None:
        self.__sodaBottles: list[SodaBottle] = sodaBottles
        return None

    def askChoice(self) -> int:
        feed = input("Your choice: ")
        choice = -1
        if feed.isdigit():
            choice = int(feed)
        return choice

    @property
    def sodaBottles(self) -> list[SodaBottle]:
        return self.__sodaBottles
    
    #Methods for menu options:
    
    def addBottle(self) -> None:
        print("Creating soda bottle.")
        brand: str = input("Insert brand: ")
        volume: float = float(input("Insert volume: "))
        newBottle = SodaBottle(brand, volume)
        self.__sodaBottles.append(newBottle)
        return None

    def showBotteles(self) -> None:
        print("#### Soda bottles ####")            
        #THIS IS JUST "for bottle in self.__sodaBottles:", BUT WITH INDEX
        for index, bottle in enumerate(self.__sodaBottles):
            print(f"Bottle {index + 1}:")
            print(bottle)
        print("#### Soda bottles ####")            
        return None

    def saveBottles(self) -> None:
        print("Saving soda bottles...")
        content = ""
        with open("inventory.txt", "w") as file:
            for bottle in self.__sodaBottles:
                content = bottle.serialize() + "\n"
                file.write(content)
        print("Saving completed!")

    def loadBottles(self) -> None:
        print("Loading inventory...")
        with open("inventory.txt", "r") as file:
            for line in file:
                newBottle = SodaBottle.deserialize(line)
                self.__sodaBottles.append(newBottle)
        print("Inventory loaded.")


    
    def run(self) -> None:
        self.loadBottles()
        choice = -1
        menuOptions: dict[int, str] = {1: "Add bottle", 2: "Show bottles", 3: "Save bottle", 0: "Exit"}
        while choice != 0:
            print("Menu:")
            for key, value in menuOptions.items():
                print(f"{key} - {value}")
            choice = self.askChoice()

            if choice not in menuOptions.keys():
                print("Unknown option, try again.")
            elif choice == 1:
                self.addBottle()
            elif choice == 2:
                self.showBotteles()
            elif choice == 3:
                self.saveBottles()
            elif choice == 0:
                pass
            print("")
        print("Exiting program.")
        return None
