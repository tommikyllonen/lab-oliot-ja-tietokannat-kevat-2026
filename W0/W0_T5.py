def main():
    value = 0
    currentValue = 0.0
    while(value != ""):
        print(f"current Value {currentValue}")
        value = input("Add number(empty stops): ")
        if value.isnumeric():
            currentValue += int(value)
    
    print(f"Final value {currentValue}")
if __name__ == "__main__":
    main()