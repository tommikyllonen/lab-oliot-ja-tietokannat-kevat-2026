class CointAcceptor:
    def __init__(self):
        self.__amount:int = 0
        self.__value: float = 0.0
    
    def insertCoin(self, newValue:float) -> None:
        self.__amount += 1
        self.__value += newValue
        print("Inserting...")
        print(f"Inserted coins - {self.__amount}, value - {self.__value}€\n")
        return None

    def getAmount(self) -> int:
        return self.__amount
    def returnCoins(self) -> tuple[int, float]:
        print("Returning coins...")
        amount = self.__amount
        value = self.__value
        self.__amount = 0
        self.__value = 0.0
        print(f"{amount} coins with {value}€ value returned.")
        print(f"Inserted coins - {self.__amount}, value - {0 if self.__value == 0.0 else self.__value}€\n")
        return (amount, value)