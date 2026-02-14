
class SodaBottle:
    def __init__(self, brand: str, volume: float) -> None:
        self.__brand: str = brand
        self.__volume: float = volume
        return None

    @property
    def brand(self) -> str:
        return self.__brand
    @property
    def volume(self) -> float:
        return self.__volume

    def __str__(self) -> str:
        return f"  brand - {self.__brand}\n  volume - {self.__volume}" 
    
    def serialize(self) -> str:
        return ';'.join([self.__brand, str(self.__volume)])
    
    @staticmethod
    def deserialize(sbottle: str) -> "SodaBottle":
        #remove newline if exists:
        brand, sVolume = sbottle.split(';')
        return SodaBottle(brand, float(sVolume))