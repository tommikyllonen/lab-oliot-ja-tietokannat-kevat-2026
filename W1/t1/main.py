from person import Person

def main() -> None:
    print("Initializing persons...")
    person1: Person = Person("Jane", "Morgan")
    person2: Person = Person("John", "Doe")
    print("Persons initialized, names below.")
    person1.fullName()
    person2.fullName()
    print("Program Ending.")
    return None
if __name__ == "__main__":
    main()
