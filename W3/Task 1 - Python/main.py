from person import Person

class Main:
   def __init__(self)-> None:
    print("Program starting.")
    print("Creating person...")
    newperson: Person = Person("John", "Doe", 30)
    print("Person created.")
    print(f"Name: {newperson.getFullname()}")
    print(f"Age: {newperson.getAge()}")
    print("Person has now birthday...")
    newperson.ageUp()
    print(f"New age: {newperson.getAge()}")
    print("Program ending.") 
    return None

if __name__ == "__main__":
    app = Main()

