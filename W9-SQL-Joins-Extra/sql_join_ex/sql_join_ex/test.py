from asiakas import Asiakas
from tilaus import Tilaus
d = list(Asiakas.__dataclass_fields__.keys())
a = d[0]
print(a)