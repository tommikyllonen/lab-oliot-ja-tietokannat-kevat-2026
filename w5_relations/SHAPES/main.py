from color import Color
from point import Point
from ellipse import Ellipse
from shape import Shape
from square import Square
from rectangle import Rectangle
from circle import Circle


class Main:
    def __init__(self)-> None:
        print("Hello from Shapes!")
        s:Shape = Ellipse('Ellu', Point(10, 20), Color.RED, 123, 456)
        print(s)

        print(f"Ellipse Area: {s.area()}")
        print(f"Ellipse Perimeter: {s.perimeter()}")
        # note: while s being originally Shape type, here it is Ellipse type.
        s.a = 1 
        print(s)
        print(f"Ellipse Area: {s.area()}")
        print(f"Ellipse Perimeter: {s.perimeter()}")
        s = Rectangle()
        print(s)
        print(f"Rectangle Area: {s.area()}")
        print(f"Rectangle Perimeter: {s.perimeter()}")
        s = Square('SQ', Point(3,4), Color.GREEN, 10)
        print(s)
        print(f"Square Area: {s.area()}")
        print(f"Square Perimeter: {s.perimeter()}")
        s = Circle('CL', Point(33,44), Color.GREY, 5)
        print(s)
        print(f"Circle Area: {s.area()}")
        print(f"Circle Perimeter: {s.perimeter()}")


        return None



if __name__ == "__main__":
    app = Main()
