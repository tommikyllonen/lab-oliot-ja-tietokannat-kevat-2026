from enum import Enum

class Color(Enum):
    RED = "Red"
    GREEN = "Green"
    BLUE = "Blue"
    YELLOW = "Yellow"
    BLACK = "Black"
    WHITE = "White"
    BROWN = "Brown"
    GREY = "Grey"
    NONE = "None"

    def __str__(self):
        return self.value