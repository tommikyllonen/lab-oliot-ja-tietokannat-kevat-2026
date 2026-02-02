from coin_acceptor import CointAcceptor

class Main:
    def __init__(self) -> None:
        selection = -1
        #remove linechange after the "Program starting." print
        print("Program starting.", end="")
        coinAcceptor = CointAcceptor()

        while(selection != 0):
            selection = printMenu()
            match selection:
                case 1:
                    coinAcceptor.insertCoin()
                case 2:
                    print(f"Currently '{coinAcceptor.getAmount()}' coins in coin acceptor")
                case 3:
                    print(f"Coin acceptor returned '{coinAcceptor.returnCoins()}' coins.")
                case 0:
                    print("Program ending.")
                    return None
        return None


def printMenu() -> int:
    print("")
    print("1 - Insert coin")
    print("2 - Show coins")
    print("3 - Return coins")
    print("0 - Exit program")
    try:
        selection: int = int(input("Your choice: "))
    except ValueError:
       print("Invalid input, please enter a number.") 
    
    return selection



if __name__ == "__main__":
    Main()