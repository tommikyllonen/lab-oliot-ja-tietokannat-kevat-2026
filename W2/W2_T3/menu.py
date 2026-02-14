class Menu:
    def askChoice(self) -> int:
        feed = input("Your choice: ")
        choice = -1
        if feed.isdigit():
            choice = int(feed)
        return choice
    
    def run(self) -> None:
        choice = -1
        menuOptions: dict[int, str] = {1: "Add bottle", 2: "Show bottle", 3: "Save bottle", 0: "Exit"}
        while choice != 0:
            print("Menu:")
            for key, value in menuOptions.items():
                print(f"{key} - {value}")
            choice = self.askChoice()

            if choice not in menuOptions.keys():
                print("Unknown option, try again.")
            elif choice == 1:
                print(f"'{menuOptions[choice]}' not implemented yet.")
            elif choice == 2:
                print(f"'{menuOptions[choice]}' not implemented yet.")
            elif choice == 3:
                print(f"'{menuOptions[choice]}' not implemented yet.")
            elif choice == 0:
                pass
            # else:
            #     print("Unknown option, try again.")
            print("")
        print("Exiting program.")
        return None
