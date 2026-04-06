from dataclasses import dataclass
@dataclass
class Tilaus:
    id: int
    asiakas_id: int
    summa: float
    def __str__(self):
        return f"Tilaus {self.id} asiakas id {self.asiakas_id} summa {self.summa:.2f} €"

