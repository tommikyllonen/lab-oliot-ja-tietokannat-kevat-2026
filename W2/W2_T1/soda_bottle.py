
class SodaBottle:
    def __init__(self, brand: str, volume: float) -> None:
        self.__brand: str = brand
        self.__volume: float = volume
        return None
    

    # def __str__(self):
    #     return f"{self.__brand} soda bottle with {self.__volume}ml"
    def serialize(self) -> str:
        # return f"{self.__brand};{self.__volume}" #TAI SITTEN NÄIN
        return ';'.join([self.__brand, str(self.__volume)])
