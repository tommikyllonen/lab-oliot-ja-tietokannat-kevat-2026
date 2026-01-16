class Car:
    engine_on: bool
    color: str
    def __init__(self, color: str) -> None:
        self.color = color
        self.engine_on = False
        return None

    def start(self) -> None:
        if (self.engine_on == False):
            print(f"{self.color} car started")
            self.engine_on = True
        else:
            print(f"{self.color } is already running.")
        return None
