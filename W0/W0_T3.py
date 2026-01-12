def main() -> None:
    age: int = int(input("Insert age: "))
    if age >= 18:
        print("Adult")
    else:
        print("Child")
    return None
if __name__ == "__main__":
    main()