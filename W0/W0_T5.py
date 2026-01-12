def main():
    value = 0.0
    currentValue = 0.0
    while True:
        print(f"Current value {currentValue}")
        value = input("Add number(empty stops): ")
        if value == "":
            break
        currentValue += float(value)
    print(f"Final value {currentValue}")

if __name__ == "__main__":
    main()