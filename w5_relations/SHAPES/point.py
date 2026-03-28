class Point:
    def __init__(self, x:float = 0, y:float = 0) -> None:
        self.x = x
        self.y = y
        return None

    @property
    def x(self) -> float:
        return self.__x
    @x.setter
    def x(self, value: float) -> None:
        # possible error checking, but now we accept all values
        self.__x = value
    @property
    def y(self) -> float:
        return self.__y
    @y.setter
    def y(self, value: float) -> None:
        self.__y = value

    def __str__(self) -> str:
        return f"({self.x},{self.y})"

if __name__ == "__main__":
    p: Point = Point(12.3,4.7)
    p.x = 100
    print("p.x: ", p.x)
    print(p)
