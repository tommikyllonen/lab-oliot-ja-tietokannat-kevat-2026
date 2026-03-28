from color import Color
from point import Point
from shape import Shape
from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, name='ASquare', location=Point(), color=Color.RED, side:float = 300):
        super().__init__(name, location, color, side, side)

    @property
    def side(self) -> float:
        return self.width # or self.height since they should be equal
    @side.setter
    def side(self, value:float) -> None:
        self.width = self.height = value

    def __str__(self):
        # if we want to call Shape.__str__() which is grandparent method...
#        return f"{super().super().__str__()} with side {self.side}" # this is not possible..
        return f"{Shape.__str__(self)} with side {self.side}" # ...but this works
    
if __name__ == "__main__":
    s:Shape = Square()
    print(s)
    print("Area: ",s.area())
    print("Perimeter: ", s.perimeter())
    s.side = 123
    print(s)
    print("Area: ",s.area())
    print("Perimeter: ", s.perimeter())

