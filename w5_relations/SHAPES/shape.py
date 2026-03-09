# abstract class definition needs ABC base class
# abstract method definition needs @abstractmethod
from abc import ABC, abstractmethod
from point import Point
from color import Color
 # Pass in the ABC, means inherit the Abstract Base Class
 # after that we cant create instances of this class, 
 # but we can create instances of the subclasses that inherit from it
 # and we can also define abstract methods that must be implemented by the subclasses
class Shape(ABC):
    def __init__(self, name:str = 'AShape', location:Point = Point(), color:Color = Color.NONE) -> None:
        self.name = name
        self.location = location
        self.color = color

    @property
    def name(self) -> str:
        return self.__name
    @name.setter
    def name(self, value:str) -> None:
        # we may need some validity...
        self.__name = value
    @property
    def location(self) -> Point:
        return self.__location
    @location.setter
    def location(self, value:Point):
        # Point class checks internal values --> no need to check validity
        self.__location = value
    @property
    def color(self) -> Color:
        return self.__color 
    @color.setter
    def color(self, value:Color) -> None:
        self.__color = value
    def __str__(self):
        return f"{self.name}, color {self.color} at {self.location}"
    @abstractmethod
    def area(self) -> float:
        #raise NotImplementedError("Subclasses should calculate the area...")
        return 0
    @abstractmethod
    def perimeter(self) -> float:
        #raise NotImplementedError("Subclasses should calculate the perimeter...")
        return 0

if __name__ == "__main__":
    # Shape is an abstract class --> cannot be instantiated!
    s:Shape = Shape("MyShape", Point(100,200), Color.BLUE) # error!
    print(s)
    #print("Area: ",s.area())
    #print("Perimeter: ",s.perimeter())
