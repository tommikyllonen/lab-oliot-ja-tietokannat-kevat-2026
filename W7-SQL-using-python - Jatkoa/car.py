class Car:
    def __init__(self, brand:str, model:str, year:int, color:str, engine_id:int) -> None:
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.engine_id = engine_id
        return None

    def __str__(self) -> str:
        return f"{self.brand} {self.model} {self.year} {self.color}"

        
#write here, how this would look as a data class
# from dataclasses import dataclass
# @dataclass
# class Car:
#     brand: str
#     model: str
#     year: int
#     color: str

#     def __str__(self) -> str:
#         return f"{self.brand} {self.model} {self.year} {self.color}
#write here, how this would look as a data class