from color import Color
from point import Point
from shape import Shape
import math

class Ellipse(Shape):
    def __init__(self, name = 'ARect', location = Point(), color = Color.BLACK, a:float = 100, b:float = 50) -> None:
        # super ctor call is much better than...
        super().__init__(name, location, color) # parent class Shape ctor call, must be the first call!
        # ...omit the super init --> python interpreter calls the super default ctor and
        # we must call the inherited property methods!
        # self.name = name
        # self.location = location
        # self.color = color
        self.a = a
        self.b = b
        return None

    @property
    def a(self) -> float:
        return self.__a
    @a.setter
    def a(self, value:float) -> None:
        if value <= 0:
            self.__a = 10
        else:
            self.__a = value
    @property
    def b(self) -> float:
        return self.__b
    @b.setter
    def b(self, value:float) -> None:
        if value <= 0:
            self.__b = 10
        else:
            self.__b = value
    def area(self):
        return math.pi * self.a * self.b    
    def perimeter(self):
        # approximation, since there is no exact formula for ellipse perimeter
        return 2 * math.pi * math.sqrt((self.a ** 2 + self.b ** 2) / 2)
