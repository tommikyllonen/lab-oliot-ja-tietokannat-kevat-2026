def main() -> None:
    value: float = 0.0
    currentValue: float = 0.0
    while True:
        print(f"Current value {currentValue}")
        value = input("Add number(empty stops): ")
        if value == "":
            break
        currentValue += float(value)
    print(f"Final value {currentValue}")
    return None

if __name__ == "__main__":
    main()