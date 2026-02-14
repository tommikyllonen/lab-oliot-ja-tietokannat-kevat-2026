from menu import Menu

class Main:
    def __init__(self)-> None:
        print("Program starting.")
        menu = Menu()
        menu.run()
        print("Program ending.")
        return None 

if __name__ == "__main__":
    app = Main()