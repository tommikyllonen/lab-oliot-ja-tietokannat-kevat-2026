
class Engine():
    def __init__(self, fuel:str, cc: int, hp: int) -> None:
        self.fuel = fuel
        self.cc = cc
        self.hp = hp
        return None

    def __str__(self) -> str:
        return f"fuel: {self.fuel} cc: {self.cc} hp: {self.hp}"