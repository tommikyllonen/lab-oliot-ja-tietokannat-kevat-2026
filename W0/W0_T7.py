def main() -> None:
    try:
        value: float = float(input("Insert number: "))
        print(f"Inserted value is '{float(value)}'")

    except ValueError:
        print("Oops! That wasn't valid number.")
    return None
    
if __name__ == "__main__":
    main()