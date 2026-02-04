from date import Date



class Person:
    def __init__(self, name = "Keijo", birth_date: Date = Date(2026,1,1)) -> None:
        # initialize person's name and age
        # when needed to be private, use underscore prefix
        self._name = name
        self._birth_date = birth_date
        return None
    
    def __str__(self) -> str: 
        return f"{self._name}, birth Date: {self._birth_date}"
    #PROPERTIES
    @property
    def name(self) -> str:
        return self._name
    @property
    def birth_date(self) -> Date:
        return self._birth_date
    
    # Setters with validation ( in setter we usually use value as parameter name, however you can use any name you want)
    @name.setter
    def name(self, value: str) -> None:
        v: str = value.strip()
        if len(v) < 2:
            raise ValueError("Name cannot be shorter that 2 characters.")
        self._name = v

    @birth_date.setter
    def birth_date(self, value: Date) -> None:
        self._birth_date = value
    

# This __name__ == "__main__" i true only when wer run this file directly e.g. c:/>python3 person.py
# When this file is imported as a module, the code block is not executed.
if __name__ == "__main__":
    try:
        person = Person("Alice", Date(1990, 6, 22))
        print(person) #uses __str__ function when printing the object
        person.name = " Bob   "
        print(person)
        # person.name = "d" #raise and ValueError
    except ValueError as e:
        print(f"Error: {e}") 
        print(f"Error: {e.args[0]}") #basically same as e (e.message)
        
    # if you dont provide parameters, default values are used
    person2 = Person()
    
    # you can just provide one parameter if there are default values for the other parameters
    person3 = Person(birth_date=Date(1320,2,29))
    person4 = Person(name="Cecilia")
    print(person2)
    print(person3)
    print(person4)
