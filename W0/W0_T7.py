def main():
    try:
        value = float(input("Insert number: "))
        print(f"Inserted value is '{float(value)}'")

    except ValueError:
        print("Oops! That wasn't valid number.")
    
if __name__ == "__main__":
    main()