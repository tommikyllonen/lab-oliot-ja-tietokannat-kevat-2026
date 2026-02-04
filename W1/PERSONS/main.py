from person import Person
from date import Date;
from locale import setlocale, LC_ALL

class Main:
    def __init__(self) -> None:
       
       setlocale(LC_ALL, '')  #User's default locale settings
       self.value = "Hello, World from Main!"
       p: Person = Person("John Doe", Date(1995, 5, 15))
       print(p)
       p.birth_date = Date(2000, 12, 31)
       print(p)
       p.name = " Jane Doe "
       print(p)
       p = Person()
       print(p)
    
if __name__ == "__main__":
    app: Main = Main()