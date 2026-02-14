
class SodaBottle:
    def __init__(self, brand: str, volume: float) -> None:
        self.__brand: str = brand
        self.__volume: float = volume
        return None
   
    #Make getters for brand and volume, so that they can be read but not changed after object creation. 
    @property
    def brand(self) -> str:
        return self.__brand
    @property
    def volume(self) -> float:
        return self.__volume

    def serialize(self) -> str:
        return ';'.join([self.brand, str(self.volume)])
    
    @staticmethod
    def deserialize(sbottle: str) -> "SodaBottle":
        #remove newline if exists:
        brand, sVolume = sbottle.split(';')
        return SodaBottle(brand, float(sVolume))

