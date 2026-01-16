
class Person:
    first_name: str
    last_name: str
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        return None
        
    def fullName(self) -> None:
        print(f"{self.first_name} {self.last_name}")
        return None
