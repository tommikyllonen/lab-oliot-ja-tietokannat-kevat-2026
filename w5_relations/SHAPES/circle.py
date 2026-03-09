from color import Color
from point import Point
from ellipse import Ellipse
from shape import Shape
class Circle(Ellipse):
    def __init__( self, name = 'ACircle', location = Point(), color = Color.BLACK, r=500) -> None:
        super().__init__(name, location, color, r, r)
        return None
    @property
    def r(self) -> float:
        return self.a # or self.b since they should be equal
    @r.setter
    def r(self, value:float) -> None:
        self.a = self.b = value

    def __str__(self):
        # if we want to call Shape.__str__() which is grandparent method...
        return f"{Shape.__str__(self)} with r {self.r}"