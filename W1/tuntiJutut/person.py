class Person:
    def __init__(self, name, age):
        # initialize person's name and age
        # when needed to be private, use underscore prefix
        self._name = name
        self._age = age

    def greet(self):
        return f"Hello, my name is {self._name} and I am {self._age} years old."
    

# This __name__ == "__main__" i true only when wer run this file directly e.g. c:/>python3 person.py
# When this file is imported as a module, the code block is not executed.
if __name__ == "__main__":
    person = Person("Alice", 30)
    print(person.greet())
