from counter import Counter

def main():
    print("Program starting.")
    print("Initializing counter...")
    counter = Counter(0)
    print("Counter initialized.")
    selection: int = -1
    while(selection != 0):
        selection = printMenu()
        match selection:
            case 1:
                counter.addCount()
                print("count increased")
            case 2:
                print(f"Current count is: {counter.getCount()}")
            case 3:
                counter.zeroCount()
                print("Count zeroed")
            case 0:
                
                print("\nProgram ending.")
                return None
        print()



    return None

def printMenu() -> int:
    print("Options:")
    print("1) Add count")
    print("2) Get count")
    print("3) Zero count")
    print("0) Exit program")
    try:
        selection: int = int(input("Choice: "))
    except ValueError:
       print("Invalid input, please enter a number.") 

    return selection


if __name__ == "__main__":
    main()