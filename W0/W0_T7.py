def main():
    value = input("Insert number: ")
    if value.isnumeric():
        print(f"Inserted value is '{float(value)}'")
    else:
        print("Oops! That wasn't valid number.")
    
if __name__ == "__main__":
    main()