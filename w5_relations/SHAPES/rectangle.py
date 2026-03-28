from color import Color
from point import Point
from shape import Shape

class Rectangle(Shape):
    def __init__(self, name = 'ARect', location = Point(), color = Color.BLACK, width:float = 100, height:float = 50) -> None:
        # super ctor call is much better than...
        super().__init__(name, location, color) # parent class Shape ctor call, must be the first call!
        # ...omit the super init --> python interpreter calls the super default ctor and
        # we must call the inherited property methods!
        # self.name = name
        # self.location = location
        # self.color = color
        self.width = width
        self.height = height

    @property
    def width(self) -> float:
        return self.__width 
    @width.setter
    def width(self, value:float) -> None:
        if value <= 0:
            self.__width = 10
        else:
            self.__width = value
    @property
    def height(self) -> float:
        return self.__height
    @height.setter
    def height(self, value:float) -> None:
        if value <= 0:
            self.__height = 10
        else:
            self.__height = value

    def __str__(self):
        return f"{super().__str__()}, w: {self.width} h: {self.height}"
    
    # overridden from Shape
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
    
if __name__ == "__main__":
    s:Shape = Rectangle()
    
    print(s)
    # we have Shape-type variable, but when we instantiate that with Rectangle and call overridden methods
    # --> polumorphism works!
    print("Area: ",s.area()) # theoretically Shape.area() but actually Rectangle.area()
    print("Perimeter: ", s.perimeter()) # theoretically Shape.perimeter() but actually Rectangle.perimeter()
