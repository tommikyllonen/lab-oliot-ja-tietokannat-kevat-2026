from soda_bottle import SodaBottle

class Main:
    def __init__(self)-> None:
        print("Program starting.")
        print("Constructing soda bottle.")
        brand: str = input("Insert brand: ")
        volume: float = float(input("Insert volume: "))
        bottle: SodaBottle = SodaBottle(brand, volume)
        print('SodaBottle object created!')
        print('Serializing SodaBottle object.')
        print('Serialized sodabottle:')
        print(bottle.serialize())
        print("Program ending.")

        return None


if __name__ == "__main__":
    Main()

