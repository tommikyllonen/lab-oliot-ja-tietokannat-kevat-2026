from coin_acceptor import CointAcceptor


def main() -> None:
    selection: int = 0
    print("Program starting.")
    print("Welcome to coin acceptor program.")
    print("Insert new coin by typing it's value (0 returns the money, -1 exits the program)")
    print("")

    coinAcceptor = CointAcceptor()
    
    while(selection != -1):
        
        selection = printMenu()
        if (selection == -1):
            print("Exiting program.")
            break
        elif (selection == 0):
            coinAcceptor.returnCoins()
        else:
            coinAcceptor.insertCoin(selection)
    print("\nProgram ending.")
    return None


def printMenu() -> float:
    try:
        selection: float = float(input("Insert coin(0 return, -1 exit): "))
    except ValueError:
       print("Invalid input, please enter a number.") 
    return selection



if __name__ == "__main__":
    main()
    

