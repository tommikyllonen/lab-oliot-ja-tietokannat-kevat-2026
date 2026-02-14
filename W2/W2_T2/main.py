from soda_bottle import SodaBottle

class Main:
    def __init__(self)-> None:
        print("Program starting.")
        fName = input("Insert filename: ")
        
        firstRow: str = ""
        with open(fName, 'r') as file:
            firstRow = file.readline().strip()
        
        print(f'Deserializing "{firstRow}"')

        bottle: SodaBottle = SodaBottle.deserialize(firstRow)
        # brand, volume = bottle.serialize().split(';')
        print(f"Looks like {bottle.volume} litre {bottle.brand} bottle.")
        print('Program ending.')
        

        return None

if __name__ == "__main__":
    app = Main()

