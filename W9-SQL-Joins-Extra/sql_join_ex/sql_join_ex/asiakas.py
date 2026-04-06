from dataclasses import dataclass
@dataclass
class Asiakas:
    id: int
    nimi: str
    sahkoposti: str
    def __str__(self):        
        return f"{self.id}: {self.nimi} ({self.sahkoposti})"