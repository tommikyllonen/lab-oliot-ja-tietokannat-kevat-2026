from car import Car
class Main:

        def __init__(self) -> None:
                print("Program starting.")
                print("Initializing three car objects.")
                car1: Car = Car("red")
                car2: Car = Car("green")
                car3: Car = Car("blue")
                print("Car objects initialized.")
                print("Starting the first car object.")
                car1.start()
                print("Starting the second car object.")
                car2.start()
                print("Starting the third car object.")
                car3.start()
                print("Starting the third car object.")
                car3.start()
                print("Program ending.")
                return None


if __name__ == "__main__":
        Main()
